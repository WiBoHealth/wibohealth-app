import translations from './locales/ar.json';

class I18n {
  constructor() {
    this.translations = translations;
  }

  t(key) {
    const keys = key.split('.');
    let value = this.translations;
    
    for (const k of keys) {
      value = value[k];
      if (value === undefined) {
        return key;
      }
    }
    
    return value;
  }
}

export default new I18n();
