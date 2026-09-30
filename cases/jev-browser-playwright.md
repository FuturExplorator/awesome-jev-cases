---
slug: "jev-browser-playwright"
name_en: "Jev Browser by tontoko"
name_zh: "tontoko 的 Jev 浏览器工具"
project_url: "https://github.com/tontoko/jev-browser"
source_url: "https://github.com/tontoko/jev-browser/blob/73a39641653dbefc88f5f9664afaa63e3370b92b/README.md"
source_kind: "github"
author: "tontoko"
source_date: "2026-09-30"
source_date_kind: "commit"
last_checked: "2026-09-30"
source_revision: "73a39641653dbefc88f5f9664afaa63e3370b92b"
jev_relation: "uses_typesafe"
scenario: "browser"
content_kind: "integration"
status: "verified"
claim_status: "source_reviewed"
upstream_license: "Apache-2.0"
evidence_file: "research/evidence/jev-browser-playwright.json"
---

# Jev Browser by tontoko / tontoko 的 Jev 浏览器工具

## 中文

### 项目简介

把 Playwright 的浏览器操作封装为 SDK、CLI 与 MCP 接口，同时提供基于页面证据的语义定位和断言。

### Jev 的具体作用

工具收集当前页面的候选元素或证据，并把任务与限定的选择问题送给 TypeSafe System One；Jev 选择匹配的目标、动作或语义判断，代码检查返回值并由 Playwright 执行操作。原生点击、截图及精确断言本身无需 Jev。

### 如何复现

从固定版本 README 的安装章节开始，准备 Node.js 22.15+，安装依赖与 Chromium。可先运行无需模型的原生浏览器命令；语义操作需要自己的 TypeSafe 凭据，或自行配置兼容的 System One 服务端。按 README 的 SDK 示例做一次只读语义定位，再核查实际页面结果。

### 证据与限制

已核对仓库身份、README、TypeSafe SDK 决策调用与 Apache-2.0 许可证。作者描述了浏览器任务的验证边界；本库未安装运行、未测试语义准确率或安全性。源码允许配置兼容端点，本案例只确认其默认的 TypeSafe 调用路径。与其他同名浏览器仓库为不同项目。

## English

### Overview

A Playwright browser tool exposed through SDK, CLI and MCP interfaces, with page-grounded semantic location and assertions.

### Jev's specific role

The tool collects current page candidates or evidence and sends the task and bounded choice questions to TypeSafe System One. Jev selects a target, action or semantic judgment; code checks the response and Playwright performs effects. Native clicks, screenshots and exact assertions do not require Jev.

### Reproduction

Follow the pinned README installation section with Node.js 22.15+, dependencies and Chromium. Native browser commands work without a model. Semantic operations require your own TypeSafe credentials or a configured compatible System One endpoint. Try a read-only semantic location from the SDK example and check the page result yourself.

### Evidence and limitations

Repository identity, README, TypeSafe SDK decision call and Apache-2.0 license were reviewed. The author describes verification boundaries; installation, semantic accuracy and security were not independently tested here. The code permits a compatible endpoint; this case confirms the default TypeSafe path. This is a distinct repository from other similarly named browser projects.

## Sources / 来源

- [项目仓库 / Repository](https://github.com/tontoko/jev-browser)
- [固定版本 README / Pinned README](https://github.com/tontoko/jev-browser/blob/73a39641653dbefc88f5f9664afaa63e3370b92b/README.md)
- [决策调用 / Decision call](https://github.com/tontoko/jev-browser/blob/73a39641653dbefc88f5f9664afaa63e3370b92b/src/decision.ts)
- [语义判断 / Semantic judgment](https://github.com/tontoko/jev-browser/blob/73a39641653dbefc88f5f9664afaa63e3370b92b/src/semantic.ts)
- [原始许可证 / Upstream license](https://github.com/tontoko/jev-browser/blob/73a39641653dbefc88f5f9664afaa63e3370b92b/LICENSE)
