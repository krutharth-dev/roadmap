# Day 4 - Marks Checker with Pass/Fail Logic

subject = input("Enter subject name: ")
mark = float(input("Enter mark out of 100: "))

print("\n--- Mark Result ---")
print(f"Subject: {subject}")
print(f"Mark: {mark}/100")

if mark < 0 or mark > 100:
    print("Result: Invalid mark")
    print("Grade: Invalid")
elif mark >= 50:
    print("Result: Pass")

    if mark >= 90:
        print("Grade: A+")
    elif mark >= 80:
        print("Grade: A")
    elif mark >= 70:
        print("Grade: B")
    elif mark >= 60:
        print("Grade: C")
    else:
        print("Grade: D")
else:
    print("Result: Fail")
    print("Grade: F")