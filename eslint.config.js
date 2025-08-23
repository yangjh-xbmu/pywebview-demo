import { config } from "@repo/eslint-config/base";

export default [
  ...config,
  {
    ignores: [
      "dist/**",
      "build/**",
      "node_modules/**",
      "venv/**",
      ".next/**",
      "*.min.js",
      "coverage/**",
      ".turbo/**",
    ],
  },
];