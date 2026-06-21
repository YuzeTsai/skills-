# Skills

收集我為 Claude Code 製作的自訂 skill 集合。

[English](README.md)

---

## 使用方式

在 Claude Code 中，透過 `/install-skill` 安裝，或直接將 `.skill` 檔拖入 Claude Code 使用。  
安裝後遇到相關情境會自動觸發，不需要手動呼叫。

---

## Skill 列表

### `grad-admissions-advisor.skill`

國外碩士申請全程顧問，以台灣學生的申請情境為核心設計，同樣適用於其他背景的申請者。

**三種工作模式：**

| 指令 | 功能 |
|---|---|
| `/school` | 產出客製化選校清單（Dream / Match / Safety）——透過 web agent 即時抓取各校官網的截止日期、錄取統計、學費與相關教授 |
| `/essay [SOP/PS/CV]` | 文書協助——結構建議、逐段批注、改寫方向 |
| `/plan` | 從 Deadline 倒推，產出完整申請時程表 |

**其他指令：**

| 指令 | 功能 |
|---|---|
| `/profile` | 填寫或更新申請者資料（GPA、語言成績、經歷、目標） |
| `/review` | 貼上文書草稿，獲得完整批改意見 |
| `/status` | 顯示目前 Profile 摘要與進度 |
| `/faq` | 快速回答申請常見問題 |

**涵蓋範圍：**
- 國家：美國、英國、加拿大、澳洲、歐洲
- 領域：CS、商學、設計、人文、理工等
- 文件：SOP、PS、CV / Resume、推薦信素材準備

**顧問風格：** 誠實直白，不說空洞鼓勵。每個建議都附上理由與潛在風險。

**依賴工具：** `/school` 模式需要 `firecrawl_search` + `firecrawl_scrape`（若不可用會 fallback 至 `WebSearch` + `WebFetch`）。建議安裝 [Firecrawl MCP](https://github.com/mendableai/firecrawl-mcp-server) 以獲得最佳效果。

---

## 關於

> 蔡佑澤 (Yuze Tsai) · [GitHub](https://github.com/YuzeTsai)
