# Intermediate Sums
# You will be given a list of numbers. After every tenth element, add an additional element containing the sum of those ten values. If the list does not end aligned evenly with ten elements, add one last sum that includes those last elements not yet been included in one of the earlier sums. Given the array [1,2,1,2,1,2,1,2,1,2,1,2,1,2], change it to [1,2,1,2,1,2,1,2,1,2,15,1,2,1,2,6]

def intermediate_sums(list):
    sum = 0
    chunk = 10

    #loop through the list in chunks of 10
    # (the incrementer is 11 b/c the sum is inserted into the list after each group of 10)
    for i in range(0, len(list), 11):
        print(f"------i loop {i}------\nlist[i] = {list[i]}")
        print(f"len(list)-i = {len(list)-i}")
        #check list length at each chunk to determine sum workflow
        if len(list)-i > 10:
            for j in range(i, chunk):   #loop through the first chunk of 10
                print(f"------j loop {j}------")
                print(f"chunk = {chunk}")
                sum += list[j]      #sum values for the chunk of 10
                print(f"sum = {sum}")
            print(list)

            #loop through remaining list indecies to make room for sum    
            list.append(list[len(list)-1])
            print(list)
            print(f"chunk = {chunk}")
            for k in range(len(list)-1, chunk, -1):
                print(f"------k loop {k}------")
                print(list)
                list[k-1] = list[k-2]
                print(list)
            print(f"sum = {sum}")
            print(f"j+1 = {j+1}")
            print(f"list[j+1] = {list[j+1]}")
            list[chunk] = sum         #insert the sum into the list
            print(list)
        else:
            for l in range(i,len(list)):
                print(f"l = {l}")
                sum += list[l]
            list.append(sum)
        sum = 0     #reset the sum for the next chunk
        chunk *= 2

    return list


print(intermediate_sums([1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5]))