'''def add():
    num=int(input('enter number : '))
    num1=int(input('enter number : '))
    res=num+num1
    print('Result : ',res)
add()'''

#digit seperation
'''def digits():
    num=int(input("enter number : "))
    res=0
    while num>0:
        res=num%10
        print(res)
        num=int(num/10)
digits()'''

#reverse the number
'''def digits():
    num=int(input('enter number : '))
    res=0
    sum=0
    while num>0:
        res=num%10
        sum=(sum*10)+res
        print(sum)
        num=int(num/10)
    print(sum)
digits()'''

#palindrome
'''def digits():
    num=int(input('enter number : '))
    temp=num
    res=0
    sum=0
    while num>0:
        res=num%10
        sum=(sum*10)+res
        num=int(num/10)
    if(temp==sum):
        print("number is palindrome")
    else:
        print("number is not palindrome")
digits()'''


#Armstrong number
'''def digits():
    num=int(input('enter number : '))
    temp=num
    rem=0
    sum=0
    while num>0:
        rem=num%10
        sum=(rem*rem*rem)
        print(sum)
        num=int(num/10)
    if(temp==sum):
        print('number is armstrong number')
    else:
        print('number is not armstrong number')
digits()'''

#calculate the power 
def powerCalculations():
    num=int(input('enter number : '))
    p=int(input('enter power : '))
    sum=1
    while p> 0:
        sum*=num
        print(sum)
        p-=1
    print(sum)
powerCalculations()