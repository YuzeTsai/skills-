# Skills

A collection of custom skills / agents I've built for Claude.

[繁體中文版](README.zh-TW.md)

---

## Repo Structure

```
skills-/
├── grad-admissions-advisor/        ← source (SKILL.md + scripts + references)
│   ├── SKILL.md                    ← prompt instructions
│   ├── scripts/
│   │   └── fetch_school_info.py   ← Firecrawl scraper for /school mode
│   └── references/                ← country guides, field guides, FAQ
└── grad-admissions-advisor.skill   ← packaged for Claude Code (zip of the above)
```

---

## How to Use

### Option A — Claude Code (recommended)

Install via `/install-skill` or drag the `.skill` file into Claude Code.  
The skill activates automatically when relevant. The `/school` mode runs `scripts/fetch_school_info.py` via the bash tool.

**Setup:**
```bash
export FIRECRAWL_API_KEY=your_key_here
```

### Option B — Any Claude interface (API, claude.ai, Cursor, etc.)

Copy the contents of `grad-admissions-advisor/SKILL.md` as your system prompt.

For `/school` mode with live data, run the script manually and paste the output back:
```bash
export FIRECRAWL_API_KEY=your_key_here
pip install requests
python grad-admissions-advisor/scripts/fetch_school_info.py \
  --school "Columbia University" \
  --program "MS in Data Science" \
  --season "2027 Fall" \
  --field "data science"
```

Without the script, `/school` falls back to asking Claude to search the web using available tools (or lists `[待確認]` if no web tools are available).

---

## Skill List

### `grad-admissions-advisor`

A full-service graduate school admissions advisor for international master's programs.  
Designed with Taiwanese students in mind, but applicable to any applicant.

**Three working modes:**

| Command | Function |
|---|---|
| `/school` | Generate a customized school list (Dream / Match / Safety) — fetches real deadlines, admission stats, tuition, and faculty from official program pages via `fetch_school_info.py` |
| `/essay [SOP/PS/CV]` | Essay coaching — structure feedback, paragraph-level comments, rewrite suggestions |
| `/plan` | Build a full application timeline working backwards from deadlines |

**Additional commands:**

| Command | Function |
|---|---|
| `/profile` | Fill in or update applicant profile (GPA, test scores, experience, goals) |
| `/review` | Paste a draft essay for detailed critique |
| `/status` | View current profile summary and progress |
| `/faq` | Quick answers to common admissions questions |

**Coverage:**
- Countries: US, UK, Canada, Australia, Europe
- Fields: CS, Business, Design, Humanities, STEM, and more
- Documents: SOP, Personal Statement, CV/Resume, recommendation letter prep

**Advisor style:** Honest, specific, no empty encouragement. Every suggestion comes with reasoning and tradeoffs.

---

## About

> Yuze Tsai · [GitHub](https://github.com/YuzeTsai)
