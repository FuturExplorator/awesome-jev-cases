---
slug: "opencode-jev-compaction"
name_en: "opencode-jev-compaction"
name_zh: "opencode 的 Jev 上下文压缩插件"
project_url: "https://github.com/quinnjr/opencode-jev-compaction"
source_url: "https://github.com/quinnjr/opencode-jev-compaction/blob/9181265438237451d727acc529340096b80e5127/README.md"
source_kind: "github"
author: "quinnjr"
source_date: "2026-09-21"
source_date_kind: "commit"
last_checked: "2026-10-08"
source_revision: "9181265438237451d727acc529340096b80e5127"
jev_relation: "uses_typesafe"
scenario: "coding"
content_kind: "integration"
status: "verified"
claim_status: "source_reviewed"
upstream_license: "MIT"
evidence_file: "research/evidence/opencode-jev-compaction.json"
---

# opencode-jev-compaction / opencode 的 Jev 上下文压缩插件

## 中文

### 项目简介

opencode 的上下文压缩插件：在每次向模型发请求之前，判断较早的工具调用及其结果是否还值得发送。README 说明它与 opencode 自带的 LLM 有损摘要不同，不改写任何内容，只决定丢弃或截断；保留下来的原样发送，用户和助手的文字不会被动。

### Jev 的具体作用

固定的 `jev-compaction.ts` 挂在 `experimental.chat.messages.transform` 钩子上。上下文估算超过阈值（默认 15k token）后，它把对话骨架作为 state 发往 `https://api.typesafe.ai/v1/systemone`，对每个未固定的工具调用批量提两个 Noul 问题：调用是否保留、结果是否原样保留；再按 `JEV_KEEP_THRESHOLD`（默认 0.5）决定保留、截断结果或连同结果一起移除。README 说明第一条消息和最近 6 条消息固定不动，进行中的调用不会被移除。

### 如何复现

需要支持 TypeScript 插件的 opencode（README 写 `@opencode-ai/plugin` 1.3.x）和 TypeSafe Key。把 `jev-compaction.ts` 复制到 `~/.config/opencode/plugins/` 或项目的 `.opencode/plugins/`，`export TYPESAFE_API_KEY=...` 后重启 opencode；设置 `JEV_COMPACTION_DEBUG=1` 可查看保留、截断和移除记录。

### 证据与限制

已核对固定 README、`jev-compaction.ts` 的请求、阈值与决策代码和 MIT LICENSE；未安装插件、未调用付费接口，也未测量节省的 token 或对任务质量的影响。README 写明会发送给 Jev 的内容包括消息角色与序号、节选的对话文字、文件名/URL、工具名与输入摘要，工具结果正文不发送，可用 `JEV_STATE_INCLUDE_TEXT=0` 只发工具元数据。README 还提醒该钩子是实验性的、token 数按字符估算、概率不等于可以安全删除的证明。

## English

### Overview

A context-compaction plugin for opencode that decides, before every request to the model, whether older tool calls and their results are still worth sending. The README says that unlike opencode’s own lossy LLM summary it rewrites nothing: it only drops or truncates, everything kept is sent verbatim, and user and assistant text is never touched.

### Jev's specific role

Pinned `jev-compaction.ts` hooks `experimental.chat.messages.transform`. Once the estimated context exceeds the threshold (default 15k tokens) it sends a skeletal view of the conversation as state to `https://api.typesafe.ai/v1/systemone` and asks two Noul questions per non-pinned tool call in batches: should the call stay, and should the result stay verbatim. `JEV_KEEP_THRESHOLD` (default 0.5) then decides between keeping, truncating the result, or removing the call with its result. The README says the first message and the newest six are pinned and in-flight calls are never removed.

### Reproduction

Requires opencode with TypeScript plugin support (the README names `@opencode-ai/plugin` 1.3.x) and a TypeSafe key. Copy `jev-compaction.ts` into `~/.config/opencode/plugins/` or a project’s `.opencode/plugins/`, `export TYPESAFE_API_KEY=...` and restart opencode. `JEV_COMPACTION_DEBUG=1` logs what is kept, truncated or removed.

### Evidence and limitations

The pinned README, the request, threshold and decision code in `jev-compaction.ts`, and the MIT license were reviewed. The plugin was not installed, no paid call was made, and token savings and effects on task quality were not measured. The README states what is sent to Jev: message roles and indexes, abridged conversation text, file names/URLs, tool names and summarised inputs; tool result bodies are not sent, and `JEV_STATE_INCLUDE_TEXT=0` restricts the state to tool metadata. It also warns that the hook is experimental, token sizes are estimated from characters, and a probability is not proof that a result is safe to delete.

## Sources / 来源

- [项目仓库 / Repository](https://github.com/quinnjr/opencode-jev-compaction)
- [固定版本 README / Pinned README](https://github.com/quinnjr/opencode-jev-compaction/blob/9181265438237451d727acc529340096b80e5127/README.md)
- [实现 / Implementation: jev-compaction.ts](https://github.com/quinnjr/opencode-jev-compaction/blob/9181265438237451d727acc529340096b80e5127/jev-compaction.ts)
- [原始许可证 / Upstream license](https://github.com/quinnjr/opencode-jev-compaction/blob/9181265438237451d727acc529340096b80e5127/LICENSE)
- [核验记录 / Review receipt](../research/evidence/opencode-jev-compaction.json)
