arr = [10,20,30,40,50]

for i in range(1, len(arr)):
    arr[i -1] = arr[i]
    
arr.pop()

print(arr)

'''
The shifting of elements from right to left
and during the shifting the elements gets overwritten like this

The Overwriting Process
Step 1: Index 1 (20) overwrites Index 0 (10).

Array becomes: [20, 20, 30, 40] (The 10 is now gone)

Step 2: Index 2 (30) overwrites Index 1 (20).

Array becomes: [20, 30, 30, 40]

Step 3: Index 3 (40) overwrites Index 2 (30).

Array becomes: [20, 30, 40, 40]


Complexity AnalysisTime Complexity: $O(n)$, where $n$ is the number of elements in the array. Because you have to move every single remaining element, the time it takes grows linearly with the size of the array. If you have 1,000,000 elements, you have to perform 999,999 shift operations.Space Complexity: $O(1)$ (In-place). You aren't creating a new array; you are modifying the existing one, so it uses no extra memory.

'''
