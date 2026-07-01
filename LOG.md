# Learning Log

This file records my daily progress through the Python, Databases & Cybersecurity Roadmap.

The README explains the overall roadmap.
This LOG records what I actually completed each day.

---

## Day 1 - Python Setup and First Programs

**Date:** 22 June 2026
**Week:** Week 1
**Phase:** Python Foundations
**Planned hours:** 4-5 hours
**Actual hours:**
**Status:** Completed

### Task

Set up the roadmap folder structure, create the first Python files, write basic Python programs, and run them successfully in VS Code.

### Files created

```text
01_py/week1/day1/hello.py
01_py/week1/day1/world.py
01_py/week1/day1/age.py
01_py/week1/day1/code.py
```

### What I learned

* How to create folders using `mkdir`
* How to move between folders using `cd`
* How to create files using `touch`
* How to organise a coding roadmap folder
* How to create and run `.py` files
* How to use `print()`
* How to write comments using `#`
* How to use `input()` to collect user input
* How to use `int()` to convert input into a number
* How to use Python’s `datetime` module to get the current year
* How to calculate approximate age using current year minus birth year
* Why VS Code Terminal is needed for programs that use `input()`
* How to initialise Git using `git init -b main`

### What I built

* `hello.py` - first Python Hello World program
* `world.py` - personalised coding roadmap greeting
* `age.py` - age calculator using the current year
* `code.py` - extra Day 1 Python practice

### Problems faced

* The VS Code Output panel did not allow keyboard input for the age calculator.
* I learned that the Output panel is read-only and that interactive programs should be run in the Terminal.

### How I solved them

* I used the VS Code Terminal to run Python files manually.
* I ran the program using:

```bash
python3 01_py/week1/day1/age.py
```

### Evidence / GitHub link

* To be added after pushing to GitHub.

### Next step

Start Day 2: variables, data types, and operators.

---

## Weekly Reflection - Week 1

### What went well

* I successfully created the roadmap folder structure.
* I created my first Python files.
* I wrote and ran my first Python programs.
* I learned how to initialise Git.

### What was difficult

* Understanding the difference between the VS Code Output panel and Terminal.

### What I need to revise

* Running Python files from the Terminal
* `input()`
* `int()`
* `print()`
* Basic Git commands

### Best file or program I created this week

* `age.py`

### Next focus

* Variables, data types, arithmetic operators, and clearer user input/output.

# Day 2 Log - Variables, Data Types and Operators

## Date

Day 2

## Planned focus

Today I focused on Python variables, basic data types and arithmetic operators.

## Concepts learned

* A variable stores a value that can be reused later in the program.
* `int` is used for whole numbers.
* `float` is used for decimal numbers, especially values like money, distance and averages.
* `str` is used for text.
* `bool` stores `True` or `False`.
* `input()` collects user input, but the value comes in as text, so I need to convert it using `int()` or `float()` before doing calculations.
* Arithmetic operators can be used to perform calculations:

  * `+` for addition
  * `-` for subtraction
  * `*` for multiplication
  * `/` for normal division
  * `//` for floor division
  * `%` for remainder
  * `**` for power

## Programs built

1. `unit_converter.py`

   * Took a distance input from the user.
   * Converted the value into the correct numeric type.
   * Applied a conversion formula.
   * Printed the converted result clearly.

2. `bill_splitter.py`

   * Took the total bill amount.
   * Took the number of people.
   * Divided the bill equally.
   * Printed how much each person should pay.

3. `simple_calculator.py`

   * Took two numbers from the user.
   * Performed multiple arithmetic operations.
   * Displayed the answers with clear labels.

## Main logic I understood

The general structure of all three programs was:

1. Ask the user for input.
2. Convert the input into the correct data type.
3. Store values in variables.
4. Use arithmetic operators to calculate the result.
5. Print the final result in a readable format.

## Errors or difficulties faced

* I had to remember that `input()` gives a string, even when the user enters a number.
* I had to use `float()` for decimal values.
* I had to use `int()` for whole-number values like number of people.
* I need to be careful with division and avoid dividing by zero for now.

## Testing completed

* Tested the unit converter with small and decimal values.
* Tested the bill splitter with different bill amounts and number of people.
* Tested the calculator with different pairs of numbers.

## Files completed

* `day_02/unit_converter.py`
* `day_02/bill_splitter.py`
* `day_02/simple_calculator.py`

## Actual hours studied

Planned hours: 5
Actual hours: ___

## Reflection

Today I became more comfortable using variables, data types and arithmetic operators. I understood that most beginner programs follow the same basic pattern: input, conversion, calculation and output.

## Next starting point

Next, I need to move toward strings, type conversion, f-strings and cleaner output formatting.


# Day 3 Log - Strings and Type Conversion

## Date

24 June 2026

## Topics Learned

* Used `input()` to take user input.
* Understood that `input()` always stores values as strings.
* Used `int()` to convert whole-number input.
* Used `float()` to convert decimal-number input.
* Used f-strings to display clean output.
* Used string methods such as `.strip()`, `.title()`, and `.lower()`.

## Files Created

* `name_formatter.py`
* `price_calculator.py`

## Programs Completed

### 1. Name Formatter

Created a program that:

* Takes first name and last name as input.
* Removes extra spaces.
* Formats the name in title case.
* Creates a lowercase username.
* Displays initials.

### 2. Price Calculator

Created a program that:

* Takes item name, price, quantity, discount percentage, and tax/GST percentage.
* Converts user input into correct number types.
* Calculates subtotal.
* Applies discount.
* Applies tax/GST.
* Prints a formatted receipt with two decimal places.

## What I Understood

Today I understood that user input needs to be converted before doing calculations. I also learned how string methods help clean and format messy text input. I practiced using f-strings to make the output easier to read.

## Difficulties Faced

* Remembering that `input()` returns a string even when the user types a number.
* Understanding when to use `int()` and when to use `float()`.
* Formatting prices correctly to two decimal places using `:.2f`.

## Status

Completed

## Actual Study Time

[Write your actual time here]



# Day 4 - Conditions

## Topics Learned
- if statements
- elif statements
- else statements
- Comparison operators
- Indentation
- Pass/fail logic
- Basic grading logic

## Programs Built

### 1. even_odd.py
Checks whether a number is even or odd.

### 2. eligibility_checker.py
Checks whether a person is eligible based on age.

### 3. grading_program.py
Converts a mark into a grade.

### 4. marks_checker.py
Checks subject mark, pass/fail result and grade.

## What I Practised
- Writing decision-based programs.
- Using comparison operators like >=, <, > and ==.
- Using if, elif and else correctly.
- Keeping indentation correct.
- Creating a marks checker with pass/fail logic.

## Difficulties
- Remembering that Python needs correct indentation.
- Understanding that elif order matters.

## Status
Completed Day 4 conditions practice.



## Day 5 - Boolean Logic and Input Validation

### Topics Covered
- Boolean values
- and
- or
- not
- Range validation
- Invalid input handling
- Simple password rule checking

### Files Created
- week1/day5/mark_validator.py
- week1/day5/password_rule_checker.py
- week1/day5/range_checker.py

### Programs Completed
1. Mark Validator
   - Checks whether a mark is valid.
   - Rejects marks below 0 or above 100.

2. Password Rule Checker
   - Checks simple password rules using Boolean logic.

3. Range Checker
   - Practises checking whether numbers are inside an allowed range.

### What I Practised
- Combining conditions using and, or and not.
- Rejecting invalid input before using it.
- Writing cleaner decision logic.

### Status
Completed.

## Day 6 - Marks Calculator v1

### Topics Covered
- Planning inputs
- Calculating total marks
- Calculating average marks
- Calculating percentage
- Finding highest mark
- Finding lowest mark
- Pass/fail logic
- Grade logic

### Files Created
- week1/day6/marks_calculator_v1.py

### Program Completed
1. Marks Calculator v1
   - Takes marks for multiple subjects.
   - Calculates total.
   - Calculates average.
   - Calculates percentage.
   - Finds highest and lowest marks.
   - Displays pass/fail result.
   - Displays grade.

### What I Practised
- Combining input, calculations and conditions in one program.
- Using max() and min().
- Formatting a clean marks report.
- Planning the program before coding.

### Status
Completed.

