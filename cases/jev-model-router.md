---
slug: "jev-model-router"
name_en: "Jev Model Router"
name_zh: "模型档位路由"
project_url: "https://github.com/rajdhakad9826/jev-router"
source_url: "https://github.com/rajdhakad9826/jev-router/blob/5fe292964f45dd288943dfcb1df30762c3d58aae/README.md"
source_kind: "github"
author: "rajdhakad9826"
source_date: "2026-09-21"
source_date_kind: "commit"
last_checked: "2026-09-29"
source_revision: "5fe292964f45dd288943dfcb1df30762c3d58aae"
jev_relation: "uses_typesafe"
scenario: "routing"
content_kind: "integration"
status: "verified"
claim_status: "source_reviewed"
upstream_license: "MIT"
evidence_file: "research/evidence/jev-model-router.json"
---

# Jev Model Router / 模型档位路由

## 中文

### 项目简介

一个 TypeScript 路由库，按查询要求在调用方提供的两到三个模型档位间选择。

### Jev 的具体作用

查询与各档位说明进入 TypeSafe System One；Jev 返回档位概率，代码按阈值选择模型，并在接口错误时使用配置的回退项。

### 如何复现

从 README Setup 与 Example 开始，安装 jev-model-router，设置自己的 TYPESAFE_API_KEY，按弱到强排序两个或三个模型并调用 Router.route。

### 证据与限制

已核对公开仓库身份、固定版本 README、调用实现与许可证；`verified` 仅指来源核验通过。未安装运行，未进行独立效果测试。“最便宜且胜任”是作者的目标，本库未验证实际成本或任务质量。返回的是路由结果，不代表下游模型已执行任务。

## English

### Overview

A TypeScript routing library that selects among two or three caller-defined model tiers.

### Jev's specific role

The query and tier descriptions enter TypeSafe System One. Jev returns tier probabilities; code applies thresholds and a configured fallback on API failure.

### Reproduction

Follow Setup and Example: install jev-model-router, configure your own TYPESAFE_API_KEY, order two or three models from weaker to stronger, and call Router.route.

### Evidence and limitations

Public identity, pinned README, implementation and license were reviewed. `verified` means source-verified only; installation, runtime and independent effectiveness tests were not performed. The cheapest-capable-model framing is the author’s goal, not a verified cost or quality result. A route response does not mean the downstream model executed the task.

## Sources / 来源

- 项目与作者 / Project and owner: [rajdhakad9826/jev-router](https://github.com/rajdhakad9826/jev-router)
- 所核对版本 / Reviewed revision: [`5fe292964f45`](https://github.com/rajdhakad9826/jev-router/commit/5fe292964f45dd288943dfcb1df30762c3d58aae); `source_date` is this commit's date, not a launch date / 来源日期为提交日期，不是发布日期。
- [README.md](https://github.com/rajdhakad9826/jev-router/blob/5fe292964f45dd288943dfcb1df30762c3d58aae/README.md)
- [src/jev/classifier.ts](https://github.com/rajdhakad9826/jev-router/blob/5fe292964f45dd288943dfcb1df30762c3d58aae/src/jev/classifier.ts)
- [src/router.ts](https://github.com/rajdhakad9826/jev-router/blob/5fe292964f45dd288943dfcb1df30762c3d58aae/src/router.ts)
- [LICENSE](https://github.com/rajdhakad9826/jev-router/blob/5fe292964f45dd288943dfcb1df30762c3d58aae/LICENSE)
- [核验记录与 SHA-256 / Review receipt and SHA-256](../research/evidence/jev-model-router.json)
- [第三方权利 / Third-party rights](../THIRD_PARTY_NOTICES.md): MIT
- 关联案例浏览网站 / Related browsing site: [jevforagents.com](https://jevforagents.com) — no case-specific page is asserted / 未宣称对应详情页存在。
