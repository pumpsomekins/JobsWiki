# JobsWiki - 职业生命周期数据平台

一个专注于职业数据分析与可视化的项目，帮助用户了解不同职业的收入潜力、技能发展路径以及AI自动化风险。

## 项目结构

```
JobsWiki/
├── jobs/                    # 职业数据JSON文件
│   ├── chef.json            # 厨师职业数据
│   ├── dasher.json          # 外卖骑手职业数据
│   └── income-types.json    # 收入类型配置
├── prototypes/              # 职业展示HTML页面（调用jobs/中的JSON）
│   ├── chef.html            # 厨师职业页面
│   └── dasher.html          # 外卖骑手职业页面
├── job-template.html        # 新职业页面模板
├── docs/                    # 项目文档
├── .trae/                   # Trae IDE 技能配置
└── README.md
```

## 核心功能

### 1. 职业数据展示
- **收入分析**: 展示不同国家、不同级别的薪资数据，支持自定义计算器
- **职业发展路径**: 清晰的晋升路径和时间预估
- **终身价值(LTV)**: 总收益、安全收益、风险收益、自动化指数、风险年龄

### 2. 多维度比较
- **国家对比**: 覆盖美、英、澳、德、日、新、台、中8个地区
- **城市热力图**: 各城市薪资与生活成本对比
- **语言要求**: 各地区语言能力要求评估
- **教育与社交**: 名校推荐、MBTI匹配、名人堂

### 3. 风险评估
- **AI自动化威胁**: 各任务被AI替代的可能性和时间预估
- **职业危害**: 工作环境风险等级评估
- **生存策略**: 应对自动化的职业发展建议

## 技术特点

- **纯前端实现**: 无需后端，HTML从JSON加载数据即可运行
- **响应式设计**: 适配桌面和移动设备
- **数据驱动**: JSON配置，HTML页面通过fetch动态加载数据，易于扩展新职业
- **深色主题**: 现代化深色UI设计

## 使用方法

用本地服务器打开（需解决跨域fetch问题）：

```bash
# 例如用 Python
cd JobsWiki
python -m http.server 8000

# 然后访问
# http://localhost:8000/prototypes/chef.html
# http://localhost:8000/prototypes/dasher.html
```

## 数据规范

职业数据遵循 `Job Data JSON Specification (v2.0)` 规范，包含：
- `meta`: 职业基本信息和计算配置
- `search`: 搜索关键词和别名
- `industries`: 行业分类
- `countries`: 各国数据（薪资、自动化指数等）
- `levels`: 职业级别定义
- `promotions`: 晋升路径
- `levelUSD` / `levelLocal`: 各级别薪资
- `languages`: 语言要求
- `cities`: 城市薪资数据
- `countryMeta`: 各国工作条件
- `extendedMeta`: 教育、创业、MBTI等扩展信息
- `famousPersons`: 名人堂
- `networkCards`: 社交策略卡片
- `insightCards`: 洞察卡片配置
- `tasksByLevel`: 各级别任务及AI风险评估

## 扩展指南

如需添加新职业：
1. 复制 `jobs/chef.json` 或 `jobs/dasher.json` 作为模板，修改数据
2. 复制 `job-template.html` 或现有 `prototypes/` 下的HTML，修改fetch路径和职业相关字段
3. 确保JSON遵循 `.trae/skills/job-data-json-specification-v1-0/SKILL.md` 规范

## 项目状态

🚀 **开发中** - 持续更新更多职业数据和功能

---

*项目由 Trae IDE 驱动*
