---
slug: "neo4jev"
name_en: "neo4jev"
name_zh: "neo4jev：Jev 图导航演示"
project_url: "https://github.com/jexp/neo4jev"
source_url: "https://github.com/jexp/neo4jev/blob/d157bbe496eb91813475156942bef1c6badfb342/README.md"
source_kind: "github"
author: "jexp"
source_date: "2026-09-18"
source_date_kind: "commit"
last_checked: "2026-10-08"
source_revision: "d157bbe496eb91813475156942bef1c6badfb342"
jev_relation: "uses_typesafe"
scenario: "routing"
content_kind: "experiment"
status: "verified"
claim_status: "source_reviewed"
upstream_license: "MIT"
evidence_file: "research/evidence/neo4jev.json"
---

# neo4jev / neo4jev：Jev 图导航演示

## 中文

### 项目简介

jexp 发布的演示（LICENSE 署名 Michael Hunger）：在 Neo4j 图上一跳一跳地导航，用结构化决策代替自由文本生成。默认连接公开的 Neo4j Companies KG 示例库；README 说明标签、关系类型和属性名都在运行时内省得到，没有硬编码。

### Jev 的具体作用

固定的 `src/neo4jev/navigator.py` 使用 `typesafe_sdk` 的 `system_one`：在每个访问到的节点，把出边（关系类型、关系属性、目标节点的标签与属性）作为 Choice 选项，同一次调用里附带一个 Noul 问题“目标是否已达到”，因此每一跳只需一次往返。README 说明代码对返回的概率做 top-k / 截断选择以实现束搜索，以对数概率之和给路径排序，并用 `neo4j-viz` 可视化结果。

### 如何复现

需要 Python 3.12+ 和 `uv`：`uv sync`，复制环境模板并填写 Neo4j 连接信息与 `TYPESAFE_API_KEY`，之后按固定 README 运行 `notebooks/` 中的笔记本或 `app/streamlit_app.py` 的 Streamlit 界面。README 列出自由文本目标、指定目标节点、路径意图三种目标模式。

### 证据与限制

已核对固定 README、`navigator.py` 和 MIT LICENSE；未安装、未连接 Neo4j、未调用付费接口。README 说明没有 `TYPESAFE_API_KEY` 时每次调用仍会尝试、失败原样显示，后续流程用明确标注的替代答案继续；那部分输出不是 Jev 的结果。导航质量和路径正确性未评估。

## English

### Overview

A demo published by jexp (the LICENSE names Michael Hunger) that navigates a Neo4j graph one hop at a time with structured decisions instead of free-text generation. It targets the public Neo4j Companies KG instance by default; the README says labels, relationship types and property names are discovered by introspection at run time rather than hardcoded.

### Jev's specific role

Pinned `src/neo4jev/navigator.py` uses `system_one` from `typesafe_sdk`: at each visited node the outgoing relationships (type, properties, target label and properties) become Choice options, and a Noul question, “has the goal been reached?”, rides in the same call, so each hop is one round-trip. The README says top-k/cutoff selection over the returned probabilities implements a beam search, paths are ranked by summed log-probabilities, and results render with `neo4j-viz`.

### Reproduction

Requires Python 3.12+ and `uv`: `uv sync`, copy the environment template and fill in Neo4j credentials and `TYPESAFE_API_KEY`, then follow the pinned README to run the notebooks under `notebooks/` or the Streamlit UI in `app/streamlit_app.py`. The README lists three goal modes: free-text goal, explicit target node and path intent.

### Evidence and limitations

The pinned README, `navigator.py` and the MIT license were reviewed. Nothing was installed, Neo4j was not connected and no paid call was made. The README says that without `TYPESAFE_API_KEY` each call is still attempted, its failure is shown verbatim and the pipeline continues on explicitly labelled stand-in answers; that output does not come from Jev. Navigation quality and path correctness were not assessed.

## Sources / 来源

- [项目仓库 / Repository](https://github.com/jexp/neo4jev)
- [固定版本 README / Pinned README](https://github.com/jexp/neo4jev/blob/d157bbe496eb91813475156942bef1c6badfb342/README.md)
- [实现 / Implementation: src/neo4jev/navigator.py](https://github.com/jexp/neo4jev/blob/d157bbe496eb91813475156942bef1c6badfb342/src/neo4jev/navigator.py)
- [原始许可证 / Upstream license](https://github.com/jexp/neo4jev/blob/d157bbe496eb91813475156942bef1c6badfb342/LICENSE)
- [核验记录 / Review receipt](../research/evidence/neo4jev.json)
