#1. Creating Newlist
NewList =[12,34,56]
print(" New List :", NewList)

#2. Adding new item to list
#2.1 Adding New element to list syntax
#ListName.append()
NewList.append("100.90")
print("After append :",NewList)


#2.2 insertng at Particular Location(index)
NewList.insert(3,241097)
print("After insert :",NewList)

#3. Length of list
print("List Contain Element:",len(NewList))

#4 Accessing Element from list
#4.1 Indexing list Elemet
print("last element :",NewList[-1])
print("first element :",NewList[0])
print("1st to 3rd element :",NewList[0:3])


#5. Deleting Elements from List
Fruits= ["Orange","Apple","Banana","Mango","Grapes"]

print("Starting list :",Fruits)

#5.1 Getting and removing Element from list using pop
print("1st poped element:",Fruits.pop())
print("After 1st pop:", Fruits)

print("2nd poped element:",Fruits.pop())
print("After 2nd pop:", Fruits)

print("3rd poped element:",Fruits.pop(1))
print("After 3rd pop:", Fruits)

Fruits.append("New Fruit")
print("After Adding new fruit :",Fruits)


#5.2 Remove (value)

Fruits.remove("New Fruit")
print("After removing 'new fruit':",Fruits)

#6. Empty the list
Fruits.clear()
print("After clearing Element :", Fruits)

### 1.TUPLE

#1. Creating Tuples
Courses = ('CS','ME','CE','E&C','EEE')
print("Staring Tuple :",Courses)

#2.check variable type
print(" Variable Type:",type(Courses))

#3. check length of Tuple
print("Tuple Length :",len(Courses))


##6. Accessing Element

print(" First Element :",Courses[0])
print(" Last Element :",Courses[-1])
print(" First to 2nd Element :",Courses[0:3])


#Advance list operations
#multiple list
first_rollnumber1 =["Dhanu",90,85]
first_rollnumber2 =["Dhanu",90,85]
first_rollnumber3 =["Dhanu",90,85]
first_rollnumber4 =["Dhanu",90,85]

firstStandardStudents = [first_rollnumber1,first_rollnumber2,first_rollnumber3,first_rollnumber4]

Courses = ['CS','ME','CE','E&C','EEE']

#SHALLOW COPY
New_list= Courses
print(" Courses :", Courses)
print(" New_list :",New_list)

New_list.append("Is")
print("After append courses :", Courses)
print("After New_list:",New_list)

#Hallow Copy
New_list2=Courses.copy()

print("Courses :",Courses)
print("New_list2 :", New_list2)

New_list2.append("New Element")
print("After append Courses :" , Courses)
print("After New_list2:", New_list2)

values = ["Hello World",1,2,3,5.0,[['A','B','C','D'],20,30,40,50,60]]

#STRING
print(values[0][0:5])

#list
print(values[-1][0][0:2])
