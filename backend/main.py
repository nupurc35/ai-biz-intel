from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import agents

app = FastAPI(title="AI Business Intelligence API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnalysisRequest(BaseModel):
    topic: str
    industry: str

class AnalysisResponse(BaseModel):
    topic: str
    industry: str
    analysis: str
    strategies: str
    summary: str
    agents_used: List[str]

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.post("/analyze", response_model=AnalysisResponse)
async def run_analysis(request: AnalysisRequest):
    try:
        # Step 1: Market Analysis
        analysis = await agents.analyst_agent(request.topic, request.industry)
        
        # Step 2: Actionable Strategies
        strategies = await agents.strategist_agent(analysis, request.topic)
        
        # Step 3: Executive Summary
        summary = await agents.summary_agent(analysis, strategies, request.topic)
        
        return {
            "topic": request.topic,
            "industry": request.industry,
            "analysis": analysis,
            "strategies": strategies,
            "summary": summary,
            "agents_used": ["Analyst", "Strategist", "Summarizer"]
        }
    except Exception as e:
        print(f"Error during analysis: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
