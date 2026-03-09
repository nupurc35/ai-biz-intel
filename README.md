# AI-Biz-Intel: Multi-Agent Business Intelligence

AI-Biz-Intel is a powerful business intelligence tool that leverages a sequence of three specialized AI agents to transform a simple topic and industry into a comprehensive, actionable business report.

## 🚀 Multi-Agent Architecture

The system uses a linear pipeline where each agent's output informs the next, ensuring depth and coherence.

```ascii
[ User Input ] 
      |
      v
+-----------------+   (1) Market Analysis
|  Analyst Agent  |----------------------------+
+-----------------+                            |
      |                                        |
      v                                        v
+-----------------+   (2) Strategy Generation  +---------------------+
| Strategist Agent|--------------------------> |   C-Suite Summary    |
+-----------------+                            |   Summary Agent     |
      |                                        +---------------------+
      v                                                  |
[ Actionable Plan ] <------------------------------------+
```

### The Agents
1.  **Analyst Agent**: Conducts deep market research, identifying trends, competitors, risks, and opportunities.
2.  **Strategist Agent**: Takes the analysis and formulates 5 concrete, actionable business strategies.
3.  **Summary Agent**: Distills everything into a crisp, one-page executive briefing for decision-makers.

## 🛠 Tech Stack
- **Frontend**: Vite + React, Vanilla CSS (Premium Dark Theme)
- **Backend (Local)**: FastAPI, Uvicorn, Groq SDK
- **Backend (Edge)**: Vercel Serverless Functions (Node.js)
- **AI Model**: Llama-3.3-70b-versatile (via Groq)

## 📸 Demo
![Project Demo](https://via.placeholder.com/800x450.png?text=AI-Biz-Intel+Demo+Placeholder)

## ⚙️ Setup Instructions

### 1. Prerequisites
- Node.js (v18+)
- Python (3.10+)
- Groq API Key

### 2. Environment Variables
Create a `.env` file in the `backend` folder:
```env
GROQ_API_KEY=your_groq_api_key_here
```

### 3. Local Development (Full App)

**Backend:**
```bash
cd backend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt  # Or create manual setup as per walkthrough
python main.py
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

### 4. Vercel Deployment
The `api/generate.js` file is ready for Vercel deployment. Ensure `GROQ_API_KEY` is set in your Vercel project settings.

---
Built with ⚡ by AI Agents
