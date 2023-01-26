# Swap Pairs
# Write a function to swap positions of successive pairs of values of given list. If length is odd, do not change the final element.
# For example: 
# - For input [1,2,3,4], return [2,1,4,3].
# - For input [1,2,3,4,5], return [2,1,4,3,5].  
# - For input ["Brian",True,42], return [True,"Brian",42]. 
# Do this without using any built-in list methods.

def swapPairs(list):
    for i in range(0,len(list)-1,2):
        temp = list[i]       #hold the pair's first list value
        list[i] = list[i+1]  #replace the pair's first value with the second
        list[i+1] = temp     #use temp to put the pair's first value into the second
    return list

print(swapPairs([1,2,3,4])) 
print(swapPairs([1,2,3,4,5,6,7,8,9,10,11,12,13]))  
print(swapPairs(["Brian",True,42]))
