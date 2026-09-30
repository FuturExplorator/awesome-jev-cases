# 首版验收报告 / First-release review

日期 / Date: 2026-09-29

本文件保留首版当时的验收快照；当前目录与候选状态见[增补审核](FOLLOW_UP_REVIEW.md)和[候选台账](CANDIDATES.md)。 / This document preserves the first-release snapshot. See the [follow-up review](FOLLOW_UP_REVIEW.md) and [candidate ledger](CANDIDATES.md) for current catalog and candidate status.

## 交付 / Delivery

- 个人账号 / Personal owner: **FuturExplorator**。
- **11 个独立项目**进入公开目录，全部 `verified` / `source_reviewed`，分为 6 类；每条中英文同文件。 / **11 distinct projects**, in six categories, each bilingual and source-reviewed.
- 补齐 MIT、第三方权利及逐项来源清单、格式契约、投稿模板、Issue 表单和 PR 检查表。 / MIT, third-party notice and attribution, case contract, templates and contribution forms are included.
- 22 条候选记录，经已知别名去重为 20 个项目/线索：11 verified、4 under_review、5 withheld、2 rejected（重复别名）。 / 22 candidate records, 20 projects/leads after known aliases: 11 verified, 4 under review, 5 withheld, 2 duplicate aliases rejected.

## 未通过与待完成 / Not admitted

| 项目或线索 / Project or lead | 原因 / Reason |
| --- | --- |
| SkillRanker | 固定版本 LICENSE 含 OpenAI/Anthropic 附加限制，不标为标准 MIT，暂缓案例发布及进一步实现分析。 / Restrictive rider; not standard MIT. Case publication and further implementation analysis withheld. |
| Hermes iMessage、Vlad Terin browser、Cline browser、aibuilderclub browser | 本轮内置网页工具打开准确 X 原帖均返回 Internal Error，缺少当前可读取原文与身份链；不是已证实删除。 / Exact X posts returned Internal Error; current original text and identity chain unavailable, not confirmed deleted. |
| tontoko/jev-browser、wy-coliney/jev-browser-use、Ying-Kai-Liao/jev-browser、typesafe-ai/skills | 已打开仓库与 README，尚未完成固定版本实现、许可及双语成稿审核；保留 under_review，不判定项目无效。 / Repositories opened; pinned implementation, rights and bilingual review incomplete, not invalidated. |
| jev-mcp、typesafe-skills 历史记录 / legacy records | 与现有规范项目为同仓库别名，拒绝重复收录。 / Same-repository aliases, not additional cases. |

准确来源及逐项记录见 [CANDIDATES.md](CANDIDATES.md) 和 [candidates.json](candidates.json)。
See those ledgers for exact source URLs and individual dispositions.

## 核验范围 / Review scope

1. 使用 Codex 内置网页工具打开原始仓库；公开 GitHub 元数据核对账号/仓库 ID、公开状态及 fork 状态。固定提交后通过无登录 raw URL 取得 README、特定实现文件与 LICENSE，记录原始字节 SHA-256。没有复制全文到本仓库。 / Opened primary repositories with Codex web; checked identity and visibility, pinned revisions, and captured public raw-file hashes. No full third-party material is redistributed.
2. 对照原文逐项编写中英说明，核对 Jev 输入、判断、输出及调用路径；具体读取范围在 [receipts](evidence/README.md)。 / Compared bilingual descriptions with primary text and targeted implementation; receipts delimit inspection scope.
3. 修正旧材料中不能沿用的概括：BorisLeMeec/jev 是 Go 插件；Astra-Ares 是独立补丁 CLI；Compact Adviser 的 Codex 模式仅提示；ClearJev 的启发式回退不是 Jev 实测。 / Corrected inherited generalizations about language, host scope, hint-only behavior and heuristic fallbacks.
4. 上游许可证逐项核对；Context Diet 的 MIT 含上游派生署名，GitHub 的 NOASSERTION 未直接当作无许可证。 / Inspected licenses, including Context Diet's upstream attribution, instead of relying only on GitHub detection.

**未验证 / Not tested:** 没有安装运行 11 个上游项目，没有独立性能、成本、安全性或效果实测；所有作者测量保持作者声称。没有进行网站媒体实播复测。 / No upstream installations or independent runtime, performance, cost, security or effectiveness tests. Author measurements remain author claims; website media was not re-tested.

首版审阅者为 Codex，按负责人明确授权执行；不存在本轮人工签字。 / Reviewer: Codex under explicit owner instruction; no human sign-off is claimed.

## 检查结果 / Validation

- `python3 scripts/validate_catalog.py`：通过，11 条已核验案例；格式、枚举、项目与来源去重、receipt 一致性、状态/分类/署名覆盖以及本地链接均通过。 / Passed for 11 verified cases, including metadata, identity, receipts, indexes, attribution and local links.
- `python3 scripts/test_validate_catalog.py`：7/7 通过。覆盖正常目录、未核验条目进入分类、兼容模式冒充接入、重复项目、无凭据的独立实测声明、来源读取失败及缺双语/权利说明。 / 7/7 checks cover valid input and publication-boundary failures.
- **67/67 外链返回 HTTP 200**（无登录 GET，不重试），GitHub 文件页面还检查路径存在；结果见 [link-checks.json](link-checks.json)。范围为 README、治理/投稿/权利说明、来源清单及 11 条公开案例。 / 67/67 public-catalog links returned HTTP 200; GitHub file pages also contained their expected path.
- 另有 **43 份固定版本原始文件读取成功**，字节哈希保存在各 case receipt。它们是审阅输入，不是运行测试。 / 43 pinned raw files were retrieved successfully and hashed in receipts; this is source evidence, not runtime testing.
- 已逐项对照双语正文的项目用途、操作前提、作者声明、未运行状态及限制；没有将作者性能数据提升为独立事实。 / Bilingual role, prerequisites, claims, not-run status and limitations were compared against primary sources.
- 上述外链通过率不含候选台账中无法读取的 4 条 X 原帖；这些仍为 withheld，未进入目录。HTTP 成功只是当时可达性，不能证明技术效果。 / The four inaccessible candidate X posts are excluded from the success count and remain withheld. HTTP success is reachability, not technical effectiveness.

## 边界与待决策 / Boundaries and owner decision

本轮无 AIsa 付费接口、模型运行、每日发现、自动发布、网站同步，未修改或部署 jevforagents.com。只在案例库仓库内交付文档、案例、审核元数据和离线校验工具。
No AIsa or paid model execution, scheduled discovery, automatic publication, website synchronization, website edits or deployment. Changes are confined to this catalog.

没有阻塞首版的问题。后续需决定：是否允许对含限制性许可条款的项目建立仅链接索引（目前 SkillRanker 保持 withheld）。其余待审核来源可以以后补证，不需要为首版降低门槛。
No decision blocks this release. For later work, decide whether projects with restrictive licenses may receive link-only entries; SkillRanker remains withheld. Other candidates can await evidence without weakening admission.
