# Day 6 - Marks Calculator v1
# This version does not use functions yet

print("--- Marks Calculator v1 ---")

english = float(input("Enter English mark out of 100: "))
maths = float(input("Enter Maths mark out of 100: "))
science = float(input("Enter Science mark out of 100: "))
history = float(input("Enter History mark out of 100: "))
computer = float(input("Enter Computer mark out of 100: "))

if (
    english < 0 or english > 100 or
    maths < 0 or maths > 100 or
    science < 0 or science > 100 or
    history < 0 or history > 100 or
    computer < 0 or computer > 100
):
    print("Invalid marks entered. All marks must be between 0 and 100.")
else:
    total = english + maths + science + history + computer
    average = total / 5
    percentage = (total / 500) * 100

    highest = max(english, maths, science, history, computer)
    lowest = min(english, maths, science, history, computer)

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    if percentage >= 50:
        result = "Pass"
    else:
        result = "Fail"

    print("\n--- Marks Report ---")
    print(f"English: {english}/100")
    print(f"Maths: {maths}/100")
    print(f"Science: {science}/100")
    print(f"History: {history}/100")
    print(f"Computer: {computer}/100")

    print(f"\nTotal: {total}/500")
    print(f"Average: {round(average, 2)}")
    print(f"Percentage: {round(percentage, 2)}%")
    print(f"Highest Mark: {highest}")
    print(f"Lowest Mark: {lowest}")
    print(f"Grade: {grade}")
    print(f"Result: {result}")