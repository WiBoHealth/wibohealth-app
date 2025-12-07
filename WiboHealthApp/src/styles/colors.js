// 🎨 ألوان تطبيق WiBo Health - نفس ألوان الموقع

export const COLORS = {
  // الألوان الأساسية
  primary: '#10b981', // الأخضر الأساسي (emerald-500)
  primaryDark: '#059669', // أخضر غامق (emerald-600)
  primaryLight: '#34d399', // أخضر فاتح (emerald-400)
  
  // ألوان الخلفية - الوضع النهاري
  light: {
    background: '#ffffff',
    backgroundSecondary: '#f9fafb',
    card: '#ffffff',
    text: '#111827',
    textSecondary: '#6b7280',
    border: '#e5e7eb',
    shadow: 'rgba(0, 0, 0, 0.1)',
  },
  
  // ألوان الخلفية - الوضع الليلي
  dark: {
    background: '#0f172a',
    backgroundSecondary: '#1e293b',
    card: '#1e293b',
    text: '#f1f5f9',
    textSecondary: '#94a3b8',
    border: '#334155',
    shadow: 'rgba(0, 0, 0, 0.3)',
  },
  
  // ألوان الحالة
  success: '#10b981',
  error: '#ef4444',
  warning: '#f59e0b',
  info: '#3b82f6',
  
  // ألوان إضافية
  white: '#ffffff',
  black: '#000000',
  gray: {
    50: '#f9fafb',
    100: '#f3f4f6',
    200: '#e5e7eb',
    300: '#d1d5db',
    400: '#9ca3af',
    500: '#6b7280',
    600: '#4b5563',
    700: '#374151',
    800: '#1f2937',
    900: '#111827',
  },
  
  // ألوان الفئات
  categories: {
    breakfast: '#f59e0b',
    lunch: '#3b82f6',
    dinner: '#8b5cf6',
    snack: '#10b981',
    dessert: '#ec4899',
    vegetables: '#10b981',
    fruits: '#f59e0b',
    protein: '#ef4444',
    dairy: '#3b82f6',
    grains: '#f59e0b',
  },
};

export default COLORS;
