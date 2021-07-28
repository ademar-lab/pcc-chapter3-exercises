guests = ["leonardo", "michelangelo", "donatello", "raphael"]
for guest in guests:
    print(f"It would be an honnor to have you at my party tonight Mr. {guest.title()}")
print(f"{guests[-1]].title()} can't make it to the party tonight")
guests[-1] = "venus de milo"
for guest in guests:
    print(f"It would be an honnor to have you at my party tonight Mr. {guest.title()}")