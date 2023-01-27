# Skyline Heights
# Let’s say you are given a list with heights of consecutive buildings, starting closest to you and extending away. List[-1,7,3] would represent three buildings: first is actually out of view below street level, behind it is second at 7 stories high, third is 3 stories high (hidden behind the 7-story). You are situated at street level. Return a list containing heights of buildings you can see, in order. Given [-1,1,1,7,3] return [1,7]. Given [0,4] return [4]. As always with challenges, do not use built-in list functions.

def skyline(building_list):
    visible_buildings = [] 
    highest_building = 0
    
    #find the tallest buildings sequentially and add to the visible buildings list
    for i in range(0,len(building_list)):   
        if building_list[i] > highest_building:
            highest_building = building_list[i]
            visible_buildings.append(highest_building)

    return visible_buildings

print(skyline([-1,1,1,7,3]))
print(skyline([0,4]))
print(skyline([11,1,1,7,3]))
print(skyline([5,1,6,5,20,12,12,14,22]))
