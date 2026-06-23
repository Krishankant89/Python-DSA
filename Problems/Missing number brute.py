def missing_number(arr,n):
    for i in range(n + 1):
        flag = 0
        
        for j in range(len(arr)):
            if arr[j] == i:
                flag = 1
                break
            
        if flag == 0:
            return i
        
arr = [0,1,2,4,5]
n = 5
print(missing_number(arr,n))