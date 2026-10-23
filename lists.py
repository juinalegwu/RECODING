tickets = ["WiFi problem", "Broken keyboard", "Software error"]

print(tickets)
print(tickets[0])
print(tickets[1])
print(tickets[2])
tickets.append("Network problem")
tickets.remove("Software error")
print(tickets)

print(len(tickets))

for ticket in tickets:
    print(ticket)

for number, ticket in enumerate(tickets, start=1):
    print(number, ticket)
