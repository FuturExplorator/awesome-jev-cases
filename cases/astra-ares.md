---
slug: "astra-ares"
name_en: "Astra-Ares"
name_zh: "任务中的推理力度选择"
project_url: "https://github.com/miuuyy/Astra-Ares"
source_url: "https://github.com/miuuyy/Astra-Ares/blob/b2011446d88202329dcdc5163500ca818aba9dbb/README.md"
source_kind: "github"
author: "miuuyy"
source_date: "2026-09-23"
source_date_kind: "commit"
last_checked: "2026-09-29"
source_revision: "b2011446d88202329dcdc5163500ca818aba9dbb"
jev_relation: "uses_typesafe"
scenario: "routing"
content_kind: "experiment"
status: "verified"
claim_status: "source_reviewed"
upstream_license: "MIT"
evidence_file: "research/evidence/astra-ares.json"
---

# Astra-Ares / 任务中的推理力度选择

## 中文

### 项目简介

在单独打补丁的实验版 Codex CLI 中，按任务进展调整所选模型的推理力度。

### Jev 的具体作用

Jev 读取有界任务上下文与近期工具结果，选择下一次生成的推理力度及该配置持续的生成轮数；打过补丁的 CLI 负责应用该选择。

### 如何复现

按固定 README 的 Get started 准备 Node.js 22+、Rust 和编译环境，执行独立 CLI 的构建流程，再配置 Jev 提供方凭据；先用本地 doctor 检查。

### 证据与限制

已核对公开仓库身份、固定版本 README、调用实现与许可证；`verified` 仅指来源核验通过。未安装运行，未进行独立效果测试。作者将其定位为实验参考实现，默认新安装走 OpenRouter。缓存收益与费用节省未由本库验证；不是桌面 App 的原生功能。

## English

### Overview

An experimental, separately patched Codex CLI that adjusts reasoning effort as a task progresses.

### Jev's specific role

Jev reads bounded task context and recent tool results, selects effort for the next generation and a duration in generations; the patched host applies the choice.

### Reproduction

Follow Get started in the pinned README: prepare Node.js 22+, Rust and build tools, build the separate CLI, configure Jev-provider credentials, and start with the local doctor check.

### Evidence and limitations

Public identity, pinned README, implementation and license were reviewed. `verified` means source-verified only; installation, runtime and independent effectiveness tests were not performed. The author labels it a reference experiment; new installations default to OpenRouter. Cache benefits and savings were not verified here. This is not a native desktop App feature.

## Sources / 来源

- 项目与作者 / Project and owner: [miuuyy/Astra-Ares](https://github.com/miuuyy/Astra-Ares)
- 所核对版本 / Reviewed revision: [`b2011446d882`](https://github.com/miuuyy/Astra-Ares/commit/b2011446d88202329dcdc5163500ca818aba9dbb); `source_date` is this commit's date, not a launch date / 来源日期为提交日期，不是发布日期。
- [README.md](https://github.com/miuuyy/Astra-Ares/blob/b2011446d88202329dcdc5163500ca818aba9dbb/README.md)
- [src/jev.mjs](https://github.com/miuuyy/Astra-Ares/blob/b2011446d88202329dcdc5163500ca818aba9dbb/src/jev.mjs)
- [LICENSE](https://github.com/miuuyy/Astra-Ares/blob/b2011446d88202329dcdc5163500ca818aba9dbb/LICENSE)
- [核验记录与 SHA-256 / Review receipt and SHA-256](../research/evidence/astra-ares.json)
- [第三方权利 / Third-party rights](../THIRD_PARTY_NOTICES.md): MIT
- 关联案例浏览网站 / Related browsing site: [jevforagents.com](https://jevforagents.com) — no case-specific page is asserted / 未宣称对应详情页存在。
