# This program uses all the functions and methods that
# the chapter 3 of the Python Crash Course covers

random_words = ["java", "windows", "git", "linux", "css", "html", "go"]
random_words.append("macos")
print(f"Adding \"macos\" to the end of the list with the append() method:\n\t{random_words}")
random_words.insert(3, "algorithms")
print(f"Inserting \"algorithms\" into the middle of the list with the insert() method:\n\t{random_words}")
del random_words[0]
print(f"Removing the first element of the list by using the del statement:\n\t{random_words}")
popped_item = random_words.pop()
print(f"Popping the \"{popped_item}\" item and storing it in the popped_item variable\n\t{random_words}")
popped_item = random_words.pop(3)
print(f"Popping by position the fourth item({popped_item}) of the list and storing it in the popped_item variable:\n\t{random_words}")
removed_item = random_words.remove("html")
print(f"Removing by value the \"{removed_item}\" item and storing it into the removed_item value:\n\t{random_words}")
print(f"Sorting the list temporarily with the sorted() function:\n\t{sorted(random_words)}")
random_words.reverse()
print(f"Reversing the list permanently with the reverse() method:\n\t {random_words}")
random_words.sort()
print(f"Sorting the list permanently with the sort() method:\n\t {random_words}")
print(f"Finding the lenght of the list with the len() function\n\t The lenght of the list is {len(random_words)}")