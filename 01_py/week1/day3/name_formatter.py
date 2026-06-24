# name_formatter.py

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

clean_first_name = first_name.strip().title()
clean_last_name = last_name.strip().title()

full_name = f"{clean_first_name} {clean_last_name}"

username = f"{clean_first_name.lower()}.{clean_last_name.lower()}"

initials = f"{clean_first_name[0]}.{clean_last_name[0]}."

print("\n--- Name Formatter Result ---")
print(f"Full name: {full_name}")
print(f"Username: {username}")
print(f"Initials: {initials}")