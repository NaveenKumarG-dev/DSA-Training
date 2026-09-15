



def display(arr):
    count = 0
    for i in arr:
        print(i,end=" ")
        count+=1
        if count==4:
            print("")
            count=0

        

arr = [90,67,87,56,83,97,99,35,70]
display(arr)