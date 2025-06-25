#dictionery creation
thedist={"brand":"ford",
           "Model":"Mustang",
           "year":1964
        }
print(thedist)
print(type(thedist))

#accesing values using keys
print(thedist["brand"])
print(thedist["Model"])
print(thedist["year"])

#calculating length of dictionery
print(len(thedist))

#assigning multiple values to the key
dict={"student":['anuja','priyanka','samruddhi'],
       "roll":[13,12,36],
       "gender":['f','f','f']
     }
print(dict)
x=dict["roll"]
print(type(x))

#accessing values using various methods
print(dict["student"])
print(dict.get('roll'))

#accessing keys & values
print(dict.keys())
print(dict.values())

#checking the presence of an element in dictionery
print("roll" in dict)
print("roll" not in dict)

#change the values using key
print(thedist)
thedist["year"]=2025
thedist["color"]="black"
print(thedist)
#the color key is not present in dictionery so,it will get added to the dictionery

#update method
thedist.update({'year':2026})
print(thedist)

#pop method
dict.pop("roll")
print(dict)

#popitem method
dict.popitem()
print(dict)

#clearing the dictionery
dict.clear()
print(dict)

#deleting the dictionery
del dict
#accesing keys using for loop
for i in thedist:
    print(i)

#accessing both the keys and values using for loop
for i in thedist:
    print(i," - ",thedist[i])

#accesing the values
for i in thedist.values():
    print(i)

#accessing both the keys & values
for x,y in thedist.items():
    print(x,"-",y)

#copying the dictionery
dict1=thedist.copy()
print(dict1)

dict2=dict(dict1)
print(dict2)