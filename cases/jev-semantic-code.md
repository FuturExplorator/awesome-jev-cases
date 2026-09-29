---
slug: "jev-semantic-code"
name_en: "Jev Semantic Code Reading"
name_zh: "语义代码定位与读取"
project_url: "https://github.com/BorisLeMeec/jev"
source_url: "https://github.com/BorisLeMeec/jev/blob/e81c1d006b8b23a616486610f311039088521d0c/README.md"
source_kind: "github"
author: "BorisLeMeec"
source_date: "2026-09-18"
source_date_kind: "commit"
last_checked: "2026-09-29"
source_revision: "e81c1d006b8b23a616486610f311039088521d0c"
jev_relation: "uses_typesafe"
scenario: "coding"
content_kind: "integration"
status: "verified"
claim_status: "source_reviewed"
upstream_license: "MIT"
evidence_file: "research/evidence/jev-semantic-code.json"
---

# Jev Semantic Code Reading / 语义代码定位与读取

## 中文

### 项目简介

一个 Go 实现的 Claude Code 插件，用自然语言定位代码、询问代码属性并缩小大型文件读取范围。

### Jev 的具体作用

Jev 对文件相关性和有界问题给出判断，再对候选代码块做选择；插件返回位置或相关窗口，Claude Code 继续阅读与执行任务。

### 如何复现

按 README Install 准备 Go 1.22+ 和自己的 TYPE_SAFE_AI_KEY，安装插件；从一个非敏感小仓库的 jev find 或 jev ask 开始查看原始代码位置。

### 证据与限制

已核对公开仓库身份、固定版本 README、调用实现与许可证；`verified` 仅指来源核验通过。未安装运行，未进行独立效果测试。作者的小样本 token 结果未在本库复测；部分 find/ask 数据集针对私有仓库，不能声称完整公开复现。概率不是正确性的证明。

## English

### Overview

A Go-based Claude Code plugin for semantic code search, bounded code questions and narrower large-file reads.

### Jev's specific role

Jev judges file relevance and bounded questions, then selects candidate code chunks. The plugin returns locations or relevant windows for Claude Code to inspect and act on.

### Reproduction

Follow Install with Go 1.22+ and your own TYPE_SAFE_AI_KEY. Install the plugin and try jev find or jev ask on a small non-sensitive repository, checking the returned locations.

### Evidence and limitations

Public identity, pinned README, implementation and license were reviewed. `verified` means source-verified only; installation, runtime and independent effectiveness tests were not performed. Small-sample token results are author-reported, not rerun here. Some find/ask datasets concern private repositories, so full public reproducibility is not established. Probabilities are not correctness proofs.

## Sources / 来源

- 项目与作者 / Project and owner: [BorisLeMeec/jev](https://github.com/BorisLeMeec/jev)
- 所核对版本 / Reviewed revision: [`e81c1d006b8b`](https://github.com/BorisLeMeec/jev/commit/e81c1d006b8b23a616486610f311039088521d0c); `source_date` is this commit's date, not a launch date / 来源日期为提交日期，不是发布日期。
- [README.md](https://github.com/BorisLeMeec/jev/blob/e81c1d006b8b23a616486610f311039088521d0c/README.md)
- [internal/typesafe/client.go](https://github.com/BorisLeMeec/jev/blob/e81c1d006b8b23a616486610f311039088521d0c/internal/typesafe/client.go)
- [LICENSE](https://github.com/BorisLeMeec/jev/blob/e81c1d006b8b23a616486610f311039088521d0c/LICENSE)
- [核验记录与 SHA-256 / Review receipt and SHA-256](../research/evidence/jev-semantic-code.json)
- [第三方权利 / Third-party rights](../THIRD_PARTY_NOTICES.md): MIT
- 关联案例浏览网站 / Related browsing site: [jevforagents.com](https://jevforagents.com) — no case-specific page is asserted / 未宣称对应详情页存在。
