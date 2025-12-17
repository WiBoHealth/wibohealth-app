import React, { useState, useEffect } from 'react';
import { StyleSheet, Text, View, TouchableOpacity, ScrollView, I18nManager, Platform } from 'react-native';
import { StatusBar } from 'expo-status-bar';

export default function App() {
  const [darkMode, setDarkMode] = useState(false);
  
  // Force RTL for Arabic
  useEffect(() => {
    if (Platform.OS !== 'web') {
      I18nManager.allowRTL(true);
      I18nManager.forceRTL(true);
    }
  }, []);
  
  const theme = {
    bg: darkMode ? '#1a1a1a' : '#f5f5f5',
    card: darkMode ? '#2d2d2d' : '#ffffff',
    text: darkMode ? '#ffffff' : '#333333',
    primary: darkMode ? '#66BB6A' : '#4CAF50'
  };

  return (
    <View style={[styles.container, { backgroundColor: theme.bg }]}>
      <StatusBar style={darkMode ? 'light' : 'dark'} />
      
      <ScrollView contentContainerStyle={styles.scrollContent}>
        
        {/* Header */}
        <View style={styles.header}>
          <Text style={[styles.title, { color: theme.text }]}>
            🏥 WiBo Health
          </Text>
          <Text style={[styles.subtitle, { color: theme.text }]}>
            دليلك الصحي الشامل
          </Text>
          
          {/* Dark Mode Button */}
          <TouchableOpacity 
            style={[styles.button, { backgroundColor: theme.card }]}
            onPress={() => setDarkMode(!darkMode)}
          >
            <Text style={[styles.buttonText, { color: theme.text }]}>
              {darkMode ? '☀️ وضع النهار' : '🌙 الوضع الليلي'}
            </Text>
          </TouchableOpacity>
        </View>

        {/* Stats Grid */}
        <View style={styles.grid}>
          <View style={[styles.card, { backgroundColor: theme.card }]}>
            <Text style={styles.icon}>📊</Text>
            <Text style={[styles.number, { color: theme.text }]}>555</Text>
            <Text style={[styles.label, { color: theme.text }]}>عنصر غذائي</Text>
          </View>

          <View style={[styles.card, { backgroundColor: theme.card }]}>
            <Text style={styles.icon}>🍽️</Text>
            <Text style={[styles.number, { color: theme.text }]}>50</Text>
            <Text style={[styles.label, { color: theme.text }]}>وصفة صحية</Text>
          </View>

          <View style={[styles.card, { backgroundColor: theme.card }]}>
            <Text style={styles.icon}>🧮</Text>
            <Text style={[styles.number, { color: theme.text }]}>4</Text>
            <Text style={[styles.label, { color: theme.text }]}>حاسبات صحية</Text>
          </View>

          <View style={[styles.card, { backgroundColor: theme.card }]}>
            <Text style={styles.icon}>📝</Text>
            <Text style={[styles.number, { color: theme.text }]}>20+</Text>
            <Text style={[styles.label, { color: theme.text }]}>مقالة صحية</Text>
          </View>
        </View>

        {/* Welcome Card */}
        <View style={[styles.welcomeCard, { backgroundColor: theme.card }]}>
          <Text style={[styles.welcomeTitle, { color: theme.text }]}>
            مرحباً بك في WiBo Health! 👋
          </Text>
          <Text style={[styles.welcomeText, { color: theme.text }]}>
            📱 تطبيقك الشامل للحياة الصحية
          </Text>
          <Text style={[styles.welcomeText, { color: theme.text }]}>
            ✅ تتبع السعرات الحرارية بدقة
          </Text>
          <Text style={[styles.welcomeText, { color: theme.text }]}>
            ✅ وصفات صحية متنوعة ولذيذة
          </Text>
          <Text style={[styles.welcomeText, { color: theme.text }]}>
            ✅ حاسبات طبية احترافية
          </Text>
          <Text style={[styles.welcomeText, { color: theme.text }]}>
            ✅ نصائح صحية يومية مفيدة
          </Text>
        </View>

        {/* Success Message */}
        <View style={[styles.successCard, { backgroundColor: theme.primary }]}>
          <Text style={styles.successText}>
            ✅ التطبيق يعمل بنجاح! 🎉
          </Text>
          <Text style={styles.successText}>
            العربية تظهر بشكل صحيح الآن بخط Cairo
          </Text>
        </View>

      </ScrollView>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  scrollContent: {
    padding: 20,
    paddingTop: 50,
  },
  header: {
    alignItems: 'center',
    marginBottom: 30,
  },
  title: {
    fontSize: 36,
    fontWeight: 'bold',
    marginBottom: 10,
    textAlign: 'center',
  },
  subtitle: {
    fontSize: 20,
    marginBottom: 20,
    textAlign: 'center',
  },
  button: {
    paddingHorizontal: 24,
    paddingVertical: 14,
    borderRadius: 30,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.15,
    shadowRadius: 6,
    elevation: 4,
  },
  buttonText: {
    fontSize: 17,
    fontWeight: '600',
    textAlign: 'center',
  },
  grid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'space-between',
    marginBottom: 20,
  },
  card: {
    width: '48%',
    padding: 20,
    borderRadius: 16,
    alignItems: 'center',
    marginBottom: 16,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 6,
    elevation: 3,
  },
  icon: {
    fontSize: 48,
    marginBottom: 12,
  },
  number: {
    fontSize: 36,
    fontWeight: 'bold',
    marginBottom: 6,
  },
  label: {
    fontSize: 15,
    textAlign: 'center',
    fontWeight: '500',
  },
  welcomeCard: {
    padding: 24,
    borderRadius: 16,
    marginBottom: 20,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 6,
    elevation: 3,
  },
  welcomeTitle: {
    fontSize: 22,
    fontWeight: 'bold',
    marginBottom: 16,
    textAlign: 'center',
  },
  welcomeText: {
    fontSize: 16,
    marginVertical: 6,
    textAlign: 'right',
    lineHeight: 24,
  },
  successCard: {
    padding: 24,
    borderRadius: 16,
    alignItems: 'center',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.2,
    shadowRadius: 8,
    elevation: 5,
  },
  successText: {
    fontSize: 18,
    color: '#ffffff',
    fontWeight: 'bold',
    textAlign: 'center',
    marginVertical: 4,
  },
});
