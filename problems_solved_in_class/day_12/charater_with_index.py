

def str_index(s):
    if len(s) == 0:
        print("It's a empty string")
        return 
    for i in range(len(s)):
        print(f"{i} : {s[i]}")

try:
   str_index(input())

except Exception as e:
    print(f"Error {e}")