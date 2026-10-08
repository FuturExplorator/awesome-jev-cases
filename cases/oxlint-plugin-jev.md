---
slug: "oxlint-plugin-jev"
name_en: "oxlint-plugin-jev"
name_zh: "oxlint-plugin-jev：用自然语言写 lint 规则"
project_url: "https://github.com/wobsoriano/oxlint-plugin-jev"
source_url: "https://github.com/wobsoriano/oxlint-plugin-jev/blob/d9a1838f32e3b5a15b441dec91b2ef816802006f/README.md"
source_kind: "github"
author: "wobsoriano"
source_date: "2026-09-24"
source_date_kind: "commit"
last_checked: "2026-10-08"
source_revision: "d9a1838f32e3b5a15b441dec91b2ef816802006f"
jev_relation: "uses_typesafe"
scenario: "coding"
content_kind: "integration"
status: "verified"
claim_status: "source_reviewed"
upstream_license: "MIT"
evidence_file: "research/evidence/oxlint-plugin-jev.json"
---

# oxlint-plugin-jev / oxlint-plugin-jev：用自然语言写 lint 规则

## 中文

### 项目简介

一个 Oxlint 插件：用自然语言写 lint 规则。每条规则是针对函数、调用、JSX 元素或整个文件的一个是/否问题，Jev 给出“是”的概率，达到你设定的 cutoff 就报错。README 标注该包为实验性。

### Jev 的具体作用

固定的 `src/jev.ts` 为每个文件构造请求：state 是匹配到的代码片段，每个片段对应一个 Noul 问题；带 `location` 的文件规则再加一个 Choice 问题，从带行号的源码中选出疑似违规的位置。`src/worker.ts` 在工作线程中用官方 `@typesafe-ai/sdk` 的 `systemOne` 发送。README 说明回答缓存在 `node_modules/.cache/oxlint-plugin-jev`，每条诊断会标明作答的模型版本。

### 如何复现

`npm i -D oxlint oxlint-plugin-jev`，设置 `TYPESAFE_API_KEY`，在 `.oxlintrc.json` 的 `jsPlugins` 中加入插件，并在 `jev/ask` 规则的选项里写下自己的问题。仓库 `example/` 提供三条示例规则（日志中的个人信息、函数名与行为不符、提示注入）以及一个会失败和一个能通过的文件，用 `npm run example` 运行。

### 证据与限制

已核对固定 README、`src/jev.ts`、`src/worker.ts` 和 MIT LICENSE；未安装、未运行 lint、未调用付费接口，也未评估误报或漏报。README 提醒：在编辑器里每次按键都可能触发一次付费请求并阻塞语言服务器，建议只在 CI 和 pre-push 的配置中启用；无法访问 Jev 时默认只警告并跳过，除非设置 `ci: "fail"`。

## English

### Overview

An Oxlint plugin for lint rules written in plain English. Each rule is a yes/no question about a function, a call, a JSX element or a whole file; Jev returns the yes-probability and the plugin reports an error when it reaches your cutoff. The README marks the package as experimental.

### Jev's specific role

Pinned `src/jev.ts` builds the request for each file: the state holds the matched snippets and each snippet gets one Noul question; a file rule with `location` adds a Choice question that selects the suspected location from numbered source. `src/worker.ts` sends it on a worker thread through `systemOne` from the official `@typesafe-ai/sdk`. The README says answers are cached under `node_modules/.cache/oxlint-plugin-jev` and each diagnostic names the model version that answered.

### Reproduction

`npm i -D oxlint oxlint-plugin-jev`, set `TYPESAFE_API_KEY`, add the plugin to `jsPlugins` in `.oxlintrc.json` and write your questions in the options of the `jev/ask` rule. The repository’s `example/` has three rules (PII in logs, name versus behaviour, prompt injection) with one failing and one passing file; run it with `npm run example`.

### Evidence and limitations

The pinned README, `src/jev.ts`, `src/worker.ts` and the MIT license were reviewed. Nothing was installed, no lint run was made, no paid call was made and false positives or negatives were not assessed. The README warns that in an editor every keystroke inside a match can be a paid request that blocks the language server, so it recommends enabling the rule only in CI and pre-push configs; when Jev cannot be reached it warns and skips by default unless `ci: "fail"` is set.

## Sources / 来源

- [项目仓库 / Repository](https://github.com/wobsoriano/oxlint-plugin-jev)
- [固定版本 README / Pinned README](https://github.com/wobsoriano/oxlint-plugin-jev/blob/d9a1838f32e3b5a15b441dec91b2ef816802006f/README.md)
- [实现 / Implementation: src/jev.ts](https://github.com/wobsoriano/oxlint-plugin-jev/blob/d9a1838f32e3b5a15b441dec91b2ef816802006f/src/jev.ts)
- [实现 / Implementation: src/worker.ts](https://github.com/wobsoriano/oxlint-plugin-jev/blob/d9a1838f32e3b5a15b441dec91b2ef816802006f/src/worker.ts)
- [原始许可证 / Upstream license](https://github.com/wobsoriano/oxlint-plugin-jev/blob/d9a1838f32e3b5a15b441dec91b2ef816802006f/LICENSE)
- [核验记录 / Review receipt](../research/evidence/oxlint-plugin-jev.json)
