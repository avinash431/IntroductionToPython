# > 80 -> A
# [65, 80] -> B
# [50 - 65] -> C
# [30 - 50] -> D
# < 30 -> Fail

marks = int(input("Enter your marks: "))
if marks >= 80:
    grade = "A"
elif 65 <= marks < 80:
    grade = "B"
elif 50 <= marks < 65:
    grade = "C"
elif 30 <= marks < 50:
    grade = "D"
else:
    grade = "E"
print(f"Student got {grade} grade")
