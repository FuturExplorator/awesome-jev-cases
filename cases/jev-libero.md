---
slug: "jev-libero"
name_en: "Jev × LIBERO"
name_zh: "Jev × LIBERO 机器人仿真控制"
project_url: "https://github.com/Dimweaker/jev-libero"
source_url: "https://github.com/Dimweaker/jev-libero/blob/3bdad985b225aeccc39fbe5863c6eea2e81c515a/README.md"
source_kind: "github"
author: "Dimweaker"
source_date: "2026-09-21"
source_date_kind: "commit"
last_checked: "2026-10-08"
source_revision: "3bdad985b225aeccc39fbe5863c6eea2e81c515a"
jev_relation: "uses_typesafe"
scenario: "game"
content_kind: "experiment"
status: "verified"
claim_status: "source_reviewed"
upstream_license: "MIT"
evidence_file: "research/evidence/jev-libero.json"
---

# Jev × LIBERO / Jev × LIBERO 机器人仿真控制

## 中文

### 项目简介

在 LIBERO 机器人仿真任务中用 Jev 做细粒度控制的实验。README 展示了关微波炉、关上层抽屉、抓取汤罐放入篮子三个任务配置，它们共用一个控制引擎，并提供可交互回放的 Decision Lab 页面。

### Jev 的具体作用

README 描述分层决策：Jev 依次选择意图、接触/运动类别和具体输入（共 27 种输入），本地物理预览在可回退的仿真分支中评估候选动作效果。固定的 `src/jev_libero/client.py` 为每一层构造一个 Choice 问题，并校验返回的选项必须在候选之内；可经 OpenRouter 的 `typesafe/jev-1.13`，或直接经 `https://api.typesafe.ai/v1/systemone`（`jev-latest`）调用。

### 如何复现

Python 3.10 或 3.11：克隆后 `pip install -e .`，`jev-libero tasks` 列出任务，`jev-libero inspect examples/records/top_drawer_seed1` 查看已记录的运行；README 说明这两步不需要仿真环境。要实际运行回合，需另行准备 LIBERO / robosuite / MuJoCo 环境并设置 `LIBERO_ROOT`，以及所选提供方的 API Key。

### 证据与限制

已核对固定 README、`client.py`、THIRD_PARTY.md 和 MIT LICENSE；未安装、未运行仿真、未调用付费接口。README 中各任务的决策数和环境步数（例如关微波炉 14 次决策、111 步）来自作者记录，未复现。THIRD_PARTY.md 写明 GIF/MP4 是仿真回合的渲染，不是实体机器人画面；LIBERO 资产需另行下载并遵循其各自许可。

## English

### Overview

An experiment in fine-grained robot control with Jev on LIBERO simulation tasks. The README shows three task configurations sharing one control engine (close the microwave, close the top drawer, grasp a soup can and lower it into a basket) and links an interactive Decision Lab replay.

### Jev's specific role

The README describes layered decisions: Jev selects an intent, a contact/motion family and an input (27 inputs in total), while local physics previews evaluate candidate effects in reversible simulator branches. Pinned `src/jev_libero/client.py` builds one Choice question per layer and rejects any returned choice outside the candidates. It can call `typesafe/jev-1.13` through OpenRouter or `jev-latest` directly at `https://api.typesafe.ai/v1/systemone`.

### Reproduction

With Python 3.10 or 3.11: clone, `pip install -e .`, list tasks with `jev-libero tasks` and inspect a recorded run with `jev-libero inspect examples/records/top_drawer_seed1`; the README says these need no simulator. Running episodes needs your own LIBERO / robosuite / MuJoCo environment, `LIBERO_ROOT`, and an API key for the chosen provider.

### Evidence and limitations

The pinned README, `client.py`, THIRD_PARTY.md and the MIT license were reviewed. Nothing was installed, no simulation was run and no paid call was made. Decision and step counts per task (for example 14 decisions and 111 environment steps for the microwave) come from the author’s records and were not reproduced. THIRD_PARTY.md states the GIFs/MP4s are renders of simulated episodes, not physical-robot footage, and that LIBERO assets are downloaded separately under their own licenses.

## Sources / 来源

- [项目仓库 / Repository](https://github.com/Dimweaker/jev-libero)
- [固定版本 README / Pinned README](https://github.com/Dimweaker/jev-libero/blob/3bdad985b225aeccc39fbe5863c6eea2e81c515a/README.md)
- [实现 / Implementation: src/jev_libero/client.py](https://github.com/Dimweaker/jev-libero/blob/3bdad985b225aeccc39fbe5863c6eea2e81c515a/src/jev_libero/client.py)
- [文档 / Document: THIRD_PARTY.md](https://github.com/Dimweaker/jev-libero/blob/3bdad985b225aeccc39fbe5863c6eea2e81c515a/THIRD_PARTY.md)
- [原始许可证 / Upstream license](https://github.com/Dimweaker/jev-libero/blob/3bdad985b225aeccc39fbe5863c6eea2e81c515a/LICENSE)
- [核验记录 / Review receipt](../research/evidence/jev-libero.json)
