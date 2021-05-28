states = {
        "Oregon": "OR",
        "Florida": "FL",
        "California": "CA",
        "New York": "NY",
        "Michigan": "MI"
        }
cities = {
        "CA": "San Francisco",
        "MI": "Detroit",
        "FL": "Jacksonville"
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print some cities
print('_'*10)
print("NY State has:", cities['NY'])

# print cities usieng the states then cities dict
print('_'*10)
print('Michigan has: ', cities[states['Michigan']])

# print all abbreviations
print('_'*10)
for state, abbrev in states.items():
    print( "%s is abbreviated as %s " % (state, abbrev))

# print every city in state
for abbrev, city in cities.items():
    print( "%s has the city %s " % (abbrev, city))

# now both
for state, abbrev in states.items():
    print( "%s is abbreviated as %s and has the city %s" % (state, abbrev, cities[abbrev]))

# try to get a state not in dict
print('_'*10)
state = states.get('Texas', None)
if not state:
    print("No texas yet")
