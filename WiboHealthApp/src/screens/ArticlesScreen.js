import React from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
} from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import COLORS from '../styles/colors';

const articles = [
  {
    id: 1,
    title: 'فوائد شرب الماء للصحة',
    category: 'تغذية',
    icon: 'water',
    color: '#06b6d4',
    summary: 'الماء ضروري لجميع وظائف الجسم، تعرف على فوائده وكم تحتاج يومياً',
  },
  {
    id: 2,
    title: 'أهمية البروتين في النظام الغذائي',
    category: 'تغذية',
    icon: 'nutrition',
    color: '#ef4444',
    summary: 'البروتين أساسي لبناء العضلات والأنسجة، اكتشف مصادره الصحية',
  },
  {
    id: 3,
    title: 'نصائح لخسارة الوزن الصحية',
    category: 'رشاقة',
    icon: 'fitness',
    color: COLORS.primary,
    summary: 'خطوات عملية وآمنة لتحقيق وزن مثالي دون حرمان',
  },
  {
    id: 4,
    title: 'أفضل الأطعمة لتقوية المناعة',
    category: 'صحة',
    icon: 'shield-checkmark',
    color: '#8b5cf6',
    summary: 'الأطعمة الطبيعية التي تعزز جهازك المناعي وتحميك من الأمراض',
  },
];

export default function ArticlesScreen({ isDarkMode }) {
  const theme = isDarkMode ? COLORS.dark : COLORS.light;

  return (
    <ScrollView
      style={[styles.container, { backgroundColor: theme.background }]}
      contentContainerStyle={styles.contentContainer}
    >
      <Text style={[styles.headerTitle, { color: theme.text }]}>
        📰 مقالات صحية مفيدة
      </Text>
      <Text style={[styles.headerSubtitle, { color: theme.textSecondary }]}>
        اقرأ أحدث المقالات الصحية والنصائح المفيدة
      </Text>

      {articles.map((article) => (
        <TouchableOpacity
          key={article.id}
          style={[
            styles.articleCard,
            { backgroundColor: theme.card },
            isDarkMode && styles.articleCardDark,
          ]}
        >
          <View
            style={[
              styles.articleIcon,
              { backgroundColor: article.color + '20' },
            ]}
          >
            <Ionicons name={article.icon} size={32} color={article.color} />
          </View>
          
          <View style={styles.articleContent}>
            <View style={styles.articleHeader}>
              <Text style={[styles.articleTitle, { color: theme.text }]}>
                {article.title}
              </Text>
              <View
                style={[
                  styles.categoryBadge,
                  { backgroundColor: article.color + '20' },
                ]}
              >
                <Text style={[styles.categoryText, { color: article.color }]}>
                  {article.category}
                </Text>
              </View>
            </View>
            
            <Text style={[styles.articleSummary, { color: theme.textSecondary }]}>
              {article.summary}
            </Text>
            
            <TouchableOpacity style={styles.readMoreButton}>
              <Text style={[styles.readMoreText, { color: article.color }]}>
                اقرأ المزيد
              </Text>
              <Ionicons
                name="arrow-back"
                size={16}
                color={article.color}
                style={styles.readMoreIcon}
              />
            </TouchableOpacity>
          </View>
        </TouchableOpacity>
      ))}

      {/* Coming Soon Section */}
      <View
        style={[
          styles.comingSoonCard,
          { backgroundColor: theme.card },
          isDarkMode && styles.comingSoonCardDark,
        ]}
      >
        <Ionicons name="rocket" size={48} color={COLORS.primary} />
        <Text style={[styles.comingSoonTitle, { color: theme.text }]}>
          المزيد قريباً!
        </Text>
        <Text style={[styles.comingSoonText, { color: theme.textSecondary }]}>
          نعمل على إضافة المزيد من المقالات الصحية المفيدة
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
  headerTitle: {
    fontSize: 24,
    fontWeight: 'bold',
    textAlign: 'right',
    marginBottom: 8,
  },
  headerSubtitle: {
    fontSize: 14,
    textAlign: 'right',
    marginBottom: 24,
  },
  articleCard: {
    flexDirection: 'row-reverse',
    padding: 16,
    borderRadius: 12,
    marginBottom: 16,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 3,
  },
  articleCardDark: {
    borderWidth: 1,
    borderColor: COLORS.dark.border,
  },
  articleIcon: {
    width: 64,
    height: 64,
    borderRadius: 32,
    alignItems: 'center',
    justifyContent: 'center',
    marginLeft: 16,
  },
  articleContent: {
    flex: 1,
  },
  articleHeader: {
    marginBottom: 8,
  },
  articleTitle: {
    fontSize: 16,
    fontWeight: 'bold',
    textAlign: 'right',
    marginBottom: 8,
  },
  categoryBadge: {
    paddingHorizontal: 12,
    paddingVertical: 4,
    borderRadius: 12,
    alignSelf: 'flex-end',
  },
  categoryText: {
    fontSize: 12,
    fontWeight: '600',
  },
  articleSummary: {
    fontSize: 14,
    textAlign: 'right',
    lineHeight: 20,
    marginBottom: 12,
  },
  readMoreButton: {
    flexDirection: 'row-reverse',
    alignItems: 'center',
  },
  readMoreText: {
    fontSize: 14,
    fontWeight: '600',
  },
  readMoreIcon: {
    marginRight: 4,
  },
  comingSoonCard: {
    padding: 32,
    borderRadius: 12,
    alignItems: 'center',
    marginTop: 16,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 3,
  },
  comingSoonCardDark: {
    borderWidth: 1,
    borderColor: COLORS.dark.border,
  },
  comingSoonTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    marginTop: 16,
    marginBottom: 8,
  },
  comingSoonText: {
    fontSize: 14,
    textAlign: 'center',
    lineHeight: 20,
  },
});
