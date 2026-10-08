---
slug: "jevfind-code-search"
name_en: "Jev Code Finder (JevFind)"
name_zh: "Jev 语义代码搜索"
project_url: "https://github.com/Peu77/JevFind"
source_url: "https://github.com/Peu77/JevFind/blob/c286f60a61d24b0f4249b2ea88495a4f52dfd51e/README.md"
source_kind: "github"
author: "Peu77"
source_date: "2026-09-20"
source_date_kind: "commit"
last_checked: "2026-10-08"
source_revision: "c286f60a61d24b0f4249b2ea88495a4f52dfd51e"
jev_relation: "uses_typesafe"
scenario: "coding"
content_kind: "application"
status: "verified"
claim_status: "source_reviewed"
upstream_license: "MIT"
evidence_file: "research/evidence/jevfind-code-search.json"
---

# Jev Code Finder (JevFind) / Jev 语义代码搜索

## 中文

### 项目简介

Rust 命令行工具 `jev-code-finder`：用自然语言描述一个概念，返回相关文件、行范围、置信度和代码片段。仓库还附带一个供编码代理使用的 Agent Skill；两者属于同一个仓库案例。

### Jev 的具体作用

固定源码向 TypeSafe `/v1/systemone` 发送 Noul 问题，分两步：先让 Jev 判断每个源码路径与查询是否相关，达到 `--file-threshold` 的文件才会被打开并切成有重叠、大小受限的代码窗口；再对这些窗口分批提问，只输出达到 `--threshold` 的匹配。遍历仓库、遵守 `.gitignore`、切窗、重试和输出都由 Rust 代码完成。

### 如何复现

需要自己的 `TYPESAFE_API_KEY`、Rust 1.88+ 以及到 `api.typesafe.ai` 的网络。按固定 README 用 `cargo install --path .` 安装后运行 `jev-code-finder "where does user JWT authentication happen?"`，可用 `--path`、`--file-threshold`、`--threshold`、`--parallelism` 调整；README 还给出 Homebrew tap 和 `npx skills add Peu77/JevFind --skill jev-code-finder` 两个入口。

### 证据与限制

已核对固定 README、`src/main.rs` 中的请求、阈值与重试逻辑以及 MIT LICENSE；未编译或运行，未调用付费接口，也未检验检索准确率或速度。README 中的示例输出是作者示例，不是本库实测。路径预筛会把低于阈值的文件排除在后续请求之外，README 建议在更看重召回时设 `--file-threshold 0`。

## English

### Overview

A Rust command-line tool, `jev-code-finder`: describe a concept in plain English and get relevant files, line ranges, confidence scores and snippets. The repository also ships an Agent Skill for coding agents; both belong to this one repository case.

### Jev's specific role

Pinned code posts Noul questions to TypeSafe `/v1/systemone` in two passes. Jev first judges whether each source path is relevant to the query; only files meeting `--file-threshold` are opened and split into overlapping, size-bounded windows. Those windows are then asked in batches, and only matches meeting `--threshold` are printed. Repository walking, `.gitignore` handling, windowing, retries and output are Rust code.

### Reproduction

Requires your own `TYPESAFE_API_KEY`, Rust 1.88+ and network access to `api.typesafe.ai`. Following the pinned README, install with `cargo install --path .` and run `jev-code-finder "where does user JWT authentication happen?"`; tune with `--path`, `--file-threshold`, `--threshold` and `--parallelism`. The README also documents a Homebrew tap and `npx skills add Peu77/JevFind --skill jev-code-finder`.

### Evidence and limitations

The pinned README, the request, threshold and retry logic in `src/main.rs`, and the MIT license were reviewed. Nothing was compiled or run, no paid call was made, and retrieval accuracy and speed were not checked. The sample output in the README is the author’s example, not a result measured here. The path prefilter keeps below-threshold files out of later requests; the README suggests `--file-threshold 0` when recall matters more.

## Sources / 来源

- [项目仓库 / Repository](https://github.com/Peu77/JevFind)
- [固定版本 README / Pinned README](https://github.com/Peu77/JevFind/blob/c286f60a61d24b0f4249b2ea88495a4f52dfd51e/README.md)
- [实现 / Implementation: src/main.rs](https://github.com/Peu77/JevFind/blob/c286f60a61d24b0f4249b2ea88495a4f52dfd51e/src/main.rs)
- [原始许可证 / Upstream license](https://github.com/Peu77/JevFind/blob/c286f60a61d24b0f4249b2ea88495a4f52dfd51e/LICENSE)
- [核验记录 / Review receipt](../research/evidence/jevfind-code-search.json)
