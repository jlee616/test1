try:
    num = int(input("Choose a number: "))
    print(10/num)
except ZeroDivisionError:
    print("Can't divide by 0")
except ValueError:
    print("Please input a valid number")
