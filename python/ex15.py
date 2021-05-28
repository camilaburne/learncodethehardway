from sys import argv

# Here we are storing the two arguments we pass when we execute the file.
# The name itself (script) plus the file name
script, filename = argv

# Now we are open the filename, and saving it on txt.
txt = open(filename)

print("Here's your file %r: " % filename)
# Read is a method applied to a file, we show its contents
print(txt.read())

print("Type the filename again:")
# Now we read the file, but using a raw input
file_again = input(">")
txt_again = open(file_again)
print(txt_again.read())
