from sys import exit
import random

# the game was lame, I removed the bridge and made it shorter.

class Scene(object):
    def enter(self):
        print("You got lost in a scene that doesn't exists.")
        exit(1)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map
    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print("\n\n\n\n")
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)


class Death(Scene):
    def enter(self):
        msg = ["You died.","You died, surprisingly.","Looks like you died."]
        print(random.choice(msg))
        exit(1)


class Finished(Scene):
    def enter(self):
        msg = ["You are amazing.","You survived, surprisingly.","Looks like you survived."]
        print(random.choice(msg))
        print("\nGreat pandemic surviving!")
        exit(0)

class CentralCorridor(Scene):
    def enter(self):
        print("You entered a pandemic. Do you know how are you going to survive it?")
        action = input("Will you stay *in*, *out* or...? \n...")

        if action == 'in':
            print('You went crazy. You died')
            return 'death'

        elif action == 'out':
            print('You got infected. You died')
            return 'death'
        else:
            return 'laser_weapon_armory'


class LaserWeaponArmory(Scene):
    def enter(self):
        print("""You wont survive unless you accurately estimate
                 how many people are left infected, in 3 guesses.""")

        ans = int(random.choice([100,1000,10000]))
        guess = int(input("Are there 10000, 1000, or 100 infected?\n..."))
        guesses = 0

        while guesses < 3 and  guess!=  ans:
            guesses += 1
            guess = int(input("Try guessing again!\n..."))

        if guess==ans:
            print("You live another day!")
            return 'escape_pod'
        elif guess < ans:
            print("You overestimated the danger. You were too cautious and went bananas.")
            return 'death'
        elif guess > ans:
            print("You understimated the danger. You were too reckless and put yourself at risk.")
            return 'death'
        else:
            print("Your estimate was off")
            return 'death'

class EscapePod(Scene):
    def enter(self):
        print("You face one last challenge! Apparently you have to choose a number now")
        good_pod = random.choice([1,2])
        guess = int(input("Choose 1 or 2\n..."))

        if int(guess) != good_pod:
            print("Wrong choice")
            return 'death'
        else:
            print("You made it!")
            return 'finished'

class Map(object):

    scenes = {
                'central_corridor': CentralCorridor(),
                'laser_weapon_armory': LaserWeaponArmory(),
                'escape_pod': EscapePod(),
                'death': Death(),
                'finished': Finished()
                }

    def __init__(self,start_scene):
        self.start_scene = start_scene

    def next_scene(self,scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map("central_corridor")
a_game = Engine(a_map)
a_game.play()
