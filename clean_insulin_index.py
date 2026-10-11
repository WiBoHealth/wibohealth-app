"""
WiBo Health - تنقية مؤشر الإنسولين (Insulin Index Cleanup)

يحتفظ بقيمة ii فقط للأصناف المفحوصة مخبرياً في:
  - Holt SH et al., Am J Clin Nutr 1997;66(5):1264-76
  - Bao J et al., Am J Clin Nutr 2009;90(4):986-92
ويحوّل أي صنف آخر إلى ii: null.

المصدر الوحيد للقيم هو insulin_index_sources.csv، ولا يُطبَّق إلا الصف الذي:
  - فيه ii_value رقمي
  - و verified = yes (أي تمت مطابقته يدوياً مع جدول الدراسة الأصلية)

الاستخدام:
  python clean_insulin_index.py            # معاينة فقط بدون أي تعديل
  python clean_insulin_index.py --apply    # تطبيق التعديل على js/data.js
  python clean_insulin_index.py --apply --min-verified 20   # خفض حد الحماية عمداً
"""

import csv
import os
import re
import shutil
import sys

DATA_FILE = os.path.join("js", "data.js")
SOURCES_FILE = "insulin_index_sources.csv"
BACKUP_FILE = os.path.join("js", "data.before-ii-cleanup.js")
REPORT_FILE = "insulin_index_report.csv"
# حماية: لا نطبّق إن كانت القائمة الموثقة أقصر من هذا (يمنع تصفير كل الأصناف بالخطأ)
MIN_VERIFIED = 30

def load_verified_sources():
    verified, pending = {}, []
    with open(SOURCES_FILE, encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            food_id = int(row["food_id"])
            value = (row.get("ii_value") or "").strip()
            is_verified = (row.get("verified") or "").strip().lower() in ("yes", "y", "1", "true")
            if is_verified and re.fullmatch(r"\d+(\.\d+)?", value):
                if food_id in verified:
                    sys.exit(f"[!] الصنف {food_id} مكرر في {SOURCES_FILE}")
                verified[food_id] = (float(value) if "." in value else int(value), row)
            else:
                pending.append(row)
    return verified, pending

def main():
    apply = "--apply" in sys.argv
    min_verified = MIN_VERIFIED
    if "--min-verified" in sys.argv:
        min_verified = int(sys.argv[sys.argv.index("--min-verified") + 1])
    verified, pending = load_verified_sources()

    with open(DATA_FILE, encoding="utf-8", newline="") as f:
        content = f.read()

    item_re = re.compile(r"(\{\s*id:\s*(\d+),[^\n]*?\bii:\s*)(null|[\d.]+)")
    all_ids = {int(m.group(2)) for m in item_re.finditer(content)}
    missing = sorted(set(verified) - all_ids)
    if missing:
        sys.exit(f"[!] أرقام غير موجودة في data.js: {missing}")

    kept, nulled = [], 0
    def replace(m):
        nonlocal nulled
        food_id = int(m.group(2))
        if food_id in verified:
            value, row = verified[food_id]
            kept.append((food_id, row["nameEn"], row["study"], row["study_food_name"], m.group(3), value))
            return f"{m.group(1)}{value}"
        if m.group(3) != "null":
            nulled += 1
        return f"{m.group(1)}null"

    new_content = item_re.sub(replace, content)

    print(f"[*] أصناف في data.js: {len(all_ids)}")
    print(f"[✓] موثقة سريرياً (ستحتفظ برقمها): {len(verified)}")
    print(f"[-] ستتحول إلى null: {nulled}")
    print(f"[?] صفوف بانتظار التحقق في {SOURCES_FILE}: {len(pending)}")
    for food_id, name, study, study_name, old, new in sorted(kept):
        change = "" if str(old) == str(new) else f"  (كان {old})"
        print(f"    {food_id:>4} {name} <- {study}: {study_name} = {new}{change}")

    if not apply:
        print("\n[i] معاينة فقط. أضف --apply للتطبيق.")
        return
    if len(verified) < min_verified:
        sys.exit(f"\n[!] تم الإلغاء: {len(verified)} صنفاً موثقاً فقط (الحد الأدنى {min_verified}). "
                 f"أكمل التحقق في {SOURCES_FILE} أولاً.")

    shutil.copyfile(DATA_FILE, BACKUP_FILE)
    with open(DATA_FILE, "w", encoding="utf-8", newline="") as f:
        f.write(new_content)
    with open(REPORT_FILE, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["food_id", "nameEn", "study", "study_food_name", "old_ii", "verified_ii"])
        w.writerows(sorted(kept))
    print(f"\n[🎉] تم التطبيق. نسخة احتياطية: {BACKUP_FILE} | التقرير: {REPORT_FILE}")

if __name__ == "__main__":
    main()
