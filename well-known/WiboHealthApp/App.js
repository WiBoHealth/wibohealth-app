import React, { useState, useEffect } from 'react';
import { StyleSheet, Text, View, TouchableOpacity, ScrollView, Platform, I18nManager } from 'react-native';
import { strings } from './strings';

export default function App() {
  const [darkMode, setDarkMode] = useState(false);
  
  // Force RTL for Arabic
  useEffect(() => {
    if (Platform.OS !== 'web') {
      I18nManager.allowRTL(true);
      I18nManager.forceRTL(true);
    }
  }, []);
  
  const theme = darkMode ? darkTheme : lightTheme;

  return (
    <View style={[styles.container, { backgroundColor: theme.background }]}>
      <ScrollView style={styles.scrollView}>
        {/* Header */}
        <View style={styles.header}>
          <Text style={[styles.title, { color: theme.text }]}>
            🏥 {strings.app.name}
          </Text>
          <Text style={[styles.subtitle, { color: theme.text }]}>
            {strings.app.subtitle}
          </Text>
          
          {/* Dark Mode Toggle */}
          <TouchableOpacity 
            style={[styles.darkModeButton, { backgroundColor: theme.card }]}
            onPress={() => setDarkMode(!darkMode)}
          >
            <Text style={styles.darkModeText}>
              {darkMode ? `☀️ ${strings.darkMode.light}` : `🌙 ${strings.darkMode.dark}`}
            </Text>
          </TouchableOpacity>
        </View>

        {/* Stats Cards */}
        <View style={styles.statsContainer}>
          <View style={[styles.statCard, { backgroundColor: theme.card }]}>
            <Text style={styles.statIcon}>📊</Text>
            <Text style={[styles.statNumber, { color: theme.text }]}>555</Text>
            <Text style={[styles.statLabel, { color: theme.text }]}>
              {strings.stats.foods}
            </Text>
          </View>

          <View style={[styles.statCard, { backgroundColor: theme.card }]}>
            <Text style={styles.statIcon}>🍽️</Text>
            <Text style={[styles.statNumber, { color: theme.text }]}>50</Text>
            <Text style={[styles.statLabel, { color: theme.text }]}>
              {strings.stats.recipes}
            </Text>
          </View>

          <View style={[styles.statCard, { backgroundColor: theme.card }]}>
            <Text style={styles.statIcon}>🧮</Text>
            <Text style={[styles.statNumber, { color: theme.text }]}>4</Text>
            <Text style={[styles.statLabel, { color: theme.text }]}>
              {strings.stats.calculators}
            </Text>
          </View>

          <View style={[styles.statCard, { backgroundColor: theme.card }]}>
            <Text style={styles.statIcon}>📝</Text>
            <Text style={[styles.statNumber, { color: theme.text }]}>20+</Text>
            <Text style={[styles.statLabel, { color: theme.text }]}>
              {strings.stats.articles}
            </Text>
          </View>
        </View>

        {/* Welcome Card */}
        <View style={[styles.welcomeCard, { backgroundColor: theme.card }]}>
          <Text style={[styles.welcomeTitle, { color: theme.text }]}>
            {strings.app.welcome} 👋
          </Text>
          <Text style={[styles.welcomeText, { color: theme.text }]}>
            📱 {strings.app.description}
          </Text>
          <Text style={[styles.welcomeText, { color: theme.text }]}>
            ✅ {strings.features.calories}
          </Text>
          <Text style={[styles.welcomeText, { color: theme.text }]}>
            ✅ {strings.features.recipes}
          </Text>
          <Text style={[styles.welcomeText, { color: theme.text }]}>
            ✅ {strings.features.calculators}
          </Text>
          <Text style={[styles.welcomeText, { color: theme.text }]}>
            ✅ {strings.features.tips}
          </Text>
        </View>

        {/* Success Message */}
        <View style={styles.successContainer}>
          <Text style={styles.successText}>
            ✅ {strings.success.title} 🎉
          </Text>
          <Text style={styles.successText}>
            {strings.success.message}
          </Text>
        </View>

      </ScrollView>
    </View>
  );
}

const lightTheme = {
  background: '#f5f5f5',
  card: '#ffffff',
  text: '#333333',
  primary: '#4CAF50'
};

const darkTheme = {
  background: '#1a1a1a',
  card: '#2d2d2d',
  text: '#ffffff',
  primary: '#66BB6A'
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    paddingTop: Platform.OS === 'ios' ? 50 : 30,
  },
  scrollView: {
    flex: 1,
  },
  header: {
    padding: 20,
    alignItems: 'center',
  },
  title: {
    fontSize: 32,
    fontWeight: 'bold',
    marginBottom: 8,
    textAlign: 'center',
  },
  subtitle: {
    fontSize: 18,
    marginBottom: 20,
    textAlign: 'center',
  },
  darkModeButton: {
    paddingHorizontal: 20,
    paddingVertical: 12,
    borderRadius: 25,
    marginTop: 10,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 3,
  },
  darkModeText: {
    fontSize: 16,
    textAlign: 'center',
  },
  statsContainer: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    padding: 10,
    justifyContent: 'space-around',
  },
  statCard: {
    width: '45%',
    padding: 20,
    borderRadius: 15,
    alignItems: 'center',
    marginVertical: 8,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 3,
  },
  statIcon: {
    fontSize: 40,
    marginBottom: 10,
  },
  statNumber: {
    fontSize: 32,
    fontWeight: 'bold',
    marginBottom: 5,
  },
  statLabel: {
    fontSize: 16,
    textAlign: 'center',
  },
  welcomeCard: {
    margin: 15,
    padding: 20,
    borderRadius: 15,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 3,
  },
  welcomeTitle: {
    fontSize: 22,
    fontWeight: 'bold',
    marginBottom: 15,
    textAlign: 'center',
  },
  welcomeText: {
    fontSize: 16,
    marginVertical: 5,
    textAlign: 'right',
  },
  successContainer: {
    margin: 15,
    padding: 20,
    backgroundColor: '#4CAF50',
    borderRadius: 15,
  },
  successText: {
    fontSize: 18,
    color: '#ffffff',
    textAlign: 'center',
    fontWeight: 'bold',
  },
});
