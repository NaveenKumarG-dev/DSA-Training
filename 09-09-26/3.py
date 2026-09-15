# cook your dish here

n = int(input())

for i in range(n):
    students = list(map(int,input("").split()))
    absentees = 0
    for student in students:
        if not student:
            absentees+=1

    if absentees:
        print(f"{absentees} student absent")
    else:
        print(f"No absentees")