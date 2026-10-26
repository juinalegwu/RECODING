import json


def find_ticket(tickets, ticket_id):
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            return ticket

    return None


def show_tickets(tickets):
    if not tickets:
        print("No tickets found.")
        return

    for ticket in tickets:
        print("ID:", ticket["id"])
        print("Title:", ticket["title"])
        print("Status:", ticket["status"])
        print("-------------------")


def update_status(tickets, ticket_id, new_status):
    allowed_statuses = ["open", "in_progress", "resolved"]
    new_status = new_status.strip().lower()

    if new_status not in allowed_statuses:
        return False

    ticket = find_ticket(tickets, ticket_id)

    if ticket is None:
        return False

    current_status = ticket["status"]

    if current_status == "open" and new_status == "in_progress":
        ticket["status"] = new_status
        return True

    elif current_status == "in_progress" and new_status == "resolved":
        ticket["status"] = new_status
        return True

    elif current_status == "resolved" and new_status == "open":
        ticket["status"] = new_status
        return True

    return False


def create_ticket(tickets, title):
    title = title.strip()

    if not title:
        return None

    # Find the highest existing ticket number.
    highest_number = 0

    for ticket in tickets:
        ticket_id = ticket["id"]

        if ticket_id.startswith("T") and ticket_id[1:].isdigit():
            number = int(ticket_id[1:])

            if number > highest_number:
                highest_number = number

    new_id = f"T{highest_number + 1:03d}"

    ticket = {
        "id": new_id,
        "title": title,
        "status": "open"
    }

    tickets.append(ticket)

    return ticket


# Load tickets from the JSON file.
with open("tickets.json", "r") as file:
    tickets = json.load(file)


while True:
    print("\n===== TICKET SYSTEM =====")
    print("1. Display all tickets")
    print("2. Find a ticket")
    print("3. Update ticket status")
    print("4. Create a new ticket")
    print("5. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        show_tickets(tickets)

    elif choice == "2":
        ticket_id = input("Enter ticket ID: ").strip()
        result = find_ticket(tickets, ticket_id)

        if result is not None:
            print("ID:", result["id"])
            print("Title:", result["title"])
            print("Status:", result["status"])
        else:
            print("Ticket not found.")

    elif choice == "3":
        ticket_id = input("Enter ticket ID: ").strip()
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
                print(
                    "Status change not allowed. "
                    "Check the ticket's current status."
                )
        else:
            print("Ticket not found.")

    elif choice == "4":
        title = input("Enter ticket title: ").strip()
        ticket = create_ticket(tickets, title)

        if ticket is not None:
            with open("tickets.json", "w") as file:
                json.dump(tickets, file, indent=4)

            print("Ticket created successfully!")
            print("Ticket ID:", ticket["id"])
        else:
            print("Ticket title cannot be empty.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Choose 1, 2, 3, 4, or 5.")
 