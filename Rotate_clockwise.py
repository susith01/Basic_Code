arr= [1, 2, 3]
k=4
for _ in range(k):
    if k<5:
        first = arr.pop(0)   
        arr.append(first)   
        
print(arr)
