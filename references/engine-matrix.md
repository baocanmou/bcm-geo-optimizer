# Engine Matrix

## General rule

Use official data and observed answers when available. Provider behavior changes; verify current documentation before implementing provider-specific assumptions.

| Surface | Primary evidence | High-value checks | Common overclaim |
|---|---|---|---|
| Google Search / AI surfaces | Search Console readback, public results, observed AI answer | index coverage, canonical, structured facts, source quality | submission equals index or AI use |
| Microsoft Bing / Copilot | Webmaster readback, IndexNow receipt, public results, observed answer | crawl/index state, entity consistency, cited sources | IndexNow receipt equals ranking |
| Baidu | resource platform readback, public results, observed answer | verification, crawl/index signals, mobile/public accessibility | push success equals inclusion |
| Other domestic search engines | official console where available, public result sampling | ownership, sitemap, crawl access, regional performance | verified site equals traffic |
| ChatGPT | observed answer with provider/model/time, referral analytics | source citations, entity and decision facts, repeatability | one mention equals stable recommendation |
| Claude | observed answer with provider/model/time | answer usefulness, cited evidence when surfaced | generated answer equals indexed knowledge |
| Gemini | observed answer and source links | Google ecosystem retrieval, source clarity, freshness | Search Console data proves Gemini use |
| Perplexity | observed answer and cited URLs | citation eligibility, concise proof, source diversity | citation alone equals endorsement |
| Doubao (豆包, ByteDance) | observed answer with app/version, mode and time; reference links when surfaced | whether web search ran, which sources are shown, Chinese decision facts | one consumer-app answer equals Volcengine Ark API or Coze behavior |
| DeepSeek | observed answer with the web-search and deep-thinking toggle states recorded | answers with search on vs off, sources when shown, entity facts | an answer with search off reflects current web visibility |
| Kimi (Moonshot AI) | observed answer; reference links when surfaced | whether a search was actually triggered, which sources are shown | no search on one prompt means the page is not indexed |
| Tencent Yuanbao (腾讯元宝) | observed answer with the selected model (Hunyuan, DeepSeek or other) and shown sources | which source types appear, model choice, Chinese decision facts | one selected model represents Yuanbao as a whole |
| Qwen (通义千问 / 千问, Alibaba) | observed answer; API `search_info` only when sources are requested | whether search ran, shown sources, entity consistency | an API answer without sources means no sources were used |
| ERNIE (文心, Baidu) | observed answer; Baidu Search readback recorded separately | Baidu crawl/index state, entity facts, sources when shown | Baidu inclusion equals ERNIE answer use |

## Chinese AI assistants: verified properties

Properties change often. The table records only what an official source stated
when this reference was checked (2026-10-05). `待核实` means no official source was
confirmed; treat the property as unknown and record what you actually observe.
Consumer apps and the vendor's developer API are different surfaces: never use an
API result as evidence for the app, or the reverse.

| Surface | Web search in consumer product | Sources shown in consumer answers | Developer API and search sources | Official source |
|---|---|---|---|---|
| Doubao (豆包) | 待核实 | 待核实 | Volcengine Ark (火山方舟) documents a web-search tool; request and citation format 待核实 | <https://www.volcengine.com/docs/82379/1956278> |
| DeepSeek | Web chat has a user-controlled “联网搜索” toggle (announced 2024-12) | 待核实 | Same announcement says the API did not support search; current status 待核实 (unofficial reports claim later support) | <https://api-docs.deepseek.com/zh-cn/news/news1210>, <https://api-docs.deepseek.com/> |
| Kimi | Help center: Kimi decides by itself whether to search; no manual switch | Help center describes search results as traceable; actual display 以实际观测为准 | Kimi Open Platform provides an API; search-tool details 待核实 | <https://www.kimi.com/zh-cn/help/new-user-guide/overview> |
| Tencent Yuanbao (腾讯元宝) | 待核实 (media report integration with WeChat search; not an official source) | 待核实 | Hunyuan API (not the Yuanbao app): `enable_enhancement` search switch, `citation` markers, `search_info` returned when requested | <https://cloud.tencent.com/document/product/1729/111007> |
| Qwen (通义千问 / 千问) | 待核实 | 待核实 | Model Studio API: `enable_search`; DashScope returns `search_info` with `enable_source` and `[n]` markers with `enable_citation`; the OpenAI-compatible Chat Completions endpoint returns no sources | <https://help.aliyun.com/zh/model-studio/web-search> |
| ERNIE (文心) | 待核实 (the consumer app has been renamed more than once; record the visible name) | 待核实 | Qianfan API documents search-related parameters; exact names and citation output 待核实 | <https://cloud.baidu.com/doc/WENXINWORKSHOP/s/Vlxygsvyo> |

How to collect these observations:

- Consumer chat apps usually have no automation route the user has authorized.
  Use the manual paste-back route in [browser-observation.md](browser-observation.md)
  and record `collection_method: manual`.
- Record the visible mode for every observation (web search on/off, deep thinking,
  selected model). Do not compare a baseline and retest that used different modes.
- Some products answer without a visible source list. Without a shown source, the
  highest supportable state is `mentioned` or `recommended`, never `cited`.

## Provider-independent tests

For each chosen engine:

1. Can it access the public page?
2. Can official tools confirm ownership and provide real data readback?
3. Is the intended canonical page discoverable and indexed?
4. Does the observed answer mention, cite, recommend, reject, or omit the brand?
5. Which sources and selection criteria appear in that answer?
6. Does the cited page convert the intended visitor?

## Freshness

Record collection time and verify current platform documentation before changing APIs, authentication, or submission methods. Do not hard-code assumptions about provider crawling, training, retrieval, or ranking.
