---
slug: "compact-adviser"
name_en: "Compact Adviser"
name_zh: "上下文压缩时机建议"
project_url: "https://github.com/kunchenguid/compact-adviser"
source_url: "https://github.com/kunchenguid/compact-adviser/blob/0b355ff650bd7fc4179c9af8fdf9cdeeea5a0139/README.md"
source_kind: "github"
author: "kunchenguid"
source_date: "2026-09-29"
source_date_kind: "commit"
last_checked: "2026-09-29"
source_revision: "0b355ff650bd7fc4179c9af8fdf9cdeeea5a0139"
jev_relation: "uses_typesafe"
scenario: "coding"
content_kind: "integration"
status: "verified"
claim_status: "source_reviewed"
upstream_license: "MIT"
evidence_file: "research/evidence/compact-adviser.json"
---

# Compact Adviser / 上下文压缩时机建议

## 中文

### 项目简介

在代理会话工作告一段落时，判断是否适合进行上下文压缩。

### Jev 的具体作用

Jev 根据会话检查点回答工作是否完成、属于动手执行还是协调；代码结合上下文占用计算是否提示压缩。它不生成摘要。

### 如何复现

按 README 为所用客户端选择安装章节，配置自己的 TypeSafe 凭据，从 hint 模式检查建议和状态。

### 证据与限制

已核对公开仓库身份、固定版本 README、调用实现与许可证；`verified` 仅指来源核验通过。未安装运行，未进行独立效果测试。作者的评测未在本库复跑。Codex CLI 与 Grok 仅提示；Pi 与 Claude Code 的自动模式需额外启用，不能混为统一能力。

## English

### Overview

An agent plugin that identifies possible compaction boundaries after a unit of work.

### Jev's specific role

Jev judges completion and whether a checkpoint is hands-on work or coordination. Code combines those answers with context usage to decide whether to suggest compaction. Jev does not write the summary.

### Reproduction

Choose the README installation section for your host, configure your own TypeSafe credentials, and inspect advice in hint mode.

### Evidence and limitations

Public identity, pinned README, implementation and license were reviewed. `verified` means source-verified only; installation, runtime and independent effectiveness tests were not performed. Author evaluations were not rerun here. Codex CLI and Grok are hint-only; Pi and Claude Code have separately enabled automatic modes. Host capabilities are not interchangeable.

## Sources / 来源

- 项目与作者 / Project and owner: [kunchenguid/compact-adviser](https://github.com/kunchenguid/compact-adviser)
- 所核对版本 / Reviewed revision: [`0b355ff650bd`](https://github.com/kunchenguid/compact-adviser/commit/0b355ff650bd7fc4179c9af8fdf9cdeeea5a0139); `source_date` is this commit's date, not a launch date / 来源日期为提交日期，不是发布日期。
- [README.md](https://github.com/kunchenguid/compact-adviser/blob/0b355ff650bd7fc4179c9af8fdf9cdeeea5a0139/README.md)
- [packages/codex-plugin/src/judge.ts](https://github.com/kunchenguid/compact-adviser/blob/0b355ff650bd7fc4179c9af8fdf9cdeeea5a0139/packages/codex-plugin/src/judge.ts)
- [LICENSE](https://github.com/kunchenguid/compact-adviser/blob/0b355ff650bd7fc4179c9af8fdf9cdeeea5a0139/LICENSE)
- [核验记录与 SHA-256 / Review receipt and SHA-256](../research/evidence/compact-adviser.json)
- [第三方权利 / Third-party rights](../THIRD_PARTY_NOTICES.md): MIT
- 关联案例浏览网站 / Related browsing site: [jevforagents.com](https://jevforagents.com) — no case-specific page is asserted / 未宣称对应详情页存在。
