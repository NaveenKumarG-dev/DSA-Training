
def closest_pair(arr,target):
    min_i = 0
    min_j = 0
    min_val = abs(target - arr[0] + arr[1])
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            min_val = min(min_val,abs(target - arr[i] + arr[j]))
            
    return [min_i,min_j]

print(closest_pair([10,20,30,40,50,60,70,80],40))