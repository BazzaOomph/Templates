#A basic print statement, which will print out the text string "Hello, World!"
#The expected output to the console is "Hello, World!" and includes a New Line character at the end
print("Hello, World!")

#Printing using two separate arguments
#The expected outcome is "Hello how are you?" with a new line character at the end.
print("Hello", "how are you?")


#Printing from variables
#expected outcome is "apple banana cherry" with a new line character at the end.
x = "apple" 
y = "banana" 
z = "cherry"
print(x,y,z)

#Printing from variables using a different separator. Normally the separator is " " 
#but we have changed this to be "***" instead.
#expected outcome is "apple***banana***cherry" with a new line character at the end followed
#by a second line of the same. (This aids with what's coming next)
x = "apple" 
y = "banana" 
z = "cherry"
print(x,y,z, sep="***")
print(x,y,z, sep="***")

#Printing from variables using a different separator AND removing the "end" character (so there is no new line)
#expected outcome is "apple***banana***cherryapple***banana***cherry"
x = "apple" 
y = "banana" 
z = "cherry"
print(x,y,z, sep="***", end='')
print(x,y,z, sep="***", end='')

#Just printing an empty string so it puts in a new line character, that way the next bit of code
#doesn't output onto the same line as the previous bit of code.
print("")

#Printing from variables using a different separator AND changing the "end" character (so there is no new line)
#expected outcome is "apple***banana***cherry!apple***banana***cherry!"
x = "apple" 
y = "banana" 
z = "cherry"
print(x,y,z, sep="***", end='!')
print(x,y,z, sep="***", end='!')