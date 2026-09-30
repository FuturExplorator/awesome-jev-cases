---
slug: "browser-use-jev-ultrafast"
name_en: "Jev Ultrafast by Browser Use"
name_zh: "Browser Use 的 Jev Ultrafast"
project_url: "https://github.com/browser-use/jev-ultrafast"
source_url: "https://github.com/browser-use/jev-ultrafast/blob/1231850a0bf1a0c0341fe408ef1668dbbfdfac46/README.md"
source_kind: "github"
author: "browser-use"
source_date: "2026-09-18"
source_date_kind: "commit"
last_checked: "2026-09-30"
source_revision: "1231850a0bf1a0c0341fe408ef1668dbbfdfac46"
jev_relation: "uses_typesafe"
scenario: "browser"
content_kind: "application"
status: "verified"
claim_status: "source_reviewed"
upstream_license: "MIT"
evidence_file: "research/evidence/browser-use-jev-ultrafast.json"
website_url: "https://jevforagents.com/builds/browser-use-flights"
---

# Jev Ultrafast by Browser Use / Browser Use 的 Jev Ultrafast

## 中文

### 项目简介

Browser Use 的浏览器代理实验：根据当前页面生成带编号的可操作元素表，并围绕一个自然语言目标循环执行浏览器步骤。网站中的航班演示和该仓库属于同一项目，因此这里只收录一次。

### Jev 的具体作用

程序将目标、可见页面状态、允许的操作和相容元素交给 TypeSafe Jev。Jev 在一次请求中选择操作及对应目标；程序校验选项、重新检查页面并执行动作。输入字段内容在需要时由另外的小型文本模型生成，不能归为 Jev 的输出。

### 如何复现

按固定版本 README 安装 `uv` 依赖，配置自己的 `TYPESAFE_API_KEY`；若任务涉及输入文本，还需配置文本模型凭据。先从 README 的 Wikipedia 导航示例或本地检查器入手，再检查元素表与执行轨迹。航班示例只查找匹配航班，不预订或付款。

### 证据与限制

已核对原始仓库、固定版本 README、TypeSafe API 请求、浏览器循环及 MIT 许可证。作者提供航班演示、时间与比较数据，本库未运行或复测。默认浏览器循环不用截图做 Jev 输入；这不代表所有检查界面或演示都没有截图。网站详情页已确认指向同一仓库。

## English

### Overview

A Browser Use browser-agent experiment. It builds a numbered table of actionable elements from the current page and executes bounded steps toward a natural-language goal. The flight demo on the associated website and this repository describe one project, counted once here.

### Jev's specific role

Code sends the goal, visible page state, permitted operations and compatible elements to TypeSafe Jev. Jev chooses an operation and its target in one request; code validates the answer, rechecks the page and executes the action. A separate small text model generates field values when needed; that text is not Jev output.

### Reproduction

Follow the pinned README to install dependencies with `uv` and configure your own `TYPESAFE_API_KEY`; tasks requiring typed text also need text-model credentials. Start with the documented Wikipedia navigation example or local inspector and inspect the element table and trace. The flight example searches matching flights; it does not book or pay.

### Evidence and limitations

The repository, pinned README, TypeSafe API request, action loop and MIT license were reviewed. Flight timing and comparisons are author-reported; this catalog did not run or reproduce them. The default Jev loop does not use screenshots as input, which does not mean the inspector or demo never shows screenshots. The website detail page was checked against the same repository.

## Sources / 来源

- [项目仓库 / Repository](https://github.com/browser-use/jev-ultrafast)
- [固定版本 README / Pinned README](https://github.com/browser-use/jev-ultrafast/blob/1231850a0bf1a0c0341fe408ef1668dbbfdfac46/README.md)
- [Jev 请求与候选动作 / Jev request and candidate actions](https://github.com/browser-use/jev-ultrafast/blob/1231850a0bf1a0c0341fe408ef1668dbbfdfac46/jev_ultrafast/model.py)
- [浏览器循环 / Browser loop](https://github.com/browser-use/jev-ultrafast/blob/1231850a0bf1a0c0341fe408ef1668dbbfdfac46/jev_ultrafast/agent.py)
- [网站中的同一项目 / Same project on JevForAgents](https://jevforagents.com/builds/browser-use-flights)
- [原始许可证 / Upstream license](https://github.com/browser-use/jev-ultrafast/blob/1231850a0bf1a0c0341fe408ef1668dbbfdfac46/LICENSE)
