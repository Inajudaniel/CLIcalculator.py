def calculator():

    print("===== SIMPLE CLI CALCULATOR =====")

    while True:
        print("\n choose an operation:")
        print("1. Addition(+)")
        print("2. Subtraction(-)")
        print("3. Multiplication(*)")
        print("4. Division(/)")
        print("5. Exit")

        choice = input("Enter you choice (1-5):")
        if choice == "5":
            print("Thank you for using this Calculator, GoodBye")
            break
    
        if choice not in("1","2","3","4"):
            print("Invalid option, Please choose a number from 1 to 5.")
            continue

    try:
        num1 = float(input("Enter the First Number: "))
        num2 = float(input("Enter the Second Number: "))
    except ValueError:
        print("invalid Input, please enter numbers only")
        continue
    
    if choice == "1":
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")
    
        if choice == "2":
            result = num1 - num2
            print(f"Result: {num1} - {num2} = {result}")

        if choice == "3":
            result = num1 * num2
            print(f"Result: {num1} * {num2} = {result}")

        if choice == "4":
            result = num1 / num2
            if num2 == 0:
                print("invalid input, cannot be divided by zero")
            else: 
                print(f"Result: {num1} / {num2} = {result}")


calculator()
