---
slug: "ha-jev-home-assistant"
name_en: "Jev for Home Assistant"
name_zh: "Home Assistant 的 Jev 集成"
project_url: "https://github.com/AboveColin/HA-Jev"
source_url: "https://github.com/AboveColin/HA-Jev/blob/a4714ea79d4665ceb0fec90a18ceefc5f35d6ab3/README.md"
source_kind: "github"
author: "AboveColin"
source_date: "2026-09-29"
source_date_kind: "commit"
last_checked: "2026-09-30"
source_revision: "a4714ea79d4665ceb0fec90a18ceefc5f35d6ab3"
jev_relation: "uses_typesafe"
scenario: "integration"
content_kind: "integration"
status: "verified"
claim_status: "source_reviewed"
upstream_license: "MIT"
evidence_file: "research/evidence/ha-jev-home-assistant.json"
website_url: "https://jevforagents.com/builds/ha-jev"
---

# Jev for Home Assistant / Home Assistant 的 Jev 集成

## 中文

### 项目简介

社区维护的 Home Assistant 集成，把家庭状态的类型化判断呈现为传感器、自动化动作和 Assist 会话入口。

### Jev 的具体作用

集成整理配置的家庭状态与问题，通过 `jevclient` 将状态和问题送给 Jev；返回的二元概率、选项或分数被转成传感器状态或自动化响应。Home Assistant 负责设备状态采集和动作执行，Jev 负责指定问题的判断。

### 如何复现

按固定版本 README，在兼容的 Home Assistant 实例中通过 HACS 自定义仓库或手动复制集成安装；配置自己的 TypeSafe API key，从一条普通的“是否忘记洗衣”问题或项目示例开始观察传感器结果。OpenRouter 是另外一种提供方配置，不能用来证明 TypeSafe 托管端点的实测。

### 证据与限制

已核对仓库、README、集成的 `jevclient` 调用、服务定义和 MIT 许可证；未安装 Home Assistant 或运行 Jev。上游自称与 TypeSafe 无隶属关系。不要把示例自动化当作生命安全或无人值守的安全控制；费用统计含 API 返回的 token 与按可变价格计算的估值。

## English

### Overview

A community Home Assistant integration exposing typed judgments about household state as sensors, automation actions and an Assist conversation entry point.

### Jev's specific role

The integration assembles configured household state and questions, then sends them through `jevclient` to Jev. Binary probabilities, choices or scores become sensor state or automation responses. Home Assistant collects device state and performs actions; Jev judges specified questions.

### Reproduction

Follow the pinned README to install the integration in a compatible Home Assistant instance through a HACS custom repository or manual copy. Configure your own TypeSafe API key and start with an ordinary laundry reminder question or project example to inspect the resulting sensor. OpenRouter is a separate provider configuration and does not establish a TypeSafe-hosted test.

### Evidence and limitations

The repository, README, `jevclient` call, service definitions and MIT license were reviewed; Home Assistant and Jev were not run here. The upstream author says the integration is unaffiliated with TypeSafe. Example automations are not evidence for life-safety or unattended safety control. Usage totals include API-reported tokens, while money is estimated from a configurable price.

## Sources / 来源

- [项目仓库 / Repository](https://github.com/AboveColin/HA-Jev)
- [固定版本 README / Pinned README](https://github.com/AboveColin/HA-Jev/blob/a4714ea79d4665ceb0fec90a18ceefc5f35d6ab3/README.md)
- [Jev 客户端调用 / Jev client call](https://github.com/AboveColin/HA-Jev/blob/a4714ea79d4665ceb0fec90a18ceefc5f35d6ab3/custom_components/jev/coordinator.py)
- [自动化服务 / Automation services](https://github.com/AboveColin/HA-Jev/blob/a4714ea79d4665ceb0fec90a18ceefc5f35d6ab3/custom_components/jev/services.py)
- [网站中的同一项目 / Same project on JevForAgents](https://jevforagents.com/builds/ha-jev)
- [原始许可证 / Upstream license](https://github.com/AboveColin/HA-Jev/blob/a4714ea79d4665ceb0fec90a18ceefc5f35d6ab3/LICENSE)
