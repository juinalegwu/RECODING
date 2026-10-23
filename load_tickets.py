 
import json

with open("tickets.json", "r") as file:
    tickets = json.load(file)


def find_ticket(tickets, ticket_id):
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            return ticket

    return None


ticket_id = input("Enter ticket ID: ")

result = find_ticket(tickets, ticket_id)
 
def update_status(tickets, ticket_id, new_status):
    ticket = find_ticket(tickets, ticket_id)

    if ticket is not None:
        ticket["status"] = new_status
        return True

    return False
 
if result is not None:
    print("ID:", result["id"])
    print("Title:", result["title"])
    print("Status:", result["status"])
else:
    print("Ticket not found")
 