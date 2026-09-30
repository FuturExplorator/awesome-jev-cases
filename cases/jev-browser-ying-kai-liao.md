---
slug: "jev-browser-ying-kai-liao"
name_en: "jev-browser by Ying-Kai Liao"
name_zh: "Ying-Kai Liao 的 jev-browser"
project_url: "https://github.com/Ying-Kai-Liao/jev-browser"
source_url: "https://github.com/Ying-Kai-Liao/jev-browser/blob/e35ab134f65033d29c528132d92bf06e8d6adcb5/README.md"
source_kind: "github"
author: "Ying-Kai-Liao"
source_date: "2026-09-22"
source_date_kind: "commit"
last_checked: "2026-09-30"
source_revision: "e35ab134f65033d29c528132d92bf06e8d6adcb5"
jev_relation: "uses_typesafe"
scenario: "browser"
content_kind: "application"
status: "verified"
claim_status: "source_reviewed"
upstream_license: "MIT"
evidence_file: "research/evidence/jev-browser-ying-kai-liao.json"
---

# jev-browser by Ying-Kai Liao / Ying-Kai Liao 的 jev-browser

## 中文

### 项目简介

一个独立的 Playwright 浏览器自动化库、CLI 与 MCP 服务：调用方给出目标，程序读取页面，Jev 参与下一步决策。

### Jev 的具体作用

程序把页面文本和元素、目标、历史及可用输入值发给 TypeSafe System One。Jev 以类型化问题判断任务是否完成、是否受阻、下一步工具与目标元素，以及动作是否可能不可逆；Playwright 执行动作，程序处理确认和停止条件。

### 如何复现

按固定版本 README 从源码安装依赖与 Chromium，配置自己的 `TYPESAFE_API_KEY`，先运行无需网络的本地测试；要复现 Jev 路径则按 README 的示例使用 MCP、CLI 或 SDK，并观察实际页面与动作记录。网络端到端测试会调用提供方，运行前应自行评估费用与数据范围。

### 证据与限制

已核对仓库身份、README、TypeSafe API 客户端、浏览器会话代码与 MIT 许可证。作者报告了任务正确率、调用时延与上下文节省数据，本库没有独立复测，也未安装运行。项目自称非 TypeSafe 官方。与其他 `jev-browser` 同名仓库是不同项目。

## English

### Overview

An independent Playwright browser automation library, CLI and MCP server. The caller supplies a goal, code observes the page and Jev helps choose the next step.

### Jev's specific role

Code sends page text and elements, goal, history and available values to TypeSafe System One. Typed Jev questions judge completion, blockage, the next tool and target element, and whether an action may be irreversible. Playwright executes actions while code manages confirmation and stopping.

### Reproduction

Follow the pinned README to install dependencies and Chromium from source, configure your own `TYPESAFE_API_KEY`, and run the offline tests first. To exercise the Jev path, use the documented MCP, CLI or SDK example and inspect the actual page and action log. Network end-to-end tests call a provider; assess cost and data scope before running them.

### Evidence and limitations

Repository identity, README, TypeSafe API client, browser session code and MIT license were reviewed. Task correctness, call latency and context-saving figures are author-reported and were not reproduced here. No installation or run was performed. The project identifies itself as unofficial. It is distinct from other repositories named `jev-browser`.

## Sources / 来源

- [项目仓库 / Repository](https://github.com/Ying-Kai-Liao/jev-browser)
- [固定版本 README / Pinned README](https://github.com/Ying-Kai-Liao/jev-browser/blob/e35ab134f65033d29c528132d92bf06e8d6adcb5/README.md)
- [TypeSafe 客户端 / TypeSafe client](https://github.com/Ying-Kai-Liao/jev-browser/blob/e35ab134f65033d29c528132d92bf06e8d6adcb5/src/jev.mjs)
- [会话实现 / Session implementation](https://github.com/Ying-Kai-Liao/jev-browser/blob/e35ab134f65033d29c528132d92bf06e8d6adcb5/src/session.mjs)
- [原始许可证 / Upstream license](https://github.com/Ying-Kai-Liao/jev-browser/blob/e35ab134f65033d29c528132d92bf06e8d6adcb5/LICENSE)
