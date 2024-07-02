def get_number(num):
    while True:
        try:
            number = int(input(num))
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def divide_numbers(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    else:
        return result

def main():
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")

    result = divide_numbers(num1, num2)
    if result is not None:
        print(f"{num1}/{num2} is: {result}")

if __name__ == "__main__":
    main()
