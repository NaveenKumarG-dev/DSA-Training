#count the occurence of all the elements in the array


try:
    arr = list(map(int,input().split()))
    seen = {}

    for i in arr:
        if i not in seen.keys():
            seen[i] = 1
            continue
        seen[i]+=1

    print("element | occurence")
    for i in seen.keys():
        print(f"{i} | {seen[i]}")

except Exception as e:
    print(e)