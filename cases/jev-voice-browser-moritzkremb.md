---
slug: "jev-voice-browser-moritzkremb"
name_en: "Jev Voice Browser"
name_zh: "Jev 语音浏览器"
project_url: "https://github.com/moritzkremb/jev-voice-browser"
source_url: "https://github.com/moritzkremb/jev-voice-browser/blob/198a0764395a666f8398026c0d8abdaf6d1866c5/README.md"
source_kind: "github"
author: "moritzkremb"
source_date: "2026-09-21"
source_date_kind: "commit"
last_checked: "2026-09-30"
source_revision: "198a0764395a666f8398026c0d8abdaf6d1866c5"
jev_relation: "uses_typesafe"
scenario: "browser"
content_kind: "application"
status: "verified"
claim_status: "source_reviewed"
upstream_license: "MIT"
evidence_file: "research/evidence/jev-voice-browser-moritzkremb.json"
---

# Jev Voice Browser / Jev 语音浏览器

## 中文

### 项目简介

一个语音控制浏览器的本地演示：控制页接收 Chrome/Edge 的语音识别文本，服务端驱动另一扇 Chromium 窗口。也可以在控制页直接输入命令。

### Jev 的具体作用

每次语音转写更新将转写文本、当前页面和可操作元素、近期动作送到 Jev；它以 Choice/Noul/Score 判断意图、元素目标、命令是否完整、是否危险和滚动幅度。代码中的 policy 依据阈值决定等待、确认或执行，controller 再让 Playwright 操作页面。语音转写来自浏览器 Web Speech API，不是 Jev。

### 如何复现

按固定 README 使用 Node 20+ 安装依赖与 Playwright Chromium，配置自己的 `TYPESAFE_API_KEY`，运行 `./run.sh`，在普通 Chrome 打开 `http://localhost:8787` 并点击 Start mic；受控的是另开的 Chromium 窗口。可先用控制页文本框试简单命令。不要在受控配置文件中登录敏感账户。

### 证据与限制

已核对 README、Jev SDK 调用、策略与执行代码及 MIT LICENSE；未运行浏览器或测量延迟。作者的约 300ms、危险操作确认和语音识别效果未经本库验证；确认机制不能视为安全保证。

## English

### Overview

A local voice-controlled browser demo. A control page receives Chrome/Edge speech recognition text while the server drives a separate Chromium window. Commands can also be typed into the control page.

### Jev's specific role

Each transcript update sends the text, page and actionable elements, and recent actions to Jev. Choice/Noul/Score answers identify intent, target, completeness, destructive potential and scroll amount. Code policy applies thresholds to wait, confirm or act; a controller then operates Playwright. Speech transcription comes from the browser Web Speech API, not Jev.

### Reproduction

Follow the pinned README with Node 20+, install dependencies and Playwright Chromium, set your own `TYPESAFE_API_KEY`, run `./run.sh`, then open `http://localhost:8787` in normal Chrome and click Start mic. A separate Chromium window is controlled. Start with a simple typed command if preferred. Avoid sensitive logins in the controlled profile.

### Evidence and limitations

README, Jev SDK call, policy, executor and MIT license were reviewed. The browser was not run and latency was not measured. The author’s ~300 ms, destructive-action confirmation and speech-recognition claims were not verified; confirmation is not a security guarantee.

## Sources / 来源

- [项目仓库 / Repository](https://github.com/moritzkremb/jev-voice-browser)
- [固定版本 README / Pinned README](https://github.com/moritzkremb/jev-voice-browser/blob/198a0764395a666f8398026c0d8abdaf6d1866c5/README.md)
- [实现 / Implementation: src/jev.js](https://github.com/moritzkremb/jev-voice-browser/blob/198a0764395a666f8398026c0d8abdaf6d1866c5/src/jev.js)
- [实现 / Implementation: src/policy.js](https://github.com/moritzkremb/jev-voice-browser/blob/198a0764395a666f8398026c0d8abdaf6d1866c5/src/policy.js)
- [实现 / Implementation: src/controller.js](https://github.com/moritzkremb/jev-voice-browser/blob/198a0764395a666f8398026c0d8abdaf6d1866c5/src/controller.js)
- [原始许可证 / Upstream license](https://github.com/moritzkremb/jev-voice-browser/blob/198a0764395a666f8398026c0d8abdaf6d1866c5/LICENSE)
