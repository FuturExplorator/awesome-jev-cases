# 网站与 Similarweb 线索整理 / Website and Similarweb intake

本页保留目录增至 20 条时的审核快照。后续 CSV 原始仓库核验已将目录增至 27 条，并提供[完整去重分流和使用入口](CSV_REPOSITORIES.md)。 / This page preserves the 20-case intake snapshot. Later CSV repository review brought the catalog to 27; see the [deduplicated triage and usage entry points](CSV_REPOSITORIES.md).

本次整理把本地 `Jev-For-Agents/data/build-records.json` 与用户提供的 Similarweb `github.com` 落地页 CSV 作为**候选线索**，再到各项目原始仓库核验。网站原有 `verified`、页面文案和落地页访问量都没有自动继承为本仓库的案例证据。完整的本地比对结果见 [source-inventory.json](source-inventory.json)；该文件只存网站来源指针、GitHub 仓库身份和匹配状态，不公开 CSV 中的访问量或第三方素材。

We used the local website catalog and the user-supplied Similarweb GitHub landing-page export as **leads**, then reviewed primary repositories. Website statuses, editorial copy and traffic estimates were not inherited as case evidence. The [source inventory](source-inventory.json) contains only source pointers, repository identities and match hints, not CSV traffic metrics or third-party media.

| 输入 / Input | 整理结果 / Result |
| --- | ---: |
| 网站记录 / Website records | 487 |
| 网站规范 slug / Canonical website slugs | 478 (9 aliases) |
| 网站链接的不同 GitHub 仓库 / Distinct website GitHub repositories | 244 |
| CSV 落地页 / CSV landing-page rows | 297 |
| CSV 归一化后的不同 GitHub 仓库 / Distinct CSV GitHub roots | 245 |
| CSV 与网站仓库交集 / CSV–website repository overlap | 37 |
| 当前 20 个公开案例中与 CSV 仓库相交 / Published cases matched to CSV roots | 9 |

这些数字的分母不同，不能相加为独立案例数。网站规范 slug 不等同于独立项目：例如 `vercel-labs/json-render` 在网站中对应两个不同 slug，仍须先核对其项目关系。CSV 中也有 GitHub 个人页、话题页和同仓库文件页；访问量只用于决定审核优先级，不用于证明 Jev 用途或效果。两个来源分别保留 SHA-256 以便日后复核输入版本。

These counts have different denominators and cannot be summed into distinct cases. A canonical website slug need not equal an independent project; for example, two site slugs point to `vercel-labs/json-render`. The CSV also contains profile/topic and file URLs. Traffic estimates prioritize review but do not prove Jev usage or effectiveness. Input hashes preserve the reviewed source versions.

## 本轮进入公开目录 / Admitted this pass

| 独立项目 / Project | 线索 / Lead | 核对的 Jev 用途 / Reviewed Jev role |
| --- | --- | --- |
| [Browser Use Jev Ultrafast](../cases/browser-use-jev-ultrafast.md) | 网站及原始仓库 / Site and repository | 浏览器操作选择 / Browser action selection |
| [fast-jev-compaction](../cases/fast-jev-compaction-tamara-tran.md) | 网站及原始仓库 / Site and repository | 工具调用与结果保留判断 / Tool-call and result retention |
| [jev-router by gargpratyush](../cases/jev-router-gargpratyush.md) | 网站及原始仓库 / Site and repository | 模型档位选择 / Model tier selection |
| [HA-Jev](../cases/ha-jev-home-assistant.md) | 网站及原始仓库 / Site and repository | 家庭状态类型化判断 / Typed home-state judgments |
| [Jev Review](../cases/jev-review-devagrawal.md) | 网站及原始仓库 / Site and repository | 代码审查证据与风险筛选 / Code-review evidence and risk selection |
| [Jev Arena](../cases/jev-arena-nanmicoder.md) | CSV 及原始仓库 / CSV and repository | 评论分类对比 / Comment-label comparison |

前四个网站详情页本轮可访问并能对应到原始仓库。Jev Review 的旧网站详情页返回 404，但原始仓库与代码可独立核验，所以案例只链接仓库。Jev Arena 未找到对应的网站项目记录。六个案例均固定源代码版本、审阅实现和许可证，并存有[核验回执](evidence/README.md)；未运行上游项目，性能和准确率仍是作者声称。

The first four site detail pages resolved to their primary repositories. Jev Review's old site page returned 404, but its repository and code were independently reviewable, so the case links the repository only. No website record matched Jev Arena. All six have pinned source, implementation and license receipts. Upstream projects were not executed; performance and accuracy remain author claims.

## 暂不发布 / Held out

- [NanoJev](https://github.com/TianyuCodings/NanoJev) 自述是 Jev 的复刻模型，不是调用 TypeSafe Jev 的应用案例；即使 CSV 有较多落地页流量也不能改变项目身份。 / The repository calls itself a Jev replica, rather than an application using TypeSafe Jev.
- [awesome-jev](https://github.com/yibie/awesome-jev) 等索引仓库可继续提供线索，但索引本身不是 Jev 实现案例。 / Curated indexes are useful leads, not implementations themselves.
- 网站别名和同仓库多 slug 先按仓库身份去重；未核对原帖/代码/权利的条目继续保持待审核。 / Site aliases and same-repository slugs are deduplicated; entries without reviewed posts, implementation and rights remain leads.
- 已有 [4 个 under_review、6 个 withheld](CANDIDATES.md) 项目仍按原状态保留；本次没有用网站或 CSV 线索越过证据门槛。 / Four under-review and six withheld entries keep their status; website and CSV leads do not override the evidence gate.

下一批优先审核已有独立原始仓库且用途不同的 [JevFind](https://github.com/Peu77/JevFind)、[jev-seo](https://github.com/AgriciDaniel/jev-seo)、[jevseo](https://github.com/epergaboni/jevseo) 和 [jev-cloud-quiz](https://github.com/minorun365/jev-cloud-quiz)。需要逐一固定版本、核对实际 Jev 调用和许可证，再决定是否发布。网站本地项目及 jevforagents.com 均未修改或部署。

The next batch should review JevFind, the two distinct SEO repositories and jev-cloud-quiz against pinned code, actual Jev calls and licenses before admission. Neither the local website project nor jevforagents.com was changed or deployed.
