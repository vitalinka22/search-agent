from langgraph.graph import StateGraph, END
from typing import TypedDict

import sys 
import os 
sys.path.append(os.path.dirname(__file__))

from agents import search_agent, analysis_agent, report_agent, critic_agent

class ResearchState (TypedDict):
    query : str
    search_results : str
    analysis : str
    report : str
    feedback : str
    
def create_graph():
    graph = StateGraph(ResearchState)
    
    graph.add_node("search", search_agent)
    graph.add_node("analysis", analysis_agent)
    graph.add_node("report", report_agent)
    graph.add_node("critic", critic_agent)   
    
    graph.set_entry_point("search")
    
    graph.add_edge("search", "analysis")
    graph.add_edge("analysis", "report")
    graph.add_edge("report", "critic")
    graph.add_edge("critic", END)
    
    return graph.compile()