"""Simple Command-Line Interface(CLI) Application"""

import json
import os  

#validate user input to prevent empty titles and descriptions.
FILE = "ticket.json"
def create_ticket():
    ticket_id = input("Enter ticket_id: ").strip()
    title = input("Enter ticket title: ").strip()
    description = input("Enter ticket description: ").strip()

    if not title or not description:
        print("Error: Title and description cannot be empty.")
        return
    
#store tickets in tickets.json using python's json module.
    tickets = []
    if os.path.exists(FILE):
        try:
            with open(FILE, "r") as f:
                tickets = json.load(f)
        except (json.JSONDECODER):
            print("Error reading tickets file.")
            return
        
    ticket = {
        "ticket_id": ticket_id,
        "title": title,
        "description": description  
    }
    tickets.append(ticket)
#create JSON file automatically.
    try:
        with open(FILE, "w") as f:
            json.dump(tickets, f, indent=4)

        print("Ticket created by Juliet successfully!")
        print()

    except OSError:
        print("Error saving ticket.")
if __name__ == "__main__":
    create_ticket()
      