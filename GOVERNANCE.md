# Governance

## Purpose

`awesome-jev-cases` is a source-backed catalog. The repository values evidence, clear attribution, useful reproduction details, and honest uncertainty over the number of entries.

## Maintainer

The repository owner is the initial maintainer and has final responsibility for:

- the catalog scope;
- the evidence policy;
- publication status;
- schema changes;
- the relationship with [jevforagents.com](https://jevforagents.com).

The maintainer may request more evidence, keep a relevant record withheld, or remove a record that no longer meets the source policy.

## Case admission rules

Every case must have:

1. a specific project, post, article, or official page URL;
2. enough primary text to establish what the project is;
3. a concrete explanation of what Jev does;
4. a project identity that is distinct from similarly named repositories;
5. a Chinese and an English summary;
6. limitations and claim status;
7. a link that a reader can open without relying on private access.

An X profile, search result, project name, star count, Similarweb row, or generated summary is not sufficient evidence by itself.

## Source and attribution policy

- Preserve the original source URL, author, date, and relevant source scope.
- Keep author-reported metrics labelled as author-reported.
- Label independent tests separately from source claims.
- Prefer short attributed excerpts and links over copying full third-party documents.
- Do not upload third-party images or videos unless their use and license are clear.
- Do not add a GitHub link unless the repository is public and matches the specific case.
- Do not create a second record merely to fill a category or keyword count.

## Status policy

```text
candidate       discovered, evidence not yet complete
under_review    evidence captured, editorial review pending
verified        source, identity, Jev relationship, and links checked
withheld        relevant lead with missing or blocked evidence
rejected        source checked and inclusion unsupported
```

Only `verified` entries may be included in generated public indexes or synchronized to the website.

## Bilingual policy

- Chinese and English are kept in the same case file.
- The two versions must describe the same evidence and limitations.
- Translation may improve readability but may not add metrics, architecture, dependencies, or reproduction steps absent from the source.
- The original source remains the authority for quotations and claims.
- If a translation is uncertain, preserve the original term and explain the uncertainty.

## Pull Requests

A case Pull Request should contain:

- one project or one clearly scoped source;
- the source URL and project URL;
- the proposed case file;
- evidence and capture date;
- a note about whether claims are author-reported or independently tested;
- no unrelated formatting or catalog changes.

The maintainer may merge a contribution as `under_review` before it becomes `verified`.

## Automation boundary

Automation may:

- normalize URLs;
- find duplicate projects;
- capture public source text;
- calculate hashes;
- prepare a review report;
- open a Pull Request.

Automation may not:

- publish directly to `verified`;
- invent source text or metrics;
- infer Jev usage from a project name;
- replace missing media with unrelated media;
- bypass a failed evidence or link check.

Provider-specific automation is optional. The base contribution path should work without AIsa or another paid provider.

## Website relationship

The website may link to this repository and may link verified cases back to detailed pages on `jevforagents.com`. The repository does not depend on the website being online to remain useful.

## License boundary

The maintainer selected MIT for original material this repository has the right to license: code, scripts, schemas, bilingual case descriptions, and editorial annotations. Third-party source materials retain their original rights and licenses.

The repository will not claim to relicense third-party README text, posts, images, videos, or source code. An MIT license file and a third-party attribution notice will be added before the first case import.
