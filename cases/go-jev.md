---
slug: "go-jev"
name_en: "go-jev"
name_zh: "go-jev：Go SDK 与命令行"
project_url: "https://github.com/mattn/go-jev"
source_url: "https://github.com/mattn/go-jev/blob/85f5994cb5136ff5360dd904b65253469dc95d2e/README.md"
source_kind: "github"
author: "mattn"
source_date: "2026-09-23"
source_date_kind: "commit"
last_checked: "2026-10-08"
source_revision: "85f5994cb5136ff5360dd904b65253469dc95d2e"
jev_relation: "uses_typesafe"
scenario: "integration"
content_kind: "integration"
status: "verified"
claim_status: "source_reviewed"
upstream_license: "MIT"
evidence_file: "research/evidence/go-jev.json"
---

# go-jev / go-jev：Go SDK 与命令行

## 中文

### 项目简介

mattn 发布的 Go SDK，以及基于它的命令行工具 `jev-cli`，用于在 Go 程序和 UNIX 管道中获取 Jev 的类型化回答（是/否概率、选项、分数）。

### Jev 的具体作用

固定的 `jev.go` 把 `state`、`model`（默认 `jev-latest`）和 `questions` 以 JSON POST 到默认端点 `https://api.typesafe.ai/v1/systemone`，提供 `Ask`（单个问题）和 `Evaluate`（一次请求多个问题）；设置了 Key 时附带 Bearer 头。README 说明 429 / 529 会指数退避重试，`jev-cli` 提供 `noul`、`choice`、`score`、`grep`、`ask` 子命令，例如按语义过滤 stdin 的行，或用退出码表示是/否。

### 如何复现

SDK：`go get github.com/mattn/go-jev`。命令行：`go install github.com/mattn/go-jev/cmd/jev-cli@latest`，设置 `TYPESAFE_API_KEY` 后可运行 `echo 'Help! My payouts have been failing for 3 days.' | jev-cli noul 'Does this convey urgency?'`。`JEV_MODEL`、`JEV_API_URL`、`JEV_TIMEOUT` 可覆盖默认值。

### 证据与限制

已核对固定 README、`jev.go` 的请求代码和 MIT LICENSE；未编译、未调用付费接口，也没有通读 `cmd/jev-cli` 的实现。README 中的示例输出（如 `0.95`）是作者示例。README 说明端点可以指向作者另一个项目 tensai 的本地服务器；那是兼容接口，不属于本条核验的 TypeSafe Jev 调用。

## English

### Overview

A Go SDK published by mattn, plus the `jev-cli` command-line tool built on it, for getting Jev’s typed answers (yes/no probability, choice, score) in Go programs and UNIX pipelines.

### Jev's specific role

Pinned `jev.go` POSTs `state`, `model` (default `jev-latest`) and `questions` as JSON to the default endpoint `https://api.typesafe.ai/v1/systemone`, exposing `Ask` for one question and `Evaluate` for several in one request; a Bearer header is sent when a key is set. The README says 429 / 529 are retried with exponential backoff and that `jev-cli` offers `noul`, `choice`, `score`, `grep` and `ask`, for example filtering stdin lines by meaning or returning yes/no as an exit status.

### Reproduction

SDK: `go get github.com/mattn/go-jev`. CLI: `go install github.com/mattn/go-jev/cmd/jev-cli@latest`, set `TYPESAFE_API_KEY`, then for example `echo 'Help! My payouts have been failing for 3 days.' | jev-cli noul 'Does this convey urgency?'`. `JEV_MODEL`, `JEV_API_URL` and `JEV_TIMEOUT` override the defaults.

### Evidence and limitations

The pinned README, the request code in `jev.go` and the MIT license were reviewed. Nothing was compiled, no paid call was made and the `cmd/jev-cli` implementation was not read in full. Sample outputs in the README such as `0.95` are the author’s examples. The README notes the endpoint can point at a local server from the author’s separate tensai project; that is a compatible interface and not the TypeSafe Jev call reviewed here.

## Sources / 来源

- [项目仓库 / Repository](https://github.com/mattn/go-jev)
- [固定版本 README / Pinned README](https://github.com/mattn/go-jev/blob/85f5994cb5136ff5360dd904b65253469dc95d2e/README.md)
- [实现 / Implementation: jev.go](https://github.com/mattn/go-jev/blob/85f5994cb5136ff5360dd904b65253469dc95d2e/jev.go)
- [原始许可证 / Upstream license](https://github.com/mattn/go-jev/blob/85f5994cb5136ff5360dd904b65253469dc95d2e/LICENSE)
- [核验记录 / Review receipt](../research/evidence/go-jev.json)
