# Age calculator

from datetime import date

name = input("Enter your name: ")
birth_year = int(input("Enter the year you were born: "))

current_year = date.today().year
age = current_year - birth_year

print("Hey", name)
print("The current year is:", current_year)
print("You are approximately", age, "years old.")