# List: Reverse
# Given a numerical list reverse the order of values, in-place. The reversed list should have the same length, with existing elements moved to other indices so that order of elements is reversed. Working ‘in-place’ means that you cannot use a second list– you must move values within the list that you are given. As always, do not use built-in list functions.

def reverse(list):
    #iterate through half the list since we're reversing
    for i in range(int(len(list)/2)): 
        #swap outermost pairs, moving inward in the list with each loop
        temp = list[i]           #hold the pair's right-side list value
        list[i] = list[len(list)-1-i]  #replace the pair's right-side value with the left-side
        list[len(list)-1-i] = temp            #use temp to put the pair's right-side value into the left-side
        
    return list

print(reverse(['g', 'f', 'e', 'd', 'c', 'b', 'a']))
print(reverse(['j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']))
