# 核验记录 / Review receipts

每个已收录项目一个 JSON：公开身份、固定提交、文件 URL、读取时间、HTTP 状态、SHA-256、用途、限制和核验方式。
内容哈希针对原始下载字节；网页工具的文本解析结果不作为哈希输入。完整原始文件没有纳入本仓库。
`source_date` 为固定提交的 UTC 日期，不是首次发布日期。

Each admitted project has a JSON receipt recording public identity, pinned commit, file URLs, retrieval timestamps, HTTP observations, SHA-256 hashes, role, limitations and method.
Hashes describe downloaded raw bytes, not browser-rendered text. Complete source files are not redistributed here. Source dates are UTC dates of the pinned commits, not first-publication dates.

首版核验由 Codex 按负责人明确执行授权完成；未虚构人工签字，也未运行上游项目或付费模型。`source_reviewed` 不代表 `independently_tested`。文件的 `inspected_scope` 区分实际阅读范围与抓取范围。
Codex performed the first-release review under explicit owner instruction. No human sign-off, upstream execution or paid model run is claimed. `source_reviewed` does not mean `independently_tested`. `inspected_scope` distinguishes inspection from capture scope.

[来源与权利清单 / Attribution](../ATTRIBUTION.md) · [候选台账 / Candidate ledger](../CANDIDATES.md)
