# 2026-10-08 批次审阅 / 2026-10-08 batch review

审核日 / Reviewed: 2026-10-08 UTC

## 本批结果 / Result

公开目录从 27 条增至 **43 条**，全部 `verified` / `source_reviewed`。新增 16 个独立仓库：3 个来自上一轮的 `under_review` 队列（JevFind、epergaboni/jevseo、jev-cloud-quiz），13 个来自 [CSV 仓库分流表](CSV_REPOSITORIES.md) 中此前只有模型分流的条目。选择时优先补足此前较薄的场景，并要求仓库带有可读的许可证文件；Star 数只作为线索，不作为证据。

The public catalog grows from 27 to **43** `verified` / `source_reviewed` cases. Sixteen distinct repositories were added: three from the previous `under_review` queue (JevFind, epergaboni/jevseo, jev-cloud-quiz) and thirteen from [CSV triage](CSV_REPOSITORIES.md) rows that previously had model triage only. Selection favoured thinly covered scenarios and repositories with a readable license file; star counts were leads, not evidence.

| 案例 / Case | 场景 / Scenario | Jev 的作用 / Jev role |
| --- | --- | --- |
| [Jev Voice](../cases/jev-voice-kevinbadi.md) | `device` | 把语音转写变成动作类型和参数 / Turns a transcript into an action type and arguments |
| [Live Jev](../cases/live-jev-okinaaudio.md) | `device` | 选择 Ableton Live 操作、目标轨道和幅度 / Chooses the Ableton Live action, target track and step |
| [Mobile Jev](../cases/mobile-jev-droidrun.md) | `device` | 在 Android 屏幕上选操作和目标 / Picks the operation and target on an Android screen |
| [Jev Code Finder](../cases/jevfind-code-search.md) | `coding` | 判断路径与代码窗口是否相关 / Judges path and code-window relevance |
| [opencode-jev-compaction](../cases/opencode-jev-compaction.md) | `coding` | 判断旧工具调用和结果是否保留 / Decides whether old tool calls and results stay |
| [oxlint-plugin-jev](../cases/oxlint-plugin-jev.md) | `coding` | 回答自然语言 lint 规则并定位 / Answers plain-English lint rules and locates findings |
| [JevSEO](../cases/jevseo-epergaboni.md) | `evaluation` | 页面评判问题与整站动作选择 / Page judgments and per-page site actions |
| [Jev Logs](../cases/jevlogs.md) | `evaluation` | 日志诊断价值、优先级与是否调查 / Log value, priority and investigation need |
| [neo4jev](../cases/neo4jev.md) | `routing` | 每一跳选择要走的关系 / Chooses the relationship to follow at each hop |
| [go-jev](../cases/go-jev.md) | `integration` | Go SDK 与命令行封装 / Go SDK and CLI wrapper |
| [n8n-nodes-typesafe-jev](../cases/n8n-nodes-typesafe-jev.md) | `integration` | n8n 工作流中的类型化问题 / Typed questions inside n8n workflows |
| [jev-factorio](../cases/jev-factorio-agent.md) | `game` | 目标、下一步动作与卡住检测 / Goal, next action and stuck detection |
| [Jev × LIBERO](../cases/jev-libero.md) | `game` | 分层选择意图、动作类别与输入 / Layered intent, motion-family and input choices |
| [jev-skip](../cases/jev-skip.md) | `other` | 字幕片段分类 / Caption-segment classification |
| [jev-leftpad](../cases/jev-leftpad.md) | `other` | 一个 Choice 决定空格数 / One Choice picks the number of spaces |
| [Jev Cloud Quiz](../cases/jev-cloud-quiz.md) | `other` | 三选一并展示概率 / Three-way choice with visible probabilities |

## 核验方法与边界 / Method and boundary

每个仓库都经 GitHub REST API 读取公开元数据（数字 ID、所有者、是否 fork/归档、默认分支最新提交），再在该固定提交上阅读 README、调用 Jev 的目标实现文件和 LICENSE，并从 `raw.githubusercontent.com` 抓取这些文件的原始字节计算 SHA-256；阅读用的副本与抓取字节的哈希做过比对。逐文件的读取范围记录在各 [receipt](evidence/README.md) 的 `inspected_scope`。本批链接检查见 [batch-2026-10-08-link-checks.json](batch-2026-10-08-link-checks.json)：16 个仓库根和 58 个固定版本原始文件均返回 HTTP 200；个别请求曾因网络瞬断重试。

Each repository’s public metadata (numeric ID, owner, fork/archive state, latest commit on the default branch) was read through the GitHub REST API. At that pinned commit the README, the targeted Jev call path and the LICENSE were read, and the raw bytes of those files were fetched from `raw.githubusercontent.com` for SHA-256 hashes; the copies that were read were compared against the captured hashes. Per-file scope is recorded as `inspected_scope` in each [receipt](evidence/README.md). The [link record](batch-2026-10-08-link-checks.json) covers 16 repository roots and 58 pinned raw files, all HTTP 200; some requests were retried after transient network failures.

**没有做的事 / Not done:** 没有安装或运行任何上游项目，没有调用 TypeSafe 或其他付费接口，没有复测作者的延迟、成本、准确率或演示。审阅由 Claude Code 按维护者指示完成，receipt 标明 `human_review: not_performed`，不虚构人工签字。作者数字在案例中一律标为作者自述。

No upstream project was installed or run, no TypeSafe or other paid API was called, and no author latency, cost, accuracy or demo claim was reproduced. Claude Code performed the review under the maintainer’s instruction; receipts state `human_review: not_performed` and no human sign-off is invented. Author figures are labelled author-reported throughout.

## 需要留意的身份与托管情况 / Identity and hosting notes

- **仓库更名 / Rename:** 线索表中的 `completedottech/jev-factorio-agent` 现解析为 `jevplays-games/jev-factorio-agent`，数字 ID 相同（1379060982），按现行地址收录一次。该仓库更新频繁，案例只对应固定提交。 / The lead `completedottech/jev-factorio-agent` now resolves to `jevplays-games/jev-factorio-agent` with the same numeric ID and is cataloged once at the current address. It changes frequently; the case describes the pinned commit only.
- **第三方托管 / Third-party hosting:** [Jev Logs](../cases/jevlogs.md) 经 Vercel AI Gateway 以 `typesafe-ai/jev` 调用；[Jev × LIBERO](../cases/jev-libero.md) 可经 OpenRouter 的 `typesafe/jev-1.13` 或 TypeSafe 直连；[jev-factorio](../cases/jev-factorio-agent.md) 另含 Cloudflare 客户端。按[治理规则](../GOVERNANCE.md)，能确认模型为 TypeSafe Jev 的第三方托管可以收录，案例中已写明提供方。 / Jev Logs calls `typesafe-ai/jev` through the Vercel AI Gateway; Jev × LIBERO can use OpenRouter’s `typesafe/jev-1.13` or the direct API; jev-factorio also has a Cloudflare client. Under the [governance](../GOVERNANCE.md), third-party hosting is eligible when the model is identifiably TypeSafe Jev, and each case names the provider.
- **Mock 与兼容接口 / Mocks and compatible endpoints:** jev-factorio 的 `MockJevClient`、go-jev 可指向的 tensai 本地服务器、neo4jev 无 Key 时的替代答案，都不作为调用 TypeSafe Jev 的证据。 / The jev-factorio `MockJevClient`, the tensai local server go-jev can target, and neo4jev’s stand-in answers without a key are not treated as evidence of a TypeSafe Jev call.

## 未进入公开目录 / Held out

- [knowlet/agentworld-web-simulator](https://github.com/knowlet/agentworld-web-simulator)（线索表中的 `knowlet/jev-agentworld-web-simulator`）：固定 README 写明演示用的决策模型是 `inception/mercury-decide:free`，只有代码默认端点指向 TypeSafe；在确认实际调用的是 TypeSafe Jev 之前保持 `under_review`。 / Its pinned README says the demo uses the decision model `inception/mercury-decide:free`, while only the code default points at TypeSafe; it stays `under_review` until an actual TypeSafe Jev call path is established.
- `maker-kk/todo-jev`：本轮读取仓库元数据后未能取得默认分支提交，未继续审阅，也不据此推定仓库状态。 / After reading repository metadata, the default-branch commit could not be retrieved this round; it was not reviewed further and no conclusion is drawn about the repository.
- CSV 分流表中其余只有模型分流的仓库仍未逐项核验。 / The remaining triage-only repositories in the CSV table are still unreviewed.

## 分类调整 / Taxonomy change

新增场景 `device`（桌面、手机与语音控制 / Desktop, mobile and voice control），收录 Jev Voice、Live Jev 和 Mobile Jev；此前已收录的案例没有移动。[案例格式](../schema/README.md)与 JSON Schema 已同步。没有修改或部署 jevforagents.com。

A new scenario, `device` (desktop, mobile and voice control), holds Jev Voice, Live Jev and Mobile Jev; no previously published case moved. The [case contract](../schema/README.md) and JSON Schema were updated. jevforagents.com was not edited or deployed.

[公开分类 / Published categories](../categories/README.md) · [候选台账 / Candidate ledger](CANDIDATES.md) · [证据规则 / Governance](../GOVERNANCE.md)
