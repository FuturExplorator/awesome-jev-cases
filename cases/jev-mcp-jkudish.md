---
slug: "jev-mcp-jkudish"
name_en: "Jev MCP"
name_zh: "MCP 类型化判断工具"
project_url: "https://github.com/jkudish/jev-mcp"
source_url: "https://github.com/jkudish/jev-mcp/blob/53fe5756252956863af2ecbd2952339352e82e15/README.md"
source_kind: "github"
author: "jkudish"
source_date: "2026-09-29"
source_date_kind: "commit"
last_checked: "2026-09-29"
source_revision: "53fe5756252956863af2ecbd2952339352e82e15"
jev_relation: "uses_typesafe"
scenario: "evaluation"
content_kind: "integration"
status: "verified"
claim_status: "source_reviewed"
upstream_license: "MIT"
evidence_file: "research/evidence/jev-mcp-jkudish.json"
---

# Jev MCP / MCP 类型化判断工具

## 中文

### 项目简介

把证据核对、候选筛选与排序等判断封装成可供代理调用的 MCP 工具。

### Jev 的具体作用

调用方提供证据、主张或候选集合；工具构造有界问题发送给 Jev，并返回概率和类型化结果供调用方处理。

### 如何复现

按 README Install 准备 Node.js 22+、自己的 TypeSafe 凭据并注册 @jkudish/jev-mcp；使用一组可手工核对的主张和证据检查输出。

### 证据与限制

已核对公开仓库身份、固定版本 README、调用实现与许可证；`verified` 仅指来源核验通过。未安装运行，未进行独立效果测试。作者的速度与费用说法未在本库复测。判断只针对提供的证据，不等于独立查证事实。此项目与同一作者的浏览器工具分别对应不同仓库与用途。

## English

### Overview

An MCP server exposing typed judgments for evidence checking, candidate selection and ranking.

### Jev's specific role

The caller supplies evidence, claims or candidates. Tools construct bounded Jev questions and return probabilities and typed results for the caller to handle.

### Reproduction

Follow Install with Node.js 22+, your own TypeSafe credentials and the @jkudish/jev-mcp registration. Inspect a small claim/evidence set you can check manually.

### Evidence and limitations

Public identity, pinned README, implementation and license were reviewed. `verified` means source-verified only; installation, runtime and independent effectiveness tests were not performed. Speed and cost claims were not tested here. Judging supplied evidence is not independent fact discovery. This server and the same author’s browser tool are distinct repositories with different purposes.

## Sources / 来源

- 项目与作者 / Project and owner: [jkudish/jev-mcp](https://github.com/jkudish/jev-mcp)
- 所核对版本 / Reviewed revision: [`53fe57562529`](https://github.com/jkudish/jev-mcp/commit/53fe5756252956863af2ecbd2952339352e82e15); `source_date` is this commit's date, not a launch date / 来源日期为提交日期，不是发布日期。
- [README.md](https://github.com/jkudish/jev-mcp/blob/53fe5756252956863af2ecbd2952339352e82e15/README.md)
- [src/provider.ts](https://github.com/jkudish/jev-mcp/blob/53fe5756252956863af2ecbd2952339352e82e15/src/provider.ts)
- [src/lib.ts](https://github.com/jkudish/jev-mcp/blob/53fe5756252956863af2ecbd2952339352e82e15/src/lib.ts)
- [LICENSE](https://github.com/jkudish/jev-mcp/blob/53fe5756252956863af2ecbd2952339352e82e15/LICENSE)
- [核验记录与 SHA-256 / Review receipt and SHA-256](../research/evidence/jev-mcp-jkudish.json)
- [第三方权利 / Third-party rights](../THIRD_PARTY_NOTICES.md): MIT
- 关联案例浏览网站 / Related browsing site: [jevforagents.com](https://jevforagents.com) — no case-specific page is asserted / 未宣称对应详情页存在。
