---
slug: "jev-leftpad"
name_en: "jev-leftpad"
name_zh: "jev-leftpad：用 Jev 左填充字符串"
project_url: "https://github.com/f/jev-leftpad"
source_url: "https://github.com/f/jev-leftpad/blob/4f405354de756cc372826d19aa8dfbee2b675778/README.md"
source_kind: "github"
author: "f"
source_date: "2026-09-21"
source_date_kind: "commit"
last_checked: "2026-10-08"
source_revision: "4f405354de756cc372826d19aa8dfbee2b675778"
jev_relation: "uses_typesafe"
scenario: "other"
content_kind: "experiment"
status: "verified"
claim_status: "source_reviewed"
upstream_license: "MIT"
evidence_file: "research/evidence/jev-leftpad.json"
---

# jev-leftpad / jev-leftpad：用 Jev 左填充字符串

## 中文

### 项目简介

一个自嘲式的 npm 包：用一次 Jev 调用给字符串做左填充。README 开头就承认这件事用 `padStart()` 一行就能完成，并不需要模型。

### Jev 的具体作用

固定的 `src/index.js` 通过官方 `@typesafe-ai/sdk` 提交一个 Choice 问题，选项为 `space_0` 到 `space_10`，state 是待填充的值和目标长度；JavaScript 读取所选编号，生成相应数量的空格并拼在值前面。每次调用一个请求，重试被关闭。

### 如何复现

Node.js 20+：`npm install jev-leftpad`，设置 `TYPESAFE_API_KEY`，然后 `import leftPad from 'jev-leftpad'` 并调用 `await leftPad('jev', 8)`。README 说明仓库内 `npm test` 使用 Mock，不需要 Key，也不消耗额度。

### 证据与限制

已核对固定 README、`src/index.js`、`package.json` 和 MIT LICENSE；未安装、未调用付费接口，也未核对 npm 上发布的包内容。README 自己写明：最多只能补 10 个空格，请求可能失败，Jev 可能选错，成本高于 `padStart()`，不要用于生产。它适合作为只含一个 Choice 问题的完整示例来阅读。

## English

### Overview

A tongue-in-cheek npm package that left-pads a string with one Jev call. The README opens by admitting this could be one line with `padStart()` and needs no model.

### Jev's specific role

Pinned `src/index.js` submits one Choice question through the official `@typesafe-ai/sdk` with the options `space_0` to `space_10`; the state is the value and target length. JavaScript reads the selected number, creates that many spaces and prepends them. There is one request per call and retries are disabled.

### Reproduction

With Node.js 20+: `npm install jev-leftpad`, set `TYPESAFE_API_KEY`, then `import leftPad from 'jev-leftpad'` and call `await leftPad('jev', 8)`. The README says `npm test` in the repository mocks Jev, needs no key and spends no credits.

### Evidence and limitations

The pinned README, `src/index.js`, `package.json` and the MIT license were reviewed. Nothing was installed, no paid call was made and the package published on npm was not compared. The README itself says it can add at most 10 spaces, the request can fail, Jev can choose wrongly, it costs more than `padStart()` and it should not be used in production. It reads well as a complete example with a single Choice question.

## Sources / 来源

- [项目仓库 / Repository](https://github.com/f/jev-leftpad)
- [固定版本 README / Pinned README](https://github.com/f/jev-leftpad/blob/4f405354de756cc372826d19aa8dfbee2b675778/README.md)
- [实现 / Implementation: src/index.js](https://github.com/f/jev-leftpad/blob/4f405354de756cc372826d19aa8dfbee2b675778/src/index.js)
- [文档 / Document: package.json](https://github.com/f/jev-leftpad/blob/4f405354de756cc372826d19aa8dfbee2b675778/package.json)
- [原始许可证 / Upstream license](https://github.com/f/jev-leftpad/blob/4f405354de756cc372826d19aa8dfbee2b675778/LICENSE)
- [核验记录 / Review receipt](../research/evidence/jev-leftpad.json)
