
arr = list(map(int,input("Enter a number : ").split()))

even_sum = 0
odd_sum = 0
even_count=0
odd_count=0

for i in arr:
    if i%2==0:
        even_sum+=i
        even_count+=1
    else:
        odd_sum+=i
        odd_count+=1

if even_count == 0:
    print("Even Average:",0)
else:
    print(f"Even Average: {even_sum/even_count:.2f}")

if odd_count == 0:
    print("Odd Average:",0)
else:
    print(f"Odd Average: {odd_sum/odd_count:.2f}")
