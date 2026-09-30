---
slug: "jev-router-gargpratyush"
name_en: "jev-router by gargpratyush"
name_zh: "gargpratyush 的 jev-router"
project_url: "https://github.com/gargpratyush/jev-router"
source_url: "https://github.com/gargpratyush/jev-router/blob/38da6b84ea01241bfc41fbddc0928d0f40a703f0/README.md"
source_kind: "github"
author: "gargpratyush"
source_date: "2026-09-19"
source_date_kind: "commit"
last_checked: "2026-09-30"
source_revision: "38da6b84ea01241bfc41fbddc0928d0f40a703f0"
jev_relation: "uses_typesafe"
scenario: "routing"
content_kind: "integration"
status: "verified"
claim_status: "source_reviewed"
upstream_license: "MIT"
evidence_file: "research/evidence/jev-router-gargpratyush.json"
website_url: "https://jevforagents.com/builds/jev-router"
---

# jev-router by gargpratyush / gargpratyush 的 jev-router

## 中文

### 项目简介

给 Claude Code 与 Codex CLI 增加逐轮模型路由的启动器。它与本库已收录的 `rajdhakad9826/jev-router` 是不同仓库，两个项目各保留一条。

### Jev 的具体作用

新用户轮次的提示词、当前模型、上下文规模和可选模型进入 TypeSafe SDK。Jev 回答任务复杂度、推理需求、工具复杂度，并选择建议模型；代码策略检查置信度与可用性后才决定实际使用的模型。Jev 失败时按源码策略保留当前模型。

### 如何复现

按固定版本 README 安装 `jev-router`，设置自己的 `JEV_API_KEY` 或 `TYPESAFE_API_KEY`，然后通过 `jev-claude` 或 `jev-codex` 启动已登录的对应 CLI。可先运行项目的离线测试，再用一个简单新任务检查路由记录；实时路由会调用 TypeSafe API。

### 证据与限制

已核对固定 README、TypeSafe SDK 请求、后续策略与 MIT 许可证；本库没有安装、运行或测试路由效果。项目 README 说明在特定 Windows/CLI 版本上开发和测试，不能据此推断其他环境同样通过。路由结果依赖可用模型、任务描述及项目策略，并非 Jev 单独控制。

## English

### Overview

A launcher adding per-turn model routing to Claude Code and Codex CLI. It is a distinct repository from the already cataloged `rajdhakad9826/jev-router`; each project has one entry.

### Jev's specific role

The new user prompt, current model, context size and available models go to the TypeSafe SDK. Jev answers task complexity, reasoning need and tool complexity, and recommends a model. Code policy checks confidence and availability before choosing the model actually used. If Jev fails, source policy keeps the current model.

### Reproduction

Install `jev-router` from the pinned README, set your own `JEV_API_KEY` or `TYPESAFE_API_KEY`, then start an already authenticated CLI through `jev-claude` or `jev-codex`. Run the offline tests first and inspect the routing record for a simple new task; live routing calls the TypeSafe API.

### Evidence and limitations

The pinned README, TypeSafe SDK request, downstream policy and MIT license were reviewed. This catalog did not install, run or test routing quality. The README describes development and testing against specified Windows/CLI versions, which does not establish results elsewhere. Actual routing depends on available models, the task and code policy, not Jev alone.

## Sources / 来源

- [项目仓库 / Repository](https://github.com/gargpratyush/jev-router)
- [固定版本 README / Pinned README](https://github.com/gargpratyush/jev-router/blob/38da6b84ea01241bfc41fbddc0928d0f40a703f0/README.md)
- [Jev SDK 请求 / Jev SDK request](https://github.com/gargpratyush/jev-router/blob/38da6b84ea01241bfc41fbddc0928d0f40a703f0/src/router.mjs)
- [最终路由策略 / Final routing policy](https://github.com/gargpratyush/jev-router/blob/38da6b84ea01241bfc41fbddc0928d0f40a703f0/src/policy.mjs)
- [网站中的同一项目 / Same project on JevForAgents](https://jevforagents.com/builds/jev-router)
- [原始许可证 / Upstream license](https://github.com/gargpratyush/jev-router/blob/38da6b84ea01241bfc41fbddc0928d0f40a703f0/LICENSE)
