import json

tickets = [
    {
        "id": "T001",
        "title": "WiFi problem",
        "status": "open"
    },
    {
        "id": "T002",
        "title": "Broken keyboard",
        "status": "in_progress"
    }
]

for ticket in tickets:
    print(ticket["id"], ticket["title"], ticket["status"])
 
for ticket in tickets:
    if ticket["id"] == "T002":
        print(ticket["title"])
 
def find_ticket(tickets, ticket_id):
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            return ticket

    return None

  
print("Tickets saved successfully!")
 
 
ticket_id = input("Enter ticket ID: ")
result = find_ticket(tickets, ticket_id)

if result is not None:
    print("ID:", result["id"])
    print("Title:", result["title"])
    print("Status:", result["status"])
else:
    print("Ticket not found")
 
open_count = 0

for ticket in tickets:
    if ticket["status"] == "in_progress":
        open_count += 1

print("In-progress tickets:", open_count) 
print("Total tickets:", len(tickets))


open_count = 0
in_progress_count = 0
resolved_count = 0 
for ticket in tickets:
    if ticket["status"] == "open":
        open_count += 1
    elif ticket["status"] == "in_progress":
        in_progress_count += 1
    elif ticket["status"] == "resolved":
        resolved_count += 1

print("Open tickets:", open_count)
print("In-progress tickets:", in_progress_count)
print("Resolved tickets:", resolved_count)

 
for ticket in tickets:
    if ticket["id"] == "T001":
        ticket["status"] = "resolved"


with open("tickets.json", "w") as file:
    json.dump(tickets, file, indent=4)


print("Updated status:", tickets[0]["status"])
print("New ticket status:", tickets[0]["status"])