import time

#  Create an empty list called my_list
my_list = []
print("🌟 Our list is born! An empty vessel ready for magical numbers!")

#  Append the following elements to my_list: 10, 20, 30, 40
print("\n🎩 Adding numbers to the list one by one...")
numbers_to_add = [10, 20, 30, 40]
for num in numbers_to_add:
    my_list.append(num)
    print(f"Added {num}! 🪄 Current list: {my_list}")
    time.sleep(1)  # Adding a short delay for dramatic effect

#  Insert the value 15 at the second position in the list
print("\n🚀 Inserting 15 at the second position...")
my_list.insert(1, 15)
print(f"✨ List magic complete! Now it's: {my_list}")

#  Extend my_list with another list: [50, 60, 70]
print("\n🎉 Extending the list with [50, 60, 70]...")
my_list.extend([50, 60, 70])
print(f"Voila! The list has grown: {my_list}")

#  Remove the last element from my_list
print("\n💨 Removing the last element...")
my_list.pop()
print(f"Whoosh! The list is now: {my_list}")

#  Sort my_list in ascending order
print("\n🔄 Sorting the list in ascending order...")
my_list.sort()
print(f"✨ Sorted list: {my_list}")

#  Find and print the index of the value 30 in my_list
print("\n🔍 Searching for the value 30...")
try:
    index_of_30 = my_list.index(30)
    print(f"🎉 Found 30! It's at index {index_of_30}.")
except ValueError:
    print("😱 Oops! 30 is not in the list.")

# Final state of the list
print("\n🎨 The grand finale! Our final list is:", my_list)

# A fun ending
print("\n🎆 Thanks for joining this list adventure! 🎆")
