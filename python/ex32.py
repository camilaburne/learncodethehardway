the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# This first kind of for loop goes through a list
for number in the_count:
    print("this is count %d" % number)

# again but list made of strings
for fruit in fruits:
    print("A fruit of type: %s" % fruit)

# Also we can go through mixed lists
for i in change:
    print("I got %r" % i )

# We can build lists, starting with an empty one
elements = []

# Then we use range funtciont to do 0 to 5 counts
for i in range(0,6):
    print("Adding %d to the list. " % i)
    elements.append(i)
    
# And now we can print them
for i in elements:
    print("Elements was: %d " % i)
