import { defineConfig } from 'vite';
import tailwindcss from '@tailwindcss/vite';
import ViteRails from 'vite-plugin-rails';

process.env.VITE_RUBY_CONFIG_PATH = 'vite_django_config.json';

const config = defineConfig({
  plugins: [
    ViteRails({
      fullReload: {
        // Specify the paths to watch for full page reloads
        overridePaths: [
          // 'django_app/**/*.py',
          // 'django_app/**/*.html',
        ]
      },
      compress: false,
    }),
    tailwindcss(),
  ],
});

export default config;
