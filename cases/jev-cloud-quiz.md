---
slug: "jev-cloud-quiz"
name_en: "Jev Cloud Quiz"
name_zh: "Jev 云服务名称判定演示"
project_url: "https://github.com/minorun365/jev-cloud-quiz"
source_url: "https://github.com/minorun365/jev-cloud-quiz/blob/c8afdf57e20c78baaae872fe20ba76e60696b08f/README.md"
source_kind: "github"
author: "minorun365"
source_date: "2026-09-20"
source_date_kind: "commit"
last_checked: "2026-10-08"
source_revision: "c8afdf57e20c78baaae872fe20ba76e60696b08f"
jev_relation: "uses_typesafe"
scenario: "other"
content_kind: "experiment"
status: "verified"
claim_status: "source_reviewed"
upstream_license: "Apache-2.0"
evidence_file: "research/evidence/jev-cloud-quiz.json"
---

# Jev Cloud Quiz / Jev 云服务名称判定演示

## 中文

### 项目简介

一个日文教学演示：选一个去掉了品牌名的云服务功能名称，页面显示 Jev 判断它属于 AWS、Azure 还是 Google Cloud 的概率分布。作者说明共 30 道题，并挑选了三家云中角色相近的服务，使其只看名字难以分辨。

### Jev 的具体作用

固定的 `server/server.mjs` 用官方 `@typesafe-ai/sdk` 提交一个 Choice 问题，三个云作为选项，再把返回的选项、概率分布和模型名交给前端。README 说明页面上的三根柱直接画的是模型返回的 `probabilities`，API Key 只由服务端持有，不下发浏览器。

### 如何复现

按固定 README：`npm install`，设置 `TYPESAFE_API_KEY`，`npm run serve` 启动提供 `/api/classify` 和静态页面的服务器；`npm run dev` 用于前端热更新。README 还给出部署到 AWS 的步骤（SSM SecureString 加 CDK），那会产生云资源费用。

### 证据与限制

已核对固定 README、服务端调用代码和 Apache-2.0 LICENSE；未运行、未调用付费接口、未访问作者部署的演示站点，也未评估判定正确率。这是用于观察 Choice 概率输出的教学演示，不是生产级云代理。

## English

### Overview

A Japanese-language teaching demo: pick a cloud feature name with its brand removed and the page shows Jev’s probability distribution over AWS, Azure and Google Cloud. The author states there are 30 questions, chosen so that similar services across the three clouds are hard to tell apart by name.

### Jev's specific role

Pinned `server/server.mjs` submits one Choice question through the official `@typesafe-ai/sdk`, with the three clouds as options, and passes the chosen option, probabilities and model name to the front end. The README says the three bars draw the returned `probabilities` directly and the API key stays on the server, never in the browser.

### Reproduction

Per the pinned README: `npm install`, set `TYPESAFE_API_KEY`, then `npm run serve` starts the server for `/api/classify` and static files; `npm run dev` is for front-end hot reload. The README also documents an AWS deployment (SSM SecureString plus CDK), which incurs cloud costs.

### Evidence and limitations

The pinned README, server call code and Apache-2.0 license were reviewed. Nothing was run, no paid call was made, the author’s hosted demo was not visited and classification accuracy was not assessed. It is a teaching demo for observing Choice probabilities, not a production cloud agent.

## Sources / 来源

- [项目仓库 / Repository](https://github.com/minorun365/jev-cloud-quiz)
- [固定版本 README / Pinned README](https://github.com/minorun365/jev-cloud-quiz/blob/c8afdf57e20c78baaae872fe20ba76e60696b08f/README.md)
- [实现 / Implementation: server/server.mjs](https://github.com/minorun365/jev-cloud-quiz/blob/c8afdf57e20c78baaae872fe20ba76e60696b08f/server/server.mjs)
- [原始许可证 / Upstream license](https://github.com/minorun365/jev-cloud-quiz/blob/c8afdf57e20c78baaae872fe20ba76e60696b08f/LICENSE)
- [核验记录 / Review receipt](../research/evidence/jev-cloud-quiz.json)
