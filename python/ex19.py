def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("you have %d cheeses!" % cheese_count)
    print("you have %d boxes of crackers!" % boxes_of_crackers)
    print("Thats enough for a party, get a blanket.\n")

print("we can give the function numbers directly")
cheese_and_crackers('abc',0)

print("or use variables from our script")
amount_of_chesse = 10
amount_of_crackers = 20

cheese_and_crackers(10,20)

print("we can do math inside too")
cheese_and_crackers(10+20,20+30)


print("and combine the variables")
cheese_and_crackers(amount_of_chesse+20,amount_of_crackers+30)
