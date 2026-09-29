---
slug: "clearjev"
name_en: "ClearJev"
name_zh: "Codex CLI 提示路由"
project_url: "https://github.com/huncijr/ClearJev"
source_url: "https://github.com/huncijr/ClearJev/blob/859ef1d9d821713864ad62e9a15963d882a9c004/README.md"
source_kind: "github"
author: "huncijr"
source_date: "2026-09-26"
source_date_kind: "commit"
last_checked: "2026-09-29"
source_revision: "859ef1d9d821713864ad62e9a15963d882a9c004"
jev_relation: "uses_typesafe"
scenario: "routing"
content_kind: "integration"
status: "verified"
claim_status: "source_reviewed"
upstream_license: "MIT"
evidence_file: "research/evidence/clearjev.json"
---

# ClearJev / Codex CLI 提示路由

## 中文

### 项目简介

在 Codex CLI 提示执行前，选择会话所用的模型与推理配置。

### Jev 的具体作用

提示与仓库上下文进入 Jev 的批量判断，路由代码将任务要求映射到模型和推理档位；缓存与启发式路径可跳过 Jev 请求。

### 如何复现

先阅读 README Install 和安装脚本，再按文档配置自己的 TypeSafe Key、重启 CLI 并信任 Hook；开启路由后检查状态和决策来源。

### 证据与限制

已核对公开仓库身份、固定版本 README、调用实现与许可证；`verified` 仅指来源核验通过。未安装运行，未进行独立效果测试。作者的成本与自动切换说法未在本库复测。缺 Key 时会启发式回退，这不是 Jev 运行证据。项目明确限于 CLI，不适用于桌面 App。

## English

### Overview

A Codex CLI routing layer that chooses the session model and reasoning configuration before a prompt runs.

### Jev's specific role

Jev receives a prompt and repository context for batched judgments. Routing code maps task demands to model and effort; caches and heuristics can bypass Jev calls.

### Reproduction

Read Install and the installer first, configure your own TypeSafe key, restart the CLI and trust its hook; enable routing and inspect status and decision provenance.

### Evidence and limitations

Public identity, pinned README, implementation and license were reviewed. `verified` means source-verified only; installation, runtime and independent effectiveness tests were not performed. Cost and automatic switching claims were not tested here. Keyless heuristic fallback is not evidence of a Jev run. The project explicitly targets CLI, not the desktop App.

## Sources / 来源

- 项目与作者 / Project and owner: [huncijr/ClearJev](https://github.com/huncijr/ClearJev)
- 所核对版本 / Reviewed revision: [`859ef1d9d821`](https://github.com/huncijr/ClearJev/commit/859ef1d9d821713864ad62e9a15963d882a9c004); `source_date` is this commit's date, not a launch date / 来源日期为提交日期，不是发布日期。
- [README.md](https://github.com/huncijr/ClearJev/blob/859ef1d9d821713864ad62e9a15963d882a9c004/README.md)
- [scripts/jev_route.py](https://github.com/huncijr/ClearJev/blob/859ef1d9d821713864ad62e9a15963d882a9c004/scripts/jev_route.py)
- [LICENSE](https://github.com/huncijr/ClearJev/blob/859ef1d9d821713864ad62e9a15963d882a9c004/LICENSE)
- [核验记录与 SHA-256 / Review receipt and SHA-256](../research/evidence/clearjev.json)
- [第三方权利 / Third-party rights](../THIRD_PARTY_NOTICES.md): MIT
- 关联案例浏览网站 / Related browsing site: [jevforagents.com](https://jevforagents.com) — no case-specific page is asserted / 未宣称对应详情页存在。
