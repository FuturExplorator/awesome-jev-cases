---
slug: "n8n-nodes-typesafe-jev"
name_en: "n8n-nodes-typesafe-jev"
name_zh: "n8n 社区节点：TypeSafe Jev"
project_url: "https://github.com/n3ndor/n8n-nodes-typesafe-jev"
source_url: "https://github.com/n3ndor/n8n-nodes-typesafe-jev/blob/f1eb5e25901c911251d06bb4cb06d0341f7a2d96/README.md"
source_kind: "github"
author: "n3ndor"
source_date: "2026-09-23"
source_date_kind: "commit"
last_checked: "2026-10-08"
source_revision: "f1eb5e25901c911251d06bb4cb06d0341f7a2d96"
jev_relation: "uses_typesafe"
scenario: "integration"
content_kind: "integration"
status: "verified"
claim_status: "source_reviewed"
upstream_license: "MIT"
evidence_file: "research/evidence/n8n-nodes-typesafe-jev.json"
---

# n8n-nodes-typesafe-jev / n8n 社区节点：TypeSafe Jev

## 中文

### 项目简介

一个 n8n 社区节点，让工作流在一个节点里就同一份 state 提出多个类型化问题，再把结果交给 Switch、Filter 等节点分支。README 声明它是非官方、社区维护的，与 TypeSafe 没有隶属关系。

### Jev 的具体作用

固定的 `nodes/TypeSafeJev/transport.ts` 通过 n8n 自带的 HTTP 助手向 `/v1/systemone` 发 POST，基础地址默认 `https://api.typesafe.ai`；凭据文件使用 Bearer Key，并以 `/v1/models` 测试连接。README 说明节点支持 Choice、Yes/No 和 Score 三种问题，可用表单或 JSON 定义；开启 Simplify 后每个答案只保留用于分支的单个值；节点设置了 `usableAsTool`，可以直接挂到 AI Agent 上。

### 如何复现

在 n8n 的 Settings → Community Nodes 中安装 `@n3ndor/n8n-nodes-typesafe-jev`，新建 TypeSafe API 凭据，粘贴自己的 Key 并按 Test 确认。仓库 `examples/` 下有工单分流示例工作流。README 要求 Node.js 20.15+。

### 证据与限制

已核对固定 README、传输层与凭据代码和 MIT LICENSE；未安装节点、未运行工作流、未调用付费接口，也未核对 npm 发布包或其 provenance 证明。仓库 VERIFICATION.md 中“2026-09-19 对 api.typesafe.ai 验证 16/16 项假设”是作者的记录，不是本库实测。

## English

### Overview

An n8n community node that lets a workflow ask several typed questions about the same state in one node and branch on the results with Switch, Filter and similar nodes. The README states it is unofficial, community-maintained and not affiliated with TypeSafe.

### Jev's specific role

Pinned `nodes/TypeSafeJev/transport.ts` POSTs to `/v1/systemone` through n8n’s own HTTP helper, with the base URL defaulting to `https://api.typesafe.ai`; the credential file uses a Bearer key and tests the connection against `/v1/models`. The README says the node supports Choice, Yes/No and Score questions defined field by field or as JSON, that Simplify reduces each answer to the single value you would branch on, and that `usableAsTool` lets it attach directly to an AI Agent.

### Reproduction

In n8n, go to Settings → Community Nodes and install `@n3ndor/n8n-nodes-typesafe-jev`, add a TypeSafe API credential, paste your own key and press Test. The repository’s `examples/` folder has a ticket-triage workflow. The README requires Node.js 20.15+.

### Evidence and limitations

The pinned README, transport and credential code, and the MIT license were reviewed. The node was not installed, no workflow was run, no paid call was made, and the published npm package and its provenance attestation were not checked. The statement in VERIFICATION.md that 16/16 assumptions held against `api.typesafe.ai` on 2026-09-19 is the author’s record, not a test performed here.

## Sources / 来源

- [项目仓库 / Repository](https://github.com/n3ndor/n8n-nodes-typesafe-jev)
- [固定版本 README / Pinned README](https://github.com/n3ndor/n8n-nodes-typesafe-jev/blob/f1eb5e25901c911251d06bb4cb06d0341f7a2d96/README.md)
- [实现 / Implementation: nodes/TypeSafeJev/transport.ts](https://github.com/n3ndor/n8n-nodes-typesafe-jev/blob/f1eb5e25901c911251d06bb4cb06d0341f7a2d96/nodes/TypeSafeJev/transport.ts)
- [实现 / Implementation: credentials/TypeSafeApi.credentials.ts](https://github.com/n3ndor/n8n-nodes-typesafe-jev/blob/f1eb5e25901c911251d06bb4cb06d0341f7a2d96/credentials/TypeSafeApi.credentials.ts)
- [文档 / Document: VERIFICATION.md](https://github.com/n3ndor/n8n-nodes-typesafe-jev/blob/f1eb5e25901c911251d06bb4cb06d0341f7a2d96/VERIFICATION.md)
- [原始许可证 / Upstream license](https://github.com/n3ndor/n8n-nodes-typesafe-jev/blob/f1eb5e25901c911251d06bb4cb06d0341f7a2d96/LICENSE)
- [核验记录 / Review receipt](../research/evidence/n8n-nodes-typesafe-jev.json)
