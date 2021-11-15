# gaven
# assignment examples

# you can assign "values" by using an equals sign (right side goes into left side)
x = 5

# when python reads a variable name i replaces it with its stored value
y= x + 5

# there are 4 different primitive datatypes
# integers: any whole number, positive or negative
age = 42
#Float: any number with a decimal, positive or negative
Grade = 98.6
# string: a string of human-readable characters
name = "chris mclean"
# numbers in a string are not numbers they are letters
favoritenumber = "1"
# boolean: true or false
# true is any value that is not false or empty
isSmart = True

#you can output tothr console by uing 'print()'
print(age)
print(Grade)
print(name)
print(favoritenumber)
print(isSmart)

# you can concatinate values together
print("my name is " + name)
# you can use functions to convert datatypes
print ("and my age is " + str(age))
# if you want to convert a value permentantly, you must assgn the converted value to a variable
age = str(age)
# you can convert back and forth with int(), str(), and float()
print(int(age))
print(float(age))
print (bool(age))
