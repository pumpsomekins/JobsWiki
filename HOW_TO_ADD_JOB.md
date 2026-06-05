# 添加新职业指南

## 快速开始

1. **复制模板文件**：复制 `jobs/template-job.json` 并重命名为 `jobs/[职业slug].json`
2. **填写数据**：按照模板中的注释填写职业数据
3. **测试**：访问 `job-template.html?job=[职业slug]` 验证效果

## 必须填写的字段

### meta 对象
| 字段 | 说明 | 示例 |
|------|------|------|
| `job` | 职业名称（显示用） | `"Chef / Cook"` |
| `slug` | 唯一标识（英文小写） | `"chef"` |
| `heroImage` | 英雄图片URL | Unsplash图片链接 |
| `hallOfFameDesc` | 名人堂描述 | `"These chefs scaled..."` |

### famousPersons 对象
- 将原来的 `famousChefs` / `famousDashers` 统一改为 `famousPersons`
- 至少包含8个国家的数据：US, UK, AU, DE, JP, SG, TW, CN

## 使用示例

```bash
# 复制模板创建新职业
cp jobs/template-job.json jobs/doctor.json

# 编辑数据后访问
# http://localhost:8000/job-template.html?job=doctor
```

## 验证清单

- [ ] `meta.job` 已填写
- [ ] `meta.slug` 与文件名一致
- [ ] `meta.heroImage` 已填写
- [ ] `meta.hallOfFameDesc` 已填写
- [ ] `famousPersons` 字段已配置（非 `famousXxx`）
- [ ] 所有8个国家数据完整

## 注意事项

- 禁止空字符串 `""`，无数据请填 `null`
- JSON 文件必须格式正确
- 新增职业后无需修改 `job-template.html`