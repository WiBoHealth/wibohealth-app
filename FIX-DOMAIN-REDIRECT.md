# 🔧 Fix Domain Redirect Issue - WiBo Health
**Date:** December 4, 2025  
**Problem:** Google Play Console error: "لم يتم اجتياز التحقّق من إمكانية الوصول إلى النطاق بدون عمليات إعادة توجيه"

---

## 🎯 **Problem:**
`wibohealth.com` redirects to `wibohealth-app.vercel.app`, preventing Google from verifying the domain.

---

## ✅ **Solution:**

### **Option 1: Remove Redirect (Recommended)**

#### **If hosted on GitHub Pages:**
1. Go to GitHub repository settings
2. **Settings** → **Pages**
3. Ensure **Custom domain** is set to: `wibohealth.com`
4. Remove any redirect rules

#### **If hosted on Vercel:**
1. Go to Vercel Dashboard
2. Select the project
3. **Settings** → **Domains**
4. Ensure `wibohealth.com` is the primary domain
5. Remove any redirects to `vercel.app`
6. Check `vercel.json` for redirect rules and remove them

#### **If using Cloudflare:**
1. Login to Cloudflare
2. Select `wibohealth.com`
3. **Rules** → **Page Rules**
4. Remove any forwarding/redirect rules
5. Check **Redirect Rules** and delete any

---

### **Option 2: Use Both Domains (Quick Fix)**

Keep both domains working:
- `wibohealth-app.vercel.app` ✅ (Already verified)
- `wibohealth.com` ✅ (Fix redirect, then verify)

**Steps:**
1. Remove redirect from `wibohealth.com`
2. Ensure both domains serve the same content
3. Ensure `assetlinks.json` exists on both:
   - `https://wibohealth-app.vercel.app/.well-known/assetlinks.json` ✅
   - `https://wibohealth.com/.well-known/assetlinks.json` ✅

---

## 🧪 **Test:**

### **Before fix:**
```bash
curl -I https://wibohealth.com
# Shows: Location: https://wibohealth-app.vercel.app
```

### **After fix:**
```bash
curl -I https://wibohealth.com
# Shows: 200 OK (no redirect)
```

---

## 🚀 **After fixing redirect:**

1. Wait 5 minutes for DNS/CDN cache to clear
2. Test: `https://wibohealth.com/.well-known/assetlinks.json`
3. Should return JSON (no redirect)
4. Go to Google Play Console → App Settings → Web Links
5. Click on `wibohealth.com`
6. Click **"Verify"** or **"Re-check"**
7. Wait 2-3 minutes
8. Status will change from ❌ to ✅

---

## 📋 **Common Redirect Sources:**

### **1. DNS Level (Cloudflare, etc.):**
- Page Rules
- Redirect Rules
- Forwarding

### **2. Server Level (vercel.json, _redirects):**
```json
// Remove this from vercel.json:
{
  "redirects": [
    {
      "source": "https://wibohealth.com/:path*",
      "destination": "https://wibohealth-app.vercel.app/:path*"
    }
  ]
}
```

### **3. HTML Meta Redirect:**
```html
<!-- Remove this from index.html: -->
<meta http-equiv="refresh" content="0; url=https://wibohealth-app.vercel.app">
```

---

## ✅ **Expected Result:**
After removing redirect, Google will successfully verify `wibohealth.com` and the status will change to ✅.

---

**Status:** ⏳ Waiting for redirect removal  
**Next Step:** Remove redirect, test, then verify in Play Console
