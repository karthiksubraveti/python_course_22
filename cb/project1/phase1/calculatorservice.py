# -*- coding: utf-8 -*-


# "calculator program"
def calculatorfunction (input1, input2, operation):
    print("inside the function now...")
    output = 0
    if (operation == "*"):
        output = input1 * input2

    elif (operation == "/"):
        output = input1 / input2

    elif (operation == "+"):
        output = input1 + input2

    elif (operation == "-"):
        output = input1 - input2

    elif (operation == "%"):
        output = input1 % input2
    else:
        pass

    return output

# main starts here
if __name__ == "main":
    input1 = int(input("enter input 1 (first value) here:  "))
    input2 = int(input("enter input 2 (second value) here:  "))
    operation = input("enter operation(*, /, +, % and -) further operations shall be available if one presses any other button besides these mentioned: ")
    output = calculatorfunction(input1, input2, operation)
    print(output)
