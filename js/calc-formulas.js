/* WiBo Health calculator formulas: pure functions, no DOM, shared by every calculator page (loaded with defer)
   and tested in Node by scripts/test_calc_formulas.js against published reference values.
   Nothing entered by a visitor leaves the browser: these functions only compute (GDPR: health data stays local).

   Sources
   - HbA1c %  <-> mmol/mol: IFCC master equation (NGSP = 0.0915 x IFCC + 2.15; IFCC = (NGSP - 2.15) x 10.929)
   - eAG: ADAG study, Nathan et al., Diabetes Care 2008;31:1473-1478 (eAG mg/dL = 28.7 x A1C - 46.7)
   - glucose mg/dL <-> mmol/L: molar mass of glucose 180.16 g/mol (factor 18.016)
   - HOMA-IR: Matthews et al., Diabetologia 1985 (insulin uU/mL x glucose mmol/L / 22.5)
   - QUICKI: Katz et al., J Clin Endocrinol Metab 2000 (1 / (log10 insulin + log10 glucose mg/dL))
   - TyG index: Simental-Mendia et al., Metab Syndr Relat Disord 2008 (ln(TG mg/dL x glucose mg/dL / 2))
   - FINDRISC: Lindstrom & Tuomilehto, Diabetes Care 2003 (8 questions, 0-26 points, 10-year risk bands) */
(function (root, factory) {
    var api = factory();
    if (typeof module === 'object' && module.exports) module.exports = api;
    else root.WiboCalc = api;
})(typeof self !== 'undefined' ? self : this, function () {
    'use strict';
    var GLUCOSE_FACTOR = 18.016;     // mg/dL per mmol/L
    var TG_FACTOR = 88.57;           // triglycerides mg/dL per mmol/L

    function round(x, d) { var p = Math.pow(10, d || 0); return Math.round(x * p) / p; }
    function num(x) { var n = typeof x === 'string' ? parseFloat(x.replace(',', '.')) : x; return isFinite(n) ? n : NaN; }

    // ---------------------------------------------------------------- HbA1c
    function hba1cPercentToMmol(pct) { return (num(pct) - 2.15) * 10.929; }
    function hba1cMmolToPercent(mmol) { return 0.0915 * num(mmol) + 2.15; }
    // + 1e-9: 28.7 x 6 - 46.7 is 125.5 exactly but 125.4999... in binary; ADA rounds it to 126
    function eagMgdl(pct) { return 28.7 * num(pct) - 46.7 + 1e-9; }
    function eagMmol(pct) { return eagMgdl(pct) / GLUCOSE_FACTOR; }
    /* band by HbA1c in mmol/mol: 'normal' < 39, 'prediabetes' 39-47 (ADA; NICE/WHO use 42-47), 'diabetes' >= 48.
       Labs report whole mmol/mol, so the value is rounded first (5.7% = 38.8 -> 39, the ADA threshold). */
    function hba1cBand(mmol) {
        var m = Math.round(num(mmol));
        if (!(m > 0)) return null;
        return m < 39 ? 'normal' : m < 48 ? 'prediabetes' : 'diabetes';
    }

    // ---------------------------------------------------------------- glucose
    function mgdlToMmol(mgdl) { return num(mgdl) / GLUCOSE_FACTOR; }
    function mmolToMgdl(mmol) { return num(mmol) * GLUCOSE_FACTOR; }
    /* glucose thresholds are defined on mmol/L with one decimal (126 mg/dL = 6.99 -> 7.0): round before comparing */
    function glucoseKey(mmol) { return round(num(mmol), 1); }
    /* fasting plasma glucose band (ADA): low < 3.9, normal 3.9-5.5, prediabetes 5.6-6.9, diabetes >= 7.0 mmol/L */
    function fastingGlucoseBand(mmol) {
        var m = glucoseKey(mmol);
        if (!(m > 0)) return null;
        return m < 3.9 ? 'low' : m < 5.6 ? 'normal' : m < 7.0 ? 'prediabetes' : 'diabetes';
    }
    /* 2 hours after a meal, people without diabetes (ADA/WHO OGTT): low < 3.9, normal < 7.8, raised 7.8-11.0, >= 11.1 */
    function afterMealBand(mmol) {
        var m = glucoseKey(mmol);
        if (!(m > 0)) return null;
        return m < 3.9 ? 'low' : m < 7.8 ? 'normal' : m < 11.1 ? 'prediabetes' : 'diabetes';
    }

    // ---------------------------------------------------------------- insulin resistance
    function homaIr(insulin, glucoseMmol) { return num(insulin) * num(glucoseMmol) / 22.5; }
    function quicki(insulin, glucoseMmol) {
        return 1 / (Math.log10(num(insulin)) + Math.log10(num(glucoseMmol) * GLUCOSE_FACTOR));
    }
    function tyg(triglyceridesMmol, glucoseMmol) {
        return Math.log(num(triglyceridesMmol) * TG_FACTOR * num(glucoseMmol) * GLUCOSE_FACTOR / 2);
    }
    /* there is no universal cut-off: informative bands only (HOMA-IR < 2 / 2-2.9 / >= 3) */
    function homaBand(h) { var x = num(h); if (!(x >= 0)) return null; return x < 2 ? 'low' : x < 3 ? 'borderline' : 'high'; }

    // ---------------------------------------------------------------- FINDRISC
    /* answers: {age, bmi, waist, sex ('m'|'f'), active (bool), vegDaily (bool), bpMeds (bool), highGlucose (bool),
                 family ('none'|'second'|'first')} -> {score, band, risk} */
    function findrisc(a) {
        var s = 0, age = num(a.age), bmi = num(a.bmi), waist = num(a.waist);
        s += age < 45 ? 0 : age < 55 ? 2 : age < 65 ? 3 : 4;
        s += bmi < 25 ? 0 : bmi <= 30 ? 1 : 3;
        if (a.sex === 'f') s += waist < 80 ? 0 : waist <= 88 ? 3 : 4;
        else s += waist < 94 ? 0 : waist <= 102 ? 3 : 4;
        s += a.active ? 0 : 2;
        s += a.vegDaily ? 0 : 1;
        s += a.bpMeds ? 2 : 0;
        s += a.highGlucose ? 5 : 0;
        s += a.family === 'first' ? 5 : a.family === 'second' ? 3 : 0;
        var band = s < 7 ? 'low' : s <= 11 ? 'slight' : s <= 14 ? 'moderate' : s <= 20 ? 'high' : 'veryhigh';
        var risk = { low: '1/100', slight: '1/25', moderate: '1/6', high: '1/3', veryhigh: '1/2' }[band];
        return { score: s, band: band, risk: risk };
    }
    function bmi(weightKg, heightCm) { var h = num(heightCm) / 100; return num(weightKg) / (h * h); }

    // ---------------------------------------------------------------- energy, weight loss, protein (batch C, 2026-11-23)
    /* Mifflin-St Jeor 1990: 10 W + 6.25 H - 5 A + 5 (men) / - 161 (women) */
    function bmr(sex, age, weightKg, heightCm) {
        return 10 * num(weightKg) + 6.25 * num(heightCm) - 5 * num(age) + (sex === 'f' ? -161 : 5);
    }
    var KCAL_PER_KG = 7700;
    var FLOOR = { f: 1200, m: 1500 };              // minimum daily calories (doctor, 2026-11-23)
    /* weight-loss plan: o = {sex, age, height, weight, target, pal, pace (kg/week)}.
       Calories = TDEE - pace x 7700 / 7, never below the floor; recalculated after every 5 kg lost (a lighter body burns
       less), then simulated week by week, so the date is later than the simple straight-line estimate. */
    function weightLossPlan(o) {
        var w = num(o.weight), target = num(o.target), pal = num(o.pal), pace = num(o.pace), sex = o.sex === 'f' ? 'f' : 'm';
        var deficit = pace * KCAL_PER_KG / 7, floor = FLOOR[sex];
        var tdee0 = bmr(sex, o.age, w, o.height) * pal;
        var intakeAt = function (kg) { return Math.max(floor, Math.round((bmr(sex, o.age, kg, o.height) * pal - deficit) / 10) * 10); };
        var intake0 = intakeAt(w), intake = intake0, lastReset = w, cur = w, weeks = 0, reached = target < w;
        while (reached && cur > target) {
            if (lastReset - cur >= 5) { intake = intakeAt(cur); lastReset = cur; }
            var loss = (bmr(sex, o.age, cur, o.height) * pal - intake) * 7 / KCAL_PER_KG;
            if (loss <= 0.01 || weeks >= 520) { reached = false; break; }
            cur -= loss; weeks++;
        }
        var hm = num(o.height) / 100;
        return {
            tdee: tdee0, bmr: bmr(sex, o.age, w, o.height), intake: intake0, deficit: tdee0 - intake0,
            floorApplied: intake0 === floor && tdee0 - deficit < floor, belowBmr: intake0 < bmr(sex, o.age, w, o.height),
            fastPace: pace > 0.01 * w, targetBmi: target / (hm * hm), weeks: weeks, reached: reached, toLose: w - target
        };
    }
    /* weight used for protein: actual weight, or the adjusted weight when BMI >= 30
       (weight at BMI 25 + 25% of the difference; doctor, 2026-11-23) */
    function adjustedWeight(weightKg, heightCm) {
        var h = num(heightCm) / 100, w25 = 25 * h * h, w = num(weightKg);
        return w > w25 ? w25 + 0.25 * (w - w25) : w;
    }
    function proteinWeight(weightKg, heightCm) { return bmi(weightKg, heightCm) >= 30 ? adjustedWeight(weightKg, heightCm) : num(weightKg); }
    /* g/kg per goal: general 0.83 (EFSA; 1.0-1.2 from 65, PROT-AGE), weight loss 1.2-1.6, muscle 1.6-2.2, GLP-1 1.2-1.6 */
    function proteinPerKg(goal, age) {
        if (goal === 'loss' || goal === 'glp1') return [1.2, 1.6];
        if (goal === 'muscle') return [1.6, 2.2];
        return num(age) >= 65 ? [1.0, 1.2] : [0.83, 0.83];
    }

    // ---------------------------------------------------------------- body fat (US Navy) and healthy weight
    /* Hodgdon & Beckett 1984, centimetres */
    function navyBodyFat(sex, heightCm, neckCm, waistCm, hipCm) {
        var h = num(heightCm), n = num(neckCm), w = num(waistCm), hip = num(hipCm);
        if (sex === 'f') {
            if (!(w + hip - n > 0)) return NaN;
            return 495 / (1.29579 - 0.35004 * Math.log10(w + hip - n) + 0.22100 * Math.log10(h)) - 450;
        }
        if (!(w - n > 0)) return NaN;
        return 495 / (1.0324 - 0.19077 * Math.log10(w - n) + 0.15456 * Math.log10(h)) - 450;
    }
    /* Gallagher et al., Am J Clin Nutr 2000;72:694-701 (healthy %BF by sex and age; 18-19 use the 20-39 row, 80+ the 60-79
       row); below essential fat (men < 5%, women < 13%) is 'verylow' (doctor, 2026-11-23). Bands: verylow, low, healthy,
       high, veryhigh */
    var GALLAGHER = { m: [[8, 20, 25], [11, 22, 28], [13, 25, 30]], f: [[21, 33, 39], [23, 34, 40], [24, 36, 42]] };
    function bodyFatBand(sex, age, pct) {
        var s = sex === 'f' ? 'f' : 'm', a = num(age), p = round(num(pct), 1);
        var row = GALLAGHER[s][a < 40 ? 0 : a < 60 ? 1 : 2];
        if (p < (s === 'f' ? 13 : 5)) return 'verylow';
        return p < row[0] ? 'low' : p < row[1] ? 'healthy' : p < row[2] ? 'high' : 'veryhigh';
    }
    function bodyFatRow(sex, age) { var a = num(age); return GALLAGHER[sex === 'f' ? 'f' : 'm'][a < 40 ? 0 : a < 60 ? 1 : 2]; }
    function healthyWeightRange(heightCm) { var h = num(heightCm) / 100; return [18.5 * h * h, 24.9 * h * h]; }

    // ---------------------------------------------------------------- glycemic load
    /* GL = GI x available carbohydrate (carbs - fibre) in the portion / 100 */
    function glycemicLoad(gi, carbsPer100, fiberPer100, grams) {
        var avail = Math.max(0, num(carbsPer100) - (num(fiberPer100) || 0));
        return (num(gi) || 0) * avail * num(grams) / 100 / 100;
    }
    /* per food portion (University of Sydney): <= 10 low, 11-19 medium, >= 20 high; meal (guide only, no official
       cut-off; doctor 2026-11-23): < 20 low, 20-40 medium, > 40 high; day: < 80 low, 80-120 medium, > 120 high */
    function glBand(gl, kind) {
        var g = Math.round(num(gl));
        if (kind === 'meal') return g < 20 ? 'low' : g <= 40 ? 'medium' : 'high';
        if (kind === 'day') return g < 80 ? 'low' : g <= 120 ? 'medium' : 'high';
        return g <= 10 ? 'low' : g < 20 ? 'medium' : 'high';
    }

    return {
        bmr: bmr, weightLossPlan: weightLossPlan, adjustedWeight: adjustedWeight, proteinWeight: proteinWeight,
        proteinPerKg: proteinPerKg, navyBodyFat: navyBodyFat, bodyFatBand: bodyFatBand, bodyFatRow: bodyFatRow,
        healthyWeightRange: healthyWeightRange, glycemicLoad: glycemicLoad, glBand: glBand, FLOOR: FLOOR,
        round: round, num: num, GLUCOSE_FACTOR: GLUCOSE_FACTOR,
        hba1cPercentToMmol: hba1cPercentToMmol, hba1cMmolToPercent: hba1cMmolToPercent, eagMgdl: eagMgdl, eagMmol: eagMmol,
        hba1cBand: hba1cBand, mgdlToMmol: mgdlToMmol, mmolToMgdl: mmolToMgdl, fastingGlucoseBand: fastingGlucoseBand,
        afterMealBand: afterMealBand,
        homaIr: homaIr, quicki: quicki, tyg: tyg, homaBand: homaBand, findrisc: findrisc, bmi: bmi
    };
});
