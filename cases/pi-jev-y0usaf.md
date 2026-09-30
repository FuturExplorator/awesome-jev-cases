---
slug: "pi-jev-y0usaf"
name_en: "pi-jev"
name_zh: "Pi 编码代理的 Jev 判断层"
project_url: "https://github.com/y0usaf/pi-jev"
source_url: "https://github.com/y0usaf/pi-jev/blob/88e5fb3888948e7065110d47cdf6ac57abb71ba4/README.md"
source_kind: "github"
author: "y0usaf"
source_date: "2026-09-25"
source_date_kind: "commit"
last_checked: "2026-09-30"
source_revision: "88e5fb3888948e7065110d47cdf6ac57abb71ba4"
jev_relation: "uses_typesafe"
scenario: "guardrails"
content_kind: "integration"
status: "verified"
claim_status: "source_reviewed"
upstream_license: "MIT"
evidence_file: "research/evidence/pi-jev-y0usaf.json"
---

# pi-jev / Pi 编码代理的 Jev 判断层

## 中文

### 项目简介

Pi 编码代理的扩展：在工具调用前评估风险，在 bash 输出后判断泄密或错误类型，并提供 `jev_ask` 类型化提问工具。

### Jev 的具体作用

扩展把待执行工具的名称、参数、当前请求等状态发给 TypeSafe Jev，询问破坏性、外传、越界和影响程度；代码根据阈值决定提示或请求确认。输出判断另看 bash 结果。Jev 只提供概率/选项，是否阻止由扩展策略决定。

### 如何复现

在 Pi 中按 README 执行 `pi install npm:@y0usaf/pi-jev`，配置自己的 `TYPESAFE_API_KEY`，用 `/jev` 检查状态。默认 shadow 模式仅提示；需要确认拦截时显式切到 `/jev mode enforce`。无 UI 环境默认退回提示，除非另设 `gate.blockWithoutUI`。调用会把部分工具参数及输出发到 TypeSafe，应先读 README 的数据外发说明。

### 证据与限制

已核对固定 README、TypeSafe 端点、工具调用拦截代码与 MIT LICENSE；未安装 Pi 或测试拦截效果。源码在缺 Key、超时、429 等错误时允许原工具继续，不能当作强制安全边界；作者的校准样本未经复测。

## English

### Overview

A Pi coding-agent extension that evaluates risk before tool calls, judges bash output for secrets or failure type, and offers a `jev_ask` tool for typed questions.

### Jev's specific role

The extension sends a pending tool name, arguments, user request and other state to TypeSafe Jev for destructive, exfiltration, scope and impact judgments. Code thresholds decide whether to notify or request confirmation. A separate output judge reads bash results. Jev supplies probabilities and options; extension policy determines blocking.

### Reproduction

In Pi, run `pi install npm:@y0usaf/pi-jev`, set your own `TYPESAFE_API_KEY`, and inspect `/jev`. Shadow mode only warns by default; explicitly use `/jev mode enforce` for confirmation. Headless runs warn by default unless `gate.blockWithoutUI` is set. Read the README disclosure first: some tool arguments and outputs are sent to TypeSafe.

### Evidence and limitations

Pinned README, TypeSafe endpoint, tool-call hook and MIT license were reviewed. Pi was not installed and enforcement was not tested. Missing keys, timeouts and 429s fail open, so this is not a hard safety boundary; author calibration examples were not reproduced.

## Sources / 来源

- [项目仓库 / Repository](https://github.com/y0usaf/pi-jev)
- [固定版本 README / Pinned README](https://github.com/y0usaf/pi-jev/blob/88e5fb3888948e7065110d47cdf6ac57abb71ba4/README.md)
- [实现 / Implementation: src/client.ts](https://github.com/y0usaf/pi-jev/blob/88e5fb3888948e7065110d47cdf6ac57abb71ba4/src/client.ts)
- [实现 / Implementation: src/gate.ts](https://github.com/y0usaf/pi-jev/blob/88e5fb3888948e7065110d47cdf6ac57abb71ba4/src/gate.ts)
- [实现 / Implementation: src/index.ts](https://github.com/y0usaf/pi-jev/blob/88e5fb3888948e7065110d47cdf6ac57abb71ba4/src/index.ts)
- [原始许可证 / Upstream license](https://github.com/y0usaf/pi-jev/blob/88e5fb3888948e7065110d47cdf6ac57abb71ba4/LICENSE)
