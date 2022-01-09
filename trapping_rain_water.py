


# Brute Foce Solution

def trap(height):
        """
        :type height: List[int]
        :rtype: int
        """

        total_water = 0
        for p in range(len(height)):

            leftp = p
            rightp = p
            max_left = 0
            max_right = 0
            
            print (f'p -> {p}')
            
            #Look for the greatest value to the left of p
            while leftp >= 0:                              
                max_left = max(max_left, height[leftp])
                leftp -= 1
                print(f' max_left -> {max_left}')
                
            #look for the greatest value to the right of p
            while rightp < len(height):
                max_right = max(max_right, height[rightp])
                rightp += 1
                print(f'rightp {rightp} -> max_right -> {max_right}')


            current_water = min(max_left, max_right) - height[p]
            print(f'current_water : {current_water}')

            if current_water > 0:
                total_water += current_water
                
            print(f'total_water : {total_water}')

        return total_water
    
    
# Optimized Solution

