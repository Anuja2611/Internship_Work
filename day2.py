age=int(input('enter age :'))
if age>=18:
    print('user is adult')
else:
    print('user is not adult')

#percentage
per=float(input('enter percentage : '))
if per >=40:
    print("Pass")
else:
    print("Fail")

#even or odd
'''num=int(input('enter number : '))
if num %2==0:
    print(num," is Even.")
else:
    print(num," is Odd.")'''

#leap year
'''year=int(input('enetr year : '))
if year%4==0:
    print('Year is leap .')
else:
    print('year is not leap.')'''

#max
'''num1=int(input('enetr 1st number : '))
num2=int(input("enter 2nd number : "))
if num1>num2:
    print(num1," is max.")
else:
    print(num2,' is max.')'''

#positive or negative using if-elif
'''num1=int(input('enter 1st number : '))

if num1>0:
    print(num1," is +ve .")
elif num1==0:
    print(num1,' is neutral.')
else:
    print(num1,' is negative')'''

#Grade 
'''per=float(input('enter percentage : '))
if per>=80:
    print('A Grade.')
elif per >=60:
    print('B Grade.')
elif per>=40:
    print('C Grade.')
else:
    print('Fail.')'''

#greater between three numbers 
'''num1=int(input('enter 1st number : '))
num2=int(input('enter 2nd number : '))
num3=int(input('enter 3rd number : '))
if num1 >num2 and num1>num3:
    print(num1,' is max.')
elif num2>num1 and num2>num3:
    print(num2,' is max.')
else:
    print(num3,' is max.')'''

#if else nested
num1=int(input('enter 1st number : '))
num2=int(input('enter 2nd number : '))
num3=int(input('enter 3rd number : '))
if num1>num2:
    if num1>num3:
        print(num1," is max.")
    else:
        print(num3,' is max .')
else:
    if num2>num3:
        print(num2,' is max.')
    else:
        print(num3,' is max.')