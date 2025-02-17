import js from "@eslint/js";
// import globals from "globals";
import oxlint from "eslint-plugin-oxlint";
import tseslint from "typescript-eslint";

export default tseslint.config(
  {
    ignores: ["**/*.d.ts", "ecosystem.config.js", "eslint.config.js"],
  },
  js.configs.recommended,
  ...tseslint.configs.recommendedTypeChecked,
  ...tseslint.configs.stylisticTypeChecked,
  {
    languageOptions: {
      ecmaVersion: "latest",
      sourceType: "module",
      parserOptions: {
        project: true,
        tsconfigDirName: import.meta.dirname,
      },
    },
  },
  oxlint.configs["flat/recommended"], // oxlint should be the last one
);
