

def max_area_calc(heights):
    max_area = 0
    p1 = 0
    p2 = len(heights) - 1
    
    while p1 < p2:       
        
        height = min(heights[p1], heights[p2])
        width = p2-p1
        area = height * width
        
        max_area = max(area, max_area)
        
        if heights[p1] <= heights[p2]:
            p1 +=1
        else:
            p2 -=1
    
    return max_area

max_area_calc([2,3,4,5,18,17,6])