

arr = [100, 200, 150, 300]
res = []
for i in range(len(arr)):
    res.append(sum(arr[:i+1]))

print(res)