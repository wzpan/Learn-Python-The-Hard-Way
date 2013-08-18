#!/bin/python3

# ex43: Basic Object-Oriented Analysis and Design

# Class Hierarchy
# * Map
#   - next_scene
#   - opening_scene
# * Engine
#   - play
# * Scene
#   - enter
#   * Death
#   * Central Corridor
#   * Laser Weapon Armory
#   * The Bridge
#   * Escape Pod
# * Human
#   - attack
#   - defend
#   * Hero
#   * Monster

from sys import exit
from random import randint
import time
import math

class Engine(object):

    def __init__(self, scene_map, hero):
        self.scene_map = scene_map
        self.hero = hero

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print("\n--------")
            next_scene_name = current_scene.enter(self.hero)
            current_scene = self.scene_map.next_scene(next_scene_name)




class Scene(object):

    def enter(self):
        print("This scene is not yet configured. Subclass it and implement enter().")
        exit(1)

class Death(Scene):

    quips = [
        "You died.  You kinda suck at this.",
         "Your mom would be proud...if she were smarter.",
         "Such a luser.",
         "I have a small puppy that's better at this."
    ]

    def enter(self, hero):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):

    def enter(self, hero):
        print("The Gothons of Planet Percal #25 have invaded your ship and destroyed")
        print("your entire crew.  You are the last surviving member and your last")
        print("mission is to get the neutron destruct bomb from the Weapons Armory,")
        print("put it in the bridge, and blow the ship up after getting into an ")
        print("escape pod.")
        print("\n")
        print("You're running down the central corridor to the Weapons Armory when")
        print("a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume")
        print("flowing around his hate filled body.  He's blocking the door to the")
        print("Armory and about to pull a weapon to blast you.")

        action = input("> ")

        if action == "shoot!":
            print("Quick on the draw you yank out your blaster and fire it at the Gothon.")
            print("His clown costume is flowing and moving around his body, which throws")
            print("off your aim.  Your laser hits his costume but misses him entirely.  This")
            print("completely ruins his brand new costume his mother bought him, which")
            print("makes him fly into an insane rage and blast you repeatedly in the face until")
            print("you are dead.  Then he eats you.")
            return 'death'

        elif action == "dodge!":
            print("Like a world class boxer you dodge, weave, slip and slide right")
            print("as the Gothon's blaster cranks a laser past your head.")
            print("In the middle of your artful dodge your foot slips and you")
            print("bang your head on the metal wall and pass out.")
            print("You wake up shortly after only to die as the Gothon stomps on")
            print("your head and eats you.")
            return 'death'

        elif action == "tell a joke":
            print("Lucky for you they made you learn Gothon insults in the academy.")
            print("You tell the one Gothon joke you know:")
            print("Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr.")
            print("The Gothon stops, tries not to laugh, then busts out laughing and can't move.")
            print("While he's laughing you run up and shoot him square in the head")
            print("putting him down, then jump through the Weapon Armory door.")
            return 'laser_weapon_armory'

        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'

class LaserWeaponArmory(Scene):

    def enter(self, hero):
        print("You do a dive roll into the Weapon Armory, crouch and scan the room")
        print("for more Gothons that might be hiding.  It's dead quiet, too quiet.")
        print("You stand up and run to the far side of the room and find the")
        print("neutron bomb in its container.  There's a keypad lock on the box")
        print("and you need the code to get the bomb out.  If you get the code")
        print("wrong 10 times then the lock closes forever and you can't")
        print("get the bomb.  The code is 3 digits.")
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))

        print(code)

        guesses = 0

        while guesses < 10:
            guess = input("[keypad]> ")
            if guess == code:
                break
            print("BZZZZEDDD!")
            guesses += 1

        if guess == code:
            print("The container clicks open and the seal breaks, letting gas out.")
            print("You grab the neutron bomb and run as fast as you can to the")
            print("bridge where you must place it in the right spot.")
            return 'the_bridge'
        else:
            print("The lock buzzes one last time and then you hear a sickening")
            print("melting sound as the mechanism is fused together.")
            print("You decide to sit there, and finally the Gothons blow up the")
            print("ship from their ship and you die.")
            return 'death'



class TheBridge(Scene):

    def enter(self, hero):
        print("You burst onto the Bridge with the netron destruct bomb")
        print("under your arm and surprise 5 Gothons who are trying to")
        print("take control of the ship.  Each of them has an even uglier")
        print("clown costume than the last.  They haven't pulled their")
        print("weapons out yet, as they see the active bomb under your")
        print("arm and don't want to set it off.")

        action = input("> ")

        if action == "throw the bomb":
            print("In a panic you throw the bomb at the group of Gothons")
            print("and make a leap for the door.  Right as you drop it a")
            print("Gothon shoots you right in the back killing you.")
            print("As you die you see another Gothon frantically try to disarm")
            print("the bomb. You die knowing they will probably blow up when")
            print("it goes off.")
            return 'death'

        elif action == "slowly place the bomb":
            print("You point your blaster at the bomb under your arm")
            print("and the Gothons put their hands up and start to sweat.")
            print("You inch backward to the door, open it, and then carefully")
            print("place the bomb on the floor, pointing your blaster at it.")
            print("You then jump back through the door, punch the close button")
            print("and blast the lock so the Gothons can't get out.")
            print("Now that the bomb is placed you run to the escape pod to")
            print("get off this tin can.")
            return 'escape_pod'
        else:
            print("DOES NOT COMPUTE!")
            return "the_bridge"


class EscapePod(Scene):

    def enter(self, hero):
        print("You rush through the ship desperately trying to make it to")
        print("the escape pod before the whole ship explodes.  It seems like")
        print("hardly any Gothons are on the ship, so your run is clear of")
        print("interference.  You get to the chamber with the escape pods, and")
        print("now need to pick one to take.  Some of them could be damaged")
        print("but you don't have time to look.  There's 5 pods, which one")
        print("do you take?")

        good_pod = randint(1,5)
        print(good_pod)
        guess = input("[pod #]> ")


        if int(guess) != good_pod:
            print("You jump into pod %s and hit the eject button." % guess)
            print("The pod escapes out into the void of space, then")
            print("implodes as the hull ruptures, crushing your body")
            print("into jam jelly.")
            return 'death'
        else:
            print("You jump into pod %s and hit the eject button." % guess)
            print("The pod easily slides out into space heading to")
            print("the planet below.  As it flies to the planet, you look")
            print("back and see your ship implode then explode like a")
            print("bright star, taking out the Gothon ship at the same")
            print("time.  You won!")

            return 'final_fight'

class Win(Scene):
    ''' Win '''

    def enter(self, hero):

        print('''
        You Win! Good Job!
        ''')

        exit(0)

class Final(Scene):

    ''' final fight '''

    def enter(self, hero):

        # initialize a monster
        monster = Monster("Gothon")

        print("%s, You now came across the final boss %s! Let's fight!!!" % (hero.name, monster.name))


        a_combat = Combat()

        next_stage = a_combat.combat(hero, monster)
        return next_stage

class Combat(object):

    def combat(self, hero, monster):

        ''' combat between two roles '''

        round = 1
        while True:
            print('='*30)
            print('round %d' % round)
            print('='*30)
            print("Your HP: %d" % hero.hp)
            print("%s's HP: %d" % (monster.name, monster.hp))
            print('Which action do you want to take?')
            print('-'*10)
            print('1) attack - Attack the enemy')
            print('2) defend - Defend from being attacked, also will recover a bit')

            try:
                action = int(input('> '))
            except ValueError:
                print("Please enter a number!!")
                continue

            # defending should be done before attacking
            if action == 2:
                hero.defend()

            # action of monster, 1/5 possibility it will defends
            monster_action = randint(1, 6)
            if monster_action == 5:
                monster.defend()

            if action == 1:
                hero.attack(monster)
            elif action == 2:
                pass
            else:
                print("No such action!")

            if monster_action < 5:
                monster.attack(hero)

            # whether win or die
            if hero.hp <= 0:
                return 'death'

            if monster.hp <= 0:
                return 'win'

            hero.rest()
            monster.rest()

            round += 1

class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'final_fight': Final(),
        'win': Win()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)

class Human(object):

    ''' class for human '''
    defending = 0

    def __init__(self, name):
        self.name = name

    def attack(self, target):
        ''' attack the target '''
        percent = 0
        time.sleep(1)
        if target.defending == 1:
            percent = float(self.power) / 10.0 + randint(0, 10)
            target.hp = math.floor(target.hp - percent)
        else:
            percent = float(self.power) / 5.0 + randint(0, 10)
            target.hp = math.floor(target.hp - percent)
        print("%s attack %s. %s's HP decreased by %d points." % (self.name, target.name, target.name, percent))

    def defend(self):
        ''' be in the defending state. '''
        self.defending = 1
        print("%s is trying to defend." % self.name)

    def rest(self):
        ''' recover a bit after each round '''
        if self.defending == 1:
            percent = self.rate * 10 + randint(0, 10)
        else:
            percent = self.rate * 2 + randint(0, 10)
        self.hp += percent
        print("%s's HP increased by %d after rest." % (self.name, percent))
        self.defending = 0


class Hero(Human):
    ''' class for hero '''

    hp = 1000
    power = 200
    rate = 5

class Monster(Human):
    ''' class for monster '''
    hp = 5000
    power = 250
    rate = 5

a_map = Map('central_corridor')
a_hero = Hero('Joe')
a_game = Engine(a_map, a_hero)
a_game.play()
