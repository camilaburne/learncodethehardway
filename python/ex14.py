from sys import argv

script, user_name = argv
prompt = '>'

print("Hi %s I'm the %s script" % (user_name, script))

print("I'd like to ask you, do you like me %s?" % user_name)
likes = input(prompt)

print("Where do you live %s?" % user_name)
lives = input(prompt)

print("Alright, so you said %r about liking me, and you live in %r. Not sure what that is. " % (likes, lives))
