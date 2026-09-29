---
slug: "jev-ra"
name_en: "Jev-RA"
name_zh: "编码代理的浏览器执行层"
project_url: "https://github.com/brnyxx/jev-ra"
source_url: "https://github.com/brnyxx/jev-ra/blob/721fc73d4571d4e4ad90dab65481e52f5b2f2531/README.md"
source_kind: "github"
author: "brnyxx"
source_date: "2026-09-29"
source_date_kind: "commit"
last_checked: "2026-09-29"
source_revision: "721fc73d4571d4e4ad90dab65481e52f5b2f2531"
jev_relation: "uses_typesafe"
scenario: "browser"
content_kind: "application"
status: "verified"
claim_status: "source_reviewed"
upstream_license: "MIT"
evidence_file: "research/evidence/jev-ra.json"
---

# Jev-RA / 编码代理的浏览器执行层

## 中文

### 项目简介

由编码代理提供目标与输入值，通过 CLI 或 MCP 控制 Chrome。

### Jev 的具体作用

Jev 根据观察到的页面候选，选择操作、目标元素及已有输入值，并判断页面上的目标完成证据；浏览器执行由本地代码承担。

### 如何复现

按 README Quick start 配置其支持的 Jev 提供方凭据，运行 doctor 后在独立浏览器中尝试文档中的导航任务。

### 证据与限制

已核对公开仓库身份、固定版本 README、调用实现与许可证；`verified` 仅指来源核验通过。未安装运行，未进行独立效果测试。速度比较由作者在特定任务与环境下测得，本库未复测。文本值由调用方提供；不应声称 Jev 自行生成表单内容。

## English

### Overview

A CLI/MCP browser execution layer: a coding agent supplies the goal and input values, and local code drives Chrome.

### Jev's specific role

Jev selects an operation, observed target and supplied value, and judges visible completion evidence. Local browser code performs the effects.

### Reproduction

Follow the README Quick start, configure credentials for a supported Jev provider, run doctor, and try its navigation example in a separate browser.

### Evidence and limitations

Public identity, pinned README, implementation and license were reviewed. `verified` means source-verified only; installation, runtime and independent effectiveness tests were not performed. Speed comparisons are author measurements for specific tasks and environments, not reproduced here. Input values come from the caller; Jev does not generate arbitrary form text.

## Sources / 来源

- 项目与作者 / Project and owner: [brnyxx/jev-ra](https://github.com/brnyxx/jev-ra)
- 所核对版本 / Reviewed revision: [`721fc73d4571`](https://github.com/brnyxx/jev-ra/commit/721fc73d4571d4e4ad90dab65481e52f5b2f2531); `source_date` is this commit's date, not a launch date / 来源日期为提交日期，不是发布日期。
- [README.md](https://github.com/brnyxx/jev-ra/blob/721fc73d4571d4e4ad90dab65481e52f5b2f2531/README.md)
- [jev_ra/decide/client.py](https://github.com/brnyxx/jev-ra/blob/721fc73d4571d4e4ad90dab65481e52f5b2f2531/jev_ra/decide/client.py)
- [jev_ra/decide/questions.py](https://github.com/brnyxx/jev-ra/blob/721fc73d4571d4e4ad90dab65481e52f5b2f2531/jev_ra/decide/questions.py)
- [LICENSE](https://github.com/brnyxx/jev-ra/blob/721fc73d4571d4e4ad90dab65481e52f5b2f2531/LICENSE)
- [核验记录与 SHA-256 / Review receipt and SHA-256](../research/evidence/jev-ra.json)
- [第三方权利 / Third-party rights](../THIRD_PARTY_NOTICES.md): MIT
- 关联案例浏览网站 / Related browsing site: [jevforagents.com](https://jevforagents.com) — no case-specific page is asserted / 未宣称对应详情页存在。
