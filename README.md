# [Awesome Jev Cases](https://jevforagents.com)

> **43 个逐一核对过来源的 [TypeSafe Jev](https://typesafe.ai/) 真实项目**：语音控制电脑、手机与浏览器代理、编码工具、SDK、游戏和机器人仿真。每条都写清 Jev 具体判断了什么、怎么开始复现、哪些只是作者自述。
>
> **43 source-reviewed real projects built on [TypeSafe Jev](https://typesafe.ai/)**: voice control, phone and browser agents, coding tools, SDKs, games and robot simulation. Every entry states what Jev actually decides, how to start reproducing it, and which claims are only the author’s.

![cases](https://img.shields.io/badge/cases-43-2ea44f) ![bilingual](https://img.shields.io/badge/docs-%E4%B8%AD%E6%96%87%20%2B%20English-orange) ![license](https://img.shields.io/badge/license-MIT-blue) ![contributions](https://img.shields.io/badge/contributions-welcome-brightgreen)

[项目网站 / Website](https://jevforagents.com) · [中文说明](#中文说明) · [English](#english) · [案例目录 / Case directory](#案例目录--case-directory) · [分类 / Categories](categories/README.md) · [投稿 / Submit a case](https://github.com/FuturExplorator/awesome-jev-cases/issues/new?template=case.yml)

## 中文说明

这是由个人账号 **FuturExplorator** 独立维护的中英双语 [TypeSafe Jev](https://typesafe.ai/) 案例库，不是 TypeSafe 官方目录。Jev 是只输出类型化判断（是/否概率、选项、分数）而不生成文字的决策模型；这里收集的是别人真正用它做出来的东西。

**现有目录：43 个独立项目，全部为 `verified` / `source_reviewed`。** 2026-10-08 新增 16 个，并增加“桌面、手机与语音控制”分类。`verified` 表示来源、项目身份、Jev 用途和链接已核对，不表示性能、安全性、成本或运行结果已独立验证。

每条案例回答四个问题：

1. **项目做什么**：独立的项目身份、作者和具体任务。
2. **Jev 具体判断什么**：有固定版本源码支持的输入、问题类型和输出，以及哪些部分由普通代码完成。
3. **怎么开始复现**：原始文档里的安装与运行入口、前提和费用提示。
4. **证据与限制**：我们实际读了哪些文件、没有运行什么、哪些数字只是作者自述。每条都附[原始来源与核验记录](research/evidence/README.md)。

按场景浏览：[浏览器执行](categories/browser.md) 7、[桌面、手机与语音控制](categories/device.md) 3、[编码与上下文](categories/coding.md) 7、[路由与选择](categories/routing.md) 6、[证据评估](categories/evaluation.md) 7、[约束与防护](categories/guardrails.md) 2、[集成与 SDK](categories/integration.md) 4、[游戏与模拟](categories/game.md) 3、[数据流与其他](categories/other.md) 4。

不知道从哪看起，可以先看 [Jev Voice](cases/jev-voice-kevinbadi.md)（语音控制 Mac）、[Mobile Jev](cases/mobile-jev-droidrun.md)（真实 Android 手机）、[oxlint-plugin-jev](cases/oxlint-plugin-jev.md)（用自然语言写 lint 规则）、[Jev Browser](cases/jev-browser-jkudish.md)、[Pi-Heed](cases/pi-heed.md) 和 [Jev Model Router](cases/jev-model-router.md)；想看最小的完整调用，读 [jev-leftpad](cases/jev-leftpad.md)。

更多浏览与演示见 [jevforagents.com](https://jevforagents.com)。仓库可独立阅读，当前没有网站同步；仓库收录也不代表网站案例通过了新的运行或媒体测试。

见过没被收录的 Jev 项目？通过 [Issue 提交线索](https://github.com/FuturExplorator/awesome-jev-cases/issues/new?template=case.yml)，或读 [CONTRIBUTING](CONTRIBUTING.md) 后用[双语模板](templates/case.md)提交 PR。审核以[证据与治理规则](GOVERNANCE.md)和[案例格式](schema/README.md)为准；证据不足的项目不会为凑数量进入目录。如果这个目录帮你找到了思路，欢迎点一个 Star，方便更多人看到。

## English

An independent bilingual catalog of [TypeSafe Jev](https://typesafe.ai/) projects, maintained by the personal account **FuturExplorator**; it is not an official TypeSafe directory. Jev is a decision model that returns typed judgments (yes/no probability, choice, score) instead of text, and this list collects what people have actually built with it.

**Current catalog: 43 distinct projects, all `verified` / `source_reviewed`.** 16 were added on 2026-10-08, along with a “desktop, mobile and voice control” category. `verified` means provenance, identity, Jev usage and links were checked, not that performance, security, cost or runtime results were independently tested.

Every case answers four questions:

1. **What the project does**: its distinct identity, author and concrete task.
2. **What Jev decides**: inputs, question types and outputs supported by pinned source, and which parts are ordinary code.
3. **How to start reproducing it**: the install and run entry points, prerequisites and cost notes from the original docs.
4. **Evidence and limitations**: which files were actually read, what was not run, and which figures are only author claims. Each case links its [primary sources and review receipt](research/evidence/README.md).

Browse by scenario: [browser execution](categories/browser.md) (7), [desktop, mobile and voice control](categories/device.md) (3), [coding and context](categories/coding.md) (7), [routing and selection](categories/routing.md) (6), [evidence evaluation](categories/evaluation.md) (7), [constraints and guardrails](categories/guardrails.md) (2), [integrations and sdks](categories/integration.md) (4), [games and simulations](categories/game.md) (3), [streams and other uses](categories/other.md) (4).

Good starting points: [Jev Voice](cases/jev-voice-kevinbadi.md) (voice control for a Mac), [Mobile Jev](cases/mobile-jev-droidrun.md) (a real Android phone), [oxlint-plugin-jev](cases/oxlint-plugin-jev.md) (lint rules in plain English), [Jev Browser](cases/jev-browser-jkudish.md), [Pi-Heed](cases/pi-heed.md) and [Jev Model Router](cases/jev-model-router.md). For the smallest complete call, read [jev-leftpad](cases/jev-leftpad.md).

For richer browsing and demos, visit [jevforagents.com](https://jevforagents.com). This repository stands alone. No website synchronization or renewed website runtime/media verification is included in this update.

Know a Jev project that is missing? Submit a lead through an [Issue](https://github.com/FuturExplorator/awesome-jev-cases/issues/new?template=case.yml), or read [CONTRIBUTING](CONTRIBUTING.md) and open a PR with the [bilingual template](templates/case.md). The [governance](GOVERNANCE.md) and [case contract](schema/README.md) define admission; projects without enough evidence are not added to raise the count. If the catalog helped you, a star makes it easier for others to find.

## 案例目录 / Case directory

🆕 = 2026-10-08 新增 / added on 2026-10-08。“做什么”一栏是本库的编辑摘要，不是性能背书；细节与限制见各案例页。 / The “what it does” column is this catalog’s editorial summary, not a performance endorsement; see each case page for details and limits.

### 浏览器执行 / Browser execution · 7

| 案例 / Case | 作者 / Owner | 做什么 / What it does |
| --- | --- | --- |
| [Jev Browser](cases/jev-browser-jkudish.md) | jkudish | 通过 MCP、CLI 或库接口执行有步数与时间预算的浏览器任务。<br>A browser task runner exposed through MCP, CLI and a library, with step and time budgets. |
| [Jev Browser by tontoko](cases/jev-browser-playwright.md) | tontoko | 把 Playwright 的浏览器操作封装为 SDK、CLI 与 MCP 接口，同时提供基于页面证据的语义定位和断言。<br>A Playwright browser tool exposed through SDK, CLI and MCP interfaces, with page-grounded semantic location and assertions. |
| [Jev Browser Use](cases/jev-browser-use-codex.md) | wy-coliney | 将 Jev 接到 Codex 浏览器连接的社区技能与插件。<br>A community skill and plugin connecting Jev to a Codex browser session. |
| [Jev Ultrafast by Browser Use](cases/browser-use-jev-ultrafast.md) | browser-use | Browser Use 的浏览器代理实验：根据当前页面生成带编号的可操作元素表，并围绕一个自然语言目标循环执行浏览器步骤。<br>A Browser Use browser-agent experiment that loops over an indexed table of actionable page elements toward one natural-language goal. |
| [Jev Voice Browser](cases/jev-voice-browser-moritzkremb.md) | moritzkremb | 语音控制浏览器的本地演示：控制页接收语音识别文本，服务端驱动另一扇 Chromium 窗口。<br>A local voice-controlled browser demo. |
| [jev-browser by Ying-Kai Liao](cases/jev-browser-ying-kai-liao.md) | Ying-Kai-Liao | 独立的 Playwright 浏览器自动化库、CLI 与 MCP 服务：调用方给出目标，程序读取页面，Jev 参与下一步决策。<br>An independent Playwright browser automation library, CLI and MCP server. |
| [Jev-RA](cases/jev-ra.md) | brnyxx | 由编码代理提供目标与输入值，通过 CLI 或 MCP 控制 Chrome。<br>A CLI/MCP browser execution layer: a coding agent supplies the goal and input values, and local code drives Chrome. |

[分类页 / Category page](categories/browser.md)

### 桌面、手机与语音控制 / Desktop, mobile and voice control · 3

| 案例 / Case | 作者 / Owner | 做什么 / What it does |
| --- | --- | --- |
| [Jev Voice](cases/jev-voice-kevinbadi.md) 🆕 | kevinbadi | 对 Mac 说话即可打开应用、打字、搜索、滚动：本地 whisper.cpp 转写，每条指令一次 Jev 请求。<br>Talk to your Mac to open apps, type, search and scroll: local whisper.cpp plus one Jev request per command. |
| [Live Jev](cases/live-jev-okinaaudio.md) 🆕 | okinaaudio | 按 ⌘⇧Space 输入或口述一句日语/英语，控制 Ableton Live 的混音、走带、片段、音符和设备。<br>Press ⌘⇧Space and type or dictate one Japanese or English sentence to drive Ableton Live’s mixer, transport, clips, notes and devices. |
| [Mobile Jev](cases/mobile-jev-droidrun.md) 🆕 | droidrun | 给出一个目标，Jev 在通过 Mobilerun API 接入的真实 Android 手机上逐步选择操作和目标。<br>Give one goal and Jev picks each operation and target on a real Android phone reached through the Mobilerun API. |

[分类页 / Category page](categories/device.md)

### 编码与上下文 / Coding and context · 7

| 案例 / Case | 作者 / Owner | 做什么 / What it does |
| --- | --- | --- |
| [Codex Context Diet](cases/codex-context-diet.md) | konstantinosbotonakis | 针对 Codex 的大型工具结果，判断其是否仍需完整保留在会话上下文中。<br>A Codex plugin that judges whether bulky tool results still need to remain in full in conversation context. |
| [Compact Adviser](cases/compact-adviser.md) | kunchenguid | 在代理会话工作告一段落时，判断是否适合进行上下文压缩。<br>An agent plugin that identifies possible compaction boundaries after a unit of work. |
| [fast-jev-compaction](cases/fast-jev-compaction-tamara-tran.md) | tamaratran | Claude Code 插件及库：在压缩对话上下文时筛选工具调用与工具结果，减少过时内容，同时让保留的信息维持原文。<br>A Claude Code plugin and library that filters tool calls and tool results during conversation compaction, keeping retained material verbatim. |
| [Jev Code Finder (JevFind)](cases/jevfind-code-search.md) 🆕 | Peu77 | Rust 命令行：用自然语言描述概念，返回相关文件、行范围、置信度和代码片段。<br>Rust CLI that takes a plain-English concept and returns matching files, line ranges, confidence and snippets. |
| [Jev Semantic Code Reading](cases/jev-semantic-code.md) | BorisLeMeec | Go 实现的 Claude Code 插件，用自然语言定位代码、询问代码属性并缩小大型文件读取范围。<br>A Go-based Claude Code plugin for semantic code search, bounded code questions and narrower large-file reads. |
| [opencode-jev-compaction](cases/opencode-jev-compaction.md) 🆕 | quinnjr | opencode 插件：每次请求前判断旧的工具调用和结果是否还值得发送，只丢弃或截断，不改写。<br>opencode plugin that decides before every request whether old tool calls and results still deserve to be sent; it drops or truncates, never rewrites. |
| [oxlint-plugin-jev](cases/oxlint-plugin-jev.md) 🆕 | wobsoriano | Oxlint 插件：把 lint 规则写成针对函数、调用、JSX 或文件的是/否问题，概率超过 cutoff 就报错。<br>Oxlint plugin: write lint rules as yes/no questions about a function, call, JSX element or file and report when the probability clears your cutoff. |

[分类页 / Category page](categories/coding.md)

### 路由与选择 / Routing and selection · 6

| 案例 / Case | 作者 / Owner | 做什么 / What it does |
| --- | --- | --- |
| [Astra-Ares](cases/astra-ares.md) | miuuyy | 在单独打补丁的实验版 Codex CLI 中，按任务进展调整所选模型的推理力度。<br>An experimental, separately patched Codex CLI that adjusts reasoning effort as a task progresses. |
| [ClearJev](cases/clearjev.md) | huncijr | 在 Codex CLI 提示执行前，选择会话所用的模型与推理配置。<br>A Codex CLI routing layer that chooses the session model and reasoning configuration before a prompt runs. |
| [Jev Chat](cases/jev-chat-w3cj.md) | w3cj | 用聊天界面调用真实工具的本地应用，包含天气、单位换算、百科、菜谱及可选外部服务。<br>A local chat interface that invokes real tools for weather, unit conversion, Wikipedia, recipes and optional external services. |
| [Jev Model Router](cases/jev-model-router.md) | rajdhakad9826 | TypeScript 路由库，按查询要求在调用方提供的两到三个模型档位间选择。<br>A TypeScript routing library that selects among two or three caller-defined model tiers. |
| [jev-router by gargpratyush](cases/jev-router-gargpratyush.md) | gargpratyush | 给 Claude Code 与 Codex CLI 增加逐轮模型路由的启动器。<br>A launcher adding per-turn model routing to Claude Code and Codex CLI. |
| [neo4jev](cases/neo4jev.md) 🆕 | jexp | 在 Neo4j 图上逐跳导航：每一跳把出边作为 Choice 选项，并用 Noul 判断是否已到达目标。<br>Hop-by-hop Neo4j graph navigation: outgoing relationships become Choice options and a Noul asks whether the goal is reached. |

[分类页 / Category page](categories/routing.md)

### 证据评估 / Evidence evaluation · 7

| 案例 / Case | 作者 / Owner | 做什么 / What it does |
| --- | --- | --- |
| [Jev Arena](cases/jev-arena-nanmicoder.md) | NanmiCoder | 将同批评论交给 Jev 和另一模型标注的比较工具，支持 CSV/Excel 导入、回放和离线报告。<br>A comparison tool that labels the same comments with Jev and another model, with CSV/Excel import, replay and offline reports. |
| [Jev Logs](cases/jevlogs.md) 🆕 | reachjalil | 在把日志交给昂贵的 LLM 分析前，先为每条 OpenTelemetry 日志打诊断价值、优先级和是否值得调查的分。<br>Scores each OpenTelemetry log for diagnostic value, priority and whether it merits investigation before expensive LLM analysis. |
| [Jev MCP](cases/jev-mcp-jkudish.md) | jkudish | 把证据核对、候选筛选与排序等判断封装成可供代理调用的 MCP 工具。<br>An MCP server exposing typed judgments for evidence checking, candidate selection and ranking. |
| [Jev Review](cases/jev-review-devagrawal.md) | devagrawal09 | 面向 Git diff 或完整代码库的分阶段代码审查工作流，提供命令行入口和本地报告界面。<br>A staged code-review workflow for a Git diff or complete codebase, with CLI entry points and a local report interface. |
| [Jev Search](cases/jev-search-superagents.md) | superagents-lab | 展示搜索链接与摘要的网页应用，Jev 参与查询/来源选择和结果相关性判断。<br>A web app showing search links and snippets, with Jev judging query/source choice and result relevance. |
| [jev-seo by AgriciDaniel](cases/jev-seo-agrici.md) | AgriciDaniel | 从网站首页 URL 开始的本地 SEO 审核工具：抓取页面并运行确定性检查，再输出 PDF、XLSX 和 Markdown 报告。<br>A local SEO auditor starting from a homepage URL that crawls pages, applies deterministic checks and renders PDF, XLSX and Markdown reports. |
| [JevSEO by epergaboni](cases/jevseo-epergaboni.md) 🆕 | epergaboni | 给页面分别打 SEO、AEO、GEO 三项分并列出修改清单；整站模式为每个页面选择处理动作。<br>Scores a page separately for SEO, AEO and GEO with a ranked fix list; site mode picks an action per page. |

[分类页 / Category page](categories/evaluation.md)

### 约束与防护 / Constraints and guardrails · 2

| 案例 / Case | 作者 / Owner | 做什么 / What it does |
| --- | --- | --- |
| [Pi-Heed](cases/pi-heed.md) | Nyarlathoteppppp | 为 Pi 编码代理保留用户约束，并在有副作用的工具调用前检查约束。<br>A Pi coding-agent extension that retains user constraints and checks side-effecting tool calls. |
| [pi-jev](cases/pi-jev-y0usaf.md) | y0usaf | Pi 编码代理的扩展：在工具调用前评估风险，在 bash 输出后判断泄密或错误类型，并提供 `jev_ask` 类型化提问工具。<br>A Pi coding-agent extension that evaluates risk before tool calls, judges bash output for secrets or failure type, and offers a `jev_ask` tool for typed questions. |

[分类页 / Category page](categories/guardrails.md)

### 集成与 SDK / Integrations and SDKs · 4

| 案例 / Case | 作者 / Owner | 做什么 / What it does |
| --- | --- | --- |
| [go-jev](cases/go-jev.md) 🆕 | mattn | Go SDK 和 `jev-cli`：在 Go 程序与 UNIX 管道里获得是/否概率、选项和分数。<br>Go SDK and `jev-cli` for yes/no probabilities, choices and scores in Go programs and UNIX pipelines. |
| [Jev for Elixir and OTP](cases/jev-elixir-otp.md) | dannote | 把类型化判断接入 Elixir/OTP 进程的库。<br>An Elixir/OTP library for typed decisions inside processes. |
| [Jev for Home Assistant](cases/ha-jev-home-assistant.md) | AboveColin | 社区维护的 Home Assistant 集成，把家庭状态的类型化判断呈现为传感器、自动化动作和 Assist 会话入口。<br>A community Home Assistant integration exposing typed judgments about household state as sensors, automation actions and an Assist conversation entry point. |
| [n8n-nodes-typesafe-jev](cases/n8n-nodes-typesafe-jev.md) 🆕 | n3ndor | n8n 社区节点：在一个节点里对同一份数据提多个类型化问题，结果直接交给 Switch / Filter 分支。<br>n8n community node: ask several typed questions about one item and branch on the answers with Switch or Filter. |

[分类页 / Category page](categories/integration.md)

### 游戏与模拟 / Games and simulations · 3

| 案例 / Case | 作者 / Owner | 做什么 / What it does |
| --- | --- | --- |
| [Jev × LIBERO](cases/jev-libero.md) 🆕 | Dimweaker | 在 LIBERO 机器人仿真任务中，让 Jev 分层选择意图、动作类别和具体控制输入。<br>Layered Jev choices of intent, motion family and control input on LIBERO robot-simulation tasks. |
| [jev-factorio](cases/jev-factorio-agent.md) 🆕 | jevplays-games | Factorio 游戏代理实验：Jev 用类型化问题决定目标和下一步动作，确定性代码负责规则与执行。<br>Factorio agent experiment: Jev picks goals and next actions as typed questions while deterministic code owns rules and actuation. |
| [Snake Jev](cases/snake-jev-siroccomask.md) | siroccomask | 桌面贪吃蛇实验，把旧版游戏的传感器转为 Jev 判断输入；Python 负责食物、移动与碰撞等游戏运行。<br>A desktop Snake experiment that turns sensors from an earlier game into Jev judgment input; Python still runs the game mechanics. |

[分类页 / Category page](categories/game.md)

### 数据流与其他 / Streams and other uses · 4

| 案例 / Case | 作者 / Owner | 做什么 / What it does |
| --- | --- | --- |
| [Firehose Judge](cases/firehose-judge.md) | ragelink | 对 Bluesky 实时流中的采样帖子分类，并将不确定结果放入人工复核通道。<br>A sampled Bluesky stream classifier with a separate lane for uncertain results. |
| [Jev Cloud Quiz](cases/jev-cloud-quiz.md) 🆕 | minorun365 | 教学演示：选一个云服务功能名，查看 Jev 判断它属于 AWS、Azure 还是 Google Cloud 的概率。<br>Teaching demo: pick a cloud feature name and see Jev’s probabilities for AWS, Azure or Google Cloud. |
| [jev-leftpad](cases/jev-leftpad.md) 🆕 | f | 自嘲式 npm 包：用一个 Choice 问题决定要补几个空格，是最小的完整 Jev 调用示例。<br>Tongue-in-cheek npm package: one Choice question decides how many spaces to pad, a minimal complete Jev call. |
| [jev-skip](cases/jev-skip.md) 🆕 | valentynkit | 浏览器扩展：读取 YouTube 字幕，判断哪些片段是赞助口播并跳过，不依赖众包时间戳。<br>Browser extension that reads YouTube captions, decides which segments are sponsor reads and skips them without a crowd database. |

[分类页 / Category page](categories/other.md)

## 许可证 / License

[MIT](LICENSE) covers original code, schemas and original bilingual editorial content this repository has the right to license. Third-party materials retain their own rights; see [THIRD_PARTY_NOTICES](THIRD_PARTY_NOTICES.md) and the [attribution register](research/ATTRIBUTION.md).
MIT 仅适用于本库有权许可的原创内容；第三方代码、原帖、图片与视频不因此改用 MIT。

## 审核与维护 / Audit and maintenance

- [中文 PRD](PRD.zh-CN.md) · [English PRD](PRD.md)
- [2026-10-08 批次审阅 / 2026-10-08 batch review](research/BATCH_2026-10-08_REVIEW.md)
- [首版验收报告 / Release review](research/RELEASE_REVIEW.md)
- [网站与 CSV 导入审核 / Website and CSV intake review](research/IMPORT_REVIEW.md)
- [CSV 仓库分流与待审目录 / CSV repository triage](research/CSV_REPOSITORIES.md)
- [CSV 专项审阅报告 / CSV batch review](research/CSV_BATCH_REVIEW.md)
- [增补审核与下一批选题 / Follow-up review and next topics](research/FOLLOW_UP_REVIEW.md)
- [候选审核台账 / Candidate audit](research/CANDIDATES.md) — not a published-case index / 不属于已收录目录
- [来源核验记录 / Source receipts](research/evidence/README.md)

Run `python3 scripts/validate_catalog.py` for offline structural checks. It never changes status, publishes, discovers candidates, or calls a model.
运行上述命令检查格式、去重、目录和本地链接；脚本不会变更状态、发布、自动发现或调用模型。
