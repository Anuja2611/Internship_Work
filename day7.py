mylist=['abc','xyz','pqr']
print(mylist)
print(type(mylist))
print('lenth of list : ',len(mylist))
#accessing list elements
lst=['a','b','c','d','e','f']
print(lst)
lst1=[1,2,3,4]
print(lst1)
lst2=[1.5,2.5,3.4,4.5]
lst3=[lst,lst1,lst2]
print(lst3)

#index
list=['a','b','c','d','e']
print(list[2])
print(list[1:4])
print(list[:4])
print(list[1:])

#changing the index value
list[2]='g'
print(list)
list[1:3]=[1,2]
print(list)

#inserting values in list
list.insert(0,'igap') 
print(list)
#append method
list.append('welcome')
print(list)
#extending list
l=['anuja','priya','shreya']
list.extend(l)
print(list)

#remove
list.remove('shreya')
print(list)

#pop method
list.pop(4)
print(list)

#printing list elements
num=[10,20,30,40,50]
for i in num:
    print(i)

#sorting the list
num.sort()
print(num)
#reversing the list
list.reverse()
print(list)

#concatnation
a=[1,2,3,4]
b=['a','b','c']
c=a+b
print(c)

