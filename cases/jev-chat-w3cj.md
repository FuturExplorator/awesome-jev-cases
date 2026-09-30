---
slug: "jev-chat-w3cj"
name_en: "Jev Chat"
name_zh: "Jev Chat 工具聊天应用"
project_url: "https://github.com/w3cj/jev-chat"
source_url: "https://github.com/w3cj/jev-chat/blob/e543aba8c21b57a28a748ef41966502130f0f69e/README.md"
source_kind: "github"
author: "w3cj"
source_date: "2026-09-18"
source_date_kind: "commit"
last_checked: "2026-09-30"
source_revision: "e543aba8c21b57a28a748ef41966502130f0f69e"
jev_relation: "uses_typesafe"
scenario: "routing"
content_kind: "application"
status: "verified"
claim_status: "source_reviewed"
upstream_license: "MIT"
evidence_file: "research/evidence/jev-chat-w3cj.json"
---

# Jev Chat / Jev Chat 工具聊天应用

## 中文

### 项目简介

一个用聊天界面调用真实工具的本地应用，包含天气、单位换算、百科、菜谱及可选外部服务。对话状态和判断轨迹保存在 SQLite，界面提供检查面板。

### Jev 的具体作用

服务器从用户消息、历史结果和可用工具构造候选值及类型化问题，一次或多次调用 TypeSafe Jev 选择意图、工具与参数候选；代码执行 MCP 工具，并用工具返回的数据组织回复。Jev 不写最终自由文本。README 所说“不会编造事实”是作者表述，本库未验证所有执行路径。

### 如何复现

按固定 README 准备 Node 24+ 与 pnpm 11，运行 `pnpm install`，从 `.env.example` 配置至少自己的 `TYPESAFE_API_KEY`，再运行 `pnpm dev`；本地网页是 `http://localhost:5173`，服务器在 8787。先试无需其他服务 Key 的天气或单位换算；项目目前仅支持英文。

### 证据与限制

已核对固定 README、TypeSafe SDK 调用、候选池代码及 MIT LICENSE；未启动应用或验证回复正确性。Brave、Todoist、Home Assistant 等工具另需各自凭据；“无 LLM 写作”与事实性属于作者设计说明，不等于独立测试。

## English

### Overview

A local chat interface that invokes real tools for weather, unit conversion, Wikipedia, recipes and optional external services. It stores conversation state and decision traces in SQLite and exposes an inspector.

### Jev's specific role

The server builds candidate values and typed questions from the message, prior results and tools, then calls TypeSafe Jev to choose intent, tool and argument candidates. Code executes MCP tools and assembles replies from returned data. Jev does not write free-form final text. The README’s no-invented-facts claim has not been verified across all paths here.

### Reproduction

Follow the pinned README with Node 24+ and pnpm 11. Run `pnpm install`, configure at least your own `TYPESAFE_API_KEY` from `.env.example`, then run `pnpm dev`. The web UI is `http://localhost:5173` and server uses port 8787. Try weather or unit conversion before optional keyed services. The project currently supports English only.

### Evidence and limitations

Pinned README, TypeSafe SDK call, candidate-pool code and MIT license were reviewed. The app was not started and reply accuracy was not tested. Brave, Todoist and Home Assistant need separate credentials; no-LLM-writing and factuality are author design claims, not independent test results.

## Sources / 来源

- [项目仓库 / Repository](https://github.com/w3cj/jev-chat)
- [固定版本 README / Pinned README](https://github.com/w3cj/jev-chat/blob/e543aba8c21b57a28a748ef41966502130f0f69e/README.md)
- [实现 / Implementation: apps/server/src/jev/client.ts](https://github.com/w3cj/jev-chat/blob/e543aba8c21b57a28a748ef41966502130f0f69e/apps/server/src/jev/client.ts)
- [实现 / Implementation: apps/server/src/jev/pools.ts](https://github.com/w3cj/jev-chat/blob/e543aba8c21b57a28a748ef41966502130f0f69e/apps/server/src/jev/pools.ts)
- [原始许可证 / Upstream license](https://github.com/w3cj/jev-chat/blob/e543aba8c21b57a28a748ef41966502130f0f69e/LICENSE)
