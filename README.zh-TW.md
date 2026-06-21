# Skills

收集我為 Claude 製作的自訂 skill / agent 集合。

[English](README.md)

---

## 專案結構

```
skills-/
├── grad-admissions-advisor/        ← 原始碼（SKILL.md + 腳本 + 參考資料）
│   ├── SKILL.md                    ← prompt 指令
│   ├── scripts/
│   │   └── fetch_school_info.py   ← /school 模式的 Firecrawl 爬蟲腳本
│   └── references/                ← 各國制度、領域指南、FAQ
└── grad-admissions-advisor.skill   ← Claude Code 安裝包（上方資料夾的 zip）
```

---

## 使用方式

### 方式 A — Claude Code（推薦）

透過 `/install-skill` 安裝，或直接將 `.skill` 檔拖入 Claude Code。  
安裝後遇到相關情境自動觸發。`/school` 模式會透過 bash 工具執行 `scripts/fetch_school_info.py`。

**前置設定：**
```bash
export FIRECRAWL_API_KEY=your_key_here
```

### 方式 B — 任何 Claude 介面（API、claude.ai、Cursor 等）

將 `grad-admissions-advisor/SKILL.md` 的內容複製為 system prompt 即可使用。

`/school` 模式若需即時資料，可手動執行腳本並將輸出貼回對話：
```bash
export FIRECRAWL_API_KEY=your_key_here
pip install requests
python grad-admissions-advisor/scripts/fetch_school_info.py \
  --school "Columbia University" \
  --program "MS in Data Science" \
  --season "2027 Fall" \
  --field "data science"
```

若不執行腳本，`/school` 會退回使用可用的網頁工具搜尋，或在無工具時標注 `[待確認]`。

---

## Skill 列表

### `grad-admissions-advisor`

國外碩士申請全程顧問，以台灣學生的申請情境為核心設計，同樣適用於其他背景的申請者。

**三種工作模式：**

| 指令 | 功能 |
|---|---|
| `/school` | 產出客製化選校清單（Dream / Match / Safety）——透過 `fetch_school_info.py` 即時抓取各校官網的截止日期、錄取統計、學費與相關教授 |
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

---

## 關於

> 蔡佑澤 (Yuze Tsai) · [GitHub](https://github.com/YuzeTsai)
