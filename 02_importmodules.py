#import the basics module to use its code
import basics

# make new application object from the basics module
app = basics.newProgram()

# use a new method that belongs to our new applicatin object
app.print("yo mama")

# print a property of our new application object
app.print(app.debugging)

# This line wont print if app.debbugging is false
app.debug("Hello")

# we'll enable debugging for the application
app.debugging = True
app.debug("now it works")

# import a default python module
import random

# use a method from the random module
randomNumber = random.randint(1,10)
app.print(randomNumber)

