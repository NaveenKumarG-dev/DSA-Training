def arr_sol(s1,s2):
    if len(s1)!=len(s2):
        return False
    arr=[0]*26
    for i in s1:
        arr[ord(i)-ord('a')]+=1
    for i in s2:
        arr[ord(i)-ord('a')]-=1
    if arr==[0]*26:
        return True
    else:
        return False

s1=input()
s2=input()
print(arr_sol(s1,s2))