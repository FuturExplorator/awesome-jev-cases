# 核验记录 / Review receipts

每个已收录项目一个 JSON：公开身份、固定提交、文件 URL、读取时间、HTTP 状态、SHA-256、用途、限制和核验方式。
内容哈希针对原始下载字节；网页工具的文本解析结果不作为哈希输入。完整原始文件没有纳入本仓库。
`source_date` 为固定提交的 UTC 日期，不是首次发布日期。

Each admitted project has a JSON receipt recording public identity, pinned commit, file URLs, retrieval timestamps, HTTP observations, SHA-256 hashes, role, limitations and method.
Hashes describe downloaded raw bytes, not browser-rendered text. Complete source files are not redistributed here. Source dates are UTC dates of the pinned commits, not first-publication dates.

首版核验由 Codex 按负责人明确执行授权完成；未虚构人工签字，也未运行上游项目或付费模型。`source_reviewed` 不代表 `independently_tested`。文件的 `inspected_scope` 区分实际阅读范围与抓取范围。
Codex performed the first-release review under explicit owner instruction. No human sign-off, upstream execution or paid model run is claimed. `source_reviewed` does not mean `independently_tested`. `inspected_scope` distinguishes inspection from capture scope.

2026-09-30 的增补批次沿用同一核验范围：3 个独立浏览器仓库完成来源、实现与权利核对，未运行上游项目或付费模型。 / The 2026-09-30 follow-up applies the same review boundary to three distinct browser repositories; no upstream project or paid model was run.

本次网站与 CSV 导入审核另增加 6 个独立仓库：4 个与网站目录匹配、1 个网站详情页失效但原始仓库可核验、1 个仅来自 CSV 线索。全部仅完成源码与权利核验；未执行上游项目。 / This website/CSV intake adds six distinct repositories: four matched site records, one had a dead site detail page but reviewable primary repository, and one came from the CSV lead alone. All received source and rights review only; no upstream project was run.

随后 CSV 专项审阅新增 7 个独立仓库，覆盖 Elixir/OTP、语音浏览器、Pi 工具门控、工具聊天、游戏实验、SEO 审核和搜索排序。每条记录包含固定版本 README、目标调用路径及 LICENSE 的原始字节哈希；只核对来源和代码，未运行上游项目。Jev 对全部候选的辅助分类另见[仓库分流表](../CSV_REPOSITORIES.md)，模型分数不属于这些案例的核验证据。 / The later CSV batch adds seven distinct repositories across OTP, voice browsing, Pi gating, tool chat, a game experiment, SEO auditing and search ranking. Each receipt hashes pinned README, targeted code and LICENSE bytes. Upstream projects were not run. The [repository triage](../CSV_REPOSITORIES.md) is separate from case evidence.

2026-10-08 批次新增 16 个独立仓库，覆盖语音与桌面控制、Android 手机、Ableton Live、代码搜索、lint、上下文压缩、SEO、日志分流、图导航、Go SDK、n8n、Factorio、LIBERO 仿真等用途。审阅由 Claude Code 按维护者指示完成：经 GitHub REST API 核对仓库身份，在固定提交上阅读 README、目标调用路径与 LICENSE，并记录原始字节哈希；未运行上游项目或付费模型。详见[本批审阅报告](../BATCH_2026-10-08_REVIEW.md)。 / The 2026-10-08 batch adds sixteen distinct repositories across voice and desktop control, Android, Ableton Live, code search, linting, context compaction, SEO, log triage, graph navigation, a Go SDK, n8n, Factorio and LIBERO simulation. Claude Code performed the review under the maintainer’s instruction: identity through the GitHub REST API, pinned README, targeted call path and LICENSE read, raw-byte hashes recorded; no upstream project or paid model was run. See the [batch review](../BATCH_2026-10-08_REVIEW.md).

[来源与权利清单 / Attribution](../ATTRIBUTION.md) · [候选台账 / Candidate ledger](../CANDIDATES.md)
