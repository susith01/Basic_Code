#Method 1

arr= [1, 2, 3]
k=4
for _ in range(k):
    if k<5:
        first = arr.pop(0)   
        arr.append(first)   
print(arr)

#Method 2

arr= [1,2,3,4,5]
k=4
left=arr[k:]+arr[:k]
right=arr[-k:]+arr[:-k]
print(left)
print(right)