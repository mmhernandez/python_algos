# Zip It
# Create a standalone function that accepts two lists and combines their values sequentially into a new list, at alternating indices starting with first list. 
# Extra values from either list should be included afterward. 
# Given [1,2] and [10,20,30,40], return new list containing [1,10,2,20,30,40].
#     Second: combine the two list’s values into the first list, instead of into a new list. Much more fun!

def zip_it(list1, list2):
    flag = True 
    i = 1

    for item in list2: 
        if flag:        
            temp = list1[i]  
            list1[i] = item    
            list1.append(list1[(len(list1)-1)])
            for j in range(len(list1)-2,i+1,-1):
                list1[j] = list1[j-1]
            list1[i+1] = temp  
            if (len(list1)-i) <= 2:
                flag = False 
            i += 2
        else:
            list1.append(item)  
    return list1

print(zip_it([1, 2], [10, 20, 30, 40]))
print(zip_it([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))
print(zip_it([1, 3, 5, 7, 9, 11, 13, 15], [2, 4, 6]))


#* Same function below, with comments for future me :)
# def zip_it(list1, list2):
#     flag = True     #create a flag to determine if the 1st list is longer than the 2nd
#     i = 1           #incrementer for conditional

#     for item in list2:  #loop through 2nd list, to add each item inside 1st list
#         if flag:        
#             temp = list1[i]     #placeholder for 1st list item that needs to jump forward to make room for the 2nd list's item
#             list1[i] = item     #place the value from the 2nd list into the 1st list

#             #start moving each of the items in the 1st list forward to make room for the 2nd list's item
#             list1.append(list1[(len(list1)-1)])
#             for j in range(len(list1)-2,i+1,-1):
#                 list1[j] = list1[j-1]
            
#             list1[i+1] = temp   #place the value from the 1st list that was being held by temp back into the 1st list (after where the value from the 2nd list was inserted)

#             #check if the first list is running out of room for more values (e.g. it's shorter than the 2nd list)
#             if (len(list1)-i) <= 2:
#                 flag = False
#             #if not, leapfrog the incrementer forward two spaces and repeat    
#             i += 2
#         else:
#             list1.append(item)  #if the 2nd list is longer than the 1st, append each of the extra values onto the end of the list
#     return list1