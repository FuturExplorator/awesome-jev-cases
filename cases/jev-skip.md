---
slug: "jev-skip"
name_en: "jev-skip"
name_zh: "jev-skip：YouTube 赞助片段跳过"
project_url: "https://github.com/valentynkit/jev-skip"
source_url: "https://github.com/valentynkit/jev-skip/blob/6837e3e0f1a48cbfc48c85415d99bcfe3eaf0628/README.md"
source_kind: "github"
author: "valentynkit"
source_date: "2026-09-19"
source_date_kind: "commit"
last_checked: "2026-10-08"
source_revision: "6837e3e0f1a48cbfc48c85415d99bcfe3eaf0628"
jev_relation: "uses_typesafe"
scenario: "other"
content_kind: "application"
status: "verified"
claim_status: "source_reviewed"
upstream_license: "MIT"
evidence_file: "research/evidence/jev-skip.json"
---

# jev-skip / jev-skip：YouTube 赞助片段跳过

## 中文

### 项目简介

一个 Chrome / Firefox 浏览器扩展：读取正在观看的 YouTube 视频的字幕，判断哪些片段是赞助口播并自动跳过，同时在进度条上按把握程度着色。README 强调它不依赖 SponsorBlock 那样的众包时间戳数据库。

### Jev 的具体作用

固定的 `lib/questions.ts` 为视频的每个字幕片段构造一个 Choice 问题，选项为 sponsor、self_promo、intro、outro、recap、content、other，并注明字幕文本是不可信的证据而非指令。`lib/jev.ts` 把请求发往 `{baseUrl}/v1/systemone`，默认 `https://api.typesafe.ai`。README 说明扩展依据每个约 30 秒片段的概率给进度条着色并决定跳过。

### 如何复现

`git clone https://github.com/valentynkit/jev-skip && cd jev-skip`，`npm install && npm run build`，在 `chrome://extensions` 打开开发者模式并加载 `dist/chrome-mv3`，然后在弹窗中粘贴自己的 TypeSafe Key。Firefox 用 `npm run build:firefox`。README 说明视频标题、频道和字幕文本会用你的 Key 发送到所配置的端点。

### 证据与限制

已核对固定 README、`lib/jev.ts`、`lib/questions.ts` 和 MIT LICENSE；未构建或安装扩展、未调用付费接口。README 的指标（23 个视频上覆盖 77% 的赞助秒数、每小时 34 秒误跳、每视频 $0.0008 等）为作者自述；README 同时说明这些数字是通过 Vercel AI Gateway 转接层而不是直连 API 测得，演示动图回放的是录制的答案。README 还写明：只读字幕不听音频，没有字幕就不工作；获取字幕依赖 YouTube 当前的页面行为；Firefox 上内容脚本可以读取 Key。

## English

### Overview

A Chrome / Firefox extension that reads the captions of the YouTube video you are watching, decides which segments are sponsor reads, skips them and tints the seek bar by confidence. The README stresses that it does not rely on a crowd-sourced timestamp database such as SponsorBlock.

### Jev's specific role

Pinned `lib/questions.ts` builds one Choice question per caption segment with the options sponsor, self_promo, intro, outro, recap, content and other, and notes that transcript text is untrusted evidence, never instructions. `lib/jev.ts` posts to `{baseUrl}/v1/systemone`, defaulting to `https://api.typesafe.ai`. The README says the extension paints the bar and decides skips from the probability for each roughly 30-second segment.

### Reproduction

`git clone https://github.com/valentynkit/jev-skip && cd jev-skip`, `npm install && npm run build`, enable developer mode at `chrome://extensions`, load `dist/chrome-mv3` unpacked and paste your own TypeSafe key in the popup. Firefox uses `npm run build:firefox`. The README says the title, channel and caption text of the video are sent under your key to the configured endpoint.

### Evidence and limitations

The pinned README, `lib/jev.ts`, `lib/questions.ts` and the MIT license were reviewed. The extension was not built or installed and no paid call was made. The metrics in the README (77% of sponsor seconds across 23 videos, 34 s of false skips per hour, $0.0008 per video and so on) are author-reported; the README also says they were measured through a Vercel AI Gateway shim rather than the direct API and that the demo GIF replays recorded answers. It further states that it reads text, not audio, does nothing without captions, depends on YouTube’s current page behaviour, and that on Firefox a content script could read the key.

## Sources / 来源

- [项目仓库 / Repository](https://github.com/valentynkit/jev-skip)
- [固定版本 README / Pinned README](https://github.com/valentynkit/jev-skip/blob/6837e3e0f1a48cbfc48c85415d99bcfe3eaf0628/README.md)
- [实现 / Implementation: lib/jev.ts](https://github.com/valentynkit/jev-skip/blob/6837e3e0f1a48cbfc48c85415d99bcfe3eaf0628/lib/jev.ts)
- [实现 / Implementation: lib/questions.ts](https://github.com/valentynkit/jev-skip/blob/6837e3e0f1a48cbfc48c85415d99bcfe3eaf0628/lib/questions.ts)
- [原始许可证 / Upstream license](https://github.com/valentynkit/jev-skip/blob/6837e3e0f1a48cbfc48c85415d99bcfe3eaf0628/LICENSE)
- [核验记录 / Review receipt](../research/evidence/jev-skip.json)
