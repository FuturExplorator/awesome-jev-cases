---
slug: "live-jev-okinaaudio"
name_en: "Live Jev"
name_zh: "Live Jev：一句话控制 Ableton Live"
project_url: "https://github.com/okinaaudio/live-jev"
source_url: "https://github.com/okinaaudio/live-jev/blob/2446eb777ad9f59f77b96ee5b081ee8c2812e0a3/README.md"
source_kind: "github"
author: "okinaaudio"
source_date: "2026-09-21"
source_date_kind: "commit"
last_checked: "2026-10-08"
source_revision: "2446eb777ad9f59f77b96ee5b081ee8c2812e0a3"
jev_relation: "uses_typesafe"
scenario: "device"
content_kind: "application"
status: "verified"
claim_status: "source_reviewed"
upstream_license: "MIT"
evidence_file: "research/evidence/live-jev-okinaaudio.json"
---

# Live Jev / Live Jev：一句话控制 Ableton Live

## 中文

### 项目简介

用一句简短的日语或英语控制 Ableton Live：按 ⌘⇧Space 呼出小输入条，输入或口述“降 3 dB”“在新轨道上加载 Serum 2”“量化到 1/16”等，由运行在 Live 内的 Remote Script 执行。README 列出的范围包括混音、走带、片段、音符、设备和轨道操作。

### Jev 的具体作用

固定的 `intent.py` 为每句话构造一组 Choice 与 Noul 问题：操作类型、目标轨道、变化方向和幅度，以及是否需要生成内容、是否包含多个操作、是否指向上一步。`daemon.py` 把它们发往 `https://api.typesafe.ai/v1/systemone`，并在需要时让 Jev 从用户自己的插件清单中选出所指的插件名。README 说明固定短语在本地直接处理、不调用 Jev；默认不涉及 LLM，Gemini 路径是可选项。

### 如何复现

需要 Apple Silicon Mac、macOS 14+、Ableton Live 12、Homebrew、Xcode 命令行工具和自己的 TypeSafe Key。按固定 README 的 Quick start 克隆仓库，把 `remote_script/LiveJev/*.py` 复制到 Live 的 User Library，运行 `bash scripts/build-app.sh`，再在 Live 设置里选择 LiveJev 控制面；逐步检查见仓库的 INSTALL.md。

### 证据与限制

已核对固定 README、`daemon.py` 的请求代码、`intent.py` 的问题定义和 MIT LICENSE；未构建应用、未连接 Ableton Live、未调用付费接口。README 中约 20 ms 的命令耗时和价格说明为作者自述。README 列出了若干不支持的情况，例如一句话点名两条轨道的指令不会执行，撤销只对留有记录的更改有效。

## English

### Overview

Control Ableton Live with one short Japanese or English sentence: press ⌘⇧Space, type or dictate something like “turn it down 3 dB”, “Serum 2 on a new track” or “quantize to 1/16”, and a Remote Script running inside Live applies it. The README lists mixer, transport, clip, note, device and track operations.

### Jev's specific role

Pinned `intent.py` builds a set of Choice and Noul questions per utterance: the action, the target track, the direction and size of the change, and whether it needs generation, contains several actions, or refers to the previous step. `daemon.py` posts them to `https://api.typesafe.ai/v1/systemone` and, when needed, asks Jev to pick the intended plug-in from the user’s own plug-in list. The README says fixed phrases are answered locally without Jev, no LLM is involved by default, and a Gemini path is optional.

### Reproduction

Requires an Apple Silicon Mac, macOS 14+, Ableton Live 12, Homebrew, the Xcode Command Line Tools and your own TypeSafe key. Follow the pinned README’s Quick start: clone, copy `remote_script/LiveJev/*.py` into Live’s User Library, run `bash scripts/build-app.sh`, then select the LiveJev control surface in Live’s settings. INSTALL.md has a check for every step.

### Evidence and limitations

The pinned README, request code in `daemon.py`, question definitions in `intent.py` and the MIT license were reviewed. The app was not built, Ableton Live was not connected and no paid call was made. The roughly 20 ms command time and the pricing note are author-reported. The README lists unsupported cases, for example a single command naming two tracks is not executed and undo only covers changes with a kept receipt.

## Sources / 来源

- [项目仓库 / Repository](https://github.com/okinaaudio/live-jev)
- [固定版本 README / Pinned README](https://github.com/okinaaudio/live-jev/blob/2446eb777ad9f59f77b96ee5b081ee8c2812e0a3/README.md)
- [实现 / Implementation: daemon.py](https://github.com/okinaaudio/live-jev/blob/2446eb777ad9f59f77b96ee5b081ee8c2812e0a3/daemon.py)
- [实现 / Implementation: intent.py](https://github.com/okinaaudio/live-jev/blob/2446eb777ad9f59f77b96ee5b081ee8c2812e0a3/intent.py)
- [原始许可证 / Upstream license](https://github.com/okinaaudio/live-jev/blob/2446eb777ad9f59f77b96ee5b081ee8c2812e0a3/LICENSE)
- [核验记录 / Review receipt](../research/evidence/live-jev-okinaaudio.json)
