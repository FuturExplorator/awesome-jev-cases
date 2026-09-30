---
slug: "jev-seo-agrici"
name_en: "jev-seo by AgriciDaniel"
name_zh: "Jev 网站 SEO 审核"
project_url: "https://github.com/AgriciDaniel/jev-seo"
source_url: "https://github.com/AgriciDaniel/jev-seo/blob/55a184a3b0d09565a4c84268f725a47784e62528/README.md"
source_kind: "github"
author: "AgriciDaniel"
source_date: "2026-09-22"
source_date_kind: "commit"
last_checked: "2026-09-30"
source_revision: "55a184a3b0d09565a4c84268f725a47784e62528"
jev_relation: "uses_typesafe"
scenario: "evaluation"
content_kind: "application"
status: "verified"
claim_status: "source_reviewed"
upstream_license: "MIT"
evidence_file: "research/evidence/jev-seo-agrici.json"
---

# jev-seo by AgriciDaniel / Jev 网站 SEO 审核

## 中文

### 项目简介

从网站首页 URL 开始的本地 SEO 审核工具：抓取页面并运行确定性检查，生成审阅数据，再输出 PDF、XLSX 和 Markdown 报告。它还可作为 Claude Code 技能调用；这两个入口属于同一个仓库案例。

### Jev 的具体作用

固定源码把站点及页面证据发往 TypeSafe `/v1/systemone`，用 Choice、Score、Noul 问题判断页面类型、搜索意图、有用性、可信度和页面之间的竞争等。代码另运行抓取、规则检查、PageSpeed 和修复项排序；最终评分与报告不是 Jev 单独生成。

### 如何复现

按固定 README 准备 Python 3.10+ 和 WeasyPrint 所需的 Pango，安装 `requirements.txt`，从 `.env.example` 设置自己的 `TYPESAFE_API_KEY`，用 `bin/jevseo doctor` 检查环境，再对获准审核的站点执行 `bin/jevseo run https://example.com`。`--full` 会接入另一个付费 DataForSEO 服务，首轮可不启用。

### 证据与限制

已核对固定 README、Jev 请求与回答校验、评分代码和 MIT LICENSE；未抓取网站、运行付费调用或复测作者的准确率、费用、52 项规则覆盖率和示例报告。没有 TypeSafe Key 时 README 说明仍会产出标记为部分审核的结果。

## English

### Overview

A local SEO auditor starting from a homepage URL. It crawls pages, applies deterministic checks, stores review data and renders PDF, XLSX and Markdown reports. It also exposes a Claude Code skill; both entry points belong to this one repository case.

### Jev's specific role

Pinned code posts site and page evidence to TypeSafe `/v1/systemone` with Choice, Score and Noul questions about page type, search intent, helpfulness, trust and page competition. Crawling, rule checks, PageSpeed, fix prioritization and report rendering are separate code paths; the final score is not written by Jev alone.

### Reproduction

With Python 3.10+ and Pango for WeasyPrint, follow the pinned README to install `requirements.txt`, set your own `TYPESAFE_API_KEY` from `.env.example`, run `bin/jevseo doctor`, then audit an authorized site with `bin/jevseo run https://example.com`. Optional `--full` adds paid DataForSEO calls and can be omitted.

### Evidence and limitations

Pinned README, Jev request/answer validation, scoring code and MIT license were reviewed. No site was crawled, no paid call made, and the author’s accuracy, cost, 52-rule coverage and sample reports were not reproduced. Without a TypeSafe key, the README says output is labeled a partial audit.

## Sources / 来源

- [项目仓库 / Repository](https://github.com/AgriciDaniel/jev-seo)
- [固定版本 README / Pinned README](https://github.com/AgriciDaniel/jev-seo/blob/55a184a3b0d09565a4c84268f725a47784e62528/README.md)
- [实现 / Implementation: jevseo/jev.py](https://github.com/AgriciDaniel/jev-seo/blob/55a184a3b0d09565a4c84268f725a47784e62528/jevseo/jev.py)
- [实现 / Implementation: jevseo/score.py](https://github.com/AgriciDaniel/jev-seo/blob/55a184a3b0d09565a4c84268f725a47784e62528/jevseo/score.py)
- [原始许可证 / Upstream license](https://github.com/AgriciDaniel/jev-seo/blob/55a184a3b0d09565a4c84268f725a47784e62528/LICENSE)
