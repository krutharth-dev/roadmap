print("Bill Splitter")

total_bill = float(input("Enter the total bill amount: "))
number_of_people = int(input("Enter the number of people: "))

amount_per_person = total_bill / number_of_people

print("Each person should pay:", amount_per_person)