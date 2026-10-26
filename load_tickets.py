import json


def find_ticket(tickets, ticket_id):
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            return ticket

    return None


def show_tickets(tickets):
    for ticket in tickets:
        print("ID:", ticket["id"])
        print("Title:", ticket["title"])
        print("Status:", ticket["status"])
        print("-------------------")


def update_status(tickets, ticket_id, new_status):
    allowed_statuses = ["open", "in_progress", "resolved"]

    if new_status not in allowed_statuses:
        return False

    ticket = find_ticket(tickets, ticket_id)

    if ticket is not None:
        ticket["status"] = new_status
        return True

    return False


# Load tickets from the JSON file
with open("tickets.json", "r") as file:
    tickets = json.load(file)


# Display all tickets
show_tickets(tickets)


# Ask for a ticket ID
ticket_id = input("Enter ticket ID: ")

result = find_ticket(tickets, ticket_id)


# Check whether the ticket exists
if result is not None:
    print("ID:", result["id"])
    print("Title:", result["title"])
    print("Status:", result["status"])

    new_status = input("Enter new status: ")

    updated = update_status(tickets, ticket_id, new_status)

    if updated:
        with open("tickets.json", "w") as file:
            json.dump(tickets, file, indent=4)

        print("Ticket updated successfully!")
    else:
        print("Invalid status. Use open, in_progress, or resolved.")

else:
    print("Ticket not found")
 