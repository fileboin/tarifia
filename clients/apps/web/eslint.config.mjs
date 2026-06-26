import { nextJsConfig } from '@tarifia-sh/eslint-config/next-js'
import tarifiaPlugin from './eslint-rules/index.mjs'

/** @type {import("eslint").Linter.Config} */
export default [
  ...nextJsConfig,
  {
    plugins: {
      tarifia: tarifiaPlugin,
    },
    languageOptions: {
      parserOptions: {
        projectService: {
          allowDefaultProject: [
            'vitest.config.ts',
            'playwright.config.ts',
            '*.config.mjs',
            'instrumentation-client.ts',
          ],
        },
      },
    },
  },
  {
    rules: {
      'react-hooks/set-state-in-effect': 'warn',
      'react-hooks/refs': 'warn',
      'react-hooks/static-components': 'warn',
      'react-hooks/preserve-manual-memoization': 'warn',
      'react-hooks/immutability': 'warn',
      'react-hooks/purity': 'warn',
      'tarifia/no-toast-error-detail': 'error',
    },
  },
  {
    files: ['**/*.tsx'],
    rules: {
      'react/no-danger': 'error',
      'react/self-closing-comp': 'warn',
      'react/jsx-no-useless-fragment': 'warn',
      'tarifia/no-classname-box': 'error',
      'tarifia/no-classname-text': 'error',
      'tarifia/no-style-box': 'error',
      'tarifia/no-style-text': 'error',
      'tarifia/no-next-image': 'error',
    },
  },
  {
    files: [
      'src/components/CustomerPortal/**/*.{ts,tsx}',
      'src/app/**/portal/**/*.{ts,tsx}',
    ],
    rules: {
      'tarifia/no-merchant-queries-in-customer-portal': 'error',
      'tarifia/no-merchant-api-calls-in-customer-portal': 'error',
    },
  },
  {
    files: ['src/app/**/portal/**/page.tsx'],
    ignores: [
      'src/app/**/portal/page.tsx',
      'src/app/**/portal/request/page.tsx',
      'src/app/**/portal/authenticate/page.tsx',
      'src/app/**/portal/verify-email/page.tsx',
      'src/app/**/portal/claim/page.tsx',
    ],
    rules: {
      'tarifia/require-customer-portal-page': 'error',
    },
  },
  {
    files: [
      'src/app/(main)/onboarding/**/*.tsx',
      'src/components/Onboarding/**/*.tsx',
    ],
    rules: {
      'tarifia/no-raw-html-layout': 'error',
    },
  },
  {
    ignores: [
      'node_modules/**',
      '.next/**',
      'out/**',
      'build/**',
      'coverage/**',
      'eslint-rules/**',
      'src/app/.well-known/**',
      'next-env.d.ts',
      'e2e/**',
      'playwright-report/**',
      'babel.config.js',
      'scripts/**',
    ],
  },
]
