# 治理与证据规则 / Governance and evidence

## 维护权与范围 / Ownership and scope

仓库属于个人账号 **FuturExplorator**。维护者对范围、审核、状态、格式和与 [jevforagents.com](https://jevforagents.com) 的关系负责。本库不是 TypeSafe 官方目录。首版依据负责人明确授权及[中文 PRD](PRD.zh-CN.md)执行，中英文 PRD 冲突时以中文和最新明确决策为准。

The repository belongs to the personal account **FuturExplorator**. The maintainer owns scope, review, status, format and the website relationship. This is not an official TypeSafe directory. The owner's explicit instruction and Chinese PRD govern this release; latest explicit decisions take precedence over older drafts.

## 收录门槛 / Admission

每条案例必须具备：准确原始来源、可核对的项目与作者身份、具体 TypeSafe Jev 输入/判断/输出、双语说明、复现入口、来源日期、核验日期、限制与权利说明。第三方托管可以收录，但须证明是 TypeSafe Jev；仅同名、兼容接口、受其启发、Mock 或无 Key 的启发式模式不能证明实际接入。

Every case needs an exact primary source, identifiable project and author, concrete TypeSafe Jev inputs/decisions/outputs, bilingual explanations, reproduction entry, source/check dates, limitations and rights attribution. Third-party hosting is eligible when the model is demonstrably TypeSafe Jev. Names, compatibility, inspiration, mocks and keyless heuristics alone are insufficient.

同一项目只收录一次：规范化项目 URL，核对仓库 ID、重定向和别名。同一作者的不同仓库须有独立用途；同一仓库的子目录、README 与原帖只补充证据，不增加计数。历史网站状态不能替代本轮核验。

Count one case per project: normalize its URL and check repository IDs, redirects and aliases. Different repositories by one author need distinct purposes. Subdirectories, READMEs and posts supplement evidence instead of increasing counts. Historical website status cannot substitute for a fresh review.

## 状态与效果声明 / Status and claims

| Status | 中文 | English | 公开索引 / Indexed |
| --- | --- | --- | --- |
| `candidate` | 已发现，证据不全 | Discovered, incomplete evidence | No |
| `under_review` | 已有来源，审核未完成 | Source obtained, review incomplete | No |
| `verified` | 来源、身份、Jev 用途及链接已核对 | Source, identity, Jev role and links checked | Yes |
| `withheld` | 关键证据受阻或许可问题未解决 | Essential evidence blocked or rights unresolved | No |
| `rejected` | 来源不支持或重复别名 | Unsupported inclusion or duplicate alias | No |

`verified` **不等于独立实测成功**。`claim_status` 分为 `author_reported`、`source_reviewed`、`independently_tested`。公开案例至少完成来源审核；未运行必须明确写未运行。作者的基准、成本、准确率及速度不得升级为本库实测。

`verified` **does not mean independently demonstrated effectiveness**. `claim_status` separates author reports, source review and actual independent testing. Public cases must at least be source-reviewed. Record not-run explicitly; author benchmarks, costs, accuracy and speed remain author claims.

首版由 Codex 按负责人明确授权逐项审阅来源；receipt 标明审阅者及 `human_review: not_performed`，不虚构人工签字。后续投稿由维护者完成最终发布审核。校验脚本通过不能赋予 `verified`。

Codex performed the initial review under explicit owner authorization. Receipts identify the reviewer and `human_review: not_performed`; no human sign-off is invented. The maintainer controls subsequent publication. A successful checker cannot grant `verified`.

## 双语与来源 / Bilingual content and sources

双语放在同一文件，事实、限制和测试范围一致，不补造依赖、架构、性能或命令。准确仓库/文章/帖子是来源；主页、搜索片段、流量与 stars 不足以通过。GitHub 来源固定提交并记录读取范围和哈希。原始材料变更应重新审核。

Both languages share one file and the same facts, limits and test scope. Do not invent dependencies, architecture, performance or commands. Use exact repository/article/post URLs, not profiles, snippets, traffic or stars. Pin GitHub sources and record scope and hashes. Re-review changed sources.

## 投稿与撤回 / Contributions and withdrawal

通过 [Issue 或 PR](CONTRIBUTING.md)，按[格式](schema/README.md)投稿。维护者可合并 `under_review` 文件但不加公开目录。发现错误、失效来源或重复，可降级并同步移出目录、调整计数、记录原因；不删除审核历史掩盖问题。

Use [Issues or PRs](CONTRIBUTING.md) and the [case contract](schema/README.md). An `under_review` file may be merged without indexing. Errors, lost sources and duplicates may cause demotion: remove the index entry, update counts and preserve the audit reason.

## 自动化与网站 / Automation and website

首版只有手动运行的离线校验，无 AIsa、定时发现、自动发布或网站同步，不修改或部署网站。后续工具可去重、检查链接或准备待审核 PR，不能自行提升状态。网站将来只同步 verified，并继续完成自身来源、链接和媒体实播检查；仓库核验不是网站发布许可。

This release has a manually invoked offline checker, with no AIsa, scheduled discovery, automatic publication or website synchronization. The website is not modified or deployed. Future helpers may deduplicate, check links or prepare review PRs, but cannot promote status automatically. Future website synchronization must retain verified-only admission and its own source, link and media-playback gates; repository review is not website-release approval.

## 许可证 / License

[MIT](LICENSE) 仅覆盖本库有权许可的原创内容，第三方材料保留原有权利。遵循[第三方来源说明](THIRD_PARTY_NOTICES.md)；引用或翻译不赋予完整原文、图片、视频或上游代码的权利。

[MIT](LICENSE) covers original material this repository has the right to license. Third parties retain their rights; follow the [third-party notice](THIRD_PARTY_NOTICES.md). Citation or translation does not confer ownership of full source text, media or upstream code.
