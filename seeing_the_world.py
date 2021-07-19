"""This program uses some places around the 
world to showcase how to orginize a list"""

places = ["san francisco", "new zeland", "vancouver", "australia", "cancún"]
print(f"This is the original order of the list:\n\t{places}")
print(f"This is the list sorted temporarily in alphabetical order:\n\t{sorted(places)}")
print(f"Here the list is still in its original order:\n\t{places}")
print(f"This list is sorted temporarily in reverse alphabetical order:\n\t{sorted(places, reverse=True)}")
print(f"Here the list is still in its original order:\n\t{places}")
places.reverse()
print(f"This list is sorted permanently in reverse order:\n\t{places}")
places.reverse()
print(f"This list is back to its original order:\n\t{places}")
places.sort()
print(f"Now the list is permanently sorted in alphabetical order and it can never return to the original order:\n\t{places}")
places.sort(reverse=True)
print(f"Now the list is permanently sorted in reverse alphabetical order:\n\t{places}")