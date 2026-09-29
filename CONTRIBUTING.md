# 投稿方式 / Contributing

## 中文

仓库属于个人账号 **FuturExplorator**，不代表 TypeSafe 官方。

1. 先搜索[案例目录](categories/README.md)和[候选台账](research/CANDIDATES.md)。同一项目只保留一条案例；README、子目录、演示或帖子不各算一个项目。可补充已有案例的证据。
2. 只有线索：使用 [Case suggestion Issue](https://github.com/FuturExplorator/awesome-jev-cases/issues/new?template=case.yml)，提交准确原帖或项目 URL、作者及 Jev 的具体用途。不要只给作者主页或搜索截图。
3. 完整投稿：复制[模板](templates/case.md)到 `cases/<slug>.md`，保持 `under_review`，填写[格式契约](schema/README.md)要求的中英内容与证据。不要把它加进公开分类。
4. 在 `research/evidence/<slug>.json` 记录审核范围、原始来源、固定提交或快照日期、哈希、作者声称、未验证项及第三方许可。不要提交凭据、私人会话或未经许可的完整第三方材料。
5. 运行 `python3 scripts/validate_catalog.py` 并提交 PR。维护者核对项目身份、实际 Jev 用途、来源、双语一致性及权利后，才能将状态改为 `verified` 并更新对应分类、首页计数与来源清单。

不能运行项目时可以明确标记 `source_reviewed`，不能虚称 `independently_tested`。测试模式、Mock、兼容接口或启发式回退不是调用 TypeSafe Jev 的证明。使用第三方托管的 TypeSafe Jev 可以收录，但必须说明提供方与证据。

提交即表示：你有权按 [MIT](LICENSE) 提供自己新增的原创部分；第三方材料须另列原始权利，不能代表第三方授予许可。无 CLA，首版不自动合并。纯线索无需编写中英文成稿，维护者可后续整理。

## English

This repository belongs to the personal account **FuturExplorator** and is not an official TypeSafe project.

1. Search the [catalog](categories/README.md) and [candidate ledger](research/CANDIDATES.md). Keep one case per project; its README, subdirectories, demos and posts are evidence, not separate projects. Extend existing evidence when appropriate.
2. For a lead, open a [Case suggestion Issue](https://github.com/FuturExplorator/awesome-jev-cases/issues/new?template=case.yml) with an exact source/project URL, author and concrete Jev role. Profiles and search screenshots are insufficient.
3. For a full submission, copy the [template](templates/case.md) into `cases/<slug>.md`, retain `under_review`, and follow the [contract](schema/README.md). Do not add it to public categories yet.
4. Add `research/evidence/<slug>.json`: review scope, primary URLs, pinned revision or snapshot date, hashes, author claims, unknowns and upstream rights. Do not include credentials, private sessions or unauthorized full third-party material.
5. Run `python3 scripts/validate_catalog.py` and open a PR. Only after identity, concrete Jev use, evidence, bilingual parity and rights review may the maintainer promote it to `verified` and update its category, homepage counts and attribution.

Source-only review may be labelled `source_reviewed`, never `independently_tested`. Mocks, compatible endpoints and heuristic fallback do not establish TypeSafe Jev execution. Hosting TypeSafe Jev through another provider is eligible if identified and evidenced.

By contributing, you confirm the right to license your original additions under [MIT](LICENSE). Third-party material needs separate attribution and permissions; you cannot license it on its owner's behalf. No CLA or automatic merge is used. Leads do not require a finished bilingual draft.
