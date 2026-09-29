# Awesome Jev Cases

## Product Requirements Document

**Status:** v1.0 execution baseline — authorized by the owner; 11 source-reviewed cases delivered on 2026-09-29
**Repository:** `FuturExplorator/awesome-jev-cases`
**Website:** [jevforagents.com](https://jevforagents.com)

**Authoritative Chinese PRD:** [PRD.zh-CN.md](PRD.zh-CN.md). The Chinese version and the owner’s explicit decisions take precedence. See the [release review](research/RELEASE_REVIEW.md). The repository belongs to the personal account FuturExplorator.

## 1. Product definition

Awesome Jev Cases is a bilingual, source-backed catalog of real projects, integrations, experiments, and workflows that use TypeSafe Jev.

The repository is an open data and contribution project. The website remains the presentation layer for richer browsing, media, search, and detailed case pages.

The first release focuses on a reliable catalog. Discovery automation, model-assisted review, and scheduled synchronization are deliberately postponed until the catalog contract has been approved.

## 2. Goals

1. Give developers a trustworthy way to find concrete Jev use cases.
2. Preserve the source, date, author, project identity, and evidence status for every case.
3. Make each published case readable in Chinese and English.
4. Accept community contributions through GitHub Issues and Pull Requests.
5. Link useful cases to their detailed pages on [jevforagents.com](https://jevforagents.com).
6. Keep the catalog data portable so the website can consume verified entries later.

## 3. First-release scope

The first release will contain:

- the repository README and contribution rules;
- a reviewed case format;
- bilingual case documents;
- a source and evidence policy;
- an initial set reviewed individually under the owner’s explicit execution instruction;
- generated indexes only after the case format is stable.

The first release will not contain:

- automatic publication to the website;
- automatic daily discovery;
- mandatory AIsa or other paid providers;
- automatic acceptance of a case because its name contains `jev`;
- full copies of third-party READMEs, posts, images, or videos;
- the JevForAgents website application, payment system, or private operations code.

## 4. Users and contribution flow

### Reader

1. Open the README or a category page.
2. Choose a case by task, project type, or Jev role.
3. Read the Chinese or English explanation.
4. Open the original project and the detailed page on jevforagents.com.

### Contributor

1. Open an Issue or create a branch.
2. Provide the exact project or source URL.
3. Describe the task and Jev's actual role.
4. Add evidence and limitations.
5. Write the Chinese and English summaries in the same case file.
6. Open a Pull Request.

### Maintainer

1. Check project identity and duplicate records.
2. Check the original source and evidence completeness.
3. Distinguish author claims from independent verification.
4. Set the case status.
5. Merge only entries that meet the governance rules.

## 5. Case format

Each case is one Markdown file in `cases/`. Chinese and English live in the same file to prevent translation drift.

```md
---
slug: example-case
name_en: Example Case
name_zh: 示例案例
project_url: https://github.com/owner/repo
source_url: https://github.com/owner/repo
source_kind: github|x|official|article
jev_relation: uses_typesafe|compatible_only|unknown
scenario: routing|browser|coding|guardrails|evaluation|other
content_kind: application|integration|experiment|tutorial|resource
status: candidate|under_review|verified|withheld|rejected
claim_status: author_reported|source_reviewed|independently_tested
last_checked: 2026-09-29
---

# Example Case / 示例案例

## 中文

### 项目简介

### Jev 的作用

### 复现方式

### 证据与限制

## English

### Overview

### Jev's role

### Reproduction

### Evidence and limitations

## Sources

- Project:
- Original post or article:
- Official documentation:
```

The repository stores source URLs, short attributed excerpts when necessary, capture dates, and hashes. It does not republish complete third-party source documents by default.

## 6. Evidence and status contract

`candidate` means the project was discovered but its relationship to TypeSafe Jev is not confirmed.

`under_review` means the source material has been captured and is waiting for editorial review.

`verified` means the project identity, source, Jev relationship, and required links have been checked.

`withheld` means the project may be relevant but has missing source, media, identity, or reproduction evidence.

`rejected` means the source was checked and does not support inclusion.

Similarweb clicks, GitHub stars, search position, project names, and generated summaries may help prioritize research. They do not establish Jev usage or publication eligibility.

## 7. Website integration

The public repository may link to:

- the website home page: `https://jevforagents.com`;
- a detailed case page: `https://jevforagents.com/builds/<slug>` when that page exists;
- the website's submission page when it is ready.

The website may consume only cases whose status is `verified`. Candidate and review records remain outside the production catalog.

## 8. Repository layout

```text
README.md
PRD.md
GOVERNANCE.md
cases/
categories/
schema/
research/
scripts/
```

The initial draft contained no cases. The owner subsequently authorized execution; the first release includes 11 cases. The definitive [case contract](schema/README.md), [JSON Schema](schema/case.schema.json) and [template](templates/case.md) supersede the illustrative fields above.

## 9. License boundary decision

The maintainer selected MIT for original material this repository has the right to license: scripts, validation code, schemas, bilingual case descriptions, and editorial annotations. Third-party README text, posts, images, videos, and repository code are not relicensed here; retain their original URL, attribution, and applicable license information.

The [MIT license](LICENSE) and [third-party notice](THIRD_PARTY_NOTICES.md) were added before the first case files. Each published case links a pinned upstream license.

## 10. First-release acceptance criteria

- The repository is public and linked to jevforagents.com.
- The bilingual case format is documented.
- Governance defines evidence, status, review, and contribution rules.
- A case cannot become `verified` from a name match or traffic estimate alone.
- No duplicate project is created to fill a category count.
- The website sync boundary is explicit.
- License boundaries are visible before external contributions are invited.
- The owner’s execution instruction authorizes the first import; no status is inherited from the website.

## 11. Deferred roadmap

After the first catalog review:

1. Extend validation after observing maintenance needs; this release includes a manually invoked offline structural checker.
2. Add generated category indexes.
3. Package the existing prepare, capture, and review workflow as an optional CLI.
4. Generate Pull Requests instead of writing directly to `verified` data.
5. Add optional provider adapters, including AIsa, only after the no-provider workflow is usable.
6. Add a website synchronization workflow.

## 12. First-release execution record

22 candidate records represent 20 projects/leads after removing known aliases. Eleven passed source review; runtime and performance tests were not performed. Codex performed the source review under the owner’s instruction, without inventing a human sign-off. See the [candidate audit](research/CANDIDATES.md). Static indexes and the offline checker do not discover or publish content automatically. No paid AIsa calls, website edits, deployments or synchronization were performed.
