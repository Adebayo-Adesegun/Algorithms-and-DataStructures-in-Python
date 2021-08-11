
"""
    Solved using th shifting pointed technique
"""

def pair_sum(nums,target):
    
        if len(nums) < 2:
            return 0
    
        nums_map = {}
    
        for index,num in enumerate(nums):  
            num_to_find=target-num

            if num_to_find in nums_map: 
                return [index,nums_map[num_to_find]]
            else:
                nums_map[num]=index

        return []
    
pair_sum([1,3,7,9,2],11)