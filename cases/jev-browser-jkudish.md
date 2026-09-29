---
slug: "jev-browser-jkudish"
name_en: "Jev Browser"
name_zh: "Jev 浏览器"
project_url: "https://github.com/jkudish/jev-browser"
source_url: "https://github.com/jkudish/jev-browser/blob/b767894987cd45bf77a786fe410051613eabcef0/README.md"
source_kind: "github"
author: "jkudish"
source_date: "2026-09-27"
source_date_kind: "commit"
last_checked: "2026-09-29"
source_revision: "b767894987cd45bf77a786fe410051613eabcef0"
jev_relation: "uses_typesafe"
scenario: "browser"
content_kind: "application"
status: "verified"
claim_status: "source_reviewed"
upstream_license: "MIT"
evidence_file: "research/evidence/jev-browser-jkudish.json"
---

# Jev Browser / Jev 浏览器

## 中文

### 项目简介

通过 MCP、CLI 或库接口执行有步数与时间预算的浏览器任务。

### Jev 的具体作用

页面状态与候选元素进入 Jev；它选择下一动作，并判断目标是否完成、是否卡住。代码执行动作并管理停止条件。

### 如何复现

从原始 README 的 Install 与 CLI 章节开始，准备 Node.js 22+、浏览器和自己的 TypeSafe 凭据，再用一个只读导航任务检查步骤记录。

### 证据与限制

已核对公开仓库身份、固定版本 README、调用实现与许可证；`verified` 仅指来源核验通过。未安装运行，未进行独立效果测试。作者展示了速度和费用示例，本库未复测。键入文本可能使用单独的生成模型；不能把整个流程称为只有 Jev。

## English

### Overview

A browser task runner exposed through MCP, CLI and a library, with step and time budgets.

### Jev's specific role

Jev receives page state and candidate elements, selects an action, and judges completion and lack of progress. Code executes actions and controls stopping.

### Reproduction

Follow the pinned README Install and CLI sections: prepare Node.js 22+, a browser and your own TypeSafe credentials, then inspect a read-only navigation trace.

### Evidence and limitations

Public identity, pinned README, implementation and license were reviewed. `verified` means source-verified only; installation, runtime and independent effectiveness tests were not performed. Speed and cost examples are author-reported and untested here. Typing may use a separate generative model; the whole workflow is not necessarily Jev-only.

## Sources / 来源

- 项目与作者 / Project and owner: [jkudish/jev-browser](https://github.com/jkudish/jev-browser)
- 所核对版本 / Reviewed revision: [`b767894987cd`](https://github.com/jkudish/jev-browser/commit/b767894987cd45bf77a786fe410051613eabcef0); `source_date` is this commit's date, not a launch date / 来源日期为提交日期，不是发布日期。
- [README.md](https://github.com/jkudish/jev-browser/blob/b767894987cd45bf77a786fe410051613eabcef0/README.md)
- [src/navigate.ts](https://github.com/jkudish/jev-browser/blob/b767894987cd45bf77a786fe410051613eabcef0/src/navigate.ts)
- [src/provider.ts](https://github.com/jkudish/jev-browser/blob/b767894987cd45bf77a786fe410051613eabcef0/src/provider.ts)
- [src/questions.ts](https://github.com/jkudish/jev-browser/blob/b767894987cd45bf77a786fe410051613eabcef0/src/questions.ts)
- [LICENSE](https://github.com/jkudish/jev-browser/blob/b767894987cd45bf77a786fe410051613eabcef0/LICENSE)
- [核验记录与 SHA-256 / Review receipt and SHA-256](../research/evidence/jev-browser-jkudish.json)
- [第三方权利 / Third-party rights](../THIRD_PARTY_NOTICES.md): MIT
- 关联案例浏览网站 / Related browsing site: [jevforagents.com](https://jevforagents.com) — no case-specific page is asserted / 未宣称对应详情页存在。
