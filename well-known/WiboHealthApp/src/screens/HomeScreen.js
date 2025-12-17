import React from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  Dimensions,
} from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import COLORS from '../styles/colors';

const { width } = Dimensions.get('window');

export default function HomeScreen({ isDarkMode, toggleDarkMode }) {
  const theme = isDarkMode ? COLORS.dark : COLORS.light;

  const stats = [
    { icon: 'restaurant', count: '555', label: 'عنصر غذائي', color: COLORS.primary },
    { icon: 'book', count: '50', label: 'وصفة صحية', color: '#f59e0b' },
    { icon: 'calculator', count: '4', label: 'حاسبات صحية', color: '#3b82f6' },
    { icon: 'document-text', count: '20+', label: 'مقالة صحية', color: '#8b5cf6' },
  ];

  const features = [
    {
      icon: 'search',
      title: 'بحث متقدم',
      description: 'ابحث في 555 عنصر غذائي بسهولة',
      color: COLORS.primary,
    },
    {
      icon: 'nutrition',
      title: 'قيم غذائية كاملة',
      description: 'معلومات دقيقة عن السعرات والبروتين',
      color: '#f59e0b',
    },
    {
      icon: 'fitness',
      title: 'حاسبات صحية',
      description: 'BMI, BMR, السعرات، الماء',
      color: '#3b82f6',
    },
    {
      icon: 'moon',
      title: 'وضع ليلي',
      description: 'راحة للعينين في الإضاءة الخافتة',
      color: '#8b5cf6',
    },
  ];

  return (
    <ScrollView
      style={[styles.container, { backgroundColor: theme.background }]}
      contentContainerStyle={styles.contentContainer}
    >
      {/* Header */}
      <View style={styles.header}>
        <View>
          <Text style={[styles.welcomeText, { color: theme.text }]}>
            مرحباً بك في
          </Text>
          <Text style={[styles.appName, { color: COLORS.primary }]}>
            WiBo Health 🏥
          </Text>
          <Text style={[styles.subtitle, { color: theme.textSecondary }]}>
            دليلك الصحي الشامل
          </Text>
        </View>
        
        <TouchableOpacity
          style={[styles.darkModeButton, { backgroundColor: theme.card }]}
          onPress={toggleDarkMode}
        >
          <Ionicons
            name={isDarkMode ? 'sunny' : 'moon'}
            size={24}
            color={isDarkMode ? '#f59e0b' : '#8b5cf6'}
          />
        </TouchableOpacity>
      </View>

      {/* Stats Cards */}
      <View style={styles.statsContainer}>
        {stats.map((stat, index) => (
          <View
            key={index}
            style={[
              styles.statCard,
              { backgroundColor: theme.card },
              isDarkMode && styles.statCardDark,
            ]}
          >
            <View style={[styles.statIcon, { backgroundColor: stat.color + '20' }]}>
              <Ionicons name={stat.icon} size={28} color={stat.color} />
            </View>
            <Text style={[styles.statCount, { color: theme.text }]}>
              {stat.count}
            </Text>
            <Text style={[styles.statLabel, { color: theme.textSecondary }]}>
              {stat.label}
            </Text>
          </View>
        ))}
      </View>

      {/* Features */}
      <Text style={[styles.sectionTitle, { color: theme.text }]}>
        ✨ المميزات
      </Text>

      {features.map((feature, index) => (
        <View
          key={index}
          style={[
            styles.featureCard,
            { backgroundColor: theme.card },
            isDarkMode && styles.featureCardDark,
          ]}
        >
          <View style={[styles.featureIcon, { backgroundColor: feature.color + '20' }]}>
            <Ionicons name={feature.icon} size={24} color={feature.color} />
          </View>
          <View style={styles.featureContent}>
            <Text style={[styles.featureTitle, { color: theme.text }]}>
              {feature.title}
            </Text>
            <Text style={[styles.featureDescription, { color: theme.textSecondary }]}>
              {feature.description}
            </Text>
          </View>
        </View>
      ))}

      {/* Quick Actions */}
      <Text style={[styles.sectionTitle, { color: theme.text }]}>
        🚀 ابدأ الآن
      </Text>

      <TouchableOpacity
        style={[styles.actionButton, { backgroundColor: COLORS.primary }]}
      >
        <Ionicons name="search" size={24} color={COLORS.white} />
        <Text style={styles.actionButtonText}>ابحث عن طعام</Text>
      </TouchableOpacity>

      <TouchableOpacity
        style={[styles.actionButton, { backgroundColor: '#f59e0b' }]}
      >
        <Ionicons name="book" size={24} color={COLORS.white} />
        <Text style={styles.actionButtonText}>تصفح الوصفات</Text>
      </TouchableOpacity>

      <TouchableOpacity
        style={[styles.actionButton, { backgroundColor: '#3b82f6' }]}
      >
        <Ionicons name="calculator" size={24} color={COLORS.white} />
        <Text style={styles.actionButtonText}>احسب مؤشر كتلة جسمك</Text>
      </TouchableOpacity>

      {/* Footer */}
      <View style={styles.footer}>
        <Text style={[styles.footerText, { color: theme.textSecondary }]}>
          💚 مصمم بحب لصحتك
        </Text>
        <Text style={[styles.footerText, { color: theme.textSecondary }]}>
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
  contentContainer: {
    padding: 16,
  },
  header: {
    flexDirection: 'row-reverse',
    justifyContent: 'space-between',
    alignItems: 'flex-start',
    marginBottom: 24,
  },
  welcomeText: {
    fontSize: 16,
    textAlign: 'right',
  },
  appName: {
    fontSize: 32,
    fontWeight: 'bold',
    textAlign: 'right',
    marginVertical: 4,
  },
  subtitle: {
    fontSize: 14,
    textAlign: 'right',
  },
  darkModeButton: {
    width: 48,
    height: 48,
    borderRadius: 24,
    alignItems: 'center',
    justifyContent: 'center',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 3,
  },
  statsContainer: {
    flexDirection: 'row-reverse',
    flexWrap: 'wrap',
    justifyContent: 'space-between',
    marginBottom: 24,
  },
  statCard: {
    width: (width - 48) / 2,
    padding: 16,
    borderRadius: 12,
    alignItems: 'center',
    marginBottom: 12,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 3,
  },
  statCardDark: {
    borderWidth: 1,
    borderColor: COLORS.dark.border,
  },
  statIcon: {
    width: 56,
    height: 56,
    borderRadius: 28,
    alignItems: 'center',
    justifyContent: 'center',
    marginBottom: 12,
  },
  statCount: {
    fontSize: 28,
    fontWeight: 'bold',
    marginBottom: 4,
  },
  statLabel: {
    fontSize: 14,
    textAlign: 'center',
  },
  sectionTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    textAlign: 'right',
    marginBottom: 16,
    marginTop: 8,
  },
  featureCard: {
    flexDirection: 'row-reverse',
    padding: 16,
    borderRadius: 12,
    marginBottom: 12,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 3,
  },
  featureCardDark: {
    borderWidth: 1,
    borderColor: COLORS.dark.border,
  },
  featureIcon: {
    width: 48,
    height: 48,
    borderRadius: 24,
    alignItems: 'center',
    justifyContent: 'center',
    marginLeft: 12,
  },
  featureContent: {
    flex: 1,
  },
  featureTitle: {
    fontSize: 16,
    fontWeight: '600',
    textAlign: 'right',
    marginBottom: 4,
  },
  featureDescription: {
    fontSize: 14,
    textAlign: 'right',
  },
  actionButton: {
    flexDirection: 'row-reverse',
    alignItems: 'center',
    justifyContent: 'center',
    padding: 16,
    borderRadius: 12,
    marginBottom: 12,
  },
  actionButtonText: {
    color: COLORS.white,
    fontSize: 16,
    fontWeight: '600',
    marginRight: 8,
  },
  footer: {
    alignItems: 'center',
    marginTop: 24,
    marginBottom: 16,
  },
  footerText: {
    fontSize: 14,
    textAlign: 'center',
    marginVertical: 4,
  },
});
