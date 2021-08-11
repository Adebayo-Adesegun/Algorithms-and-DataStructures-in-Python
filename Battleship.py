

from typing import List
# Write any import statements here
"""
    Sample Test Case #1
    R = 2
    C = 3
    G = 0 0 1
        1 0 1
    
    Expected Return Value = 0.50000000
    
    Sample Test Case #2
    R = 2
    C = 2
    G = 1 1
        1 1
        
    Expected Return Value = 1.00000000
    
"""
def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
    hits = 0
    number_of_elements = R * C
    
    for item in G:
        for inner_item in item:
             hits += inner_item
    
    
    
    hit_probability = hits/number_of_elements

    return hit_probability


G = [[0,0,1], [1,0,1]]
getHitProbability(2,3, G)


