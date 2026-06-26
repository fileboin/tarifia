import { config } from '@tarifia-sh/eslint-config/react-internal'

/** @type {import("eslint").Linter.Config[]} */
export default [
  {
    ignores: ['node_modules/**', 'dist/**', 'coverage/**'],
  },
  ...config,
  {
    rules: {
      'react/prop-types': 'off',
    },
  },
]
