def addition(a,b):
    result=a+b
    return result
def subtraction(a,b):
    result=a-b
    return result
def division(a,b):
    result=a/b
    return result
def multiplication(a,b):
    result=a*b
    return result
print('welcome to my simple calculator')
print('for addition press ''1'' ')
print('for subtraction press ''2'' ')
print('for multiplication press ''3'' ')
print('for division press ''4'' ')
choice= int(input('what is your choice:'))

if choice==1:
    one=float(input('input your first number: '))
    two=float(input('input your second number: '))
    result=addition(one,two)
    print(result)
elif choice==2:
    one=float(input('input your first number: '))
    two=float(input('input your second number: '))
    result=subtraction(one,two)
    print(result)
elif choice==3:
    one=float(input('input your first number: '))
    two=float(input('input your second number: '))
    result=division(one,two)
    print(result)
elif choice==4:
    one=float(input('input your first number: '))
    two=float(input('input your second number: '))
    result=multiplication(one,two)
    print(result)
else:print('not in options')
