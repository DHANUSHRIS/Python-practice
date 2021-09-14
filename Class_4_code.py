#Assignment operator
x = 100
print("Before:",x)

#1. x = x+10
x +=10
print("After+10:",x)

#2. x = x-30
x -=30
print("After-30:",x)

#3. x = x*30
x *=30
print("After*30:",x)

#4.x = x/30
x /=30
print("After / 30:",x)

#COMPARION OPERATOR

x = 10
y = 20

#1. IS EQUAL
print("IS EQUALS:",x==y )

#2. Is Greater than left>right --> is left elment is grater than right element
print("Is Greater :", x>y)

#3. Is smaller than left < right --> is left element is smaller than right element
print(" Is Smaller :", x<y)

#4. Is Greater than left>=right --> is left element is greater than or equal too right element
print("Is Greater than or equal too :", x>=y)

#4. Is smaller than left<=right --> is left element is smaller than or equal too right element
print("Is Smaller than or equal too :", x<=y)



#TYPE CASTING

#VARIABLE
#1. Integer
#2. Float
#3. String

#1. int
x = 100
#1. int to float
fl=float(x)
print("int to float :", fl)

#2. int to string
fl= str(x)
print("int to string :", fl)

#2. FLOAT

y = 100.888

#1. float to int
int= int(y)
print("float to int :", int)

#2. float to string
str= str(int)
print("float to string :",int)

#3. STRING

name = "1000.09876"

#str to int
newname = float(name)
print("string to int :", newname)



#variable type
#Integer
#Float
#string

#list
#creating list [ int, float, str]
marks = [80,70,80,67,89,7978.88,"name is"]

#Indexing the list Items
print(marks[2:5])

#creating Newlist
newlist=[]
print("New list :", newlist)

#Adding New element to list syntax
newlist=['10','20','30','40']
newlist.append("100.90")
print("Newlist:",newlist)

#Inserting at particular location index
newlist.insert(3,241097)
print("after insert :",newlist)

#length of list
print (" list contain element :", len(newlist))






