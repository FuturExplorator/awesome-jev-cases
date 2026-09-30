# CSV 仓库专项审阅 / CSV repository review

审核日 / Reviewed: 2026-09-30 UTC

本轮从用户提供的 Similarweb GitHub 落地页表继续整理：297 条 URL 先归一为 245 个仓库根，按 GitHub 数字仓库 ID 再合并 3 个更名或转移别名。确认 237 个可读取的独立仓库身份；另 5 个仓库根本轮不可读取，不能推定不存在。完整映射、作者描述线索、固定 README 入口和 Jev 分流见 [CSV 仓库目录](CSV_REPOSITORIES.md)。

This batch continued the user-supplied Similarweb export: 297 landing URLs normalized to 245 repository roots. Numeric GitHub IDs merged three rename/transfer aliases. There are 237 readable distinct identities and five unavailable roots, which are not presumed nonexistent. See the [CSV directory](CSV_REPOSITORIES.md) for mapping, owner-provided descriptions, pinned README entry points and Jev triage.

## 本轮新增公开案例 / Newly published

| 案例 / Case | 是什么、怎么用 / What and how | Jev 的作用 / Jev role |
| --- | --- | --- |
| [Elixir/OTP 集成](../cases/jev-elixir-otp.md) | 在 GenServer 中接收工单判断并按回调分流 / Integrate typed decisions into GenServer callbacks | 工单类型、严重度、安全性 / Issue kind, severity and security |
| [语音浏览器](../cases/jev-voice-browser-moritzkremb.md) | 本地语音控制页驱动另一浏览器窗口 / Local voice control of a separate browser | 意图、元素目标、完成度与危险性 / Intent, target, completeness and risk |
| [Pi 工具门控](../cases/pi-jev-y0usaf.md) | Pi 扩展，默认先提示风险 / Pi extension with warning-first default | 调用前风险与 bash 输出判断 / Pre-call risk and bash-output judgments |
| [Jev Chat](../cases/jev-chat-w3cj.md) | 本地聊天界面调用实际工具 / Local chat interface invoking real tools | 意图、工具与参数候选选择 / Intent, tool and argument selection |
| [Snake Jev](../cases/snake-jev-siroccomask.md) | 每游戏 tick 的九项判断实验 / Nine judgments per game tick | 三方向碰撞与食物进展 / Collision and food progress for three moves |
| [jev-seo](../cases/jev-seo-agrici.md) | 网站抓取、规则检查和多格式报告 / Site crawl, rules and multi-format reports | 页面质量与意图的类型化判断 / Typed page-quality and intent judgments |
| [Jev Search](../cases/jev-search-superagents.md) | Search1API 多来源检索与排序 / Multi-source retrieval and ranking | 查询/来源选择及结果相关性 / Query/source choice and result relevance |

以上 7 个均核对固定提交的 README、Jev 调用与下游处理、项目身份及 MIT 原始许可证，保留 SHA-256 [证据回执](evidence/README.md)。这是 `verified` / `source_reviewed`，不是 `independently_tested`：没有运行上游应用、核验作者性能指标或代用户调用 Search1API、DataForSEO、AIsa。公开目录共 27 个独立项目。

Each of the seven has a pinned README, Jev call/consumer path, identity and original MIT license review with SHA-256 [receipts](evidence/README.md). `verified` / `source_reviewed` does not mean `independently_tested`: upstream applications, author performance claims, Search1API, DataForSEO and AIsa were not run. The public catalog has 27 distinct projects.

## 未进入公开目录 / Held out

- 221 个已确认身份的 CSV 仓库仍只有 Jev 分流或原始 README 入口，尚未逐个核对调用、复现和权利，不计入公开案例。 / 221 identifiable CSV repositories have triage or a README entry point but no complete individual admission review.
- [opaielsheikh/jev-polymarket-arb](https://github.com/opaielsheikh/jev-polymarket-arb)、[vlad-terin/jev-use](https://github.com/vlad-terin/jev-use)、[hungdangit95/IT-Book](https://github.com/hungdangit95/IT-Book)、[auggie246/dsh-jev](https://github.com/auggie246/dsh-jev)、[enderzcx/spire-jev](https://github.com/enderzcx/spire-jev) 本轮无法读取原始仓库。 / Five primary repositories were unavailable in this review.
- 既有[候选台账](CANDIDATES.md)还有 3 个 `under_review`、6 个 `withheld`、3 个 `rejected` 记录；`rejected` 包含重复别名和非 TypeSafe 复刻项目，不代表所有待审项目无价值。 / The existing candidate ledger has three under review, six withheld and three rejected records; rejected includes aliases and a non-TypeSafe replica.
- 模型将 25 次调用判为汇总索引、40 次判为兼容/替代实现、34 次判为疑似无关。这是按**调用**统计的初筛信号，含三个别名调用，不能代替人工排除决定。 / The model labeled 25 calls indexes, 40 alternatives and 34 apparently unrelated. These call-level signals include three aliases and do not themselves reject a project.

Jev 批量分流返回 644,594 输入 token、47,642 输出 token；按 [TypeSafe 公开价格](https://typesafe.ai/blog/introducing-system-one-models-and-jev)估算约 $0.027073，另有一次 526 输入/86 输出 token 试跑。具体费用以账单为准。模型只用于分流候选，没有自动发布。 / Batch triage returned 644,594 input and 47,642 output tokens, estimated at about $0.027073 from the linked public rate, plus one excluded 526-input/86-output trial. Actual billing may differ. The model only routed leads; it did not publish cases.

本轮调整了场景目录，增加 `integration` 与 `game`，并把已收录的 Home Assistant 项目移至集成类；没有修改或部署 jevforagents.com。 / The scenario taxonomy now includes `integration` and `game`, and the existing Home Assistant case moved to integrations. jevforagents.com was not edited or deployed.

仍需负责人决定是否允许在**单独的链接索引**记录带附加限制的 [SkillRanker](CANDIDATES.md)，以及未来是否另开“兼容/替代实现”研究目录。按当前 PRD，它们均不进入 TypeSafe Jev 公开案例目录。 / The owner may decide later whether SkillRanker with its extra license rider belongs in a separate link index, and whether alternatives deserve a distinct research directory. Neither enters the current TypeSafe Jev case catalog.
