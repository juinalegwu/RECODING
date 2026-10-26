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


with open("tickets.json", "r") as file:
    tickets = json.load(file)


 
while True:
    print("\n===== TICKET SYSTEM =====")
    print("1. Display all tickets")
    print("2. Find a ticket")
    print("3. Update ticket status")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        show_tickets(tickets)

    elif choice == "2":
        ticket_id = input("Enter ticket ID: ")
        result = find_ticket(tickets, ticket_id)

        if result is not None:
            print("ID:", result["id"])
            print("Title:", result["title"])
            print("Status:", result["status"])
        else:
            print("Ticket not found")

    elif choice == "3":
        ticket_id = input("Enter ticket ID: ")
        result = find_ticket(tickets, ticket_id)

        if result is not None:
            print("Current status:", result["status"])
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

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Choose 1, 2, 3, or 4.")
 