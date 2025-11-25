import React, { useState } from 'react';
import { View, Text, StyleSheet, TouchableOpacity, ScrollView } from 'react-native';

// Arabic texts as Unicode escape sequences
const TEXTS = {
  subtitle: '\u062f\u0644\u064a\u0644\u0643 \u0627\u0644\u0635\u062d\u064a \u0627\u0644\u0634\u0627\u0645\u0644', // دليلك الصحي الشامل
  darkMode: '\u0627\u0644\u0648\u0636\u0639 \u0627\u0644\u0644\u064a\u0644\u064a', // الوضع الليلي
  lightMode: '\u0627\u0644\u0648\u0636\u0639 \u0627\u0644\u0646\u0647\u0627\u0631\u064a', // الوضع النهاري
  foodItem: '\u0639\u0646\u0635\u0631 \u063a\u0630\u0627\u0626\u064a', // عنصر غذائي
  recipe: '\u0648\u0635\u0641\u0629 \u0635\u062d\u064a\u0629', // وصفة صحية
  calculator: '\u062d\u0627\u0633\u0628\u0627\u062a \u0635\u062d\u064a\u0629', // حاسبات صحية
  article: '\u0645\u0642\u0627\u0644\u0629 \u0635\u062d\u064a\u0629', // مقالة صحية
  features: '\u0627\u0644\u0645\u0645\u064a\u0632\u0627\u062a \u0627\u0644\u0631\u0626\u064a\u0633\u064a\u0629', // المميزات الرئيسية
  feature1: '\u2022 \u0628\u062d\u062b \u0645\u062a\u0642\u062f\u0645 \u0641\u064a \u0627\u0644\u0623\u0637\u0639\u0645\u0629', // • بحث متقدم في الأطعمة
  feature2: '\u2022 \u0648\u0635\u0641\u0627\u062a \u0635\u062d\u064a\u0629 \u0643\u0627\u0645\u0644\u0629', // • وصفات صحية كاملة
  feature3: '\u2022 \u062d\u0627\u0633\u0628\u0627\u062a \u0635\u062d\u064a\u0629 \u062f\u0642\u064a\u0642\u0629', // • حاسبات صحية دقيقة
  feature4: '\u2022 \u062f\u0639\u0645 \u0643\u0627\u0645\u0644 \u0644\u0644\u0639\u0631\u0628\u064a\u0629', // • دعم كامل للعربية
  clickHere: '\u0627\u0636\u0639\u0637 \u0647\u0646\u0627!', // اضغط هنا!
  success: '\u0627\u0644\u062a\u0637\u0628\u064a\u0642 \u064a\u0639\u0645\u0644 \u0628\u0646\u062c\u0627\u062d!', // التطبيق يعمل بنجاح!
  footer: '\u0645\u0635\u0645\u0645 \u0628\u062d\u0628 \u0644\u0635\u062d\u062a\u0643', // مصمم بحب لصحتك
};

export default function TestApp() {
  const [isDark, setIsDark] = useState(false);
  const [count, setCount] = useState(0);

  const theme = isDark ? {
    bg: '#0f172a',
    card: '#1e293b',
    text: '#f1f5f9',
    textSec: '#94a3b8',
  } : {
    bg: '#ffffff',
    card: '#f8fafc',
    text: '#111827',
    textSec: '#6b7280',
  };

  return (
    <ScrollView style={[styles.container, { backgroundColor: theme.bg }]}>
      {/* Header */}
      <View style={styles.header}>
        <Text style={styles.emoji}>🏥</Text>
        <Text style={[styles.title, { color: '#10b981' }]}>WiBo Health</Text>
        <Text style={[styles.subtitle, { color: theme.textSec }]}>
          {TEXTS.subtitle}
        </Text>
      </View>

      {/* Dark Mode */}
      <TouchableOpacity 
        style={[styles.button, { backgroundColor: theme.card }]}
        onPress={() => setIsDark(!isDark)}
      >
        <Text style={styles.buttonEmoji}>{isDark ? '☀️' : '🌙'}</Text>
        <Text style={[styles.buttonText, { color: theme.text }]}>
          {isDark ? TEXTS.lightMode : TEXTS.darkMode}
        </Text>
      </TouchableOpacity>

      {/* Stats */}
      <View style={styles.statsGrid}>
        <View style={[styles.statCard, { backgroundColor: theme.card }]}>
          <Text style={styles.statEmoji}>🍎</Text>
          <Text style={[styles.statNumber, { color: '#10b981' }]}>555</Text>
          <Text style={[styles.statLabel, { color: theme.textSec }]}>
            {TEXTS.foodItem}
          </Text>
        </View>

        <View style={[styles.statCard, { backgroundColor: theme.card }]}>
          <Text style={styles.statEmoji}>🍽️</Text>
          <Text style={[styles.statNumber, { color: '#f59e0b' }]}>50</Text>
          <Text style={[styles.statLabel, { color: theme.textSec }]}>
            {TEXTS.recipe}
          </Text>
        </View>

        <View style={[styles.statCard, { backgroundColor: theme.card }]}>
          <Text style={styles.statEmoji}>🧮</Text>
          <Text style={[styles.statNumber, { color: '#3b82f6' }]}>4</Text>
          <Text style={[styles.statLabel, { color: theme.textSec }]}>
            {TEXTS.calculator}
          </Text>
        </View>

        <View style={[styles.statCard, { backgroundColor: theme.card }]}>
          <Text style={styles.statEmoji}>📰</Text>
          <Text style={[styles.statNumber, { color: '#8b5cf6' }]}>20+</Text>
          <Text style={[styles.statLabel, { color: theme.textSec }]}>
            {TEXTS.article}
          </Text>
        </View>
      </View>

      {/* Features */}
      <View style={[styles.featureCard, { backgroundColor: theme.card }]}>
        <Text style={styles.featureEmoji}>✨</Text>
        <Text style={[styles.featureTitle, { color: theme.text }]}>
          {TEXTS.features}
        </Text>
        <Text style={[styles.featureText, { color: theme.textSec }]}>
          {TEXTS.feature1}{'\n'}
          {TEXTS.feature2}{'\n'}
          {TEXTS.feature3}{'\n'}
          {TEXTS.feature4}
        </Text>
      </View>

      {/* Counter */}
      <TouchableOpacity 
        style={styles.actionButton}
        onPress={() => setCount(count + 1)}
      >
        <Text style={styles.actionText}>
          {TEXTS.clickHere} ({count})
        </Text>
      </TouchableOpacity>

      {/* Success */}
      <View style={[styles.successCard, { backgroundColor: '#d1fae5' }]}>
        <Text style={styles.successEmoji}>✅</Text>
        <Text style={styles.successText}>
          {TEXTS.success}
        </Text>
      </View>

      {/* Footer */}
      <View style={styles.footer}>
        <Text style={[styles.footerText, { color: theme.textSec }]}>
          💚 {TEXTS.footer}
        </Text>
        <Text style={[styles.footerText, { color: theme.textSec }]}>
          WiBo Health © 2025
        </Text>
      </View>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  header: {
    alignItems: 'center',
    paddingTop: 60,
    paddingBottom: 20,
  },
  emoji: {
    fontSize: 64,
    marginBottom: 12,
  },
  title: {
    fontSize: 36,
    fontWeight: 'bold',
    marginBottom: 8,
  },
  subtitle: {
    fontSize: 20,
    textAlign: 'center',
  },
  button: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    padding: 16,
    marginHorizontal: 20,
    marginBottom: 24,
    borderRadius: 12,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 8,
    elevation: 3,
  },
  buttonEmoji: {
    fontSize: 24,
    marginLeft: 12,
  },
  buttonText: {
    fontSize: 18,
    fontWeight: '600',
  },
  statsGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    paddingHorizontal: 16,
    justifyContent: 'space-between',
  },
  statCard: {
    width: '48%',
    padding: 20,
    borderRadius: 16,
    alignItems: 'center',
    marginBottom: 16,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 8,
    elevation: 3,
  },
  statEmoji: {
    fontSize: 40,
    marginBottom: 8,
  },
  statNumber: {
    fontSize: 32,
    fontWeight: 'bold',
    marginBottom: 4,
  },
  statLabel: {
    fontSize: 16,
    textAlign: 'center',
  },
  featureCard: {
    marginHorizontal: 20,
    padding: 24,
    borderRadius: 16,
    marginBottom: 20,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 8,
    elevation: 3,
  },
  featureEmoji: {
    fontSize: 32,
    textAlign: 'center',
    marginBottom: 12,
  },
  featureTitle: {
    fontSize: 22,
    fontWeight: 'bold',
    textAlign: 'center',
    marginBottom: 16,
  },
  featureText: {
    fontSize: 16,
    lineHeight: 28,
    textAlign: 'right',
  },
  actionButton: {
    backgroundColor: '#10b981',
    marginHorizontal: 20,
    padding: 18,
    borderRadius: 12,
    alignItems: 'center',
    marginBottom: 20,
    shadowColor: '#10b981',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.3,
    shadowRadius: 12,
    elevation: 5,
  },
  actionText: {
    color: '#ffffff',
    fontSize: 18,
    fontWeight: 'bold',
  },
  successCard: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    marginHorizontal: 20,
    padding: 20,
    borderRadius: 12,
    marginBottom: 20,
  },
  successEmoji: {
    fontSize: 24,
    marginLeft: 12,
  },
  successText: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#10b981',
  },
  footer: {
    alignItems: 'center',
    paddingVertical: 30,
    gap: 8,
  },
  footerText: {
    fontSize: 14,
  },
});
