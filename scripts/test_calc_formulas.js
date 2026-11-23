/* Tests of js/calc-formulas.js against published reference values. Run: node scripts/test_calc_formulas.js
   (exit code 1 on any failure; run before publishing a calculator change). */
'use strict';
const C = require('../js/calc-formulas.js');
let fail = 0, n = 0;
function near(name, got, want, tol) {
    n++;
    if (!(Math.abs(got - want) <= tol)) { fail++; console.log(`FAIL ${name}: got ${got}, want ${want} ±${tol}`); }
}
function eq(name, got, want) {
    n++;
    if (JSON.stringify(got) !== JSON.stringify(want)) { fail++; console.log(`FAIL ${name}: got ${JSON.stringify(got)}, want ${JSON.stringify(want)}`); }
}

// HbA1c % <-> mmol/mol (IFCC/NGSP master equation; published conversion tables, e.g. GPnotebook / NHS)
for (const [pct, mmol] of [[5.7, 39], [6.0, 42], [6.5, 48], [7.0, 53], [8.0, 64], [9.0, 75], [10.0, 86], [11.0, 97]]) {
    near(`HbA1c ${pct}% -> mmol/mol`, Math.round(C.hba1cPercentToMmol(pct)), mmol, 0);
    near(`HbA1c ${mmol} mmol/mol -> %`, C.round(C.hba1cMmolToPercent(mmol), 1), pct, 0.05);
}
// eAG (ADA eAG/A1C calculator, ADAG): 6% -> 126, 7% -> 154, 8% -> 183, 9% -> 212 mg/dL
for (const [pct, mg] of [[6, 126], [7, 154], [8, 183], [9, 212], [10, 240]]) near(`eAG ${pct}%`, C.eagMgdl(pct), mg, 0.55);   // ADA rounds 125.5 to 126
near('eAG 7% mmol/L', C.round(C.eagMmol(7), 1), 8.6, 0.05);
eq('band 38', C.hba1cBand(38), 'normal'); eq('band 39', C.hba1cBand(39), 'prediabetes');
eq('band 47', C.hba1cBand(47), 'prediabetes'); eq('band 48', C.hba1cBand(48), 'diabetes');

// glucose: 100 mg/dL = 5.6, 126 = 7.0, 180 = 10.0, 70 = 3.9 mmol/L
for (const [mg, mm] of [[70, 3.9], [100, 5.6], [126, 7.0], [180, 10.0], [200, 11.1]]) {
    near(`${mg} mg/dL -> mmol/L`, C.round(C.mgdlToMmol(mg), 1), mm, 0.05);
    near(`${mm} mmol/L -> mg/dL`, Math.round(C.mmolToMgdl(mm)), mg, 1);
}
eq('fasting 3.8', C.fastingGlucoseBand(3.8), 'low'); eq('fasting 5.5', C.fastingGlucoseBand(5.5), 'normal');
eq('fasting 5.6', C.fastingGlucoseBand(5.6), 'prediabetes'); eq('fasting 7.0', C.fastingGlucoseBand(7.0), 'diabetes');

// HOMA-IR (Matthews 1985): insulin 10 uU/mL, glucose 5 mmol/L -> 2.22; MDCalc example insulin 15, glucose 100 mg/dL -> 3.7
near('HOMA 10/5', C.round(C.homaIr(10, 5), 2), 2.22, 0.005);
near('HOMA 15/100mg', C.round(C.homaIr(15, C.mgdlToMmol(100)), 1), 3.7, 0.05);
// QUICKI (Katz 2000): insulin 10, glucose 90 mg/dL -> 1/(1 + 1.954) = 0.339
near("QUICKI 10/90mg", C.quicki(10, C.mgdlToMmol(90)), 0.3385, 0.0005);
// TyG: TG 150 mg/dL, glucose 100 mg/dL -> ln(7500) = 8.92
near('TyG 150/100', C.round(C.tyg(150 / 88.57, C.mgdlToMmol(100)), 2), 8.92, 0.01);
eq('homa band', [C.homaBand(1.5), C.homaBand(2.5), C.homaBand(3.2)], ['low', 'borderline', 'high']);

// FINDRISC (Lindstrom 2003): point table and bands
eq('FINDRISC minimum', C.findrisc({ age: 30, bmi: 22, waist: 80, sex: 'm', active: true, vegDaily: true, bpMeds: false, highGlucose: false, family: 'none' }),
   { score: 0, band: 'low', risk: '1/100' });
eq('FINDRISC maximum', C.findrisc({ age: 70, bmi: 35, waist: 110, sex: 'm', active: false, vegDaily: false, bpMeds: true, highGlucose: true, family: 'first' }),
   { score: 26, band: 'veryhigh', risk: '1/2' });
eq('FINDRISC woman 12', C.findrisc({ age: 50, bmi: 27, waist: 85, sex: 'f', active: false, vegDaily: true, bpMeds: false, highGlucose: false, family: 'second' }).score, 11);
eq('FINDRISC bands', [6, 7, 11, 12, 14, 15, 20, 21].map(s => {
    // score s reached with age 0, high glucose 5 etc. is not needed: test band edges directly through the public function
    const base = { age: 30, bmi: 22, waist: 80, sex: 'm', active: true, vegDaily: true, bpMeds: false, highGlucose: false, family: 'none' };
    let left = s; const a = Object.assign({}, base);
    if (left >= 5) { a.highGlucose = true; left -= 5; }
    if (left >= 5) { a.family = 'first'; left -= 5; }
    if (left >= 4) { a.age = 70; left -= 4; }
    if (left >= 4) { a.waist = 110; left -= 4; }
    if (left >= 3) { a.bmi = 35; left -= 3; }
    if (left >= 2) { a.active = false; left -= 2; }
    if (left >= 2) { a.bpMeds = true; left -= 2; }
    if (left >= 1) { a.vegDaily = false; left -= 1; }
    return C.findrisc(a).band;
}), ['low', 'slight', 'slight', 'moderate', 'moderate', 'high', 'high', 'veryhigh']);
near('BMI 80kg/180cm', C.round(C.bmi(80, 180), 1), 24.7, 0.05);
near('comma decimals', C.hba1cPercentToMmol('7,0'), C.hba1cPercentToMmol(7), 1e-9);

console.log(`${n - fail}/${n} formula checks passed`);
process.exit(fail ? 1 : 0);
