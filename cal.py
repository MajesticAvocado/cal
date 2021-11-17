from io import DEFAULT_BUFFER_SIZE
import os, math, time
from types import SimpleNamespace
clear= lambda: os.system('cls')
clear()
first=0
second=0
history=[]
result= None
print('> welcome to a basic calculator \n')
def action():
    global history
    chice= input("> Type start to 'start' using the calculator or type 'history' to view calculator history\n")
    if chice == 'start':
        numbers()
    if chice == 'history':
        print(history)
        def delete():
            ask= input("> do you wish to delete history? (yes/no)\n")
            if ask == 'yes':
                history.clear()
                print('> calculator history deleted\n')
                print('> starting calculator.....\n')
                dely()
                clear()
                numbers()
            if ask == 'no':
                print('> starting calculator.....\n')
                dely()
                clear()
                numbers()
            else:
                print("> Please answer with 'yes' or 'no'\n")
                delete()
        delete()
    else:
        print("> unknown input please use 'start' or 'history'\n")
        action()
def numbers():
    global first
    global second
    global result
    first=input('> please provide the first number:\n')
    second=input('> please provide the second number:\n')
    try:
        n1= int(first)
        n2= int(second)
        operations(n1, n2)
        return
    except:
        print('> non valid numbers were added\n')
        print('> restart calculator....\n')
        dely()
        clear()
        numbers()
        return
def operations(number1, number2):
    global result
    choise= input('> what kind of operation to do? (type help to see the operations menu)\n')
    match choise:
        case 'help':
            print("""
            The types of operations you can do are:
            1) add -> to add the two numbers.
            2) sub -> to subtrct number 2 from number 1.
            3) multi -> to multiply the two numbers.
            4) div -> to divide the second number from number 1.
            5) power -> to set the first number as a base number and the secend one as an exponent of power.
            6) 
            """)
            numbers()
        case 'add':
            result= number1 + number2
            print_result()
        case 'sub':
            result= number1 - number2
            print_result()
        case 'multi':
            result= number1 * number2
            print_result()
        case 'div':
            result= number1/number2
            print_result()
        case 'power':
            result= number1**number2
            print_result()
def print_result(): 
    global result
    global history
    print(f'\n > Your result is: {result}\n')
    history.append(result)
    print('clearing......')
    dely()
    clear()
    action()
def dely():
    time.sleep(2)
    return
action()