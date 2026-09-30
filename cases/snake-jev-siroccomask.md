---
slug: "snake-jev-siroccomask"
name_en: "Snake Jev"
name_zh: "Jev 贪吃蛇实验"
project_url: "https://github.com/siroccomask/snake-jev"
source_url: "https://github.com/siroccomask/snake-jev/blob/86f01b686df2e6d5b566b80d015de9b8b34450a8/README.md"
source_kind: "github"
author: "siroccomask"
source_date: "2026-09-17"
source_date_kind: "commit"
last_checked: "2026-09-30"
source_revision: "86f01b686df2e6d5b566b80d015de9b8b34450a8"
jev_relation: "uses_typesafe"
scenario: "game"
content_kind: "experiment"
status: "verified"
claim_status: "source_reviewed"
upstream_license: "MIT"
evidence_file: "research/evidence/snake-jev-siroccomask.json"
---

# Snake Jev / Jev 贪吃蛇实验

## 中文

### 项目简介

一个桌面贪吃蛇实验，把旧版游戏的传感器转为 Jev 判断输入；Python 负责食物、移动与碰撞等游戏运行。它不是通用游戏代理。

### Jev 的具体作用

每个游戏 tick 发送一次 TypeSafe Jev 请求，同时询问左转、直行、右转各自的墙体碰撞、身体碰撞和接近食物判断，共九个问题。Python 只根据 Jev 返回的判断组合动作，再把相对方向交给原游戏；Jev 不直接输出最终移动 Choice。

### 如何复现

按固定 README 用 `uv sync` 安装，在 `.env` 中设置自己的 `JEV_API_KEY`，优先以 `uv run python sketch.py --max-calls 100` 限定请求量；桌面需支持 OpenGL，作者只在 macOS/Python 3.12 测试。空格启动/暂停，`.` 单步。每一步均可能产生 API 费用。

### 证据与限制

已核对 README、九问构造与回答合成、游戏推进代码、MIT LICENSE；未运行游戏或重现作者“461 tick 吃到 29 个食物”的单次记录。作者注明遇到错误会暂停而不会自动重试；该实验没有完整路径规划。

## English

### Overview

A desktop Snake experiment that turns sensors from an earlier game into Jev judgment input; Python still runs the food, movement and collision mechanics. It is not a general game agent.

### Jev's specific role

Each game tick makes one TypeSafe Jev request with nine questions: wall, body and food judgments for left, straight and right. Python composes an action solely from Jev’s judgments, then passes the relative move to the original game. Jev does not directly return a final move Choice.

### Reproduction

Follow the pinned README: use `uv sync`, set your own `JEV_API_KEY` in `.env`, and prefer `uv run python sketch.py --max-calls 100` to bound calls. OpenGL desktop support is needed; the author tested macOS/Python 3.12. Space starts or pauses, and `.` steps once. Each step may incur an API charge.

### Evidence and limitations

README, nine-question construction and composition, game update path, and MIT license were reviewed. The game was not run, and the author’s single 29-food/461-tick run was not reproduced. The author says errors pause without retry; the experiment has no full path planning.

## Sources / 来源

- [项目仓库 / Repository](https://github.com/siroccomask/snake-jev)
- [固定版本 README / Pinned README](https://github.com/siroccomask/snake-jev/blob/86f01b686df2e6d5b566b80d015de9b8b34450a8/README.md)
- [实现 / Implementation: jev_controller.py](https://github.com/siroccomask/snake-jev/blob/86f01b686df2e6d5b566b80d015de9b8b34450a8/jev_controller.py)
- [实现 / Implementation: jev_run.py](https://github.com/siroccomask/snake-jev/blob/86f01b686df2e6d5b566b80d015de9b8b34450a8/jev_run.py)
- [原始许可证 / Upstream license](https://github.com/siroccomask/snake-jev/blob/86f01b686df2e6d5b566b80d015de9b8b34450a8/LICENSE)
