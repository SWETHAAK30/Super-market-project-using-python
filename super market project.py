import smtplib
from email.message import EmailMessage
import math

# Stationery items
stationery_items = {
    "Pens": 10,
    "Pencils": 5,
    "Notebooks": 20,
    "Eraser": 2,
    "Ruler": 5,
    "Sharpener": 3,
    "Glue": 4,
    "Scissors": 6
}

# Kids items
kids_items = {
    "Toys": 50,
    "Books": 30,
    "Clothes": 40,
    "Shoes": 60,
    "Bags": 20,
    "Stationery": 15
}

# Grocery items
grocery_items = {
    "Rice": 20,
    "Wheat": 30,
    "Vegetables": 40,
    "Fruits": 50,
    "Dairy": 30,
    "Beverages": 20
}

# Kitchen products
kitchen_products = {
    "Pots": 50,
    "Pans": 40,
    "Utensils": 30,
    "Plates": 20,
    "Bowls": 15,
    "Cups": 10
}

def calculate_total_amount(items):
    total_amount = 0
    for item, price in items.items():
        total_amount += price
    return total_amount

def calculate_gst(total_amount):
    gst = total_amount * 0.18
    return gst

def calculate_discount(total_amount):
    discount = total_amount * 0.05
    return discount

def generate_bill(customer_name, total_amount, gst, discount):
    bill_amount = total_amount + gst - discount
    return f"Dear {customer_name},\nYour total bill amount is: {bill_amount:.2f}\n"

def send_email(customer_email, bill):
    try:
        msg = EmailMessage()
        msg.set_content(bill)
        msg["Subject"] = "Your Bill"
        msg["From"] = "supermarket@example.com"
        msg["To"] = customer_email

        server = smtplib.SMTP_SSL("smtp.example.com", 465)
        server.login("supermarket@example.com", "password")
        server.send_message(msg)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print("Error sending email:", str(e))

def display_items(items, category):
    print(f"--- {category} ---")
    for item, price in items.items():
        print(f"{item}: {price}")
    print()

def main():
    customer_name = input("Enter customer name: ")
    customer_email = input("Enter customer email: ")

    print("Welcome to our supermarket!")
    print("Here are our items:")

    display_items(stationery_items, "Stationery")
    display_items(kids_items, "Kids")
    display_items(grocery_items, "Grocery")
    display_items(kitchen_products, "Kitchen")

    total_stationery_amount = calculate_total_amount(stationery_items)
    total_kids_amount = calculate_total_amount(kids_items)
    total_grocery_amount = calculate_total_amount(grocery_items)
    total_kitchen_amount = calculate_total_amount(kitchen_products)

    total_amount = total_stationery_amount + total_kids_amount + total_grocery_amount + total_kitchen_amount
    gst = calculate_gst(total_amount)
    discount = calculate_discount(total_amount)

    bill = generate_bill(customer_name, total_amount, gst, discount)
    print("Your bill:")
    print(bill)

    send_email(customer_email, bill)

    while True:
        response = input("Do you want to continue shopping? (yes/no): ")
        if response.lower() == "yes":
            main()
        elif response.lower() == "no":
            print("Thank you for shopping with us!")
            break
        else:
            print("Invalid response. Please try again.")

if __name__ == "__main__":
    main()