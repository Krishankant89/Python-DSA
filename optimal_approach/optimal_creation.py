size = int(input("Enter the size:"))

arr = list(map(int,input("Enter elements:").split()))

if len(arr) != size:
    print("Invalid number of elements")
else:
    print(arr)