import React, { useState } from 'react';
import {
  View,
  Text,
  StyleSheet,
  FlatList,
  TextInput,
  TouchableOpacity,
  Modal,
  ScrollView,
} from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import COLORS from '../styles/colors';

// بيانات تجريبية - سيتم استبدالها بالبيانات الحقيقية
const sampleRecipes = [
  {
    id: 1,
    category: 'فطور',
    icon: '🥣',
    title: 'شوفان بالتوت والمكسرات',
    time: '10 دقائق',
    servings: 1,
    calories: 290,
    nutrition: { protein: 12, carbs: 42, fat: 8, fiber: 7 },
    ingredients: [
      '½ كوب شوفان خام',
      '1 كوب حليب قليل الدسم',
      '¼ كوب توت مشكل',
      '2 ملعقة كبيرة لوز مقطع',
      '1 ملعقة صغيرة عسل',
      'رشة قرفة',
    ],
    steps: [
      'ضع الشوفان والحليب في قدر على نار متوسطة',
      'قلّب باستمرار حتى يثخن القوام (5-7 دقائق)',
      'أطفئ النار وأضف القرفة',
      'انقل إلى وعاء التقديم',
      'زيّن بالتوت واللوز',
      'رش العسل على الوجه وقدّم ساخناً',
    ],
    tips: 'يمكنك تحضيره بارداً في الليلة السابقة (overnight oats)',
  },
];

export default function RecipesScreen({ isDarkMode }) {
  const [searchText, setSearchText] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('الكل');
  const [selectedRecipe, setSelectedRecipe] = useState(null);
  const [modalVisible, setModalVisible] = useState(false);

  const theme = isDarkMode ? COLORS.dark : COLORS.light;

  const categories = ['الكل', 'فطور', 'غداء', 'عشاء', 'سلطات', 'حلويات صحية'];

  const filteredRecipes = sampleRecipes.filter((recipe) => {
    const matchesSearch = recipe.title.includes(searchText);
    const matchesCategory =
      selectedCategory === 'الكل' || recipe.category === selectedCategory;
    return matchesSearch && matchesCategory;
  });

  const openRecipe = (recipe) => {
    setSelectedRecipe(recipe);
    setModalVisible(true);
  };

  const closeModal = () => {
    setModalVisible(false);
    setSelectedRecipe(null);
  };

  const renderRecipeCard = ({ item }) => (
    <TouchableOpacity
      style={[
        styles.recipeCard,
        { backgroundColor: theme.card },
        isDarkMode && styles.recipeCardDark,
      ]}
      onPress={() => openRecipe(item)}
    >
      <Text style={styles.recipeIcon}>{item.icon}</Text>
      <Text style={[styles.recipeTitle, { color: theme.text }]}>
        {item.title}
      </Text>
      <View style={styles.recipeInfo}>
        <View style={styles.infoItem}>
          <Ionicons name="time-outline" size={16} color={theme.textSecondary} />
          <Text style={[styles.infoText, { color: theme.textSecondary }]}>
            {item.time}
          </Text>
        </View>
        <View style={styles.infoItem}>
          <Ionicons name="flame-outline" size={16} color={COLORS.primary} />
          <Text style={[styles.infoText, { color: theme.textSecondary }]}>
            {item.calories} سعرة
          </Text>
        </View>
      </View>
      <TouchableOpacity
        style={[styles.viewButton, { backgroundColor: COLORS.primary }]}
        onPress={() => openRecipe(item)}
      >
        <Text style={styles.viewButtonText}>عرض الوصفة</Text>
      </TouchableOpacity>
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
          placeholder="ابحث عن وصفة..."
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
                backgroundColor:
                  selectedCategory === item ? COLORS.primary : theme.card,
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
                  color:
                    selectedCategory === item ? COLORS.white : theme.text,
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
        {filteredRecipes.length} وصفة صحية
      </Text>

      {/* Recipes List */}
      <FlatList
        data={filteredRecipes}
        keyExtractor={(item) => item.id.toString()}
        renderItem={renderRecipeCard}
        numColumns={2}
        contentContainerStyle={styles.listContent}
        showsVerticalScrollIndicator={false}
        columnWrapperStyle={styles.columnWrapper}
      />

      {/* Recipe Modal */}
      {selectedRecipe && (
        <Modal
          visible={modalVisible}
          animationType="slide"
          transparent={false}
          onRequestClose={closeModal}
        >
          <View style={[styles.modalContainer, { backgroundColor: theme.background }]}>
            <View style={[styles.modalHeader, { backgroundColor: theme.card }]}>
              <TouchableOpacity onPress={closeModal} style={styles.closeButton}>
                <Ionicons name="close" size={28} color={theme.text} />
              </TouchableOpacity>
              <Text style={[styles.modalTitle, { color: theme.text }]}>
                {selectedRecipe.title}
              </Text>
              <Text style={styles.modalIcon}>{selectedRecipe.icon}</Text>
            </View>

            <ScrollView style={styles.modalContent}>
              {/* Info Section */}
              <View style={styles.modalInfoSection}>
                <View style={styles.modalInfoCard}>
                  <Ionicons name="time" size={20} color={COLORS.primary} />
                  <Text style={[styles.modalInfoText, { color: theme.text }]}>
                    {selectedRecipe.time}
                  </Text>
                </View>
                <View style={styles.modalInfoCard}>
                  <Ionicons name="people" size={20} color={COLORS.primary} />
                  <Text style={[styles.modalInfoText, { color: theme.text }]}>
                    {selectedRecipe.servings} حصة
                  </Text>
                </View>
                <View style={styles.modalInfoCard}>
                  <Ionicons name="flame" size={20} color={COLORS.primary} />
                  <Text style={[styles.modalInfoText, { color: theme.text }]}>
                    {selectedRecipe.calories} سعرة
                  </Text>
                </View>
              </View>

              {/* Nutrition */}
              <View style={[styles.section, { borderColor: theme.border }]}>
                <Text style={[styles.sectionTitle, { color: theme.text }]}>
                  📊 القيم الغذائية
                </Text>
                <View style={styles.nutritionRow}>
                  <View style={styles.nutritionItem}>
                    <Text style={[styles.nutritionValue, { color: '#ef4444' }]}>
                      {selectedRecipe.nutrition.protein}g
                    </Text>
                    <Text style={[styles.nutritionLabel, { color: theme.textSecondary }]}>
                      بروتين
                    </Text>
                  </View>
                  <View style={styles.nutritionItem}>
                    <Text style={[styles.nutritionValue, { color: '#f59e0b' }]}>
                      {selectedRecipe.nutrition.carbs}g
                    </Text>
                    <Text style={[styles.nutritionLabel, { color: theme.textSecondary }]}>
                      كربوهيدرات
                    </Text>
                  </View>
                  <View style={styles.nutritionItem}>
                    <Text style={[styles.nutritionValue, { color: '#8b5cf6' }]}>
                      {selectedRecipe.nutrition.fat}g
                    </Text>
                    <Text style={[styles.nutritionLabel, { color: theme.textSecondary }]}>
                      دهون
                    </Text>
                  </View>
                  <View style={styles.nutritionItem}>
                    <Text style={[styles.nutritionValue, { color: COLORS.primary }]}>
                      {selectedRecipe.nutrition.fiber}g
                    </Text>
                    <Text style={[styles.nutritionLabel, { color: theme.textSecondary }]}>
                      ألياف
                    </Text>
                  </View>
                </View>
              </View>

              {/* Ingredients */}
              <View style={[styles.section, { borderColor: theme.border }]}>
                <Text style={[styles.sectionTitle, { color: theme.text }]}>
                  🛒 المكونات
                </Text>
                {selectedRecipe.ingredients.map((ingredient, index) => (
                  <View key={index} style={styles.ingredientItem}>
                    <Ionicons name="checkmark-circle" size={20} color={COLORS.primary} />
                    <Text style={[styles.ingredientText, { color: theme.text }]}>
                      {ingredient}
                    </Text>
                  </View>
                ))}
              </View>

              {/* Steps */}
              <View style={[styles.section, { borderColor: theme.border }]}>
                <Text style={[styles.sectionTitle, { color: theme.text }]}>
                  👨‍🍳 طريقة التحضير
                </Text>
                {selectedRecipe.steps.map((step, index) => (
                  <View key={index} style={styles.stepItem}>
                    <View style={styles.stepNumber}>
                      <Text style={styles.stepNumberText}>{index + 1}</Text>
                    </View>
                    <Text style={[styles.stepText, { color: theme.text }]}>
                      {step}
                    </Text>
                  </View>
                ))}
              </View>

              {/* Tips */}
              <View style={[styles.section, { borderColor: theme.border }]}>
                <Text style={[styles.sectionTitle, { color: theme.text }]}>
                  💡 نصيحة
                </Text>
                <View style={[styles.tipBox, { backgroundColor: COLORS.primary + '20' }]}>
                  <Ionicons name="bulb" size={20} color={COLORS.primary} />
                  <Text style={[styles.tipText, { color: theme.text }]}>
                    {selectedRecipe.tips}
                  </Text>
                </View>
              </View>
            </ScrollView>
          </View>
        </Modal>
      )}
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
    padding: 12,
  },
  columnWrapper: {
    justifyContent: 'space-between',
  },
  recipeCard: {
    width: '48%',
    padding: 16,
    borderRadius: 12,
    marginBottom: 12,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 3,
  },
  recipeCardDark: {
    borderWidth: 1,
    borderColor: COLORS.dark.border,
  },
  recipeIcon: {
    fontSize: 48,
    textAlign: 'center',
    marginBottom: 8,
  },
  recipeTitle: {
    fontSize: 16,
    fontWeight: 'bold',
    textAlign: 'center',
    marginBottom: 12,
    minHeight: 40,
  },
  recipeInfo: {
    marginBottom: 12,
  },
  infoItem: {
    flexDirection: 'row-reverse',
    alignItems: 'center',
    justifyContent: 'center',
    marginBottom: 4,
  },
  infoText: {
    fontSize: 12,
    marginRight: 4,
  },
  viewButton: {
    paddingVertical: 8,
    borderRadius: 8,
    alignItems: 'center',
  },
  viewButtonText: {
    color: COLORS.white,
    fontSize: 14,
    fontWeight: '600',
  },
  modalContainer: {
    flex: 1,
  },
  modalHeader: {
    padding: 16,
    paddingTop: 48,
    alignItems: 'center',
    borderBottomWidth: 1,
    borderBottomColor: COLORS.gray[200],
  },
  closeButton: {
    position: 'absolute',
    left: 16,
    top: 48,
    zIndex: 1,
  },
  modalTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    textAlign: 'center',
    marginBottom: 8,
  },
  modalIcon: {
    fontSize: 48,
  },
  modalContent: {
    flex: 1,
    padding: 16,
  },
  modalInfoSection: {
    flexDirection: 'row-reverse',
    justifyContent: 'space-between',
    marginBottom: 24,
  },
  modalInfoCard: {
    alignItems: 'center',
    flex: 1,
  },
  modalInfoText: {
    fontSize: 12,
    marginTop: 4,
    textAlign: 'center',
  },
  section: {
    marginBottom: 24,
    paddingBottom: 24,
    borderBottomWidth: 1,
  },
  sectionTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    marginBottom: 16,
    textAlign: 'right',
  },
  nutritionRow: {
    flexDirection: 'row-reverse',
    justifyContent: 'space-between',
  },
  nutritionItem: {
    alignItems: 'center',
  },
  nutritionValue: {
    fontSize: 20,
    fontWeight: 'bold',
    marginBottom: 4,
  },
  nutritionLabel: {
    fontSize: 12,
  },
  ingredientItem: {
    flexDirection: 'row-reverse',
    alignItems: 'center',
    marginBottom: 12,
  },
  ingredientText: {
    fontSize: 16,
    marginRight: 8,
    flex: 1,
    textAlign: 'right',
  },
  stepItem: {
    flexDirection: 'row-reverse',
    marginBottom: 16,
  },
  stepNumber: {
    width: 32,
    height: 32,
    borderRadius: 16,
    backgroundColor: COLORS.primary,
    alignItems: 'center',
    justifyContent: 'center',
    marginLeft: 12,
  },
  stepNumberText: {
    color: COLORS.white,
    fontSize: 16,
    fontWeight: 'bold',
  },
  stepText: {
    fontSize: 16,
    flex: 1,
    textAlign: 'right',
    lineHeight: 24,
  },
  tipBox: {
    flexDirection: 'row-reverse',
    padding: 16,
    borderRadius: 12,
    alignItems: 'center',
  },
  tipText: {
    fontSize: 14,
    marginRight: 12,
    flex: 1,
    textAlign: 'right',
    lineHeight: 20,
  },
});
