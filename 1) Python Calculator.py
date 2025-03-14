def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by 0 is not allowed"
    return x / y

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    while True:
        # Take input from user
        choice = input("Enter choice (1/2/3/4): ")
        
        # Check if the input is valid
        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter your first number: "))    
            num2 = float(input("Enter your second number: "))
            
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
        
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
        
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
        
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
                
            # Option to exit the loop
            next_calculation = input("Do you want to perform another calculation? (Y/N): ")
            if next_calculation.lower() != 'y':
                print("Exiting Calculator! BYE :)")
                break
        else:
            print("Invalid input! Please enter a valid option (1/2/3/4).")

# Call Calculator 
calculator()
