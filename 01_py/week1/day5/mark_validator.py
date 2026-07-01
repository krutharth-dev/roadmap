# Day 5 - Mark Validator
# Practising Boolean logic and input validation

mark = float(input("Enter your mark out of 100: "))

if mark < 0 or mark > 100:
    print("Invalid mark. Marks must be between 0 and 100.")
else:
    print("Valid mark.")

    if mark >= 50:
        print("Result: Pass")
    else:
        print("Result: Fail")