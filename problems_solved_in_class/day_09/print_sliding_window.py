
arr = [10,20,30,40,50,60,70,80]
k = 4

for i in range(len(arr)-k+1):
    for j in range(k):
        print(arr[i+j],end=" ")
    print() 