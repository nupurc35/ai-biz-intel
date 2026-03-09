import os
import asyncio
from groq import AsyncGroq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq client
client = AsyncGroq(api_key=os.getenv("GROQ_API_KEY"))

MODEL = "llama-3.3-70b-versatile"
TEMPERATURE = 0.7

async def analyst_agent(topic, industry):
    """
    Analyzes markets, identifies trends, key players, risks, and opportunities.
    """
    system_prompt = (
        "You are a senior business analyst. Your job is to analyze markets, "
        "identify trends, key players, risks, and opportunities. Be data-driven and specific."
    )
    user_prompt = (
        f"Analyze the {topic} in the {industry} industry. Cover: market size, "
        "key trends, top competitors, main risks, biggest opportunities. Be thorough and specific."
    )
    
    response = await client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=TEMPERATURE
    )
    return response.choices[0].message.content

async def strategist_agent(analysis, topic):
    """
    Receives market analysis and creates concrete actionable strategies.
    """
    system_prompt = (
        "You are a senior business strategist. You receive market analysis and "
        "create concrete actionable strategies."
    )
    user_prompt = (
        f"Based on this analysis: {analysis}. Create 5 specific actionable strategies "
        f"for a business entering or growing in this space. For each strategy include: "
        "strategy name, description, timeline, expected impact, and required resources."
    )
    
    response = await client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=TEMPERATURE
    )
    return response.choices[0].message.content

async def summary_agent(analysis, strategies, topic):
    """
    Writes crisp, clear executive briefings.
    """
    system_prompt = (
        "You are a C-suite executive assistant who writes crisp, clear executive briefings. "
        "No fluff, only what matters."
    )
    # Truncate inputs as requested
    user_prompt = (
        f"Create a one-page executive summary for: {topic}. Use this analysis: {analysis[:500]}. "
        f"And these strategies: {strategies[:500]}. Format as: Executive Summary (2 sentences), "
        "Key Findings (3 bullet points), Recommended Actions (3 bullet points), "
        "Risk Warning (1 sentence), Bottom Line (1 sentence)."
    )
    
    response = await client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=TEMPERATURE
    )
    return response.choices[0].message.content
