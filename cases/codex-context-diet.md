---
slug: "codex-context-diet"
name_en: "Codex Context Diet"
name_zh: "工具结果上下文裁剪"
project_url: "https://github.com/konstantinosbotonakis/codex-context-diet"
source_url: "https://github.com/konstantinosbotonakis/codex-context-diet/blob/6c15140d8749e1d0d3cb49c742c159a2129dafcf/README.md"
source_kind: "github"
author: "konstantinosbotonakis"
source_date: "2026-09-28"
source_date_kind: "commit"
last_checked: "2026-09-29"
source_revision: "6c15140d8749e1d0d3cb49c742c159a2129dafcf"
jev_relation: "uses_typesafe"
scenario: "coding"
content_kind: "integration"
status: "verified"
claim_status: "source_reviewed"
upstream_license: "MIT with upstream attribution"
evidence_file: "research/evidence/codex-context-diet.json"
---

# Codex Context Diet / 工具结果上下文裁剪

## 中文

### 项目简介

针对 Codex 的大型工具结果，判断其是否仍需完整保留在会话上下文中。

### Jev 的具体作用

Jev 判断原文是否仍有用、信息是否可再次获取，以及潜在指令性内容；代码据此保留结果或替换为有限片段与说明。

### 如何复现

按 README Install 安装 context-diet 市场中的插件，配置自己的 TypeSafe 凭据，信任对应 Hook 后检查其日志和保留/替换记录。

### 证据与限制

已核对公开仓库身份、固定版本 README、调用实现与许可证；`verified` 仅指来源核验通过。未安装运行，未进行独立效果测试。节省量与延迟是作者报告，本库未复测宿主替换行为或信息保真。上游许可证含 fast-jev-compaction 的派生来源说明；不能忽略该署名。

## English

### Overview

A Codex plugin that judges whether bulky tool results still need to remain in full in conversation context.

### Jev's specific role

Jev evaluates continued usefulness, recoverability and instruction-like content. Code keeps the result or replaces it with a bounded excerpt and a note.

### Reproduction

Follow Install for the context-diet marketplace plugin, configure your own TypeSafe credentials, trust the relevant hook and inspect keep/replace logs.

### Evidence and limitations

Public identity, pinned README, implementation and license were reviewed. `verified` means source-verified only; installation, runtime and independent effectiveness tests were not performed. Savings and latency are author reports. Host replacement behavior and information fidelity were not tested here. The upstream license includes attribution to fast-jev-compaction; that provenance must be retained.

## Sources / 来源

- 项目与作者 / Project and owner: [konstantinosbotonakis/codex-context-diet](https://github.com/konstantinosbotonakis/codex-context-diet)
- 所核对版本 / Reviewed revision: [`6c15140d8749`](https://github.com/konstantinosbotonakis/codex-context-diet/commit/6c15140d8749e1d0d3cb49c742c159a2129dafcf); `source_date` is this commit's date, not a launch date / 来源日期为提交日期，不是发布日期。
- [README.md](https://github.com/konstantinosbotonakis/codex-context-diet/blob/6c15140d8749e1d0d3cb49c742c159a2129dafcf/README.md)
- [src/client.ts](https://github.com/konstantinosbotonakis/codex-context-diet/blob/6c15140d8749e1d0d3cb49c742c159a2129dafcf/src/client.ts)
- [src/questions.ts](https://github.com/konstantinosbotonakis/codex-context-diet/blob/6c15140d8749e1d0d3cb49c742c159a2129dafcf/src/questions.ts)
- [src/decide.ts](https://github.com/konstantinosbotonakis/codex-context-diet/blob/6c15140d8749e1d0d3cb49c742c159a2129dafcf/src/decide.ts)
- [LICENSE](https://github.com/konstantinosbotonakis/codex-context-diet/blob/6c15140d8749e1d0d3cb49c742c159a2129dafcf/LICENSE)
- [核验记录与 SHA-256 / Review receipt and SHA-256](../research/evidence/codex-context-diet.json)
- [第三方权利 / Third-party rights](../THIRD_PARTY_NOTICES.md): MIT with upstream attribution
- 关联案例浏览网站 / Related browsing site: [jevforagents.com](https://jevforagents.com) — no case-specific page is asserted / 未宣称对应详情页存在。
