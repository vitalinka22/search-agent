from langchain_google_genai import ChatGoogleGenerativeAI
from tavily import TavilyClient
from dotenv import load_dotenv
import os 

load_dotenv()

llm = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash')
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def search_agent(state:dict) -> dict:
    """Agent 1 - searches for information"""
    
    query = state["query"]
    
    print(f"Search agent: searching for {query}")
    
    result = tavily.search(
        query = query, 
        max_results = 5
    )
    
    search_text = ""
    
    for r in result["results"]:
        search_text += f"Source: {r['url']}\n"
        search_text += f"Content {r['content']}\n\n"
        
    state["search_results"] = search_text    
    
    print(f"Found {len(result['results'])} results")
    
    return state

def analysis_agent(state:dict) -> dict:
    """
    Agent 2 - analyzes search results
    """
    
    prompt = f"""
    You are an expert analyst. Analyze the following search results and extract the most important insights.
    Original Query: {state["query"]}
    
    Search Reluts: 
    {state["search_results"]}
    
    Provide:
    1. Key findings (3-5 bullet points)
    2. Main trends identified
    3. Any contradictions or gaps
    
    """
    
    respond = llm.invoke(prompt)
    state["analysis"] = respond.content
    
    print ("Analysis Agent: complete")
    
    return state
    

def report_agent(state: dict) -> dict:
    """Agent 3 - writes structured report"""
    
    print("Report Agent : writing report ...")
    
    prompt = f"""
    You are a professional report writer.
    Write a clear structured report based on this analysis.
    
    Original Query: {state["query"]}
    
    Analysis: {state["analysis"]}
    
    Write a report with:
    - Executive Summary (2-3 sentences)
    - Key Findings (bullet points)
    - Conclusion
    
    Keep it concise and professional.
    """
    
    response = llm.invoke(prompt)
    
    state["report"] = response.content
    
    print("Report Agent : complete")
    
    return state

def critic_agent(state : dict) -> dict:
    
    """Agent 4 - reviws report quality"""
    
    print("Critic Agent : reviewing report ...")
    
    prompt = f"""
    You are a critical reviewer. Review this report and provide feedback.
    
    Original Query: {state["query"]}
    
    Report:
    {state["report"]}
    
    Evaluate:
    1. Does it answer the original query? (yes/no + explanation)
    2. What is missing?
    3. Quality score: 1-10
    4. One sentence summary of the report quality
    """
    
    response = llm.invoke(prompt)
    state["feedback"] = response.content
    
    print(" Critic Agent: complete")
    
    return state
    

