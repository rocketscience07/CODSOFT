
import math
def calculator():
    print("CALCULATOR")
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("invalid input .Enter numeric values")
            continue
    print("choose the corresponding operation:")
    print("1.addition")
    print("2.subtraction")
    print("3.multiplicaion")
    print("4.division")
    print("5.modulus")
    print("6.square of a number")
    print("7.exponential")
    print("8.square root")
    operator=int(input("choose the corresponding operation: "))
    while True:
        try:
            if operator==1:
                result=num1+num2
                sign='+'
                break
            elif operator==2:
                result=num1-num2
                sign='-'
                break
            elif operator==3:
                result=num1*num2
                sign=('*')
                break
            elif operator==4:
                if num2!=0:
                    result=num1/num2
                    sign = '/'
                    break
                else:
                    print("number is not divisible by 0")
            elif operator==5:
                if num2!=0:
                    result=num1%num2
                    sign='%'
                    break
                else:
                    print("number is not divisible by 0")
            elif operator==6:
                result=num1**2
                sign="**"
                break
            elif operator==7:
                result=num1*num2
                sign="**"
                break
            elif operator==8:
                result=math.sqrt(num1)
                sign="square root"
                break1
        except ValueError:
            print("invalid opertaion Try again")
    if num2!=0:
        print(f"{num1} {sign} {num2} = {result}")
    else:
        print(f"{num1}{sign}{num1}={result}")

calculator()


