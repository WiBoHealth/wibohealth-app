import React, { useState } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TextInput,
  TouchableOpacity,
} from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import COLORS from '../styles/colors';

export default function CalculatorsScreen({ isDarkMode }) {
  const [selectedCalculator, setSelectedCalculator] = useState('BMI');
  const [weight, setWeight] = useState('');
  const [height, setHeight] = useState('');
  const [age, setAge] = useState('');
  const [gender, setGender] = useState('male');
  const [result, setResult] = useState(null);

  const theme = isDarkMode ? COLORS.dark : COLORS.light;

  const calculators = [
    { id: 'BMI', name: 'مؤشر كتلة الجسم', icon: 'body', color: COLORS.primary },
    { id: 'BMR', name: 'معدل الأيض', icon: 'flame', color: '#f59e0b' },
    { id: 'Calories', name: 'السعرات اليومية', icon: 'restaurant', color: '#3b82f6' },
    { id: 'Water', name: 'احتياج الماء', icon: 'water', color: '#06b6d4' },
  ];

  const calculateBMI = () => {
    const w = parseFloat(weight);
    const h = parseFloat(height) / 100;
    if (w && h) {
      const bmi = (w / (h * h)).toFixed(1);
      let category = '';
      let color = '';
      
      if (bmi < 18.5) {
        category = 'نحيف';
        color = '#3b82f6';
      } else if (bmi < 25) {
        category = 'وزن طبيعي';
        color = COLORS.success;
      } else if (bmi < 30) {
        category = 'وزن زائد';
        color = '#f59e0b';
      } else {
        category = 'سمنة';
        color = '#ef4444';
      }
      
      setResult({ value: bmi, category, color, unit: '' });
    }
  };

  const calculateBMR = () => {
    const w = parseFloat(weight);
    const h = parseFloat(height);
    const a = parseFloat(age);
    
    if (w && h && a) {
      let bmr;
      if (gender === 'male') {
        bmr = (10 * w + 6.25 * h - 5 * a + 5).toFixed(0);
      } else {
        bmr = (10 * w + 6.25 * h - 5 * a - 161).toFixed(0);
      }
      setResult({
        value: bmr,
        category: 'سعرة حرارية / يوم',
        color: COLORS.primary,
        unit: 'كالوري',
      });
    }
  };

  const calculateCalories = () => {
    // نفس حساب BMR مع إضافة مستوى النشاط
    const w = parseFloat(weight);
    const h = parseFloat(height);
    const a = parseFloat(age);
    
    if (w && h && a) {
      let bmr;
      if (gender === 'male') {
        bmr = 10 * w + 6.25 * h - 5 * a + 5;
      } else {
        bmr = 10 * w + 6.25 * h - 5 * a - 161;
      }
      // نشاط متوسط (× 1.55)
      const calories = (bmr * 1.55).toFixed(0);
      setResult({
        value: calories,
        category: 'مع نشاط متوسط',
        color: COLORS.primary,
        unit: 'كالوري/يوم',
      });
    }
  };

  const calculateWater = () => {
    const w = parseFloat(weight);
    if (w) {
      const water = (w * 35 / 1000).toFixed(1);
      setResult({
        value: water,
        category: 'احتياج يومي',
        color: '#06b6d4',
        unit: 'لتر',
      });
    }
  };

  const handleCalculate = () => {
    switch (selectedCalculator) {
      case 'BMI':
        calculateBMI();
        break;
      case 'BMR':
        calculateBMR();
        break;
      case 'Calories':
        calculateCalories();
        break;
      case 'Water':
        calculateWater();
        break;
    }
  };

  const resetInputs = () => {
    setWeight('');
    setHeight('');
    setAge('');
    setResult(null);
  };

  return (
    <ScrollView
      style={[styles.container, { backgroundColor: theme.background }]}
      contentContainerStyle={styles.contentContainer}
    >
      {/* Calculator Tabs */}
      <ScrollView
        horizontal
        inverted
        showsHorizontalScrollIndicator={false}
        contentContainerStyle={styles.tabsContainer}
      >
        {calculators.map((calc) => (
          <TouchableOpacity
            key={calc.id}
            style={[
              styles.tab,
              {
                backgroundColor:
                  selectedCalculator === calc.id ? calc.color : theme.card,
                borderColor: theme.border,
              },
              isDarkMode && selectedCalculator !== calc.id && styles.tabDark,
            ]}
            onPress={() => {
              setSelectedCalculator(calc.id);
              resetInputs();
            }}
          >
            <Ionicons
              name={calc.icon}
              size={20}
              color={selectedCalculator === calc.id ? COLORS.white : theme.text}
            />
            <Text
              style={[
                styles.tabText,
                {
                  color:
                    selectedCalculator === calc.id ? COLORS.white : theme.text,
                },
              ]}
            >
              {calc.name}
            </Text>
          </TouchableOpacity>
        ))}
      </ScrollView>

      {/* Input Form */}
      <View
        style={[
          styles.formCard,
          { backgroundColor: theme.card },
          isDarkMode && styles.formCardDark,
        ]}
      >
        <Text style={[styles.formTitle, { color: theme.text }]}>
          أدخل البيانات
        </Text>

        {/* Weight Input */}
        <View style={styles.inputGroup}>
          <Text style={[styles.inputLabel, { color: theme.text }]}>
            الوزن (كجم)
          </Text>
          <TextInput
            style={[
              styles.input,
              {
                backgroundColor: theme.background,
                color: theme.text,
                borderColor: theme.border,
              },
            ]}
            placeholder="مثال: 70"
            placeholderTextColor={theme.textSecondary}
            keyboardType="numeric"
            value={weight}
            onChangeText={setWeight}
          />
        </View>

        {/* Height Input (not for Water calculator) */}
        {selectedCalculator !== 'Water' && (
          <View style={styles.inputGroup}>
            <Text style={[styles.inputLabel, { color: theme.text }]}>
              الطول (سم)
            </Text>
            <TextInput
              style={[
                styles.input,
                {
                  backgroundColor: theme.background,
                  color: theme.text,
                  borderColor: theme.border,
                },
              ]}
              placeholder="مثال: 175"
              placeholderTextColor={theme.textSecondary}
              keyboardType="numeric"
              value={height}
              onChangeText={setHeight}
            />
          </View>
        )}

        {/* Age Input (for BMR and Calories) */}
        {(selectedCalculator === 'BMR' || selectedCalculator === 'Calories') && (
          <View style={styles.inputGroup}>
            <Text style={[styles.inputLabel, { color: theme.text }]}>
              العمر (سنة)
            </Text>
            <TextInput
              style={[
                styles.input,
                {
                  backgroundColor: theme.background,
                  color: theme.text,
                  borderColor: theme.border,
                },
              ]}
              placeholder="مثال: 30"
              placeholderTextColor={theme.textSecondary}
              keyboardType="numeric"
              value={age}
              onChangeText={setAge}
            />
          </View>
        )}

        {/* Gender Selection (for BMR and Calories) */}
        {(selectedCalculator === 'BMR' || selectedCalculator === 'Calories') && (
          <View style={styles.inputGroup}>
            <Text style={[styles.inputLabel, { color: theme.text }]}>
              الجنس
            </Text>
            <View style={styles.genderButtons}>
              <TouchableOpacity
                style={[
                  styles.genderButton,
                  {
                    backgroundColor:
                      gender === 'male' ? COLORS.primary : theme.background,
                    borderColor: theme.border,
                  },
                ]}
                onPress={() => setGender('male')}
              >
                <Text
                  style={[
                    styles.genderButtonText,
                    { color: gender === 'male' ? COLORS.white : theme.text },
                  ]}
                >
                  ذكر
                </Text>
              </TouchableOpacity>
              <TouchableOpacity
                style={[
                  styles.genderButton,
                  {
                    backgroundColor:
                      gender === 'female' ? COLORS.primary : theme.background,
                    borderColor: theme.border,
                  },
                ]}
                onPress={() => setGender('female')}
              >
                <Text
                  style={[
                    styles.genderButtonText,
                    { color: gender === 'female' ? COLORS.white : theme.text },
                  ]}
                >
                  أنثى
                </Text>
              </TouchableOpacity>
            </View>
          </View>
        )}

        {/* Calculate Button */}
        <TouchableOpacity
          style={[
            styles.calculateButton,
            { backgroundColor: COLORS.primary },
          ]}
          onPress={handleCalculate}
        >
          <Ionicons name="calculator" size={20} color={COLORS.white} />
          <Text style={styles.calculateButtonText}>احسب</Text>
        </TouchableOpacity>
      </View>

      {/* Result Card */}
      {result && (
        <View
          style={[
            styles.resultCard,
            { backgroundColor: theme.card },
            isDarkMode && styles.resultCardDark,
          ]}
        >
          <Text style={[styles.resultTitle, { color: theme.text }]}>
            النتيجة
          </Text>
          <View
            style={[
              styles.resultValueContainer,
              { backgroundColor: result.color + '20' },
            ]}
          >
            <Text style={[styles.resultValue, { color: result.color }]}>
              {result.value}
            </Text>
            {result.unit && (
              <Text style={[styles.resultUnit, { color: result.color }]}>
                {result.unit}
              </Text>
            )}
          </View>
          <Text style={[styles.resultCategory, { color: theme.textSecondary }]}>
            {result.category}
          </Text>
        </View>
      )}
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  contentContainer: {
    padding: 16,
  },
  tabsContainer: {
    paddingBottom: 16,
  },
  tab: {
    flexDirection: 'row-reverse',
    alignItems: 'center',
    paddingHorizontal: 16,
    paddingVertical: 12,
    borderRadius: 12,
    marginLeft: 8,
    borderWidth: 1,
  },
  tabDark: {
    borderColor: COLORS.dark.border,
  },
  tabText: {
    fontSize: 14,
    fontWeight: '600',
    marginRight: 8,
  },
  formCard: {
    padding: 20,
    borderRadius: 12,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 3,
    marginBottom: 16,
  },
  formCardDark: {
    borderWidth: 1,
    borderColor: COLORS.dark.border,
  },
  formTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    textAlign: 'right',
    marginBottom: 20,
  },
  inputGroup: {
    marginBottom: 16,
  },
  inputLabel: {
    fontSize: 14,
    fontWeight: '600',
    textAlign: 'right',
    marginBottom: 8,
  },
  input: {
    height: 48,
    borderRadius: 8,
    paddingHorizontal: 16,
    fontSize: 16,
    textAlign: 'right',
    borderWidth: 1,
  },
  genderButtons: {
    flexDirection: 'row-reverse',
    gap: 8,
  },
  genderButton: {
    flex: 1,
    paddingVertical: 12,
    borderRadius: 8,
    alignItems: 'center',
    borderWidth: 1,
  },
  genderButtonText: {
    fontSize: 16,
    fontWeight: '600',
  },
  calculateButton: {
    flexDirection: 'row-reverse',
    alignItems: 'center',
    justifyContent: 'center',
    paddingVertical: 14,
    borderRadius: 8,
    marginTop: 8,
  },
  calculateButtonText: {
    color: COLORS.white,
    fontSize: 16,
    fontWeight: 'bold',
    marginRight: 8,
  },
  resultCard: {
    padding: 24,
    borderRadius: 12,
    alignItems: 'center',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 3,
  },
  resultCardDark: {
    borderWidth: 1,
    borderColor: COLORS.dark.border,
  },
  resultTitle: {
    fontSize: 16,
    fontWeight: '600',
    marginBottom: 16,
  },
  resultValueContainer: {
    paddingHorizontal: 32,
    paddingVertical: 16,
    borderRadius: 16,
    marginBottom: 12,
    flexDirection: 'row',
    alignItems: 'baseline',
  },
  resultValue: {
    fontSize: 48,
    fontWeight: 'bold',
  },
  resultUnit: {
    fontSize: 20,
    fontWeight: '600',
    marginLeft: 8,
  },
  resultCategory: {
    fontSize: 16,
  },
});
