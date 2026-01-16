import { defineConfig } from 'vite';
{% if cookiecutter.style_solution in ['tailwind', 'daisy'] %}
import tailwindcss from '@tailwindcss/vite';
{% endif %}
import ViteRails from 'vite-plugin-rails';

process.env.VITE_RUBY_CONFIG_PATH = 'vite_django_config.json';

const config = defineConfig({
  plugins: [
    ViteRails({
      fullReload: {
        // Specify the paths to watch for full page reloads
        overridePaths: [
          './**/*.py',
          './**/*.html',
          './**/*.js',
        ]
      },
      compress: false,
    }),
{% if cookiecutter.style_solution in ['tailwind', 'daisy'] %}
    tailwindcss(),
{% endif %}
  ],
{% if cookiecutter.style_solution in ['bootstrap'] %}
    css: {
      preprocessorOptions: {
        scss: {
          silenceDeprecations: ['import', 'mixed-decls', 'color-functions', 'global-builtin', 'if-function'],
        },
      },
    },
{% endif %}
});

export default config;
