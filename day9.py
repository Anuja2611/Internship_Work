'''class sum:
    def getdata(self):
        self.num1=int(input('enter number : '))
        self.num2=int(input('enter number : '))
    def calculate(self):
        self.result=self.num1+self.num2
    def display(self):
        print("Result : ",self.result)
obj=sum()
obj.getdata()
obj.calculate()
obj.display()

class evenodd:
    def getdata(self):
        self.num1=int(input('enter number : '))
    def check(self):
        if self.num1 % 2==0:
            print('number is even')
        else:
            print('number is odd')

obj=evenodd()
obj.getdata()
obj.check()

#parameterised class
class sum:
    def getdata(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def calculate(self):
        self.res=self.num1+self.num2
    def disp(self):
        print("Result : ",self.res)
num1=int(input('enter 1st number : '))
num2=int(input('enter 2nd number : '))
obj=sum()
obj.getdata(num1,num2)
obj.calculate()
obj.disp()

#constrructor
class evenodd:
    def __init__(self):
        self.num=int(input('enter number : '))
    def display(self):
        if self.num % 2==0:
            print('number is even.')
        else:
            print('number is odd.')
obj=evenodd()
obj.display()

#parameterised constructor
class evendemo:
    def __init__(self,num):
        self.num=num
    def display(self):
        if self.num%2==0:
            print('number is even.')
        else:
            print('number is odd.')
num=int(input('enter number : '))
obj=evendemo(num)
obj.display()

class sum:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def calculate(self):
        self.res=self.num1+self.num2

    def display(self):
        print("Result : ",self.res)
num1=int(input('enter 1st number : '))
num2=int(input('enter 2nd number : '))
obj=sum(num1,num2)
obj.calculate()
obj.display()'''

