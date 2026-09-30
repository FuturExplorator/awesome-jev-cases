---
slug: "fast-jev-compaction-tamara-tran"
name_en: "fast-jev-compaction"
name_zh: "fast-jev-compaction 上下文压缩"
project_url: "https://github.com/tamaratran/fast-jev-compaction"
source_url: "https://github.com/tamaratran/fast-jev-compaction/blob/e3f262a7f4d42bd8dd32ced30d26176f7cb545b0/README.md"
source_kind: "github"
author: "tamaratran"
source_date: "2026-09-17"
source_date_kind: "commit"
last_checked: "2026-09-30"
source_revision: "e3f262a7f4d42bd8dd32ced30d26176f7cb545b0"
jev_relation: "uses_typesafe"
scenario: "coding"
content_kind: "integration"
status: "verified"
claim_status: "source_reviewed"
upstream_license: "MIT"
evidence_file: "research/evidence/fast-jev-compaction-tamara-tran.json"
website_url: "https://jevforagents.com/builds/instant-context-compaction-tamara-tran"
---

# fast-jev-compaction / fast-jev-compaction 上下文压缩

## 中文

### 项目简介

Claude Code 插件及库：在压缩对话上下文时筛选工具调用与工具结果，减少过时内容，同时让保留的信息维持原文。网站中的演示和同仓库旧条目指向同一项目。

### Jev 的具体作用

程序将会话历史作为状态，为未固定保留的工具调用分别提出“是否保留调用”和“是否保留结果”的类型化问题。Jev 返回判断，代码据此保留、丢弃或截短内容；Jev 不生成新的摘要。默认客户端使用 TypeSafe System One API。

### 如何复现

参考固定版本 README 安装 npm 包，设置自己的 `TYPESAFE_API_KEY`，用其示例调用 `compactMessages`。要接入 Claude Code 的 `/compact`，还需按 README 启用函数 hook 并安装插件。仓库单元测试使用假的 Jev 传输；实时 demo 会调用 API，需自行评估费用。

### 证据与限制

已核对仓库身份、固定 README、客户端与压缩实现、MIT 许可证；未安装或运行。错误响应、缺 Key 或超出请求大小时会抛错，由调用方或 hook 决定回退。删错上下文可能损害后续任务；网站演示不等于独立压缩质量验证。

## English

### Overview

A Claude Code plugin and library that filters tool calls and tool results during conversation compaction, reducing stale context while keeping retained material verbatim. The website demo and its older same-repository entry describe this one project.

### Jev's specific role

Code sends conversation history as state and asks typed keep-call and keep-result questions for each non-pinned tool call. Jev returns judgments; code retains, drops or truncates material accordingly. Jev does not generate a new summary. The default client calls TypeSafe System One.

### Reproduction

Install the npm package from the pinned README, set your own `TYPESAFE_API_KEY` and call `compactMessages` with the example transcript. Claude Code `/compact` integration also needs function hooks enabled and the plugin installed. Repository unit tests use a fake Jev transport; the live demo calls the API, so assess cost first.

### Evidence and limitations

Repository identity, pinned README, client, compaction implementation and MIT license were reviewed; no installation or run was performed. Missing credentials, bad responses or oversized requests throw, leaving fallback to the caller or hook. Removing useful context can harm later work; the website demo is not independent compaction-quality evidence.

## Sources / 来源

- [项目仓库 / Repository](https://github.com/tamaratran/fast-jev-compaction)
- [固定版本 README / Pinned README](https://github.com/tamaratran/fast-jev-compaction/blob/e3f262a7f4d42bd8dd32ced30d26176f7cb545b0/README.md)
- [TypeSafe 客户端 / TypeSafe client](https://github.com/tamaratran/fast-jev-compaction/blob/e3f262a7f4d42bd8dd32ced30d26176f7cb545b0/src/client.ts)
- [压缩决策 / Compaction decisions](https://github.com/tamaratran/fast-jev-compaction/blob/e3f262a7f4d42bd8dd32ced30d26176f7cb545b0/src/compact.ts)
- [网站中的同一项目 / Same project on JevForAgents](https://jevforagents.com/builds/instant-context-compaction-tamara-tran)
- [原始许可证 / Upstream license](https://github.com/tamaratran/fast-jev-compaction/blob/e3f262a7f4d42bd8dd32ced30d26176f7cb545b0/LICENSE)
