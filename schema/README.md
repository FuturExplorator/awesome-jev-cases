# 案例格式 v1 / Case contract v1

一个项目一个 `cases/<slug>.md`，中英文同文件，公开目录只纳入 `verified`。
One project per file, both languages together; public indexes include only `verified`.

元数据字段定义见 [JSON Schema](case.schema.json)。 / See the [JSON Schema](case.schema.json) for metadata fields.

## 元数据 / Metadata

使用 YAML front matter 的简单子集：每行 `key: "JSON-escaped string"`，所有值都是字符串，不使用隐式日期、嵌套结构或多行标量。便于 Python 标准库直接检查，不引入依赖。
Use a flat YAML subset: one `key: "JSON-escaped string"` per line. All values are strings; no implicit dates, nested structures or multiline scalars. The offline checker uses only the Python standard library.

| 必填字段 / Required field | 约束 / Constraint |
| --- | --- |
| `slug` | unique lowercase kebab-case, same as filename / 唯一且与文件名相同 |
| `name_en`, `name_zh` | English and Chinese project names / 双语名称 |
| `project_url` | canonical HTTPS project identity / 规范项目地址 |
| `source_url` | exact primary evidence URL, not a profile / 准确原始证据 |
| `source_kind` | `github`, `x`, `official`, `article` |
| `author` | source author or explicitly identified repository owner / 作者或注明的仓库所有者 |
| `source_date` | `YYYY-MM-DD` or `UNKNOWN`; never guess / 不推测 |
| `source_date_kind` | `commit`, `published`, `unknown` |
| `last_checked` | actual check date / 实际核验日期 |
| `jev_relation` | `uses_typesafe`, `compatible_only`, `unknown` |
| `scenario` | `routing`, `browser`, `coding`, `guardrails`, `evaluation`, `integration`, `game`, `other` |
| `content_kind` | `application`, `integration`, `experiment`, `tutorial`, `resource` |
| `status` | `candidate`, `under_review`, `verified`, `withheld`, `rejected` |
| `claim_status` | `author_reported`, `source_reviewed`, `independently_tested` |
| `upstream_license` | actual observed terms, or `UNKNOWN`; do not infer / 实际条款或未知 |
| `evidence_file` | repository-relative review JSON path / 仓库相对核验记录路径 |

`source_revision` is required for GitHub sources: a 40-character commit SHA, with the source URL pinned to it. `source_date` then means the reviewed commit date, not the project launch date.
GitHub 来源必填 `source_revision`（40 位提交 SHA），来源 URL 必须固定到该提交；日期表示提交日期，不是项目发布日期。

`website_url` is optional and must be an actually checked case page, with a successful link record. Omit it when unknown; never derive it from the slug alone.
`website_url` 可选，必须有实际检查通过的对应详情页记录；未知则省略，不根据 slug 猜测。

## 正文与证据 / Body and evidence

按[模板](../templates/case.md)保留中文和英文各四节：项目、Jev 的输入/判断/输出、复现入口、证据与限制。两种语言的事实、测试状态与限制一致。原始来源放在文末，固定版本的文件优先。
Keep four sections in each language: overview, Jev inputs/decisions/outputs, reproduction entry, evidence/limitations. Facts, test status and limitations must match. List primary sources at the end, preferably pinned files.

审核 JSON 保留 `slug`、`project_url`、`checked_at`、`reviewer`、`review_method`、`claim_status`、`runtime_test`、`performance_test` 和 `sources`。`sources` 每项记录 URL、读取时间、状态、SHA-256 及读取范围；GitHub 案例还记录 repository ID、owner、公开状态、fork 状态、revision 和日期。首版 receipt 同时含中英文用途及限制说明。
Review JSON records identity, reviewer, method, check timestamp, claim/test status and a sources array. Each source records URL, timestamp, HTTP status, SHA-256 and inspected scope. GitHub cases also record repository ID, owner, visibility, fork status, revision and date. Initial receipts include bilingual role and limitation findings.

非 GitHub 来源必须保留完整可用正文的范围、原作者、准确帖文/文章日期（未知则注明），以及独立项目身份的证明；缺关键文本时保留 `withheld`。首版没有发布非 GitHub 来源案例，不以历史网站状态替代核验。
Non-GitHub sources require the complete available text scope, author, exact post/article date (or explicit unknown), and distinct project identity. Missing essential text means `withheld`. This release publishes no non-GitHub cases and does not inherit website statuses.

`verified` requires `uses_typesafe`, a completed source review, accessible primary evidence, duplicate checks, rights attribution and bilingual parity. It does not require an independent paid runtime test. `independently_tested` additionally requires an actual run record with environment, command, input, outputs and limitations.
`verified` 仅表示具体用途及来源核验；独立实测必须另有真实运行记录，不能从 README 中的作者测量推定。

## 校验边界 / Validation boundary

`python3 scripts/validate_catalog.py` checks structure, enums, duplicate identities, evidence consistency, index membership and local Markdown links. It is offline, does not mutate files and cannot promote a case. Editorial truth, translation quality and live link status still need review. Published HTTP observations are historical records, not a promise of future availability.
脚本只检查结构，不代替来源阅读、翻译审核或在线链接复核，也不会提升案例状态。HTTP 记录是核验时的快照，不保证未来持续可用。
