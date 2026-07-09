print("🧮 Welcome to Smart Calculator 🧮")

while True:

    print("\nChoose an Operation")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "5":
        print("👋 Thank you for using Smart Calculator!")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("❌ Invalid Choice! Try Again.")
        continue

    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))

    if choice == "1":
        print("✅ Result =", num1 + num2)

    elif choice == "2":
        print("✅ Result =", num1 - num2)

    elif choice == "3":
        print("✅ Result =", num1 * num2)

    elif choice == "4":
        if num2 == 0:
            print("❌ Division by zero is not possible.")
        else:
            print("✅ Result =", num1 / num2)