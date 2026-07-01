# Week 1 Review - Python Foundations

## Week 1 Summary

This week focused on the basic foundations of Python programming. I practised writing small programs using input, variables, type conversion, operators, conditions, Boolean logic and functions.

The main project for the week was a Marks Calculator, which started as a simple condition-based program and was later improved using functions.

---

## Day 1 - Python Setup and First Programs

### Topics Revised
- Running Python files
- Using `print()`
- Writing comments
- Creating simple programs

### Key Learning
I learned how to create and run Python files in VS Code. I also practised writing simple output using `print()`.

### Example

```python
print("Hello World")
print("Welcome to Python")
```

---

## Day 2 - Variables, Data Types and Operators

### Topics Revised
- Variables
- Strings
- Integers
- Floats
- Booleans
- Arithmetic operators

### Key Learning
I learned that variables are used to store values. I also practised using different data types and basic mathematical operators.

### Examples

```python
name = "Kruthajn"
age = 20
height = 175.5
is_student = True
```

```python
total = 50 + 20
difference = 50 - 20
product = 5 * 4
division = 20 / 5
remainder = 10 % 3
```

---

## Day 3 - Strings and Type Conversion

### Topics Revised
- `input()`
- f-strings
- String methods
- `int()`
- `float()`
- Type conversion

### Key Learning
I learned that `input()` always gives a string, so numbers need to be converted using `int()` or `float()` before doing calculations.

### Examples

```python
name = input("Enter your name: ")
print(f"Hello, {name}")
```

```python
age = int(input("Enter your age: "))
mark = float(input("Enter your mark: "))
```

---

## Day 4 - Conditions

### Topics Revised
- `if`
- `elif`
- `else`
- Comparison operators
- Indentation
- Pass/fail logic
- Grade logic

### Key Learning
I learned how to make Python programs choose between different outcomes using conditions.

### Example

```python
mark = float(input("Enter your mark: "))

if mark >= 50:
    print("Pass")
else:
    print("Fail")
```

### Comparison Operators

```python
>    # greater than
<    # less than
>=   # greater than or equal to
<=   # less than or equal to
==   # equal to
!=   # not equal to
```

---

## Day 5 - Boolean Logic and Input Validation

### Topics Revised
- Boolean values
- `and`
- `or`
- `not`
- Range validation
- Invalid input handling

### Key Learning
I learned how to combine multiple conditions and reject invalid input before using it.

### Examples

```python
mark = float(input("Enter mark: "))

if mark < 0 or mark > 100:
    print("Invalid mark")
else:
    print("Valid mark")
```

```python
password = input("Enter password: ")

if len(password) >= 8 and password != "password":
    print("Password accepted")
else:
    print("Password rejected")
```

### Boolean Logic Summary

```python
and
```

Both conditions must be true.

```python
or
```

At least one condition must be true.

```python
not
```

Reverses the condition.

---

## Day 6 - Marks Calculator v1

### Topics Revised
- Taking multiple inputs
- Calculating total
- Calculating average
- Calculating percentage
- Finding highest mark
- Finding lowest mark
- Grade logic
- Pass/fail logic

### Key Learning
I learned how to combine inputs, calculations and conditions into one complete program.

### Main Logic

```python
total = english + maths + science + history + computer
average = total / 5
percentage = (total / 500) * 100

highest = max(english, maths, science, history, computer)
lowest = min(english, maths, science, history, computer)
```

### Grade Logic

```python
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
```

---

## Day 7 - Functions and Refactoring

### Topics Revised
- Functions
- Parameters
- Return values
- `print()` vs `return`
- Refactoring code

### Key Learning
I learned how to break a long program into smaller reusable functions. This makes the code easier to read, test and modify.

### Function Example

```python
def greet(name):
    return f"Hello, {name}"

message = greet("Kruthajn")
print(message)
```

### Parameters

Parameters are values given to a function.

```python
def add_numbers(a, b):
    return a + b
```

Here, `a` and `b` are parameters.

### Return Values

A return value is the result sent back from a function.

```python
def calculate_total(a, b, c):
    return a + b + c
```

### Print vs Return

`print()` displays something on the screen.

`return` gives a value back so it can be reused later.

---

## Marks Calculator v2 Structure

In Marks Calculator v2, I used functions such as:

```python
def is_valid_mark(mark):
    return mark >= 0 and mark <= 100
```

```python
def calculate_total(english, maths, science, history, computer):
    return english + maths + science + history + computer
```

```python
def calculate_average(total):
    return total / 5
```

```python
def calculate_percentage(total):
    return (total / 500) * 100
```

```python
def get_result(percentage):
    if percentage >= 50:
        return "Pass"
    else:
        return "Fail"
```

---

## Important Mistakes to Avoid

### 1. Forgetting to convert input

Wrong:

```python
age = input("Enter age: ")
```

Correct:

```python
age = int(input("Enter age: "))
```

---

### 2. Using `=` instead of `==`

Wrong:

```python
if mark = 50:
```

Correct:

```python
if mark == 50:
```

---

### 3. Forgetting the colon

Wrong:

```python
if mark >= 50
    print("Pass")
```

Correct:

```python
if mark >= 50:
    print("Pass")
```

---

### 4. Wrong indentation

Wrong:

```python
if mark >= 50:
print("Pass")
```

Correct:

```python
if mark >= 50:
    print("Pass")
```

---

### 5. Wrong grade order

Wrong:

```python
if percentage >= 50:
    grade = "D"
elif percentage >= 80:
    grade = "A"
```

Correct:

```python
if percentage >= 80:
    grade = "A"
elif percentage >= 50:
    grade = "D"
```

---

## Week 1 Programs Completed

### Day 1
- Hello World
- Personal greeting
- Age calculator

### Day 2
- Unit converter
- Bill splitter
- Simple calculator

### Day 3
- Name formatter
- Price calculator

### Day 4
- Even/Odd checker
- Eligibility checker
- Grading program
- Marks checker

### Day 5
- Mark validator
- Password rule checker
- Range checker

### Day 6
- Marks Calculator v1

### Day 7
- Marks Calculator v2
- Week 1 review notes

---

## Final Week 1 Reflection

This week helped me build confidence with the basics of Python. I started with simple print statements and small programs, then gradually moved into conditions, validation and functions.

The most important improvement was learning how to think through a program step by step:

1. Take input
2. Convert the input if needed
3. Validate the input
4. Perform calculations
5. Use conditions to decide outcomes
6. Display clear output
7. Refactor repeated logic into functions

## Status

Week 1 completed.