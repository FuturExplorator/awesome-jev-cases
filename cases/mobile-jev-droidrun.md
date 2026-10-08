---
slug: "mobile-jev-droidrun"
name_en: "Mobile Jev"
name_zh: "Mobile Jev：Android 手机代理"
project_url: "https://github.com/droidrun/mobile-jev"
source_url: "https://github.com/droidrun/mobile-jev/blob/395fc222beac4f059f9a0beb337d114a2b066e99/README.md"
source_kind: "github"
author: "droidrun"
source_date: "2026-09-17"
source_date_kind: "commit"
last_checked: "2026-10-08"
source_revision: "395fc222beac4f059f9a0beb337d114a2b066e99"
jev_relation: "uses_typesafe"
scenario: "device"
content_kind: "application"
status: "verified"
claim_status: "source_reviewed"
upstream_license: "MIT"
evidence_file: "research/evidence/mobile-jev-droidrun.json"
---

# Mobile Jev / Mobile Jev：Android 手机代理

## 中文

### 项目简介

droidrun 发布的独立手机代理：给出一个目标，由 Jev 在一台通过 Mobilerun API 接入的真实 Android 设备上逐步决策。仓库包含 React 实时工作台、CLI、执行轨迹和请求级延迟测量；README 说明不需要 ADB 连接。

### Jev 的具体作用

固定的 `scripts/mobile-agent/policy.mjs` 把当前屏幕上观察到的控件整理成候选，向 `https://api.typesafe.ai/v1/systemone` 提出 Choice 问题：先选操作（OPEN_APP、TAP、TYPE_TEXT、SCROLL、BACK、HOME、ENTER、WAIT、DONE、BLOCKED 中当前可用的那些），再选该操作的目标。代码会校验返回的选项和概率分布是否有效，执行则通过 Mobilerun API 完成。

### 如何复现

需要 Node.js（README 推荐 24，支持 22.16+）、pnpm 10.30.1、curl 7.70+、一台就绪的 Mobilerun Android 设备，以及 Mobilerun 和 TypeSafe 两个 API Key。按固定 README：`pnpm install --frozen-lockfile`，`cp .env.example .env.local` 后填入 Key 和 `MOBILERUN_DEVICE_ID`，依次运行 `pnpm devices`、`pnpm doctor`、`pnpm dev`，打开 `http://127.0.0.1:3040`。自带演示 `pnpm demo dark-theme --reset` 不涉及账号或购买。设备与服务费用另计。

### 证据与限制

已核对固定 README、`policy.mjs` 的问题构造与校验以及 MIT LICENSE；未连接设备、未调用任何付费接口。README 的 Uber 演示写明“9 个动作约 21 秒”是录制时的计时，并且没有展示完成下单；这些均为作者自述。README 说明深色主题演示会重新读屏核对开关状态，不把模型的 DONE 当作证明。

## English

### Overview

A standalone mobile agent published by droidrun: give it one goal and Jev decides step by step on a real Android device reached through the Mobilerun API. The repository includes a live React studio, a CLI, execution traces and request-level latency measurements; the README says no ADB connection is required.

### Jev's specific role

Pinned `scripts/mobile-agent/policy.mjs` turns the controls observed on the current screen into candidates and posts Choice questions to `https://api.typesafe.ai/v1/systemone`: first the operation (whichever of OPEN_APP, TAP, TYPE_TEXT, SCROLL, BACK, HOME, ENTER, WAIT, DONE and BLOCKED are currently available), then the target for that operation. Code validates the returned choice and probability distribution, and execution goes through the Mobilerun API.

### Reproduction

Requires Node.js (24 recommended, 22.16+ supported), pnpm 10.30.1, curl 7.70+, a ready Mobilerun Android device and API keys for both Mobilerun and TypeSafe. Per the pinned README: `pnpm install --frozen-lockfile`, `cp .env.example .env.local`, add the keys and `MOBILERUN_DEVICE_ID`, then `pnpm devices`, `pnpm doctor`, `pnpm dev` and open `http://127.0.0.1:3040`. The bundled `pnpm demo dark-theme --reset` involves no accounts or purchases. Device and service charges are separate.

### Evidence and limitations

The pinned README, question construction and validation in `policy.mjs`, and the MIT license were reviewed. No device was connected and no paid call was made. The README’s Uber demo states “about 21 seconds for 9 actions” from the recorded task timer and that a completed booking is not demonstrated; these are author-reported. The README says the dark-theme demo re-reads the screen to verify the switch and does not accept a model DONE as proof.

## Sources / 来源

- [项目仓库 / Repository](https://github.com/droidrun/mobile-jev)
- [固定版本 README / Pinned README](https://github.com/droidrun/mobile-jev/blob/395fc222beac4f059f9a0beb337d114a2b066e99/README.md)
- [实现 / Implementation: scripts/mobile-agent/policy.mjs](https://github.com/droidrun/mobile-jev/blob/395fc222beac4f059f9a0beb337d114a2b066e99/scripts/mobile-agent/policy.mjs)
- [原始许可证 / Upstream license](https://github.com/droidrun/mobile-jev/blob/395fc222beac4f059f9a0beb337d114a2b066e99/LICENSE)
- [核验记录 / Review receipt](../research/evidence/mobile-jev-droidrun.json)
