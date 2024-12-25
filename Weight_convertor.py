# Pythn weight convertor
weight = float (input ("Enter the weight: "))
unit = input ("Enter the unit: K for kilograms and L for pounds: ")

if unit == "K" or unit == "k":
    # converting the weight from kilogram to pound
    weight = weight * 2.20462
    unit = "Lbs"
    print (f"{round(weight,2)} {unit}")

elif unit == "L" or unit == "l":
    # converting the weight from pound to kilogram
    weight = weight / 2.20462
    unit = "Kgs"
    print (f"{round(weight,2)} {unit}")

else:
    print ("You have entered an invalid unit")


# Temperature convertor
temperature = float (input ("Enter the temperature: "))
unit = input ("Enter the unit: C for Celsius and F for Fahrenheit: ")

if unit == "C" or unit == "c":
    # converting the temperature from Celsius to Fahrenheit
    temperature = (temperature * 1.8) + 32
    unit = "F"
    print (f"{round(temperature,2)} {unit}")

elif unit == "F" or unit == "f":
    # converting the temperature from Fahrenheit to Celsius
    temperature = (temperature - 32) / 1.8
    unit = "C 🤦‍♀️"
    print (f"{round(temperature,2)} {unit}")

else:
    print ("You have entered an invalid unit")    