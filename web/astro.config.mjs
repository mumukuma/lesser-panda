import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import AstroPWA from '@vite-pwa/astro';

// 自訂網域（apex）：https://ressapanda.com
export default defineConfig({
  site: 'https://ressapanda.com',
  base: '/',
  trailingSlash: 'ignore',
  integrations: [
    tailwind(),
    AstroPWA({
      registerType: 'autoUpdate',
      manifest: {
        name: '小熊貓圖鑑',
        short_name: '小熊貓圖鑑',
        start_url: '/',
        scope: '/',
        display: 'standalone',
        background_color: '#fdf8f2',
        theme_color: '#b5552d',
        icons: [{ src: '/icon.svg', sizes: 'any', type: 'image/svg+xml' }],
      },
      workbox: {
        navigateFallback: null,
        globPatterns: ['**/*.{html,css,js,svg,json}'],
        // 第三方（favicon、地圖圖磚）執行時快取
        runtimeCaching: [
          {
            urlPattern: ({ url }) => url.origin !== self.location.origin,
            handler: 'StaleWhileRevalidate',
            options: { cacheName: 'external' },
          },
        ],
      },
    }),
  ],
});
