/* Tests of js/calc-formulas.js against published reference values. Run: node scripts/test_calc_formulas.js
   (exit code 1 on any failure; run before publishing a calculator change). */
'use strict';
const C = require('../js/calc-formulas.js');
let fail = 0, n = 0;
function near(name, got, want, tol) {
    n++;
    if (!(Math.abs(got - want) <= tol)) { fail++; console.log(`FAIL ${name}: got ${got}, want ${want} ±${tol}`); }
}
function ok(name, cond) { eq(name, !!cond, true); }
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
// thresholds reached from the other unit (rounded the way labs report): ADA 126 / 100 / 70 mg/dL, OGTT 140 / 200, HbA1c 5.7 / 6.5 %
eq('126 mg/dL fasting = diabetes', C.fastingGlucoseBand(C.mgdlToMmol(126)), 'diabetes');
eq('125 mg/dL fasting = prediabetes', C.fastingGlucoseBand(C.mgdlToMmol(125)), 'prediabetes');
eq('100 mg/dL fasting = prediabetes', C.fastingGlucoseBand(C.mgdlToMmol(100)), 'prediabetes');
eq('99 mg/dL fasting = normal', C.fastingGlucoseBand(C.mgdlToMmol(99)), 'normal');
eq('70 mg/dL fasting = normal', C.fastingGlucoseBand(C.mgdlToMmol(70)), 'normal');
eq('69 mg/dL = low', C.fastingGlucoseBand(C.mgdlToMmol(69)), 'low');
eq('139 mg/dL after = normal', C.afterMealBand(C.mgdlToMmol(139)), 'normal');
eq('140 mg/dL after = raised', C.afterMealBand(C.mgdlToMmol(140)), 'prediabetes');
eq('200 mg/dL after = diabetes', C.afterMealBand(C.mgdlToMmol(200)), 'diabetes');
eq('eAG 6% rounds to 126 (ADA table)', Math.round(C.eagMgdl(6)), 126);
eq('6.9 mmol/L fasting = prediabetes', C.fastingGlucoseBand(6.9), 'prediabetes');
eq('5.5 mmol/L fasting = normal', C.fastingGlucoseBand(5.5), 'normal');
eq('38 mmol/mol = normal', C.hba1cBand(38), 'normal');
eq('47 mmol/mol = prediabetes', C.hba1cBand(47), 'prediabetes');
eq('7.7 mmol/L after = normal', C.afterMealBand(7.7), 'normal');
eq('199 mg/dL after = raised', C.afterMealBand(C.mgdlToMmol(199)), 'prediabetes');
eq('11.0 mmol/L after = raised', C.afterMealBand(11.0), 'prediabetes');
eq('5.6% = normal', C.hba1cBand(C.hba1cPercentToMmol(5.6)), 'normal');
eq('5.7% = prediabetes', C.hba1cBand(C.hba1cPercentToMmol(5.7)), 'prediabetes');
eq('6.4% = prediabetes', C.hba1cBand(C.hba1cPercentToMmol(6.4)), 'prediabetes');
eq('6.5% = diabetes', C.hba1cBand(C.hba1cPercentToMmol(6.5)), 'diabetes');
near('BMI 80kg/180cm', C.round(C.bmi(80, 180), 1), 24.7, 0.05);
near('comma decimals', C.hba1cPercentToMmol('7,0'), C.hba1cPercentToMmol(7), 1e-9);

// ---- batch C (2026-11-23)
// Mifflin-St Jeor worked example on the TDEE page: woman 34 y, 68 kg, 165 cm -> BMR 1380.25, x1.55 = 2139
near('BMR woman 34/68/165', C.bmr('f', 34, 68, 165), 1380.25, 1e-9);
near('BMR man 40/80/180', C.bmr('m', 40, 80, 180), 1730, 1e-9);
let plan = C.weightLossPlan({ sex: 'f', age: 34, height: 165, weight: 68, target: 60, pal: 1.55, pace: 0.5 });
eq('plan: calories = TDEE - 550, rounded to 10', plan.intake, 1590);
ok('plan: 8 kg at 0.5 kg/week takes 16-20 weeks (slower than straight line)', plan.weeks >= 16 && plan.weeks <= 20 && plan.reached);
plan = C.weightLossPlan({ sex: 'f', age: 60, height: 155, weight: 62, target: 55, pal: 1.2, pace: 0.75 });
eq('plan: floor 1200 for women', plan.intake, 1200);
ok('plan: floor flagged, fast pace flagged', plan.floorApplied && plan.fastPace);
plan = C.weightLossPlan({ sex: 'm', age: 30, height: 180, weight: 70, target: 68, pal: 1.2, pace: 0.75 });
eq('plan: floor 1500 for men', plan.intake, 1500);
plan = C.weightLossPlan({ sex: 'm', age: 45, height: 175, weight: 130, target: 85, pal: 1.2, pace: 0.5 });
ok('plan: below-BMR note for a large weight', plan.belowBmr && plan.reached);
ok('plan: target above weight is not a plan', !C.weightLossPlan({ sex: 'f', age: 30, height: 165, weight: 60, target: 65, pal: 1.2, pace: 0.5 }).reached);
near('plan: target BMI', C.weightLossPlan({ sex: 'f', age: 30, height: 160, weight: 60, target: 46, pal: 1.2, pace: 0.5 }).targetBmi, 17.97, 0.01);
// adjusted weight (doctor): weight at BMI 25 + 25% of the difference, only from BMI 30
near('adjusted weight 120 kg / 170 cm', C.adjustedWeight(120, 170), 84.19, 0.01);
near('protein weight BMI 29.9 = actual', C.proteinWeight(86.4, 170), 86.4, 1e-9);
near('protein weight BMI 41.5 = adjusted', C.proteinWeight(120, 170), 84.19, 0.01);
eq('protein loss 1.2-1.6', C.proteinPerKg('loss', 40).join('-'), '1.2-1.6');
eq('protein GLP-1 1.2-1.6', C.proteinPerKg('glp1', 40).join('-'), '1.2-1.6');
eq('protein general 0.83', C.proteinPerKg('general', 40).join('-'), '0.83-0.83');
eq('protein general 65+ 1.0-1.2', C.proteinPerKg('general', 65).join('-'), '1-1.2');
eq('protein muscle 1.6-2.2', C.proteinPerKg('muscle', 25).join('-'), '1.6-2.2');
// US Navy, cm equations agree with the original inch equations (Hodgdon & Beckett 1984) within 0.5 point
const inchM = (h, n, w) => 86.010 * Math.log10((w - n) / 2.54) - 70.041 * Math.log10(h / 2.54) + 36.76;
const inchF = (h, n, w, hip) => 163.205 * Math.log10((w + hip - n) / 2.54) - 97.684 * Math.log10(h / 2.54) - 78.387;
near('Navy man 178/38/90 vs inch formula', C.navyBodyFat('m', 178, 38, 90), inchM(178, 38, 90), 0.5);
near('Navy man 185/40/105 vs inch formula', C.navyBodyFat('m', 185, 40, 105), inchM(185, 40, 105), 0.5);
near('Navy woman 165/33/80/100 vs inch formula', C.navyBodyFat('f', 165, 33, 80, 100), inchF(165, 33, 80, 100), 0.5);
near('Navy woman 160/32/95/110 vs inch formula', C.navyBodyFat('f', 160, 32, 95, 110), inchF(160, 32, 95, 110), 0.5);
ok('Navy: waist not above neck is not a result', isNaN(C.navyBodyFat('m', 178, 40, 39)));
// Gallagher 2000 bands + essential-fat limits (doctor)
eq('man 30 y 4.9% very low', C.bodyFatBand('m', 30, 4.9), 'verylow');
eq('man 30 y 5% low', C.bodyFatBand('m', 30, 5), 'low');
eq('man 30 y 8% healthy', C.bodyFatBand('m', 30, 8), 'healthy');
eq('man 30 y 19.9% healthy', C.bodyFatBand('m', 30, 19.9), 'healthy');
eq('man 30 y 20% high', C.bodyFatBand('m', 30, 20), 'high');
eq('man 30 y 25% very high', C.bodyFatBand('m', 30, 25), 'veryhigh');
eq('man 50 y 21% healthy', C.bodyFatBand('m', 50, 21), 'healthy');
eq('man 70 y 12% low', C.bodyFatBand('m', 70, 12), 'low');
eq('woman 30 y 12.9% very low', C.bodyFatBand('f', 30, 12.9), 'verylow');
eq('woman 30 y 20% low', C.bodyFatBand('f', 30, 20), 'low');
eq('woman 30 y 21% healthy', C.bodyFatBand('f', 30, 21), 'healthy');
eq('woman 45 y 33.9% healthy', C.bodyFatBand('f', 45, 33.9), 'healthy');
eq('woman 65 y 41% high', C.bodyFatBand('f', 65, 41), 'high');
eq('woman 65 y 42% very high', C.bodyFatBand('f', 65, 42), 'veryhigh');
near('healthy weight 170 cm low', C.healthyWeightRange(170)[0], 53.465, 0.001);
near('healthy weight 170 cm high', C.healthyWeightRange(170)[1], 71.961, 0.001);
// glycemic load: white rice GI 65, 28 g carbs and 0.4 g fibre per 100 g, 150 g -> 26.9
near('GL white rice 150 g', C.glycemicLoad(65, 28, 0.4, 150), 26.91, 0.01);
near('GL watermelon 120 g (GI 72, 7.6 g carbs, 0.4 fibre)', C.glycemicLoad(72, 7.6, 0.4, 120), 6.22, 0.01);
eq('GL no carbs = 0', C.glycemicLoad(null, 0, 0, 200), 0);
eq('GL food 10 low', C.glBand(10), 'low'); eq('GL food 11 medium', C.glBand(11), 'medium');
eq('GL food 19 medium', C.glBand(19), 'medium'); eq('GL food 20 high', C.glBand(20), 'high');
eq('GL meal 19 low', C.glBand(19, 'meal'), 'low'); eq('GL meal 20 medium', C.glBand(20, 'meal'), 'medium');
eq('GL meal 40 medium', C.glBand(40, 'meal'), 'medium'); eq('GL meal 41 high', C.glBand(41, 'meal'), 'high');
eq('GL day 79 low', C.glBand(79, 'day'), 'low'); eq('GL day 120 medium', C.glBand(120, 'day'), 'medium');
eq('GL day 121 high', C.glBand(121, 'day'), 'high');

console.log(`${n - fail}/${n} formula checks passed`);
process.exit(fail ? 1 : 0);
