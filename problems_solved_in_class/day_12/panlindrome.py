


def is_palindrome_while(s):
    
    left = 0
    right = len(s)-1

    while left<right:
        if s[left] != s[right]:
            return False
        left+=1
        right-=1
    return True

def is_palindrome_slice(s):
    return s == s[::-1]

def is_palindrome_for(s):
    l = len(s)
    for i in range(l//2):
        if s[i] != s[i-l-1]:
            return False
    return True

try:
    s = input()
    s = s.lower()

    print(is_palindrome_while(s))
    print(is_palindrome_slice(s))
    print(is_palindrome_for(s))
except Exception as e:
    print(f"Error {e}")