def merge_sort(arr,low,high):
    if low >= high:
        return
    
    mid = (low + high) // 2
    #sort left half
    merge_sort(arr,low,mid)
    #sort right half
    merge_sort(arr,mid+1,high)
    #merge the two sorted halves
    merge(arr,low,mid,high)
    
    
def merge(arr,low,mid,high):
    temp = []
    
    left = low
    right = mid + 1
    #compare elements from both halves
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    #copy remaining elements from left half
    while left <= mid:
        temp.append(arr[left])
        left += 1
    #copy remaining elements from right half
    while right <= high:
        temp.append(arr[right])
        right += 1
        
    for i in range(len(temp)):
        arr[low + i] = temp[i]
        
arr = [8, 3, 5, 4, 7, 6, 1, 2]

merge_sort(arr, 0, len(arr) - 1)

print("Sorted Array:", arr)