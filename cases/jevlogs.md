---
slug: "jevlogs"
name_en: "Jev Logs"
name_zh: "Jev Logs：OpenTelemetry 日志分流"
project_url: "https://github.com/reachjalil/jevlogs"
source_url: "https://github.com/reachjalil/jevlogs/blob/500aedb82ec0fa4c5fede190b2d06ef6357be74c/README.md"
source_kind: "github"
author: "reachjalil"
source_date: "2026-10-04"
source_date_kind: "commit"
last_checked: "2026-10-08"
source_revision: "500aedb82ec0fa4c5fede190b2d06ef6357be74c"
jev_relation: "uses_typesafe"
scenario: "evaluation"
content_kind: "integration"
status: "verified"
claim_status: "source_reviewed"
upstream_license: "MIT"
evidence_file: "research/evidence/jevlogs.json"
---

# Jev Logs / Jev Logs：OpenTelemetry 日志分流

## 中文

### 项目简介

面向 OpenTelemetry 日志的分流工具：在把日志交给昂贵的 LLM 分析之前，先给每条日志打分，包括诊断价值、优先级、是否值得深入调查。仓库提供 TypeScript API、OTel exporter 包装器和一个本地 OTLP HTTP 接收器 CLI。

### Jev 的具体作用

固定的 `src/index.ts` 通过 Vercel AI SDK 的 `experimental_evaluate`，以模型标识 `typesafe-ai/jev` 经 Vercel AI Gateway 调用 Jev。这是第三方托管路径，使用的是你的 `AI_GATEWAY_API_KEY` 而不是 TypeSafe Key。每条日志问三个问题：是否值得 LLM 深入调查（布尔）、运维紧急度（Choice：critical / high / normal / low）、诊断信息价值（五级 Score）；问题说明里要求把日志当作不可信数据。README 说明受保护的记录、配置的规则、超时、超长输入和预算耗尽都由本地代码处理，并保留给后续分析。

### 如何复现

Node.js 22+。在项目根目录放 `jevlogs.config.json` 和含 `AI_GATEWAY_API_KEY` 的 `.env`，运行 `npx jevlogs@latest --live`；README 说明接收器监听 `http://127.0.0.1:4318/v1/logs`，接受 OTLP HTTP 的 JSON 或 protobuf，不支持 gRPC，每条记录输出一个 JSON 决策，不打印原始日志正文、不存储日志。

### 证据与限制

已核对固定 README、`src/index.ts` 的评估调用与问题定义和 MIT LICENSE；未安装、未发送日志、未调用付费接口，也未核对 npm 发布包。README 把项目标为公开预览，并注明准确率样本来自 Loghub 衍生数据而非生产日志、`jevlogs.com` 域名接入待完成；仓库内的基准与节省数据均为作者自述。能否调用 Jev 取决于 Vercel AI Gateway 是否提供该模型。

## English

### Overview

A triage tool for OpenTelemetry logs: before logs go to expensive LLM analysis, each one is scored for diagnostic value, priority and whether it merits deeper investigation. The repository offers a TypeScript API, an OTel exporter wrapper and a local OTLP HTTP receiver CLI.

### Jev's specific role

Pinned `src/index.ts` calls Jev with the Vercel AI SDK’s `experimental_evaluate` and the model id `typesafe-ai/jev` through the Vercel AI Gateway. This is a third-party hosted path that uses your `AI_GATEWAY_API_KEY`, not a TypeSafe key. Each log gets three questions: whether it would benefit from deeper LLM investigation (boolean), operational urgency (Choice: critical / high / normal / low) and diagnostic information value (five-level Score); the instructions tell the model to treat the log as untrusted data. The README says protected records, configured rules, timeouts, oversized input and budget exhaustion are handled by local code and stay eligible for analysis.

### Reproduction

With Node.js 22+: put `jevlogs.config.json` and a `.env` containing `AI_GATEWAY_API_KEY` at your project root and run `npx jevlogs@latest --live`. The README says the receiver listens at `http://127.0.0.1:4318/v1/logs`, accepts OTLP HTTP as JSON or protobuf but not gRPC, prints one JSON decision per record and neither prints raw log bodies nor stores logs.

### Evidence and limitations

The pinned README, the evaluate call and question definitions in `src/index.ts`, and the MIT license were reviewed. Nothing was installed, no logs were sent, no paid call was made and the published npm package was not checked. The README labels the project a public preview, says the accuracy sample is Loghub-derived rather than production logs, and that the `jevlogs.com` domain connection is pending; benchmark and savings figures in the repository are author-reported. Reaching Jev depends on the Vercel AI Gateway offering the model.

## Sources / 来源

- [项目仓库 / Repository](https://github.com/reachjalil/jevlogs)
- [固定版本 README / Pinned README](https://github.com/reachjalil/jevlogs/blob/500aedb82ec0fa4c5fede190b2d06ef6357be74c/README.md)
- [实现 / Implementation: src/index.ts](https://github.com/reachjalil/jevlogs/blob/500aedb82ec0fa4c5fede190b2d06ef6357be74c/src/index.ts)
- [原始许可证 / Upstream license](https://github.com/reachjalil/jevlogs/blob/500aedb82ec0fa4c5fede190b2d06ef6357be74c/LICENSE)
- [核验记录 / Review receipt](../research/evidence/jevlogs.json)
