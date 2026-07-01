# Day 5 - Password Rule Checker
# Practising and, or, not

password = input("Enter a password: ")

has_enough_length = len(password) >= 8
is_not_common = password != "password"
has_no_spaces = " " not in password

if has_enough_length and is_not_common and has_no_spaces:
    print("Password accepted.")
else:
    print("Password rejected.")

    if not has_enough_length:
        print("- Password must be at least 8 characters long.")

    if not is_not_common:
        print("- Password cannot be 'password'.")

    if not has_no_spaces:
        print("- Password cannot contain spaces.")