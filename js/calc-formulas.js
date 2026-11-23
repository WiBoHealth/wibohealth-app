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
    function eagMgdl(pct) { return 28.7 * num(pct) - 46.7; }
    function eagMmol(pct) { return eagMgdl(pct) / GLUCOSE_FACTOR; }
    /* band by HbA1c in mmol/mol: 'normal' < 39, 'prediabetes' 39-47 (ADA; NICE/WHO use 42-47), 'diabetes' >= 48 */
    function hba1cBand(mmol) {
        var m = num(mmol);
        if (!(m > 0)) return null;
        return m < 39 ? 'normal' : m < 48 ? 'prediabetes' : 'diabetes';
    }

    // ---------------------------------------------------------------- glucose
    function mgdlToMmol(mgdl) { return num(mgdl) / GLUCOSE_FACTOR; }
    function mmolToMgdl(mmol) { return num(mmol) * GLUCOSE_FACTOR; }
    /* fasting plasma glucose band (ADA): low < 3.9, normal 3.9-5.5, prediabetes 5.6-6.9, diabetes >= 7.0 mmol/L */
    function fastingGlucoseBand(mmol) {
        var m = num(mmol);
        if (!(m > 0)) return null;
        return m < 3.9 ? 'low' : m < 5.6 ? 'normal' : m < 7.0 ? 'prediabetes' : 'diabetes';
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

    return {
        round: round, num: num, GLUCOSE_FACTOR: GLUCOSE_FACTOR,
        hba1cPercentToMmol: hba1cPercentToMmol, hba1cMmolToPercent: hba1cMmolToPercent, eagMgdl: eagMgdl, eagMmol: eagMmol,
        hba1cBand: hba1cBand, mgdlToMmol: mgdlToMmol, mmolToMgdl: mmolToMgdl, fastingGlucoseBand: fastingGlucoseBand,
        homaIr: homaIr, quicki: quicki, tyg: tyg, homaBand: homaBand, findrisc: findrisc, bmi: bmi
    };
});
