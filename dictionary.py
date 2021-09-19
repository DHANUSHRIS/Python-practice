# create Dictionary
user_name = {
    "Akhila" :"27",
    "Dhanu_shri": "24",
    "Manoj_Chowdary": "27"
    }
# python 3.7 +
# ordered
# changeable
# does not allow duplicates

# Access Item
print(user_name["Akhila"])
print(user_name.get("Akhila"))
print(user_name.values())
print(user_name.keys())
print(user_name.items())



#Get All VALUES OF DICTIONARY

print(user_name)


#LIST = [1,1,1,2,3,4,5,3,4,5,2,4,5] PRINT UNIQUE ITEMS IN ABOVE LIST

trends =[1,1,1,2,3,4,5,3,4,5,2,4,5]
output = []
for x in trends:
    if x not in output:
        output.append(x)
        print(output)

#GET ALL VALUES FROM DICTIONARY

print(trends)

#CREATE TWO SETS FOR YOUR NAME AND SIR NAME PRINT UNION OF ABOVE TWO SETS THE PRINT INTERSECTION OF THE ABOVE TWO STEP
#Union
list1 ={'Akhila S','Dhanushri S','Sunil kumar'}
list2 ={'Akhila S','Dhanushri S','Sunil kumar','Parinitha thanda','Manoj kumar chowdary'}

List1unionlit2 = list1.union(list2)
print("list1unionlist2 :",List1unionlit2)

#Intersection
list1intersectionlist2 = list1.intersection(list2)
print("list1intersectionlist2 :",list1intersectionlist2)


#GET USER INPUT FOR THE NUMBER AND CHECK IF IT IS GREATER THAN 500 THEN PRINT , " ITEM IS AVAILABLE

numbers = int(input("enter the numbers :"))

print(numbers)

if(numbers>=500):
    print('number is greater than 500 :', numbers)

elif(numbers <500):
    print("enter a valid number ")

    print("End")
     


