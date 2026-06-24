# price_calculator.py

item_name = input("Enter item name: ")
price_per_item = input("Enter price per item: ")
quantity = input("Enter quantity: ")
discount_percentage = input("Enter discount percentage: ")
tax_percentage = input("Enter tax/GST percentage: ")

clean_item_name = item_name.strip().title()

price_per_item = float(price_per_item)
quantity = int(quantity)
discount_percentage = float(discount_percentage)
tax_percentage = float(tax_percentage)

subtotal = price_per_item * quantity

discount_amount = subtotal * discount_percentage / 100
price_after_discount = subtotal - discount_amount

tax_amount = price_after_discount * tax_percentage / 100
final_total = price_after_discount + tax_amount

print("\n--- Price Calculator Receipt ---")
print(f"Item: {clean_item_name}")
print(f"Price per item: ₹{price_per_item:.2f}")
print(f"Quantity: {quantity}")
print(f"Subtotal: ₹{subtotal:.2f}")
print(f"Discount ({discount_percentage:.1f}%): ₹{discount_amount:.2f}")
print(f"Price after discount: ₹{price_after_discount:.2f}")
print(f"Tax/GST ({tax_percentage:.1f}%): ₹{tax_amount:.2f}")
print(f"Final total: ₹{final_total:.2f}")