// 🎨 التصاميم المشتركة - WiBo Health

import { StyleSheet, Platform, I18nManager } from 'react-native';
import COLORS from './colors';

// تفعيل RTL للعربية
I18nManager.forceRTL(true);
I18nManager.allowRTL(true);

export const commonStyles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: COLORS.light.background,
  },
  
  containerDark: {
    flex: 1,
    backgroundColor: COLORS.dark.background,
  },
  
  // الحاوية مع padding
  paddedContainer: {
    flex: 1,
    padding: 16,
  },
  
  // البطاقة
  card: {
    backgroundColor: COLORS.white,
    borderRadius: 12,
    padding: 16,
    marginBottom: 12,
    shadowColor: COLORS.black,
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 3,
  },
  
  cardDark: {
    backgroundColor: COLORS.dark.card,
    borderColor: COLORS.dark.border,
    borderWidth: 1,
  },
  
  // العناوين
  heading1: {
    fontSize: 28,
    fontWeight: 'bold',
    color: COLORS.light.text,
    marginBottom: 16,
    textAlign: 'right',
    fontFamily: Platform.OS === 'ios' ? 'System' : 'sans-serif',
  },
  
  heading2: {
    fontSize: 24,
    fontWeight: 'bold',
    color: COLORS.light.text,
    marginBottom: 12,
    textAlign: 'right',
  },
  
  heading3: {
    fontSize: 20,
    fontWeight: '600',
    color: COLORS.light.text,
    marginBottom: 8,
    textAlign: 'right',
  },
  
  heading1Dark: {
    color: COLORS.dark.text,
  },
  
  heading2Dark: {
    color: COLORS.dark.text,
  },
  
  heading3Dark: {
    color: COLORS.dark.text,
  },
  
  // النصوص
  text: {
    fontSize: 16,
    color: COLORS.light.text,
    textAlign: 'right',
    writingDirection: 'rtl',
  },
  
  textDark: {
    color: COLORS.dark.text,
  },
  
  textSecondary: {
    fontSize: 14,
    color: COLORS.light.textSecondary,
    textAlign: 'right',
  },
  
  textSecondaryDark: {
    color: COLORS.dark.textSecondary,
  },
  
  // الأزرار
  button: {
    backgroundColor: COLORS.primary,
    paddingVertical: 12,
    paddingHorizontal: 24,
    borderRadius: 8,
    alignItems: 'center',
    justifyContent: 'center',
  },
  
  buttonText: {
    color: COLORS.white,
    fontSize: 16,
    fontWeight: '600',
    textAlign: 'center',
  },
  
  buttonOutline: {
    backgroundColor: 'transparent',
    borderWidth: 2,
    borderColor: COLORS.primary,
  },
  
  buttonOutlineText: {
    color: COLORS.primary,
  },
  
  // شريط البحث
  searchBar: {
    backgroundColor: COLORS.gray[100],
    borderRadius: 8,
    paddingHorizontal: 16,
    paddingVertical: 12,
    fontSize: 16,
    textAlign: 'right',
    writingDirection: 'rtl',
    marginBottom: 16,
  },
  
  searchBarDark: {
    backgroundColor: COLORS.dark.card,
    color: COLORS.dark.text,
    borderWidth: 1,
    borderColor: COLORS.dark.border,
  },
  
  // Badge (الشارات)
  badge: {
    backgroundColor: COLORS.primary,
    paddingVertical: 4,
    paddingHorizontal: 8,
    borderRadius: 12,
    alignSelf: 'flex-start',
  },
  
  badgeText: {
    color: COLORS.white,
    fontSize: 12,
    fontWeight: '600',
  },
  
  // Divider (الفاصل)
  divider: {
    height: 1,
    backgroundColor: COLORS.light.border,
    marginVertical: 16,
  },
  
  dividerDark: {
    backgroundColor: COLORS.dark.border,
  },
  
  // Shadow (الظل)
  shadow: {
    shadowColor: COLORS.black,
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 3,
  },
  
  // Center (المركز)
  center: {
    alignItems: 'center',
    justifyContent: 'center',
  },
  
  // Row (صف)
  row: {
    flexDirection: 'row-reverse', // RTL
    alignItems: 'center',
  },
  
  rowBetween: {
    flexDirection: 'row-reverse', // RTL
    alignItems: 'center',
    justifyContent: 'space-between',
  },
  
  // Spacing
  mt8: { marginTop: 8 },
  mt16: { marginTop: 16 },
  mt24: { marginTop: 24 },
  mb8: { marginBottom: 8 },
  mb16: { marginBottom: 16 },
  mb24: { marginBottom: 24 },
  mx8: { marginHorizontal: 8 },
  mx16: { marginHorizontal: 16 },
  my8: { marginVertical: 8 },
  my16: { marginVertical: 16 },
  
  p8: { padding: 8 },
  p16: { padding: 16 },
  p24: { padding: 24 },
  px8: { paddingHorizontal: 8 },
  px16: { paddingHorizontal: 16 },
  py8: { paddingVertical: 8 },
  py16: { paddingVertical: 16 },
});

export default commonStyles;
