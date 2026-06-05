---
name: Job Data JSON Specification (v2.0)
description: 生成和修改职业json时
---

# Job Data JSON Specification (v2.0)

## 1. 基本规则（Strict Rules）
- 禁止空字符串 ""，没有数据必须填 null 或实际内容
- 禁止硬编码显示值（如直接写 "High" 或 "Your Schedule"）
- 所有动态显示字段必须用 {{value}} 双花括号占位符
- 所有 task 对象必须包含 statusLabel 字段
- statusLabel 只能是以下四个值之一：
  "Replaceable" / "In-Danger" / "Intro" / "Nothing"

## 2. 顶层必填字段清单

### 必填（REQUIRED）
meta, search, industries, countries, levels, promotions,
levelUSD, levelLocal, languages, langScoreLabels, cities,
countryMeta, difficultyLabels, insightCards, extendedMeta,
startupLinks, famousXxx, accessLinks, careerRecs,
survivalStrategy, hazards, filters, mbtiData,
tasksByLevel, countryTaskMods, version, footnote

### 选填（OPTIONAL）
filialPietyCountries, ltvMethodology, highestThreat,
langPillClasses, networkCards

## 3. search 字段规范
说明 primaryTitle / primarySlug / aliases / subTitles 的
格式要求，subTitles 必须是对象数组，每个对象包含：
title, slug, levelIndex, type, aliases（至少2个）

## 4. meta.calculatorInputSpecs 规范
说明每个 slider 对象必须包含：
label, min, max, default, step, unit
并列出支持的 incomeType 枚举值：
salary / hourly / piecerate / commission / freelance

## 5. insightCards 规范
- valueTemplate 必须用 {{value}} 占位符
- metaTemplate 里的动态字段也用 {{fieldName}} 格式
- colorMode 只能是：gradient-bad / gradient-good / accent / neutral

## 6. 国家覆盖要求
必须覆盖全部 8 个国家/地区：US / UK / AU / DE / JP / SG / TW / CN
extendedMeta 里每个国家的以下字段必须有实际内容（禁止空字符串）：
hnwi, uniMeta, privateMeta, schools, retire, pivot
startupLinks 每个国家必须有至少 2 个条目，url 可用 "#" 占位
famousXxx 每个国家必须有至少 1 个条目，name 不能为空

---

参考 chef.json 和 dasher.json 的实际结构来举例说明。
文件风格要简洁清晰，给 AI 看的，不是给用户看的。