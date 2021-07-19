guests = ["leonardo", "michelangelo", "donatello", "raphael"]
for guest in guests:
    print(f"It would be an honnor to have you at my party tonight Mr. {guest.title()}")
print("I just found a bigger dinner table!")
guests.insert(0, "splinter")
guests.insert(2, "casey")
guests.append("april")
for guest in guests:
    print(f"It would be an honnor to have you at my party totnight {guest.title()}")
print("I'm sorry but now I just have space for two of you.")
max_num_guests = 2
while len(guests) > max_num_guests:
    popped_guest = guests.pop()
    print(f"I'm sorry {popped_guest.title()}, but there's no room for you anymore")
for guest in guests:
    print(f"You're still invited {guest.title()}")
del guests[0]
del guests[0]
print(guests)