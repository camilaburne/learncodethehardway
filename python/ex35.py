from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take? ")
    next = input(">")

    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number")

    if how_much < 50:
        print("Niice you're not greedy, you win")
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print("There's a bear here\nThe bear has a bunch of money\nHow are you going to move the bear? ")
    bear_moved = False

    while True:
        next = input(">")

        if next == "Take honey":
            dead("The bear looks at you thhen slaps your face off.")
        elif next == "Taunt bear" and not bear_moved:
            print("The bear has moved, you can go now")
            bear_moved = True
        elif next == "Taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off")
        elif next == "Open door" and bear_moved:
            gold_room()
        else:
            print("No idea what this means")


def cthulhu_room():
    print("Here you see the great evil Cthulhu\nWhatever stares at you and you go insane\nDo you flee for your life or eat your head? ")
    next = input(">")
    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty")
    else: cthulhu_room()

def dead(why):
    print(why, " Good job!")
    exit(0)

def start():
    print("You're in a dark room.\nThere's a door to your right and left.\nWhich one do you choose?")
    next = input(">")

    if next =='left':
        bear_room()
    elif next =='right':
        cthulhu_room()
    else:
        dead('You stuble around the room until you starve')


start()
