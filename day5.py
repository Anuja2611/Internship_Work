'''def add():
    num1=int(input("enter number : "))
    num2=int(input("enter number : "))
    res=num1+num2
    return res
result=add()
print("Result : ",result)
add=result+10
print("Result after adding 10 : ",add)'''

#evenodd
'''def evenodd():
    num=int(input('enter number : '))
    if num%2==0:
        print('number is even.')
    else:
        print('number is odd.')
res=evenodd()
print(res)
print(type(res))'''

#primenumber
'''def primenumber():
    num=int(input('enter number : '))
    cnt=2
    while cnt<=num:
        if num%cnt==0:
            break
        cnt+=1
    print(cnt)
    if num==cnt:
        print('number is prime')
    else:
        print('number is not prime')
primenumber()'''

#with parameter without return type
'''def add(num1,num2):
    res=num1+num2
    print("result : ",res)
num1=int(input("enter number : "))
num2=int(input('enter second number : '))
add(num1,num2)'''

#calculate the netsalary
'''def netsalary(bs,hra,da,pf):
    nsal=bs+hra+da-pf
    print("Net Salary : ",nsal)
bs=int(input('enter basic salary : '))
hra=int(input('enter hra : '))
da=int(input('enter da : '))
pf=int(input('enter pf : '))
netsalary(bs,hra,da,pf)'''

#with parameter with return type calculate netsalary
'''def netsalary(bs,hra,da,pf):
    salary=(bs+hra+da)-pf
    return salary
salary=netsalary(25000,2000,2000,2000)
print("Net Salary : ",salary)'''

#calculate the total
'''def total(s1,s2,s3):
    tl=s1+s2+s3
    return tl
def printpercentage(tot):
    per=tot / 3
    return per
s1=int(input('enter subject marks : '))
s2=int(input('enter subject marks : '))
s3=int(input('enter subject marks : '))
tl=total(s1,s2,s3)
print('Total : ',tl)
per=printpercentage(tl)
print('Percentage : ',per)'''

#default parameter
'''def sum(num1,num2=10):
    print("Result : ",num1+num2)
sum(12)'''


#