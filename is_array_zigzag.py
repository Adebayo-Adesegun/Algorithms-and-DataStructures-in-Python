def isZigzag(numbers):
    
    n = len(numbers)
    zig_zag_ret = []


    for zz in range(n):
        if zz + 2 > n - 1 or zz + 1 > n - 1:
            return zig_zag_ret
        
        if numbers[zz] < numbers[zz+1] and numbers[zz+1] > numbers[zz+2]:
            zig_zag_ret.append(1)
        elif numbers[zz] > numbers[zz+1] and numbers[zz+1] < numbers[zz+2]:
            zig_zag_ret.append(1)
        else:
            zig_zag_ret.append(0)
    
    
    return zig_zag_ret
        
        

