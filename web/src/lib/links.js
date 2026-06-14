export const localeDir = (locale) => (locale === 'ja' ? 'ja/' : locale === 'en' ? 'en/' : '');
export const pageUrl = (base, locale, rp) => `${base}${localeDir(locale)}${rp ? rp + '/' : ''}`;
export const pandaUrl = (base, locale, slug) => `${base}${localeDir(locale)}p/${slug}/`;
