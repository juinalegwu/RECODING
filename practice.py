import json

tickets = [
    {"id": "T001", "title": "wifi", "category": "Network", "status": "open"},
    {"id": "T002", "title": "keyboard", "category": "Hardware", "status": "closed"},
    {"id": "T003", "title": "poor network", "category": "Network", "status": "in_progress"},
    {"id": "T004", "title": "mouse", "category": "Hardware", "status": "open"},
]

with open ("tickets.json", "w") as f:
    json.dump(tickets, f, indent=2)
