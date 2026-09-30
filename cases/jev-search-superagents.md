---
slug: "jev-search-superagents"
name_en: "Jev Search"
name_zh: "Jev Search 搜索与排序"
project_url: "https://github.com/superagents-lab/jev-search"
source_url: "https://github.com/superagents-lab/jev-search/blob/67027d0185a9b22eb2a178f0eb15250d12ddabe6/README.md"
source_kind: "github"
author: "superagents-lab"
source_date: "2026-09-20"
source_date_kind: "commit"
last_checked: "2026-09-30"
source_revision: "67027d0185a9b22eb2a178f0eb15250d12ddabe6"
jev_relation: "uses_typesafe"
scenario: "evaluation"
content_kind: "application"
status: "verified"
claim_status: "source_reviewed"
upstream_license: "MIT"
evidence_file: "research/evidence/jev-search-superagents.json"
---

# Jev Search / Jev Search 搜索与排序

## 中文

### 项目简介

一个展示搜索链接与摘要的网页应用。它通过 Search1API 检索多个引擎，允许用户调整来源和时间范围，不生成综合答案。仓库自述由 Search1API 团队制作，并非 TypeSafe 官方产品。

### Jev 的具体作用

代码先让 Jev 对请求的意图、候选搜索词、来源及时间范围作类型化选择，再把查询交给 Search1API。各搜索通道返回后，Jev 评估结果与原问题的相关度；代码按相关度、引擎共识和原始排名合并排序。默认 TypeSafe 直连端点，也有 Vercel/Cloudflare 提供者配置，因此不能把所有运行都说成 TypeSafe 直连。

### 如何复现

按固定 README 准备 Node.js 22.12+ 和 pnpm 10.8，安装依赖，复制 `.dev.vars.example` 为 `.dev.vars`，设置自己的 `SEARCH1API_API_KEY` 和至少一种 Jev 提供者凭据，然后运行 `pnpm dev` 并访问 `http://localhost:3030`。这个流程会向外部提供者发送查询和搜索结果摘要，可能产生费用；本库没有执行。

### 证据与限制

已核对固定 README、TypeSafe 请求、搜索流水线、排序代码和 MIT LICENSE；未运行应用或核验排序准确率、来源覆盖、隐私与费用。搜索结果摘要可能不准确或过时，Jev 相关度分数只是模型判断，不是事实核验。

## English

### Overview

A web app showing search links and snippets. Search1API retrieves from several engines; users can adjust sources and time ranges. It does not generate a synthesized answer. The repository says Search1API built it as an independent project, not an official TypeSafe product.

### Jev's specific role

Code first asks Jev to choose typed intent, candidate query terms, sources and time window, then sends queries to Search1API. After each search lane returns, Jev judges relevance to the original request; code merges and orders by relevance, engine agreement and original rank. TypeSafe direct access is the default, with Vercel and Cloudflare provider options, so not every deployment calls TypeSafe directly.

### Reproduction

Follow the pinned README with Node.js 22.12+ and pnpm 10.8: install dependencies, copy `.dev.vars.example` to `.dev.vars`, set your own `SEARCH1API_API_KEY` and at least one Jev-provider credential, run `pnpm dev`, and open `http://localhost:3030`. This sends queries and result snippets to external providers and may incur charges; this catalog did not run it.

### Evidence and limitations

Pinned README, TypeSafe request, search pipeline, ordering code and MIT license were reviewed. The app was not run and ranking accuracy, coverage, privacy and cost were not independently measured. Snippets can be stale or wrong; Jev relevance scores are model judgments, not fact verification.

## Sources / 来源

- [项目仓库 / Repository](https://github.com/superagents-lab/jev-search)
- [固定版本 README / Pinned README](https://github.com/superagents-lab/jev-search/blob/67027d0185a9b22eb2a178f0eb15250d12ddabe6/README.md)
- [实现 / Implementation: src/lib/typesafe.ts](https://github.com/superagents-lab/jev-search/blob/67027d0185a9b22eb2a178f0eb15250d12ddabe6/src/lib/typesafe.ts)
- [实现 / Implementation: src/lib/pipeline.ts](https://github.com/superagents-lab/jev-search/blob/67027d0185a9b22eb2a178f0eb15250d12ddabe6/src/lib/pipeline.ts)
- [实现 / Implementation: src/lib/rank.ts](https://github.com/superagents-lab/jev-search/blob/67027d0185a9b22eb2a178f0eb15250d12ddabe6/src/lib/rank.ts)
- [原始许可证 / Upstream license](https://github.com/superagents-lab/jev-search/blob/67027d0185a9b22eb2a178f0eb15250d12ddabe6/LICENSE)
