'''for num in range(2,1001):
    prime=True
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            prime=False
            break
    if prime:
        print(num)'''

#table
'''num=int(input('enter number : '))
for i in range (1,11):
    print(num," x ",i," = ",num*i)'''

#even numbers from 1 to 100
'''for i in range(0,101,2):
    print(i)'''

#even numbers using if condition
'''for i in range(1,101):
    if i%2==0:
        print(i)'''

#odd numbers using if condition
'''for i in range(1,101):
    if i%2==1:
        print(i)'''

#10 numbers from user input numbers
'''num=int(input('enter number : '))
for i in range(num+1,num+11):
    print(i)'''

#table using while loop
'''i=1
num=int(input('enter number : '))
while i<=10:
    print(num,' x ',i," = ",num*i)
    i=i+1'''

#1 to 10 numbers
'''for i in range(1,11):
    print(i)'''
 
#10 to 1 numbers
'''for i in range (10,0,-1):
    print(i)'''

#1 to 100 even numbers using while loop
'''i=1
while i<=100:
    if i%2==0:
        print(i)
    i+=1'''

#1 to 100 odd numbers using
'''i=1
while i<=100:
    if i%2!=0:
        print(i)
    i+=1
'''

#prime numbers
num=int(input("enter number"))
cnt=2
while cnt<=num:
    if num%cnt==0:
        break
    cnt+=1
print("counter",cnt)
if(cnt==num):
        print("number is prime")
else:
        print("number is not prime")