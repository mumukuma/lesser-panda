// zh-TW 在站根，其餘語系各有子目錄（ja/ en/ ko/…）；新增語系不用再改這裡
export const localeDir = (locale) => (locale === 'zh-TW' ? '' : locale + '/');
export const pageUrl = (base, locale, rp) => `${base}${localeDir(locale)}${rp ? rp + '/' : ''}`;
export const pandaUrl = (base, locale, slug) => `${base}${localeDir(locale)}p/${slug}/`;
export const zooUrl = (base, locale, slug) => `${base}${localeDir(locale)}z/${slug}/`;
