
arr = [50, 40, 70, 60, 90]
index = [3,  0,  4,  1,  2]
#Output: 40 60 90 50 70

length = len(arr)
result = [0] * length

for i in range(length):
    result[index[i]] = arr[i]

print(result)