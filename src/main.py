from dotenv import load_dotenv
import sys
import os

sys.path.append(os.path.dirname(__file__))

load_dotenv()

from graph import create_graph

graph = create_graph()

state = {
    "query": "what skills does AI Engineer need?",
    "search_results": "",
    "analysis": "",
    "report": "",
    "feedback": ""
}


print("Starting Research Multi-Agent System...")
result = graph.invoke(state)



print("\n" + "="*50)
print("📊 FINAL REPORT:")
print("="*50)
print(result["report"])

print("\n" + "="*50)
print("🔍 CRITIC FEEDBACK:")
print("="*50)
print(result["feedback"])