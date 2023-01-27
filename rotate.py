# Rotate
# Implement get_shwifty(input, shiftBy) that accepts a list and offset. Shift input’s values to the right by that amount. ‘Wrap-around’ any values that shift off the list's end to the other side, so that no data is lost. Operate in-place: given ([1,2,3],1), change the list to [3,1,2]. Don’t use built-in functions.

def get_shwifty(input, shiftyBy):
    counter = 0
    while counter < shiftyBy:
        temp = input[len(input)-1]    #store last value in a temp variable
        for z in range(len(input)-1, 0, -1):    #loop through the full list and shift indecies to the right
            input[z] = input[z-1]
        input[0] = temp    #place temp in index 0
        counter += 1
    return input 

print(get_shwifty([1,2,3],1))  #output should be [3,1,2]
print(get_shwifty(['c', 'd', 'e', 'f', 'g', 'a', 'b'], 2))  #output should be in alphabetical order
print(get_shwifty(['e', 'f', 'g', 'h', 'i', 'j', 'k', 'a', 'b', 'c', 'd'], 4)) 
