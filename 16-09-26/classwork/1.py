"""
Find the first duplicate element in the array
"""

arr = list(map(int,input("").split()))

seen = {}

for i in arr:
    if i in seen.keys():
        print(i)
        break
    seen[i] = 1

print(0)