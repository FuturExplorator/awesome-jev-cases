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

[来源与权利清单 / Attribution](../ATTRIBUTION.md) · [候选台账 / Candidate ledger](../CANDIDATES.md)
