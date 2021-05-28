people = 0
cars = 0
buses = 0

if cars > people:
    print("We should take cars")
elif cars < people:
    print("We shouldnt take cars")
else:
    print("We can't decide")

if buses > cars:
    print("too many buses")
elif buses < cars:
    print("maybe we can take the buses")
else:
    print("We still can't decide")


if people > buses:
    print("Lets take the buses")
else:
    print("Lets stay home")
