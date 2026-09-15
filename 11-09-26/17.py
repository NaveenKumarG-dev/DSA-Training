
arr = [50, 40, 70, 60, 90]
l = len(arr)

for i in range(l//2):
    arr[i],arr[l-1-i] = arr[l-1-i],arr[i]

print(arr)