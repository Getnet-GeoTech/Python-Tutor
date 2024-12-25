first_name = "Bro"
# Here we can can use f-string before the opening quotation mark. Inside this string, we can 
# write a python expression that can refer to variables or literals. The F stands for "format"
food = "Pizza"
email = "dQKX1@example.com"
print (f"Hello {first_name}")
print (f"Your favorite food is {food}")
print (f"Your email is {email}")

#Intger
age = 20
quantity = 2
num_of_students = 30
print (f"Your age is {age} years old")
print (f"You have {quantity} items in your cart")
print (f"Your class has {num_of_students} students")

#Float
price = 19.99
gpa = 3.5
distance = 10.5
print (f"The price of the item is ${price}")
print (f"Your gpa is :{gpa}")
print (f"You run {distance} kms")

#Boolean
is_a_student = True
is_a_teacher = False
# print (f"Are you a student?: {is_a_student}")
# print (f"Are you a teacher?: {is_a_teacher}")
if is_a_student:
    print ("You are a student")
else:
    print ("You are not a student")

for_sale = False
if for_sale:
    print ("This item is for sale")
else:
    print ("This item is not for sale")    
