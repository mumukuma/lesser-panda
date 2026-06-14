/** Tailwind 設定：顏色全部對應 CSS 變數，深色模式由變數切換（OS 優先 + data-theme 手動）。 */
module.exports = {
  content: ['./src/**/*.{astro,html,js,jsx,ts,tsx,vue,md}'],
  darkMode: ['selector', '[data-theme="dark"]'],
  theme: {
    extend: {
      colors: {
        bg: 'var(--bg)',
        card: 'var(--bg-card)',
        ink: 'var(--ink)',
        'ink-soft': 'var(--ink-soft)',
        rust: 'var(--rust)',
        'rust-dark': 'var(--rust-dark)',
        amber: 'var(--amber)',
        cream: 'var(--cream)',
        line: 'var(--line)',
        female: 'var(--female)',
        male: 'var(--male)',
      },
      borderRadius: { card: '14px' },
      boxShadow: { card: 'var(--shadow)' },
      fontFamily: {
        sans: ['"Hiragino Sans"', '"Noto Sans TC"', '"Noto Sans JP"', '"PingFang TC"',
          '"Microsoft JhengHei"', 'system-ui', 'sans-serif'],
      },
    },
  },
  plugins: [],
};
