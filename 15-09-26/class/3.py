#count the occurence of all the elements in the array


try:
    arr = list(map(int,input().split()))
    occurence = {}

    for i in arr:
        if i not in occurence.keys():
            occurence[i] = 1
            continue
        occurence[i]+=1

    print("element | occurence")
    for i in occurence.keys():
        print(f"{i} {occurence[i]}")

except Exception as e:
    print("Error:",e)