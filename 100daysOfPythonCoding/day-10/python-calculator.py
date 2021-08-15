calculatorLogo = '''
           _            _       _             
          | |          | |     | |            
  ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
| (_| (_| | | (__| |_| | | (_| | || (_) | |   
 \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                              
                                              
'''

Calculator_Image = '''
 _____________________
|  _________________  |
| | Enter Numbers   | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
'''


def add(num1, num2):
    return num1+num2

def substraction(num1, num2):
    return num1-num2

def multiply(num1, num2):
    return num1*num2

def divide(num1, num2):
    return num1/num2

operators = {
    "+":add,
    "-":substraction,
    "*":multiply,
    "/":divide,
}

print(f"{Calculator_Image} {calculatorLogo} \n")

num1 = 0
num2 = 0
Continue_Calculation = True

def Calculator(First, num1, num2):
    if First:
        num1 = float(input("Enter First Number: "))
    else:
        num1 = num1

    print("*** Operators ***\n")
    for key in operators:
        print(key)
    select_Operator = input("Pick any one operator from above list: ")
    num2 = float(input("Enter Second Number: "))
    Calculation_Function = operators[select_Operator]
    result = Calculation_Function(num1,num2)
    print(f"{num1} {select_Operator} {num2} = {result}")
    askUser = input("Do you want to perform another calculation os this result? Type yes or no: ")
    if askUser == "yes":
        num1 = result
        Calculator(False, num1, num2)
    else:
        newCalculation = input("Do you want to perform new calculation? Type yes or no: ")
        if newCalculation == "yes":
            Calculator(True, num1, num2)
        else:
            return


Calculator(True, num1, num2)