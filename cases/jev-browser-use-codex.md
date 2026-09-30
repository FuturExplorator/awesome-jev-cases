---
slug: "jev-browser-use-codex"
name_en: "Jev Browser Use"
name_zh: "Jev Browser Use 浏览器技能"
project_url: "https://github.com/wy-coliney/jev-browser-use"
source_url: "https://github.com/wy-coliney/jev-browser-use/blob/cf7e76607d4ec70592b24becadd0296dcda8177a/README.md"
source_kind: "github"
author: "wy-coliney"
source_date: "2026-09-23"
source_date_kind: "commit"
last_checked: "2026-09-30"
source_revision: "cf7e76607d4ec70592b24becadd0296dcda8177a"
jev_relation: "uses_typesafe"
scenario: "browser"
content_kind: "integration"
status: "verified"
claim_status: "source_reviewed"
upstream_license: "MIT"
evidence_file: "research/evidence/jev-browser-use-codex.json"
---

# Jev Browser Use / Jev Browser Use 浏览器技能

## 中文

### 项目简介

一个将 Jev 接到 Codex 浏览器连接的社区技能与插件。Codex 规划任务、输入文本并检查结果；桥接程序处理有限的浏览器操作循环。

### Jev 的具体作用

桥接程序把当前可访问性页面文本、目标、历史与允许的操作编成选择题，请 Jev 选下一次点击、滚动、按键或停止信号。程序核对置信度与页面状态后执行动作；Jev 给出完成信号时仍交回 Codex 独立验证。

### 如何复现

按固定版本 README 安装技能或插件，准备 Node.js 22+、已连接的 Codex 浏览器及自己的 TypeSafe Jev 凭据，再从 README 的设置页只读导航示例开始。安装说明也支持其他提供方；若改用它们，本案例不能算对 TypeSafe 端点的复现。

### 证据与限制

已核对仓库身份、README、技能说明、桥接请求及 MIT 许可证。作者声称浏览器操作约快 5–10 倍，未给出可由本库独立复测的结果；本库没有安装、运行或测量。当前 README 写明浏览器执行依赖 Codex Computer Use，Claude Code 的浏览器支持尚未完成。它是社区集成，不是 OpenAI 或 TypeSafe 官方产品；页面文本会发给所配置的提供方。

## English

### Overview

A community skill and plugin connecting Jev to a Codex browser session. Codex plans, enters text and checks outcomes; the bridge handles a bounded browser-action loop.

### Jev's specific role

The bridge turns current accessibility text, goal, history and permitted controls into a choice question. Jev selects the next click, scroll, key or stop signal. Code checks confidence and page freshness before acting; a completion signal returns control to Codex for independent verification.

### Reproduction

Install the skill or plugin from the pinned README, prepare Node.js 22+, a connected Codex browser and your own TypeSafe Jev credentials, then start with a read-only settings-page navigation example. The installation guide supports other providers; using them would not reproduce this case's TypeSafe endpoint path.

### Evidence and limitations

Repository identity, README, skill instructions, bridge request and MIT license were reviewed. The author's approximately 5–10× browser-operation speedup claim was not independently reproduced. No installation, run or measurement was performed here. The current README says browser execution needs Codex Computer Use; Claude Code browser support is pending. This is a community integration, not an official OpenAI or TypeSafe product. Page text goes to the configured provider.

## Sources / 来源

- [项目仓库 / Repository](https://github.com/wy-coliney/jev-browser-use)
- [固定版本 README / Pinned README](https://github.com/wy-coliney/jev-browser-use/blob/cf7e76607d4ec70592b24becadd0296dcda8177a/README.md)
- [桥接实现 / Bridge implementation](https://github.com/wy-coliney/jev-browser-use/blob/cf7e76607d4ec70592b24becadd0296dcda8177a/skills/jev-browser-use/bridge.mjs)
- [技能说明 / Skill instructions](https://github.com/wy-coliney/jev-browser-use/blob/cf7e76607d4ec70592b24becadd0296dcda8177a/skills/jev-browser-use/SKILL.md)
- [原始许可证 / Upstream license](https://github.com/wy-coliney/jev-browser-use/blob/cf7e76607d4ec70592b24becadd0296dcda8177a/LICENSE)
