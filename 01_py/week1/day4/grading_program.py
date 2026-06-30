# Day 4 - Grading Program

mark = float(input("Enter your mark out of 100: "))

if mark < 0 or mark > 100:
    print("Invalid mark. Please enter a mark between 0 and 100.")
elif mark >= 90:
    print("Grade: A+")
elif mark >= 80:
    print("Grade: A")
elif mark >= 70:
    print("Grade: B")
elif mark >= 60:
    print("Grade: C")
elif mark >= 50:
    print("Grade: D")
else:
    print("Grade: F")