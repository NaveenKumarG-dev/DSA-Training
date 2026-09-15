
#given an array and target x count the occuourance
try:
    arr = list(map(int,input().split()))
    target = int(input())
    count = 0

    for i in arr:
        if i == target:
            count+=1

    print(count)

except Exception as e:
    print(e)

    