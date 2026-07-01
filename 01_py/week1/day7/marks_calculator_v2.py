# Day 7 - Marks Calculator v2
# Refactored using functions

def is_valid_mark(mark):
    return mark >= 0 and mark <= 100


def calculate_total(english, maths, science, history, computer):
    return english + maths + science + history + computer


def calculate_average(total):
    return total / 5


def calculate_percentage(total):
    return (total / 500) * 100


def get_highest_mark(english, maths, science, history, computer):
    return max(english, maths, science, history, computer)


def get_lowest_mark(english, maths, science, history, computer):
    return min(english, maths, science, history, computer)


def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def get_result(percentage):
    if percentage >= 50:
        return "Pass"
    else:
        return "Fail"


def display_report(
    english,
    maths,
    science,
    history,
    computer,
    total,
    average,
    percentage,
    highest,
    lowest,
    grade,
    result
):
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


print("--- Marks Calculator v2 ---")

english = float(input("Enter English mark out of 100: "))
maths = float(input("Enter Maths mark out of 100: "))
science = float(input("Enter Science mark out of 100: "))
history = float(input("Enter History mark out of 100: "))
computer = float(input("Enter Computer mark out of 100: "))

if (
    not is_valid_mark(english) or
    not is_valid_mark(maths) or
    not is_valid_mark(science) or
    not is_valid_mark(history) or
    not is_valid_mark(computer)
):
    print("Invalid marks entered. All marks must be between 0 and 100.")
else:
    total = calculate_total(english, maths, science, history, computer)
    average = calculate_average(total)
    percentage = calculate_percentage(total)

    highest = get_highest_mark(english, maths, science, history, computer)
    lowest = get_lowest_mark(english, maths, science, history, computer)

    grade = get_grade(percentage)
    result = get_result(percentage)

    display_report(
        english,
        maths,
        science,
        history,
        computer,
        total,
        average,
        percentage,
        highest,
        lowest,
        grade,
        result
    )