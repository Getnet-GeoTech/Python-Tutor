# input()= a function that asks for user input and returns it as a string
# name = input(f"what is your name? ")
# age = int(input(f"what is your age? "))

# we have to cast the string age into an integer age
# age = int (age)
# age = age + 1
# print (f"Hello {name}: nice to meet you")
# print ("Happy birthday")
# print (f"You are {age} years old")

#EXERCISE-1 Area of the rectangle 
length = float (input("What is the length of the rectangle? "))
width = float (input("What is the width of the rectangle? "))
area = length * width
print (f"The area of the rectangle is {area} m^2")

#EXERCISE-2 Shopping List program
item = input ("What item would you like to buy? ")
price = float (input ("What is the price of the item? "))
quantity = int (input ("How many items would you like to buy? "))
total = price * quantity
print (f"You have to pay ${total} for {quantity} {item}")

