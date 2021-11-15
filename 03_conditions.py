# Gaven Romine

# Practice using expresssions using conditional statements

# an expression is a problem that must be solved
# 5 + 5 is an "arithmetic" expression
x = 5 + 5

#functions/methods must be solved as expressions as well
answer = input("what is your name")

# Comparison expressions resolve as True/False
print(7 > 7 )
print(7 >= 7)
print(x == 10)
print(x > 10 or x < 10)

# a conditional statement runs if its condition is ture  or not false
if answer == "Chris Mclean":
    print("Hello Chris, stay away from my kids you psycho")
    print("this line prints for chris mclean")
elif answer == "keleshnikov":
    print("Give ak now you boney bum")
else:
    print("Oh thank god you arent chris")

    
print("this line isnt inside of the if statement so it prints regaurdless")

# ^ If checks a condition
# ^ Elif checks if the previous conditions were not true (you can have more than one ELif)
# ^ Else runs if no prior conditins were true

#pokemon trainer system
age = input("welcome to the trainer enrollment course, what is your age")
age = int(age)
if age == x >= 10:
    print("welcome to the pokemon trainer course, speak with proffesor butternut to choose your pokemon")
elif age == 9:
    print("you have to wait another year before entering the trainer program")
else:
    print("you are too young to enroll in the pokemon trainer course, come back when youre old enough!")
