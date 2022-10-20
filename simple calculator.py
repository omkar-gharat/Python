first = input("Enter 1st Number :")
operator = input("Enter Operator (+, -, *, /, %) : ")
second = input("enter 2nd Number")

first = int(first)
second = int(second)

if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "*":
    print(first * second)
elif operator == "/":
    print(first / second)
elif operator == "%":
    print(first % second)
else:
    print("Plz select correct operator")
