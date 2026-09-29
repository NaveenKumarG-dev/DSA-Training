
"""
256 + 72
"""

s = input()
s_splitted = s.split()

n1 = int(s_splitted[0])
n2 = int(s_splitted[2])

operator = s_splitted[1]

if operator == "+":
    print("Sum:",n1+n2)
elif operator == "-":
    print("Difference:",n1-n2)
elif operator == "*":
    print("Product:",n1*n2)
elif operator == "/":
    print("Quotient:",n1//n2)
    print("Remainder:",n1%n2)
else:
    print("Invalid")



# def operation(n1,n2,operator):
#     if operator == "+":
#         return n1+n2
#     elif operator == "-":
#         return n1-n2
#     elif operator == "*":
#         return n1*n2
#     elif operator == "/":
#         return n1/n2

# nums = []
# operator = []
# s = input()
# s_splitted = s.split()

# for i in s_splitted:
#     if i.isnumeric():
#         nums.append(int(i))
#         continue
#     if i in {"+","-","*","/"}:
#         operator.append(i)

# ans = operation(nums[0],nums[1],operator[0])

# i = 2
# while i+1<len(nums):

    