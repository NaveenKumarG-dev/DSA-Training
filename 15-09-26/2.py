#count the ouccourance of a charater in a string 

try:
    string = input()
    target = input()
    count = 0

    for i in string:
        if i == target:
            count+=1

    print(count)

except Exception as e:
    print(e)