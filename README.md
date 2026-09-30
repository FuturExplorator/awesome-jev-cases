# [Awesome Jev Cases](https://jevforagents.com)

[项目网站 / Website](https://jevforagents.com) · [中文说明](#中文说明) · [English](#english) · [分类目录 / Categories](categories/README.md)

## 中文说明

这是由个人账号 **FuturExplorator** 独立维护的中英双语 [TypeSafe Jev](https://typesafe.ai/) 案例库。你可以从[分类目录](categories/README.md)寻找实际用法；每条案例都附有[原始来源与核验记录](research/evidence/README.md)，说明项目解决什么任务、Jev 作出什么判断，以及如何开始复现。

**现有目录：20 个独立项目，全部为 `verified` / `source_reviewed`。** 首版发布 11 个，2026-09-30 分两批增补 9 个。这表示来源、项目身份、Jev 用途和链接已核对，不表示性能、安全性、成本或运行结果已独立验证。

| 按场景浏览 | 已收录 |
| --- | ---: |
| [浏览器执行](categories/browser.md) | 6 |
| [路由与选择](categories/routing.md) | 4 |
| [编码与上下文](categories/coding.md) | 4 |
| [约束与防护](categories/guardrails.md) | 1 |
| [证据评估](categories/evaluation.md) | 3 |
| [数据流与其他](categories/other.md) | 2 |

可以从 [Jev Browser](cases/jev-browser-jkudish.md)、[Pi-Heed](cases/pi-heed.md) 和 [Jev Model Router](cases/jev-model-router.md) 开始。
更多浏览与演示见 [jevforagents.com](https://jevforagents.com)。仓库可独立阅读，当前没有网站同步；仓库收录也不代表网站案例通过了新的运行或媒体测试。

投稿请读 [CONTRIBUTING](CONTRIBUTING.md)，通过 [Issue 提交线索](https://github.com/FuturExplorator/awesome-jev-cases/issues/new?template=case.yml) 或使用[双语模板](templates/case.md)提交 PR。
审核以[证据与治理规则](GOVERNANCE.md)和[案例格式](schema/README.md)为准；不足证据的项目不会为凑数量进入目录。

## English

An independent bilingual catalog of [TypeSafe Jev](https://typesafe.ai/) projects, maintained by the personal account **FuturExplorator**. Explore the [categories](categories/README.md) to find practical uses. Each case links its [primary sources and review record](research/evidence/README.md) and explains the task, Jev's concrete decisions, and how to start reproducing the work.

**Current catalog: 20 distinct projects, all `verified` / `source_reviewed`.** The first release published 11, and nine were added in two batches on 2026-09-30. This verifies provenance, identity, Jev usage and links, not independent performance, security, cost or runtime results.

Browse [browser execution](categories/browser.md) (6), [routing](categories/routing.md) (4), [coding and context](categories/coding.md) (4), [guardrails](categories/guardrails.md) (1), [evaluation](categories/evaluation.md) (3), and [streams and other uses](categories/other.md) (2).
Start with [Jev Browser](cases/jev-browser-jkudish.md), [Pi-Heed](cases/pi-heed.md), or [Jev Model Router](cases/jev-model-router.md).

For richer browsing and demos, visit [jevforagents.com](https://jevforagents.com). This repository stands alone. No website synchronization or renewed website runtime/media verification is included in this update.
Read [CONTRIBUTING](CONTRIBUTING.md), submit a lead through an [Issue](https://github.com/FuturExplorator/awesome-jev-cases/issues/new?template=case.yml), or open a PR using the [bilingual template](templates/case.md). The [governance](GOVERNANCE.md) and [case contract](schema/README.md) define admission.

## 许可证 / License

[MIT](LICENSE) covers original code, schemas and original bilingual editorial content this repository has the right to license. Third-party materials retain their own rights; see [THIRD_PARTY_NOTICES](THIRD_PARTY_NOTICES.md) and the [attribution register](research/ATTRIBUTION.md).
MIT 仅适用于本库有权许可的原创内容；第三方代码、原帖、图片与视频不因此改用 MIT。

## 审核与维护 / Audit and maintenance

- [中文 PRD](PRD.zh-CN.md) · [English PRD](PRD.md)
- [首版验收报告 / Release review](research/RELEASE_REVIEW.md)
- [网站与 CSV 导入审核 / Website and CSV intake review](research/IMPORT_REVIEW.md)
- [增补审核与下一批选题 / Follow-up review and next topics](research/FOLLOW_UP_REVIEW.md)
- [候选审核台账 / Candidate audit](research/CANDIDATES.md) — not a published-case index / 不属于已收录目录
- [来源核验记录 / Source receipts](research/evidence/README.md)

Run `python3 scripts/validate_catalog.py` for offline structural checks. It never changes status, publishes, discovers candidates, or calls a model.
运行上述命令检查格式、去重、目录和本地链接；脚本不会变更状态、发布、自动发现或调用模型。
