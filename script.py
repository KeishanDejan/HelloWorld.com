try:
    def calculate():
        num1 = float(input("Enter First Number: "))
        op = input("Enter operator: ")
        num2 = float(input("Enter Second Number:"))
        result = str()

        if op == "+":
            result = num1 + num2
        elif op == "-":
           result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            result = num1 / num2
        else:
            result = "Invaild Operator"

        print(result)

    calculate()

except ZeroDivisionError as err:
    print(err)

except ValueError as err2:
    print(err2)
