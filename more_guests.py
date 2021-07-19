guests = ["leonardo", "michelangelo", "donatello", "raphael"]
for guest in guests:
    print(f"It would be an honnor to have you at my party tonight Mr. {guest.title()}")
print("I just found a bigger dinner table!")
guests.insert(0, "splinter")
guests.insert(2, "casey")
guests.append("april")
for guest in guests:
    print(f"It would be an honnor to have you at my party totnight {guest.title()}")