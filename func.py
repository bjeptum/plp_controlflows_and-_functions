def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.

    Parameters:
    price (float): The original price of the item.
    discount_percent (float): The discount percentage to apply.

    Returns:
    float: The final price after the discount is applied, or the original price if the discount is less than 20%.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price


# Main program execution
def main():
    """
    Prompts the user for the original price and discount percentage,
    and then calculates and prints the final price after applying the discount.
    """
    try:
        original_price = float(input("Enter the original price: "))
        discount = float(input("Enter the discount percentage: "))

        final_price = calculate_discount(original_price, discount)

        if discount >= 20:
            print(f"Discount applied. Final price: ${final_price:.2f}")
        else:
            print(f"No discount applied. Final price: ${final_price:.2f}")
    except ValueError:
        print("Please enter valid numbers for price and discount.")


# Run the program
if __name__ == "__main__":
    main()
