# 🔍 Research Multi-Agent System

An intelligent multi-agent pipeline that automatically researches any topic, analyzes findings, writes a structured report, and critically reviews its own output.

## 🏗️ Architecture

```
User Query
    │
    ▼
┌─────────────────┐
│  Search Agent   │  ← searches the web via Tavily API
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Analysis Agent  │  ← extracts key insights via Gemini AI
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Report Agent   │  ← writes structured professional report
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Critic Agent   │  ← reviews quality, scores 1-10
└────────┬────────┘
         │
         ▼
    Final Output
```

Built with **LangGraph** — each agent is a node in a state machine graph.

## ✨ Features

- 🔎 **Real-time web search** via Tavily API (top 5 sources)
- 🧠 **AI Analysis** — key findings, trends, contradictions
- 📝 **Structured Report** — Executive Summary, Key Findings, Conclusion
- ✅ **Self-evaluation** — Critic Agent scores report quality 1-10
- 🔄 **LangGraph State Machine** — clean, traceable pipeline

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| LangGraph | Agent orchestration |
| LangChain | LLM integration |
| Google Gemini 2.5 Flash | AI analysis & report writing |
| Tavily Search API | Real-time web search |
| python-dotenv | Environment management |

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/vitalinka22/search-agent.git
cd search-agent
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up API keys

Create a `.env` file in the root folder:
```
GOOGLE_API_KEY=your_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Get your keys:
- Gemini: https://aistudio.google.com/apikey
- Tavily: https://tavily.com (free tier available)

### 5. Run
```bash
python src/main.py
```

## 📊 Example Output

**Query:** `"AI trends in healthcare 2026"`

```
🔍 Search Agent: searching for AI trends in healthcare 2026
✅ Found 5 results

🧠 Analysis Agent: complete

📝 Report Agent: writing report...
✅ Report Agent: complete

🔍 Critic Agent: reviewing report...
✅ Critic Agent: complete

--- FINAL REPORT ---
Executive Summary: ...
Key Findings: ...
Conclusion: ...

--- QUALITY FEEDBACK ---
Score: 8/10
...
```

## 📁 Project Structure

```
search-agent/
├── src/
│   ├── agents.py     ← all 4 agents
│   ├── graph.py      ← LangGraph pipeline
│   └── main.py       ← entry point
├── .env              ← API keys (not committed)
├── .gitignore
├── requirements.txt
└── README.md
```

## 🧠 How It Works

**State Machine Pattern:**

Each agent receives a shared `state` dictionary, adds its results, and passes it to the next agent:

```python
state = {
    "query": "AI trends in healthcare 2026",
    "search_results": "",   # filled by Search Agent
    "analysis": "",         # filled by Analysis Agent
    "report": "",           # filled by Report Agent
    "feedback": ""          # filled by Critic Agent
}
```

LangGraph manages the flow between agents automatically.

## 🔮 Planned Features

- [ ] Streamlit UI
- [ ] Export report as PDF
- [ ] Iterative improvement loop (Critic → Report → Critic)
- [ ] Support for multiple search queries

## 👩‍💻 Author

**Vitalina Alipova** — AI Engineering Student at TU Berlin

[![GitHub](https://img.shields.io/badge/GitHub-vitalinka22-black)](https://github.com/vitalinka22)
