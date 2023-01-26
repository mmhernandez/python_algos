# Remove At
# Given a list and an index as arguments, write a function to remove and return the list value at that index and print the shortened list. Do this without using built-in list methods except pop().
# For example: 
# - For input [1,2,3,4,5] and 2, print [1,2,4,5], return 3

def removeAt(list, index):
    removed_value = list.pop(index) 
    print(list)
    return removed_value

print(removeAt([1,2,3,4,5],2))
