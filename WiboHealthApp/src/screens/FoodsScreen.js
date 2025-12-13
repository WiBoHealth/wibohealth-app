import React, { useState } from 'react';
import {
  View,
  Text,
  StyleSheet,
  FlatList,
  TextInput,
  TouchableOpacity,
} from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import COLORS from '../styles/colors';

// بيانات تجريبية - سيتم استبدالها بالبيانات الحقيقية
const sampleFoods = [
  {
    id: 1,
    name: 'تفاح أحمر',
    category: 'فواكه',
    calories: 52,
    protein: 0.3,
    carbs: 14,
    fat: 0.2,
    fiber: 2.4,
    isHealthy: true,
  },
  {
    id: 2,
    name: 'صدر دجاج',
    category: 'لحوم',
    calories: 165,
    protein: 31,
    carbs: 0,
    fat: 3.6,
    fiber: 0,
    isHealthy: true,
  },
  {
    id: 3,
    name: 'أرز بني',
    category: 'حبوب',
    calories: 111,
    protein: 2.6,
    carbs: 23,
    fat: 0.9,
    fiber: 1.8,
    isHealthy: true,
  },
  // المزيد من البيانات...
];

export default function FoodsScreen({ isDarkMode }) {
  const [searchText, setSearchText] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('الكل');
  
  const theme = isDarkMode ? COLORS.dark : COLORS.light;

  const categories = ['الكل', 'فواكه', 'خضروات', 'لحوم', 'حبوب', 'ألبان'];

  const filteredFoods = sampleFoods.filter(food => {
    const matchesSearch = food.name.includes(searchText);
    const matchesCategory = selectedCategory === 'الكل' || food.category === selectedCategory;
    return matchesSearch && matchesCategory;
  });

  const renderFoodCard = ({ item }) => (
    <TouchableOpacity
      style={[
        styles.foodCard,
        { backgroundColor: theme.card },
        isDarkMode && styles.foodCardDark,
      ]}
    >
      <View style={styles.foodHeader}>
        <View style={styles.foodTitleContainer}>
          <Text style={[styles.foodName, { color: theme.text }]}>
            {item.name}
          </Text>
          <View style={[styles.categoryBadge, { backgroundColor: COLORS.primary + '20' }]}>
            <Text style={[styles.categoryText, { color: COLORS.primary }]}>
              {item.category}
            </Text>
          </View>
        </View>
        {item.isHealthy && (
          <View style={[styles.healthyBadge, { backgroundColor: COLORS.success + '20' }]}>
            <Ionicons name="leaf" size={16} color={COLORS.success} />
          </View>
        )}
      </View>

      <View style={styles.nutritionGrid}>
        <View style={styles.nutritionItem}>
          <Text style={[styles.nutritionValue, { color: COLORS.primary }]}>
            {item.calories}
          </Text>
          <Text style={[styles.nutritionLabel, { color: theme.textSecondary }]}>
            سعرة
          </Text>
        </View>
        <View style={styles.nutritionItem}>
          <Text style={[styles.nutritionValue, { color: '#ef4444' }]}>
            {item.protein}
          </Text>
          <Text style={[styles.nutritionLabel, { color: theme.textSecondary }]}>
            بروتين
          </Text>
        </View>
        <View style={styles.nutritionItem}>
          <Text style={[styles.nutritionValue, { color: '#f59e0b' }]}>
            {item.carbs}
          </Text>
          <Text style={[styles.nutritionLabel, { color: theme.textSecondary }]}>
            كربوهيدرات
          </Text>
        </View>
        <View style={styles.nutritionItem}>
          <Text style={[styles.nutritionValue, { color: '#8b5cf6' }]}>
            {item.fat}
          </Text>
          <Text style={[styles.nutritionLabel, { color: theme.textSecondary }]}>
            دهون
          </Text>
        </View>
      </View>
    </TouchableOpacity>
  );

  return (
    <View style={[styles.container, { backgroundColor: theme.background }]}>
      {/* Search Bar */}
      <View style={styles.searchContainer}>
        <Ionicons
          name="search"
          size={20}
          color={theme.textSecondary}
          style={styles.searchIcon}
        />
        <TextInput
          style={[
            styles.searchInput,
            {
              backgroundColor: theme.card,
              color: theme.text,
              borderColor: theme.border,
            },
          ]}
          placeholder="ابحث عن طعام..."
          placeholderTextColor={theme.textSecondary}
          value={searchText}
          onChangeText={setSearchText}
        />
      </View>

      {/* Categories */}
      <FlatList
        horizontal
        inverted
        data={categories}
        keyExtractor={(item) => item}
        showsHorizontalScrollIndicator={false}
        contentContainerStyle={styles.categoriesContainer}
        renderItem={({ item }) => (
          <TouchableOpacity
            style={[
              styles.categoryButton,
              {
                backgroundColor: selectedCategory === item ? COLORS.primary : theme.card,
                borderColor: theme.border,
              },
              isDarkMode && selectedCategory !== item && styles.categoryButtonDark,
            ]}
            onPress={() => setSelectedCategory(item)}
          >
            <Text
              style={[
                styles.categoryButtonText,
                {
                  color: selectedCategory === item ? COLORS.white : theme.text,
                },
              ]}
            >
              {item}
            </Text>
          </TouchableOpacity>
        )}
      />

      {/* Results Count */}
      <Text style={[styles.resultsCount, { color: theme.textSecondary }]}>
        {filteredFoods.length} عنصر غذائي
      </Text>

      {/* Foods List */}
      <FlatList
        data={filteredFoods}
        keyExtractor={(item) => item.id.toString()}
        renderItem={renderFoodCard}
        contentContainerStyle={styles.listContent}
        showsVerticalScrollIndicator={false}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  searchContainer: {
    padding: 16,
    position: 'relative',
  },
  searchIcon: {
    position: 'absolute',
    left: 28,
    top: 28,
    zIndex: 1,
  },
  searchInput: {
    height: 48,
    borderRadius: 12,
    paddingHorizontal: 16,
    paddingRight: 40,
    fontSize: 16,
    textAlign: 'right',
    borderWidth: 1,
  },
  categoriesContainer: {
    paddingHorizontal: 16,
    paddingBottom: 12,
  },
  categoryButton: {
    paddingHorizontal: 16,
    paddingVertical: 8,
    borderRadius: 20,
    marginLeft: 8,
    borderWidth: 1,
  },
  categoryButtonDark: {
    borderColor: COLORS.dark.border,
  },
  categoryButtonText: {
    fontSize: 14,
    fontWeight: '600',
  },
  resultsCount: {
    paddingHorizontal: 16,
    paddingBottom: 8,
    fontSize: 14,
    textAlign: 'right',
  },
  listContent: {
    padding: 16,
    paddingTop: 8,
  },
  foodCard: {
    padding: 16,
    borderRadius: 12,
    marginBottom: 12,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 3,
  },
  foodCardDark: {
    borderWidth: 1,
    borderColor: COLORS.dark.border,
  },
  foodHeader: {
    flexDirection: 'row-reverse',
    justifyContent: 'space-between',
    alignItems: 'flex-start',
    marginBottom: 12,
  },
  foodTitleContainer: {
    flex: 1,
  },
  foodName: {
    fontSize: 18,
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
  healthyBadge: {
    width: 32,
    height: 32,
    borderRadius: 16,
    alignItems: 'center',
    justifyContent: 'center',
    marginLeft: 8,
  },
  nutritionGrid: {
    flexDirection: 'row-reverse',
    justifyContent: 'space-between',
  },
  nutritionItem: {
    alignItems: 'center',
  },
  nutritionValue: {
    fontSize: 18,
    fontWeight: 'bold',
    marginBottom: 4,
  },
  nutritionLabel: {
    fontSize: 12,
  },
});
