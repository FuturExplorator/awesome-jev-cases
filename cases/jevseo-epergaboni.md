---
slug: "jevseo-epergaboni"
name_en: "JevSEO by epergaboni"
name_zh: "JevSEO：搜索、答案与生成引擎评分"
project_url: "https://github.com/epergaboni/jevseo"
source_url: "https://github.com/epergaboni/jevseo/blob/2ed1fbbaf90f86715dd489e5fe39416fa4879f17/README.md"
source_kind: "github"
author: "epergaboni"
source_date: "2026-09-21"
source_date_kind: "commit"
last_checked: "2026-10-08"
source_revision: "2ed1fbbaf90f86715dd489e5fe39416fa4879f17"
jev_relation: "uses_typesafe"
scenario: "evaluation"
content_kind: "application"
status: "verified"
claim_status: "source_reviewed"
upstream_license: "MIT"
evidence_file: "research/evidence/jevseo-epergaboni.json"
---

# JevSEO by epergaboni / JevSEO：搜索、答案与生成引擎评分

## 中文

### 项目简介

一个 Next.js 应用：粘贴 URL 或草稿，分别给出 SEO、AEO（答案引擎）和 GEO（生成式引擎）三项评分，以及按优先级排序的修改清单；另有整站模式，抓取同一站点的页面并生成整站计划。它与已收录的 `AgriciDaniel/jev-seo` 是不同作者、不同仓库的独立实现。

### Jev 的具体作用

固定源码通过官方 `@typesafe-ai/sdk` 的 `systemOne`，把页面事实（标题、描述、标题层级、正文）作为 state，一次请求回答全部评判问题；整站模式再用一个 Choice 在 leave / improve / rewrite / merge / split / prune 之间为每个页面选动作，并用 Score 估计机会和工作量。README 给出的分工是：有固定阈值的规则写在代码里，需要阅读理解的判断交给 Jev，权重与截断属于代码策略。

### 如何复现

按固定 README 的 Quick start 在本地运行，并提供自己的 TypeSafe Key。README 说明数据默认存在 `.jevseo/jevseo.db`（使用 Node 22+ 内置的 `node:sqlite`），设置 `DATABASE_URL` 可改用 Postgres。作者另提供需自带 Key 的在线版 jevseo.epergaboni.com；本库没有测试该站点。

### 证据与限制

已核对固定 README、SDK 客户端封装、`judge/run.ts` 与 `judge/decisions.ts` 的请求构造以及 MIT LICENSE；未安装、未抓取任何网站、未调用付费接口。README 中“每页约两秒、约 £0.0001”“25 个问题”“45 个信号”“十页约 55,000 输入 token”等数字均为作者自述，未复测。评分是规则、Jev 判断和代码权重的组合，不是 Jev 单独给出的结论。

## English

### Overview

A Next.js app: paste a URL or draft and get three separate scores for SEO, AEO (answer engines) and GEO (generative engines) plus a ranked fix list. A site mode crawls pages on one origin and builds a site-wide plan. It is a different author and repository from the already cataloged `AgriciDaniel/jev-seo`.

### Jev's specific role

Pinned code calls `systemOne` from the official `@typesafe-ai/sdk` with page facts (title, description, headings, body text) as state, answering every judgment question in one request. Site mode adds a Choice among leave / improve / rewrite / merge / split / prune per page, with Score questions for opportunity and effort. The README’s division of labour: fixed-threshold rules live in code, reading-comprehension judgments go to Jev, and weights and cut-offs are code policy.

### Reproduction

Follow the pinned README’s Quick start locally with your own TypeSafe key. The README says data defaults to `.jevseo/jevseo.db` through `node:sqlite` (built into Node 22+), and `DATABASE_URL` switches to Postgres. The author also hosts a bring-your-own-key instance at jevseo.epergaboni.com; it was not tested here.

### Evidence and limitations

The pinned README, SDK client wrapper, request construction in `judge/run.ts` and `judge/decisions.ts`, and the MIT license were reviewed. Nothing was installed, no site was crawled and no paid call was made. Figures in the README such as “roughly two seconds and £0.0001 per page”, “25 questions”, “45 signals” and “about 55,000 input tokens for ten pages” are author-reported and were not reproduced. Scores combine rules, Jev judgments and code weights; they are not written by Jev alone.

## Sources / 来源

- [项目仓库 / Repository](https://github.com/epergaboni/jevseo)
- [固定版本 README / Pinned README](https://github.com/epergaboni/jevseo/blob/2ed1fbbaf90f86715dd489e5fe39416fa4879f17/README.md)
- [实现 / Implementation: src/lib/typesafe/client.ts](https://github.com/epergaboni/jevseo/blob/2ed1fbbaf90f86715dd489e5fe39416fa4879f17/src/lib/typesafe/client.ts)
- [实现 / Implementation: src/lib/judge/run.ts](https://github.com/epergaboni/jevseo/blob/2ed1fbbaf90f86715dd489e5fe39416fa4879f17/src/lib/judge/run.ts)
- [实现 / Implementation: src/lib/judge/decisions.ts](https://github.com/epergaboni/jevseo/blob/2ed1fbbaf90f86715dd489e5fe39416fa4879f17/src/lib/judge/decisions.ts)
- [原始许可证 / Upstream license](https://github.com/epergaboni/jevseo/blob/2ed1fbbaf90f86715dd489e5fe39416fa4879f17/LICENSE)
- [核验记录 / Review receipt](../research/evidence/jevseo-epergaboni.json)
