# Define a calculate_discount function that takes two parameters: price(float) and discount_percent (float)

def calculate_discount(price, discount_percent):
   
 # If the discount_percent is greater or equal to 20 percent, 
 #  calculate the discount_amount and subtract it from price (original price) of an item and then return final_price
 # Else return the price (original price)

    if discount_percent >= 20:
        discount_amount = price * (discount_percent/100)
        return  price - discount_amount

    else:
        return price

# Prompt user input
try:
    price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Call the function defined with the value returned and assign that value to a variable final_price
    final_price = calculate_discount(price, discount_percent)

    if discount_percent >= 20:
        print(f"Discount allowed. The final price is: {final_price:.2f}")
    else:
        print(f"No discount allowed. The price remains: {final_price:.2f}")

except ValueError:
    print("Invalid input. Please enter numeric values.")