---
slug: "firehose-judge"
name_en: "Firehose Judge"
name_zh: "实时帖子分类与复核"
project_url: "https://github.com/ragelink/firehose-judge"
source_url: "https://github.com/ragelink/firehose-judge/blob/af5a50f5cc251399cac6ffc05bd9bcdc1418552d/README.md"
source_kind: "github"
author: "ragelink"
source_date: "2026-09-19"
source_date_kind: "commit"
last_checked: "2026-09-29"
source_revision: "af5a50f5cc251399cac6ffc05bd9bcdc1418552d"
jev_relation: "uses_typesafe"
scenario: "other"
content_kind: "application"
status: "verified"
claim_status: "source_reviewed"
upstream_license: "MIT"
evidence_file: "research/evidence/firehose-judge.json"
---

# Firehose Judge / 实时帖子分类与复核

## 中文

### 项目简介

对 Bluesky 实时流中的采样帖子分类，并将不确定结果放入人工复核通道。

### Jev 的具体作用

帖子文本进入一次包含八个问题的 Jev 请求；返回主题、意图等类型化判断。代码使用置信度阈值分流，并过滤被判为不宜展示的内容。

### 如何复现

按 README Run it 准备本地 Cloudflare Wrangler 环境和自己的 TYPESAFE_API_KEY，阅读 questions.json，再启动本地开发服务。

### 证据与限制

已核对公开仓库身份、固定版本 README、调用实现与许可证；`verified` 仅指来源核验通过。未安装运行，未进行独立效果测试。延迟、费用和线上运行效果均来自作者，本库未复测。人工通道仅代表需要复核，不代表已有人工完成审核。

## English

### Overview

A sampled Bluesky stream classifier with a separate lane for uncertain results.

### Jev's specific role

One Jev request asks eight questions about each sampled post. Typed topic, intent and other judgments feed confidence-based routing and a display-safety filter.

### Reproduction

Follow Run it in the README: prepare a local Cloudflare Wrangler environment and your own TYPESAFE_API_KEY, review questions.json, then start the development service.

### Evidence and limitations

Public identity, pinned README, implementation and license were reviewed. `verified` means source-verified only; installation, runtime and independent effectiveness tests were not performed. Latency, cost and live behavior are author reports, not independently tested here. A human-review lane indicates a need for review, not completed human moderation.

## Sources / 来源

- 项目与作者 / Project and owner: [ragelink/firehose-judge](https://github.com/ragelink/firehose-judge)
- 所核对版本 / Reviewed revision: [`af5a50f5cc25`](https://github.com/ragelink/firehose-judge/commit/af5a50f5cc251399cac6ffc05bd9bcdc1418552d); `source_date` is this commit's date, not a launch date / 来源日期为提交日期，不是发布日期。
- [README.md](https://github.com/ragelink/firehose-judge/blob/af5a50f5cc251399cac6ffc05bd9bcdc1418552d/README.md)
- [src/jev.ts](https://github.com/ragelink/firehose-judge/blob/af5a50f5cc251399cac6ffc05bd9bcdc1418552d/src/jev.ts)
- [questions.json](https://github.com/ragelink/firehose-judge/blob/af5a50f5cc251399cac6ffc05bd9bcdc1418552d/questions.json)
- [LICENSE](https://github.com/ragelink/firehose-judge/blob/af5a50f5cc251399cac6ffc05bd9bcdc1418552d/LICENSE)
- [核验记录与 SHA-256 / Review receipt and SHA-256](../research/evidence/firehose-judge.json)
- [第三方权利 / Third-party rights](../THIRD_PARTY_NOTICES.md): MIT
- 关联案例浏览网站 / Related browsing site: [jevforagents.com](https://jevforagents.com) — no case-specific page is asserted / 未宣称对应详情页存在。
