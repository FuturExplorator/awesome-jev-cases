---
slug: "pi-heed"
name_en: "Pi-Heed"
name_zh: "Pi 工具调用约束"
project_url: "https://github.com/Nyarlathoteppppp/pi-heed"
source_url: "https://github.com/Nyarlathoteppppp/pi-heed/blob/b7b3c56093395a6a1af5157dc02ca6eda45afb5e/README.md"
source_kind: "github"
author: "Nyarlathoteppppp"
source_date: "2026-09-19"
source_date_kind: "commit"
last_checked: "2026-09-29"
source_revision: "b7b3c56093395a6a1af5157dc02ca6eda45afb5e"
jev_relation: "uses_typesafe"
scenario: "guardrails"
content_kind: "integration"
status: "verified"
claim_status: "source_reviewed"
upstream_license: "MIT"
evidence_file: "research/evidence/pi-heed.json"
---

# Pi-Heed / Pi 工具调用约束

## 中文

### 项目简介

为 Pi 编码代理保留用户约束，并在有副作用的工具调用前检查约束。

### Jev 的具体作用

Jev 根据新消息分类已有规则的变化，并判断自由文本禁令与待执行调用的关系；资源提取、规则状态更新及拦截由代码处理。

### 如何复现

按 README Install 安装到 Pi，配置自己的 Jev 凭据；先在默认 shadow 模式观察 /heed status 与决策记录。

### 证据与限制

已核对公开仓库身份、固定版本 README、调用实现与许可证；`verified` 仅指来源核验通过。未安装运行，未进行独立效果测试。作者提供了会话基准，本库未复跑。语义判断在低置信度或调用失败时可能放行，不是安全沙箱；无 Key 的规则模式不算 Jev 实测。

## English

### Overview

A Pi coding-agent extension that retains user constraints and checks side-effecting tool calls.

### Jev's specific role

Jev classifies changes to existing policies from new messages and judges free-text prohibitions against pending calls. Code extracts resources, updates policy state and enforces decisions.

### Reproduction

Use the README Install instructions, supply your own Jev credentials, and inspect /heed status and decisions in the default shadow mode first.

### Evidence and limitations

Public identity, pinned README, implementation and license were reviewed. `verified` means source-verified only; installation, runtime and independent effectiveness tests were not performed. The session benchmarks are author-reported, not rerun here. Uncertain or failed semantic judgments can fail open; this is not a security sandbox. Keyless rules-only operation does not demonstrate Jev.

## Sources / 来源

- 项目与作者 / Project and owner: [Nyarlathoteppppp/pi-heed](https://github.com/Nyarlathoteppppp/pi-heed)
- 所核对版本 / Reviewed revision: [`b7b3c5609339`](https://github.com/Nyarlathoteppppp/pi-heed/commit/b7b3c56093395a6a1af5157dc02ca6eda45afb5e); `source_date` is this commit's date, not a launch date / 来源日期为提交日期，不是发布日期。
- [README.md](https://github.com/Nyarlathoteppppp/pi-heed/blob/b7b3c56093395a6a1af5157dc02ca6eda45afb5e/README.md)
- [src/judge.ts](https://github.com/Nyarlathoteppppp/pi-heed/blob/b7b3c56093395a6a1af5157dc02ca6eda45afb5e/src/judge.ts)
- [src/understand.ts](https://github.com/Nyarlathoteppppp/pi-heed/blob/b7b3c56093395a6a1af5157dc02ca6eda45afb5e/src/understand.ts)
- [src/gate.ts](https://github.com/Nyarlathoteppppp/pi-heed/blob/b7b3c56093395a6a1af5157dc02ca6eda45afb5e/src/gate.ts)
- [LICENSE](https://github.com/Nyarlathoteppppp/pi-heed/blob/b7b3c56093395a6a1af5157dc02ca6eda45afb5e/LICENSE)
- [核验记录与 SHA-256 / Review receipt and SHA-256](../research/evidence/pi-heed.json)
- [第三方权利 / Third-party rights](../THIRD_PARTY_NOTICES.md): MIT
- 关联案例浏览网站 / Related browsing site: [jevforagents.com](https://jevforagents.com) — no case-specific page is asserted / 未宣称对应详情页存在。
