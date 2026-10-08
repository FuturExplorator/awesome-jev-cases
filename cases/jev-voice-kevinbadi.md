---
slug: "jev-voice-kevinbadi"
name_en: "Jev Voice"
name_zh: "Jev Voice：语音控制 Mac"
project_url: "https://github.com/kevinbadi/jev-voice"
source_url: "https://github.com/kevinbadi/jev-voice/blob/fdc23e26644df1e68d1991f41221df21620263d6/README.md"
source_kind: "github"
author: "kevinbadi"
source_date: "2026-09-23"
source_date_kind: "commit"
last_checked: "2026-10-08"
source_revision: "fdc23e26644df1e68d1991f41221df21620263d6"
jev_relation: "uses_typesafe"
scenario: "device"
content_kind: "application"
status: "verified"
claim_status: "source_reviewed"
upstream_license: "MIT"
evidence_file: "research/evidence/jev-voice-kevinbadi.json"
---

# Jev Voice / Jev Voice：语音控制 Mac

## 中文

### 项目简介

在 Apple Silicon Mac 上用语音控制电脑：打开应用、打字、搜索、滚动、按快捷键。README 描述的流程是麦克风 → 本地 whisper.cpp 转写 → 一次 Jev 请求 → macOS 动作 → `say` 播报。

### Jev 的具体作用

固定的 `jev_voice/brain.py` 向 `https://api.typesafe.ai/v1/systemone` 发送一次包含多道 Choice 和 Noul 问题的请求，把转写文本变成一个动作类型和若干参数，例如选哪个已安装应用、是否提交、是否是复合指令。README 说明候选值由代码生成，Jev 只做选择，执行由代码负责。多步任务另有 `jev-agent` 循环：从 macOS 无障碍树生成带编号的元素表，每步让 Jev 选操作和目标。

### 如何复现

按固定 README：`cp .env.example .env` 并填入自己的 `TYPESAFE_API_KEY`，运行 `./scripts/setup.sh`。README 说明该脚本会安装 whisper-cpp 和 ffmpeg、下载模型、把 Caps Lock 重映射为 F18，并打开麦克风、辅助功能和输入监控的权限面板，运行前请先阅读。可以先用 `jev --text "open chrome and go to youtube" --dry-run` 只测试路由，不使用麦克风。

### 证据与限制

已核对固定 README、`brain.py` 的问题与解析、`config.py` 的端点配置和 MIT LICENSE；未安装、未授予系统权限、未调用付费接口。README 中约 250 ms、约 100 ms 等延迟为作者自述。README 自己写明 `DONE` 只是模型的声明而非证明，多步运行有 40 个动作、80 次 Jev 调用的上限。该工具会真实操作你的桌面。

## English

### Overview

Voice control for an Apple Silicon Mac: open apps, type, search, scroll and press shortcuts. The README describes the pipeline as microphone → local whisper.cpp transcription → one Jev request → macOS actions → spoken reply through `say`.

### Jev's specific role

Pinned `jev_voice/brain.py` posts one request to `https://api.typesafe.ai/v1/systemone` containing many Choice and Noul questions, turning the transcript into an action type and arguments such as which installed app, whether to submit, and whether the command is compound. The README says code produces candidate values, Jev only selects, and code owns execution. Multi-step tasks use a separate `jev-agent` loop: an indexed element table from the macOS Accessibility tree, with Jev picking the operation and target at each step.

### Reproduction

Per the pinned README: `cp .env.example .env`, add your own `TYPESAFE_API_KEY`, and run `./scripts/setup.sh`. The README says the script installs whisper-cpp and ffmpeg, downloads a model, remaps Caps Lock to F18 and opens the Microphone, Accessibility and Input Monitoring panes, so read it first. `jev --text "open chrome and go to youtube" --dry-run` tests routing without a microphone.

### Evidence and limitations

The pinned README, the questions and parsing in `brain.py`, the endpoint settings in `config.py` and the MIT license were reviewed. Nothing was installed, no system permission was granted and no paid call was made. Latencies such as about 250 ms and about 100 ms are author-reported. The README itself says a `DONE` choice is the model’s claim, not proof, and that runs are bounded at 40 actions and 80 Jev calls. The tool really operates your desktop.

## Sources / 来源

- [项目仓库 / Repository](https://github.com/kevinbadi/jev-voice)
- [固定版本 README / Pinned README](https://github.com/kevinbadi/jev-voice/blob/fdc23e26644df1e68d1991f41221df21620263d6/README.md)
- [实现 / Implementation: jev_voice/brain.py](https://github.com/kevinbadi/jev-voice/blob/fdc23e26644df1e68d1991f41221df21620263d6/jev_voice/brain.py)
- [实现 / Implementation: jev_voice/config.py](https://github.com/kevinbadi/jev-voice/blob/fdc23e26644df1e68d1991f41221df21620263d6/jev_voice/config.py)
- [原始许可证 / Upstream license](https://github.com/kevinbadi/jev-voice/blob/fdc23e26644df1e68d1991f41221df21620263d6/LICENSE)
- [核验记录 / Review receipt](../research/evidence/jev-voice-kevinbadi.json)
