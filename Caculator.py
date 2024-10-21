def calculator():
    while True:
        num1 = float(input("Enter the first number:"))
        num2 = float(input("Enter the second number:"))
        print("Choose an option:")
        print("1.Addition(+)")
        print("2.Subtraction(-)")
        print("3.Multiplication(*)")
        print("4.Division(/)")
        print("5.Quit")
        choice = int(input("Enter your choice(1-5)"))
        if choice == 1:
            result = num1 + num2
            print("Result:", result)
        elif choice == 2:
            result = num1 - num2
            print("Result:", result)
        elif choice == 3:
            result = num1 * num2
            print("result:", result)
        elif choice == 4:
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1/ num2
                print("result:", result)
        elif choice == 5:
            print("Exiting the calculator.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5")
if __name__ == "__main__":
    calculator()
                
            
    