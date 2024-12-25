# Logiacal Operators = evaluates multiple conditions (and, or, not)

# and = both conditions must be true
# or = at least one condition must be true
# not = inverts the condition (not False, not True).

temp = 20
is_sunny = True

if temp >= 20 and is_sunny:
    print("It's a nice day")
elif temp < 0 or is_sunny:
    print ("It is too cold outside🥶")  
    print ("It is too sunny outside😊") 
elif 28 > temp > 0:
    print ("Its warm outside")
    print ("It is not too sunny outside😊"
           "It is not too cold outside🥶"
           )
elif not is_sunny:
    print ("It is not too sunny outside😊")
else:
    print ("It is too cold outside🥶")         