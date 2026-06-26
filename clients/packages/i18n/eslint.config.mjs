import { config } from '@tarifia-sh/eslint-config/base'

/** @type {import("eslint").Linter.Config[]} */
export default [
  {
    ignores: ['node_modules/**', 'dist/**'],
  },
  ...config,
]
