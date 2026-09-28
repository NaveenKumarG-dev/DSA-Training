
"""
Count the vowels and consonents in the given string
"""

def count(s):
    vowels = {"a", "e", "i", "o", "u"}

    vowels_count = 0
    consonents_count = 0

    for i in s:
        if i in vowels:
            vowels_count+=1
        else:
            consonents_count+=1
    return vowels_count,consonents_count

s = input().lower()

vowels_count,consonents_count = count(s)

print(f"Vowels:{vowels_count}\nConsonents:{consonents_count}")