# Intermediate Sums
# You will be given a list of numbers. After every tenth element, add an additional element containing the sum of those ten values. If the list does not end aligned evenly with ten elements, add one last sum that includes those last elements not yet been included in one of the earlier sums. Given the array [1,2,1,2,1,2,1,2,1,2,1,2,1,2], change it to [1,2,1,2,1,2,1,2,1,2,15,1,2,1,2,6]

def intermediate_sums(list):
    sum = 0
    chunk = 10

    #loop through the list in chunks of 10
    # the incrementer is 11 b/c the sum is inserted into the list after each group of 10
    # the high-bound of the range needs to be increased to include the additional sum values being inserted in
    for i in range(0, len(list) + int((len(list)/10)) - 1, 11):
        #check list length at each chunk to determine sum workflow
        if len(list)-i > 10:
            for j in range(i, chunk):   #loop through the chunk of 10
                sum += list[j]          #sum values for the chunk of 10

            #append the last list value to the end of the list, so everything can move forward one place in the list to make room for the sum of the chunk of 10 
            list.append(list[len(list)-1])

            #loop through remaining list indecies to make room for sum 
            for k in range(len(list)-1, chunk, -1):
                list[k-1] = list[k-2]

            list[chunk] = sum   #insert the sum into the list at the end of the chunk
        else:
            for l in range(i,len(list)):
                sum += list[l]
            list.append(sum)
        
        sum = 0             #reset the sum for the next chunk
        chunk = chunk + 11  #increase the chunk variable for the next group of 10 (increases by 11 to account for additional index inserted with the chunk's sum)
    
    return list

print(intermediate_sums([1,2,3,4,5,6]))
print(intermediate_sums([1,2,3,4,5,6,7,8,9,10]))
print(intermediate_sums([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]))
print(intermediate_sums([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))
print(intermediate_sums([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]))
