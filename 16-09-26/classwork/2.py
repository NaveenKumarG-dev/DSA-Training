"""
Problem:
After reading each element, print the maximum value seen so far.

Input:
2 5 1 8 3

output:
2 5 5 8 8
"""

arr = list(map(int,input("").split()))
max = arr[0]
for i in arr:

    if i > max :
        max = i

    print(max,end=" ")