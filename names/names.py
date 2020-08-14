from binary_search_tree import BSTNode
import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# FAST Implementation without data structure
# for names_2 in names_2:
#     if names_2 in names_1:
#         duplicates.append(names_2)

# First node
bst = BSTNode(names_1[0])

for i in range(1, len(names_1)-1):
    current_name = names_1[i]
    bst.insert(current_name)

for i in range(0, len(names_2)-1):
    current_name = names_2[i]
    if bst.contains(current_name):
        duplicates.append(current_name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
