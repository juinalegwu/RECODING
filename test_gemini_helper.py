 
from gemini_helper import suggest_solution

ticket = {
    "id": "T007",
    "title": "Internet down",
    "category": "Network",
    "urgency": "high",
    "priority": "critical"
}

suggestions = suggest_solution(ticket)

print("\nTroubleshooting suggestions:")
print(suggestions)
 