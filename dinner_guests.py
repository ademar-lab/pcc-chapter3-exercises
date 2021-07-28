guests = ["leonardo", "michelangelo", "donatello", "raphael"]
for guest in guests:
    print(f"It would be an honnor to have you at my party tonight Mr. {guest.title()}")
print("I just found a bigger dinner table!")
guests.insert(0, "splinter")
guests.insert(2, "casey")
guests.append("april")
for guest in guests:
    print(f"It would be an honnor to have you at my party totnight {guest.title()}")
num_guests =  len(guests)
print(f"The number of people who is invited tonight is: {len(guests)}")