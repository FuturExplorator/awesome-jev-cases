---
slug: "jev-factorio-agent"
name_en: "jev-factorio"
name_zh: "Jev Factorio 代理"
project_url: "https://github.com/jevplays-games/jev-factorio-agent"
source_url: "https://github.com/jevplays-games/jev-factorio-agent/blob/d8605cae485f832394d059aabea2a6395642bbc1/README.md"
source_kind: "github"
author: "jevplays-games"
source_date: "2026-10-08"
source_date_kind: "commit"
last_checked: "2026-10-08"
source_revision: "d8605cae485f832394d059aabea2a6395642bbc1"
jev_relation: "uses_typesafe"
scenario: "game"
content_kind: "experiment"
status: "verified"
claim_status: "source_reviewed"
upstream_license: "MIT"
evidence_file: "research/evidence/jev-factorio-agent.json"
---

# jev-factorio / Jev Factorio 代理

## 中文

### 项目简介

一个 Factorio 游戏代理实验：Jev 以类型化问题做宏观决策，确定性代码负责游戏规则、候选过滤和执行。该仓库在线索表中的地址是 `completedottech/jev-factorio-agent`，本次核验时 GitHub 将它解析为 `jevplays-games/jev-factorio-agent`（数字仓库 ID 相同），本库按现行地址只收录一次。

### Jev 的具体作用

README 说明 Jev 负责目标、下一步动作和卡住检测，以 Choice / Score / Noul 问题提出。固定的 `src/jev_factorio/jev_client.py` 向 `https://api.typesafe.ai/v1/systemone` 发送 `state`、`model`（默认 `jev-latest`）和 `questions`；同一文件还包含经 Cloudflare 调用 `typesafe/jev` 的客户端，以及一个不调用模型的 `MockJevClient`。

### 如何复现

离线入门不需要游戏：`python -m venv .venv && source .venv/bin/activate`，`pip install -e .`，然后 `PYTHONPATH=src python -m jev_factorio --backend mock --steps 8 --tick-seconds 0`。README 提醒 `--backend mock` 只模拟游戏，环境里若配置了 Key 仍会调用模型；要完全离线需清空提供方凭据。连接真实 Factorio 需安装 `.[fle]`、配置 RCON，并且只能使用专门标记的一次性世界，因为启动适配器会重置角色、背包和工厂实体。

### 证据与限制

已核对固定 README、`jev_client.py` 和 MIT LICENSE；未安装、未运行模拟或真实游戏、未调用付费接口。该仓库更新很频繁，本条只对应固定提交。README 中“据我们所知是第一个 Jev 驱动的游戏代理”是作者说法，本库未核实。离线 Mock 路径不是 TypeSafe Jev 的调用证明。

## English

### Overview

A Factorio game-agent experiment: Jev makes macro decisions as typed questions while deterministic code owns game rules, option filtering and actuation. The lead list recorded the repository as `completedottech/jev-factorio-agent`; at review time GitHub resolved it to `jevplays-games/jev-factorio-agent` with the same numeric repository ID, so it is cataloged once under the current address.

### Jev's specific role

The README says Jev handles the goal, next action and stuck detection as Choice / Score / Noul questions. Pinned `src/jev_factorio/jev_client.py` posts `state`, `model` (default `jev-latest`) and `questions` to `https://api.typesafe.ai/v1/systemone`. The same file also contains a client that reaches `typesafe/jev` through Cloudflare and a `MockJevClient` that calls no model.

### Reproduction

The offline start needs no game: `python -m venv .venv && source .venv/bin/activate`, `pip install -e .`, then `PYTHONPATH=src python -m jev_factorio --backend mock --steps 8 --tick-seconds 0`. The README warns that `--backend mock` only simulates the game and still calls the model if a key is configured; clear provider credentials for a fully offline run. Live Factorio needs `.[fle]`, RCON settings and a dedicated, explicitly marked disposable world, because starting the adapter resets characters, inventory and factory entities.

### Evidence and limitations

The pinned README, `jev_client.py` and the MIT license were reviewed. Nothing was installed, neither the simulation nor a real game was run, and no paid call was made. The repository changes frequently; this entry describes the pinned commit only. “To our knowledge this is the first Jev-driven game agent” is the author’s statement and was not verified. The offline mock path is not evidence of a TypeSafe Jev call.

## Sources / 来源

- [项目仓库 / Repository](https://github.com/jevplays-games/jev-factorio-agent)
- [固定版本 README / Pinned README](https://github.com/jevplays-games/jev-factorio-agent/blob/d8605cae485f832394d059aabea2a6395642bbc1/README.md)
- [实现 / Implementation: src/jev_factorio/jev_client.py](https://github.com/jevplays-games/jev-factorio-agent/blob/d8605cae485f832394d059aabea2a6395642bbc1/src/jev_factorio/jev_client.py)
- [原始许可证 / Upstream license](https://github.com/jevplays-games/jev-factorio-agent/blob/d8605cae485f832394d059aabea2a6395642bbc1/LICENSE)
- [核验记录 / Review receipt](../research/evidence/jev-factorio-agent.json)
