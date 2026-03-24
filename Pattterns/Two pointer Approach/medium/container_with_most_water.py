#Pattern = opposite side two pointer 
#reason = two check the most water in the container we have to the both end of the as left = 0 and right = len(height) -1 
#we have to find some data solve it 
#width = right - left 
#height = min(height[left],height[right])
#area = width * height 
#so by this max_water intially 0 and now max_water = max(max_water,area)
#and then to iterate if height[left] < height[right] -> left = left + 1 and right = right -1 

def container_most_water(height):
    left = 0 
    right = len(height)-1
    max_water = 0 

    while left < right :
        width = right - left 
        h = min(height[left],height[right])
        area = h * width 

        max_water = max(max_water,area) 

        if height[left] < height[right]:
            left = left + 1
        else:
            right = right - 1
    
    return max_water



height = [1,8,6,2,5,4,8,3,7]
print(container_most_water(height))