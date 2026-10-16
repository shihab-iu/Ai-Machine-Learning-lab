def simple_reflex_vacuum_agent(location, status):
    if status == "Dirty":
        return "Suck"
    return "Right" if location == "A" else "Left"
environment = {"A": "Dirty", "B": "Dirty"}
location = "A"
for step in range(6):
    status = environment[location]
    action = simple_reflex_vacuum_agent(location, status)
    print(step + 1, location, status, "->", action)
    if action == "Suck":
        environment[location] = "Clean"
    elif action == "Right":
        location = "B"
    elif action == "Left":
        location = "A"
print("Final environment:", environment)