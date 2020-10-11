# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

"""print(10*"Hello world java\n")
print("C:\"\\not")
var1 = "Hello world"
var2 = 3
var3 = 344.5
print(type(var2))"""

"""print("Enter the first no")
var1 = input()
print("Enter the first no")
var2 = input()
print("Sum is",int(var1)+int(var2))"""

# String slicing
mystr="twinkle Twinkle Little star"
print(mystr)
print(mystr[0])  # It will print the character placed at 0 index
print(mystr[0:4])
# It will print the character placed at 0,1,2,3 it will include
# the index no which is before the colon and exclude the colon no which is after the colon
print(mystr[0:5])
print(len(mystr))  # It will print the length of array
#  print(mystr[76])   It will show error string Index out of range
print(mystr[0:79])  # This will not show error but print till that index where character is present
print(mystr[0:5:3])  # third value shows how many character should be skipped
print(mystr[::])  # It will take by default 0:last index:1
print(mystr[::6000])  # It will take the first character placed at 0 index will be taken
print(mystr[-4:-2])   # It will take the character from the end of the string
print(mystr[::-1])    # It will reverse the string
print(mystr.isalpha())  # It will check whether my string is alphanumeric or not
print(mystr.endswith("star"))  # It will return the boolean whether the argument
# passed in endswith are the one with which string is ending
print(mystr.count("t"))  # It will print the how many characters passed in argument are present in string
print(mystr.capitalize())  # It will capitalize the first character
# and lowers the first character of rest all the characters of the string
print(mystr.find("Little"))  # It will print the index no from where the character little is starting
print(mystr.lower())
print(mystr.upper())
print(mystr.replace("Little","big"))