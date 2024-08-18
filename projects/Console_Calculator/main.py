operator = input("Enter an Operator (+,-,*,/): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the Second number: "))

if operator == "+":
   result = num1 + num2
   print(round(result,2))
elif operator == "-":
   result = num1 - num2
   print(round(result,2))   
elif operator == "*":
   result = num1 * num2
   print(round(result,2))     
elif operator == "/":
   result = num1 / num2
   print(round(result,2))  
else :
   print(f"{operator} is not a valid operator")      