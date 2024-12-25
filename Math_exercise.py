# # Calculate the circumference of a circle
# import math
# radius = float(input ("Enter the radius of the circle: "))
# Circumference = 2 * math.pi * radius
# print (f"The circumference of the circle is {round(Circumference,2)} cm")

# # Calculate the area of a circle
# r = float(input ("Enter the radius of the circle: "))
# Area = math.pi * pow(r,2)
# print (f"The area of the circle is {round(Area,2)} cm^2")

# # Calculate the hypotenuse of a right triangle
# a = float(input ("Enter the length of the first side: "))
# b = float(input ("Enter the length of the second side: "))
# c = math.sqrt(pow(a,2) + pow(b,2))
# print (f"The hypotenuse of the right triangle is {round(c,2)} cm")

# Calculator program
operator = input ("Enter the operator:+, -, *, /: ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if operator == "+":
    # result = num1 + num2
    # print (round(result,3))
    print (f"{round(float(num1) + float(num2), 3)}")
elif operator == "-":
    # result = num1 - num2
    # print (round(result,3))
    # Print the result with 3 decimal places rounded using f-string and round
    #print (f"{round(float(num1) - float(num2), 3)}")
    # Print the result with 2 decimal places rounded using f-string
    print (f"{float(num1) - float(num2): .2f}")
elif operator == "*":
    # result = num1 * num2
    # print (round(result,3))
   #print (f"{round(float(num1) * float(num2),3)}")
   print (f"{float(num1) * float(num2): .2f}")
elif operator == "/":
    # result = num1 / num2
    # print (round(result,3))
    #print (f"{round(float(num1) / float(num2),3)}")
    print (f"{float(num1) / float(num2): .2f}")
else:
    print (f"{operator} is an Invalid operator")
