import json
from gemini_helper import suggest_solution


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
        print("Category:", ticket.get("category", "Not set"))
        print("Urgency:", ticket.get("urgency", "Not set"))
        print("Affected users:", ticket.get("affected_users", "Not set"))
        print("Priority:", ticket.get("priority", "Not set"))
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


def calculate_priority(urgency, affected_users):
    urgency = urgency.strip().lower()

    if urgency == "high" and affected_users >= 10:
        return "critical"

    elif urgency == "high" or affected_users >= 10:
        return "high"

    elif urgency == "medium" or affected_users >= 3:
        return "medium"

    else:
        return "low"


def create_ticket(tickets, title, category, urgency, affected_users):
    title = title.strip()
    category = category.strip().title()
    urgency = urgency.strip().lower()

    allowed_categories = ["Network", "Hardware", "Software", "Other"]
    allowed_urgencies = ["low", "medium", "high"]

    if not title or category not in allowed_categories:
        return None

    if urgency not in allowed_urgencies:
        return None

    if isinstance(affected_users, bool) or not isinstance(affected_users, int):
        return None

    if affected_users <= 0:
        return None

    priority = calculate_priority(urgency, affected_users)

    highest_number = 0

    for ticket in tickets:
        ticket_id = ticket["id"]

        if ticket_id.startswith("T") and ticket_id[1:].isdigit():
            number = int(ticket_id[1:])
            highest_number = max(highest_number, number)

    new_id = f"T{highest_number + 1:03d}"

    ticket = {
        "id": new_id,
        "title": title,
        "category": category,
        "urgency": urgency,
        "affected_users": affected_users,
        "priority": priority,
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
    print("5. AI Troubleshooting Suggestions")
    print("6. Exit")

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
            print("Category:", result.get("category", "Not set"))
            print("Urgency:", result.get("urgency", "Not set"))
            print("Affected users:", result.get("affected_users", "Not set"))
            print("Priority:", result.get("priority", "Not set"))
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
        title = input("Enter ticket title: ")
        category = input(
            "Enter category (Network, Hardware, Software, Other): "
        )
        urgency = input("Enter urgency (low, medium, high): ")

        try:
            affected_users = int(
                input("How many users are affected? ")
            )
        except ValueError:
            print("Please enter a whole number.")
            continue

        ticket = create_ticket(
            tickets, title, category, urgency, affected_users
        )

        if ticket is not None:
            with open("tickets.json", "w") as file:
                json.dump(tickets, file, indent=4)

            print("Ticket created successfully!")
            print("Ticket ID:", ticket["id"])
            print("Priority:", ticket["priority"])
        else:
            print(
                "Invalid title, category, urgency, or number of users."
            )

    elif choice == "5":
        ticket_id = input(
            "Enter ticket ID for AI troubleshooting: "
        ).strip()

        ticket = find_ticket(tickets, ticket_id)

        if ticket is None:
            print("Ticket not found.")
        else:
            suggestions = suggest_solution(ticket)
            print("\n===== AI TROUBLESHOOTING SUGGESTIONS =====")
            print(suggestions)

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please select an option from 1 to 6.")