def add(a,b):
    print("Adding %d + %d" % (a,b))
    return a+b


def substract(a,b):
    print("Substracting %d - %d" % (a,b))
    return a-b

def multiply(a,b):
    print("Multiplying %d * %d" % (a,b))
    return a*b


def divide(a,b):
    print("Dividing %d / %d" % (a,b))
    return a/b


age = add(30,5)
height = substract(78,4)
# aaaah too many pointless writing

what = add(age, substract(height,1))

print('That becomes', what)
