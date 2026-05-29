# Job Data JSON Specification (v1.0)

## 1. 严格约束 (Strict Rules)
- **绝对禁止空字符串 `""`**：如果没有数据，必须填 `null` 或根据上下文编造合理内容（如补全 TW/JP/CN 地区数据）。
- **必须保留 `statusLabel`**：在 `tasksByLevel` 的每一项中，`statusLabel` 是强校验字段，必须填入 "Replaceable" / "In-Danger" / "Intro" / "Nothing" 之一。
- **动态占位符**：`valueTemplate` 中必须包含 `{{value}}`，禁止写死硬编码（如禁止直接写 "High" 或 "Your Schedule"）。

## 2. 必须包含的核心结构 (Required Structure)
1. `meta`（含 `incomeType`, `calculatorInputs` 等）
2. `search`（含 `primaryTitle`, `aliases`, `subTitles[]`）
3. `countries`（必须覆盖全部 8 个目标国家/地区）
4. `tasksByLevel`
5. `extendedMeta`（所有国家的 `famousXxx`, `startupLinks`, `retire` 等必须全部填满）

## 3. 搜索块定义 (Search Block Spec)
(把之前我们讨论的 primaryTitle / primarySlug / aliases / subTitles 结构放这里)

## 4. Calculator Inputs 定义 (Calculator Spec)
(枚举 salary / piecerate 等不同 incomeType 下的 slider 定义格式)