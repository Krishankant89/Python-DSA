def insertion_sort(arr):
    
    n = len(arr)
    
    for i in range(1,n):
        key = arr[i]
        
        j = i -1
        
        while j >= 0 and arr[j]> key:
            arr[j+1] = arr[j]
            j -= 1
            
        arr[j+1] = key
        
    return arr
arr = [24, 11, 45, 67, 56, 6]
print(insertion_sort(arr))


'''
In this code we're using the insertion sort to sort our array in which we're 
taking 'n' as the length or array and now we have the for loop that runs from
element 1 to last of array 'n' we're taking 1 index value cause we're assuming
that the index 0 element is already sorted and then that element index 1
is the key value and we have value of j which is i-1 
now in the while loop we have the condition where it check that if the value of j
is greater or equal than the 0 and the arr[j] is greater than the key if True
then it substitute the values and now j -= 1 which exits the loop cause the condition is false
then arr[j+1] = key we have j = -1 so this becomes like this arr[-1+1] = key
arr[0] = key so array becomes like this [11,24,45,67,56,6]

'''