# 增补审核与下一批选题 / Follow-up review and next topics

审核日期 / Reviewed: 2026-09-30 (UTC)

## 本轮交付 / This update

从首版的 4 个 `under_review` 项目中，3 个独立浏览器仓库完成固定版本来源、TypeSafe Jev 调用路径、仓库身份及许可证核对，进入公开目录；[TypeSafe 官方 skills](https://github.com/typesafe-ai/skills) 保留为 `withheld`，因为它是通用开发指引，当前没有一个独立实现的 Jev 场景可写成案例。目录从 11 条增至 **14 条**，全部 `verified` / `source_reviewed`。3 个新仓库的数字 ID 分别为 1374194684、1375500090、1373227372；同名不等于同项目。

Three distinct browser repositories from the first release's review queue passed pinned source, concrete Jev call-path, identity and license checks. The official [TypeSafe skills repository](https://github.com/typesafe-ai/skills) remains `withheld` as a general development guide without a distinct implemented Jev case established here. The public catalog grows from 11 to **14** `verified` / `source_reviewed` cases. Numeric repository IDs distinguish the three projects despite similar names.

审核仅阅读公开来源及特定实现代码，没有安装项目、调用付费模型或复测速度、正确率及安全性。源文件哈希及读取范围见各 [receipt](evidence/README.md)。许可证只适用于各上游自己的材料；本库只提供链接和原创双语整理。

The review read primary sources and targeted code, without installing projects, calling paid models or reproducing speed, accuracy or security claims. Source hashes and inspected scopes are in the receipts. Upstream licenses remain attached to upstream material; this catalog links sources and publishes original bilingual editorial summaries.

本轮新增来源和候选链接的检查记录在 [follow-up-link-checks.json](follow-up-link-checks.json)：22 条不同外链中 20 条无登录 GET 返回 HTTP 200；另外 2 条 GitHub 候选仓库的 Python 请求遇到 TLS EOF，随后经 Codex 内置浏览器打开并确认仓库身份，未伪称其 HTTP 检查通过。目录结构检查与 7 项校验器测试通过。 / The [link record](follow-up-link-checks.json) covers 22 distinct new external links: 20 returned HTTP 200 to unauthenticated GET. Two candidate repositories produced a Python TLS EOF but were opened in Codex's built-in browser and identified there; no HTTP pass is imputed. Catalog validation and seven validator tests passed.

## 下一批值得核验的内容 / Next review queue

这 4 项仅完成原始仓库可访问性、公开身份和项目主题初筛，状态为 `under_review`；尚未满足公开门槛。优先级考虑读者任务多样性与可解释的 Jev 判断环节，不依据 Star 数或搜索曝光推定真实性。

These four have only passed primary-repository accessibility, public-identity and topic triage. They remain `under_review`, outside the published index. Priority reflects task diversity and inspectable Jev decisions, not popularity as proof.

| 优先级 / Priority | 候选 / Candidate | 值得整理的读者问题 / Reader task | 入库前要核对 / Review gap |
| --- | --- | --- | --- |
| 1 | [Peu77/JevFind](https://github.com/Peu77/JevFind) | 如何用 Jev 找代码文件、行段和片段？ / How can Jev help find relevant code locations? | 固定 README 与调用代码，确认候选文件输入、判断、返回片段及与现有编码案例的区别；许可证原文。 / Pin README and call path; inspect candidate inputs, decisions, returned snippets, distinction from existing coding cases and license. |
| 2 | [AgriciDaniel/jev-seo](https://github.com/AgriciDaniel/jev-seo) | Jev 在站点 SEO 审核、报告中究竟判断什么？ / What does Jev judge in a site audit and report? | 核对抓取、规则、Jev 判断和报告各自职责；性能与覆盖数字保持作者声称；确认 PDF/XLSX/MD 入口及许可证。 / Separate crawling, rules, Jev judgment and report duties; keep metrics author-reported; inspect report formats and license. |
| 3 | [epergaboni/jevseo](https://github.com/epergaboni/jevseo) | 另一套 SEO/AEO/GEO 类型化判断与上项有何区别？ / How does another typed SEO/AEO/GEO approach differ? | 使用仓库 ID 与实现流程证明它独立于 AgriciDaniel/jev-seo；固定 API 调用、示例、许可证。 / Prove distinct identity and workflow; pin API call, example and license. |
| 4 | [minorun365/jev-cloud-quiz](https://github.com/minorun365/jev-cloud-quiz) | 初学者如何看到 Jev 的分类与概率输出？ / How can beginners observe a Jev classification and probabilities? | 只写教学演示，不称生产云 Agent；固定代码、输入选项、概率展示及 Apache-2.0 许可证。 / Frame as a teaching demo, not a production cloud agent; pin code, options, probability display and license. |

这几项原始仓库均已打开并用 GitHub 公开元数据确认独立仓库身份，尚未完成案例级来源审核；准确缺口见 [候选台账](CANDIDATES.md)。同类 SEO 两项若核验通过，可以作为不同实现分别收录，但不得把一个项目拆成多个案例。浏览器分类目前已有 5 条，下一批先补其他任务类型。

These primary repositories were opened and their distinct public identities checked through GitHub metadata, but case-level review is pending; see the [candidate ledger](CANDIDATES.md). The two SEO repositories may become separate cases if their workflows pass review, while one repository should not be split into multiple cases. Browser execution already has five entries, so other tasks take priority next.

## 需要负责人决定 / Owner decision

含限制性附加条款的 [SkillRanker](https://github.com/Dicklesworthstone/skillranker) 是否允许在仓库建立**仅链接的候选索引**？目前仍为 `withheld`，不在公开案例目录，也不声明为标准 MIT。这个决定不影响上述四项的逐项审核。

Should projects with restrictive riders such as [SkillRanker](https://github.com/Dicklesworthstone/skillranker) receive a **link-only lead entry** in a public candidate index? It remains `withheld`, outside the case catalog, and is not described as standard MIT. This policy decision does not block review of the four queued repositories.
