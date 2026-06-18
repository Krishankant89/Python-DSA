def move_zeros(arr):
    temp = []
    
    for num in arr:
        if num != 0:
            temp.append(num)
            
    zeros = len(arr) - len(temp)
    
    for _ in range(zeros):
        temp.append(0)
        
    return temp

arr = [1,0,2,0,3,0,4]
print(move_zeros(arr))