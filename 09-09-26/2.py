
arr = list(map(int,input().split()))
    
largest = arr[0]
largest_index = 0

second_largest = arr[1]
second_largest_index = 1
for i in range(len(arr)):
        
    if arr[i]>largest:
        largest = arr[i]
        largest_index = i
        continue
    if arr[i]>second_largest:
        second_largest = arr[i]
        second_largest_index = i
        continue


print("First Largest=",largest,", index=",largest_index+1)

print("Second Largest=",second_largest,", index=",second_largest_index+1)
