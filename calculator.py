operator =  input("Enter an Operator (+ - * / %)")
num1 = float(input("Enter First Number : "))
num2 = float(input("Enter second Number : "))

if operator =="+":
    result = num1 + num2
    print(result)
    
elif operator == "-":
    result = num1 - num2
    print(result)
    
elif operator == "*":
    result = num1 * num2
    print(result)
    
elif operator == "/":
    result = num1 / num2
    print(result)
    
elif operator == "%":
    result = num1 % num2
    print(result)

else:
    print(f"{operator} is not a valid operator")

