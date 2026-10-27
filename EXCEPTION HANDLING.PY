print("=== Exception Handling Demonstration ===")

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    result = num1 / num2

except ValueError:
    print("Error: Please enter valid numeric values.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

else:
    print("Division result:", result)

finally:
    print("Division operation completed.")


# Error Case 3: Missing input
try:
    name = input("Enter your name: ").strip()

    if not name:
        raise ValueError("Name cannot be empty.")

    print("Hello,", name)

except ValueError as e:
    print("Error:", e)


# Error Case 4: Invalid list index
try:
    numbers = [10, 20, 30]
    index = int(input("Enter a list index (0-2): "))
    print("Value:", numbers[index])

except ValueError:
    print("Error: Index must be an integer.")

except IndexError:
    print("Error: Index is outside the list range.")


# Error Case 5: Invalid file
try:
    with open("sample.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("Error: The requested file was not found.")

print("Program finished successfully.")
