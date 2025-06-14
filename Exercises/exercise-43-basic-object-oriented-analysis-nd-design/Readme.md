# Basic object oriented analysis and design

This exercise is to build a game. But before that author tells bunch of stuff which might help to build something from scratch.

The following process is for how to build somthing from python specifically with object-oriented programming (OOP):
1. Write or draw about the problem.
2. Extract key concepts from 1 and research them.
3. Create a class hierarchy and object map for the concepts.
4. Code the classes and a test to run them.
5. Repeat and refine.

This process is that it is “top down,” meaning it starts from the very abstract loose idea
and then slowly refines it until the idea is solid and something you can code.

## The Analysis of a Simple Game Engine

Game name: **Gothons from Planet Percal #25**, and it will be a small space servival game.

### 1. Write or Draw about the problem

Here surface of game

“Aliens have invaded a space ship and our hero has to go through a maze of rooms defeating them so he can escape into an escape pod to the planet below. The game will be more like a Zork or Adventure type game with text outputs and funny ways to die. The game will involve an engine that runs a map full of rooms or scenes. Each room will print its own description when the player enters it and then tell the engine what room to run next out of the map.”

### 2. Describe each scene:

|Scene|Describe|
|:---:|:---|
|Death |This is when the player dies and should be something funny.|
|Central Corridor |This is the starting point and has a Gothon already standing there that the players have to defeat with a joke before continuing.|
|Laser Weapon Armory |This is where the hero gets a neutron bomb to blow up the ship before getting to the escape pod. It has a keypad the hero has to guess the number for.|
|The Bridge |This is another battle scene with a Gothon where the hero places the bomb.|
|Escape Pod |This is where the hero escapes but only after guessing the right escape pod.|

### 3. Extract Key Concepts and Research Them
Extract some of the nouns and analyze their class hierarchy. First make a list of all the nouns:
* Alien
* Player
* Ship
* Maze
* Room
* Scene
* Gothon
* Escape Pod
* Planet
* Map
* Engine
* Death
* Central Corridor
* Laser Weapon Armory
* The Bridge

### 4. Create a Class Hierarchy and Object Map for the Concepts

Look for **What is similar to other things?** and **What is basically just another word for another thing** eg.
- “Room” and “Scene” are basically the same thing
- “Central Corridor, Death” are basically just Scenes
- “Maze” and “Map” are basically the same

Just like above eg. class hierarchy that looks like:
```
* Map
* Engine
* Scene
    * Death
    * Central Corridor
    * Laser Weapon Armory
    * The Bridge
    * Escape Pod
```

Go through and figure out what actions are needed on each thing based on verbs in the description. For example, need a way to “run” the engine, “get the next scene” from the map, get the “opening scene,” and “enter” a scene. Add those like this:

```
* Map
    − next_scene
    − opening_scene
* Engine
    − play
* Scene
    − enter
    * Death
    * Central Corridor
    * Laser Weapon Armory
    * The Bridge
    * Escape Pod
```

### 5. Code the Classes and a Test to Run Them

Once have this tree of classes and some of the functions, open up a source file in my editor and try to
write the code for it [Exercise Step-1](#exercise). Also added a little bit of code at the end to run it.

### 6. Repeat and Refine

The last step in my little process isn’t so much a step as it is a while-loop. You don’t ever do this as a one-pass operation. Instead you go back over the whole process again and refine it based on information you’ve learned from later steps. Sometimes I’ll get to step 3 and realize that I need to work on 1 and 2 more, so I’ll stop and go back and work on those. Sometimes I’ll get a flash of inspiration and jump to the end to code up the solution in my head while I have it there, but then I’ll go back and do the previous steps to make sure I cover all the possibilities I have.

The other idea in this process is that  t’s not just something you do at one single level but something that you can do at every level when you run into a particular problem. Let’s say I don’t know how to write the Engine.play method yet. I can stop and do this whole process on just that one function to figure out how to write it.

Directly take this from book.

## Top Down versus Bottom Up

The process is typically labeled “top down” since it starts at the most abstract concepts (the top) and
works its way down to actual implementation. This example follow this "top down" method.

Let see “bottom up.” Here are the general steps you follow to do this:
1. Take a small piece of the problem; hack on some code and get it to run barely.
2. Refine the code into something more formal with classes and automated tests.
3. Extract the key concepts you’re using and research them.
4. Write a description of what’s really going on.
5. Go back and refine the code, possibly throwing it out and starting over.
6. Repeat, moving on to some other piece of the problem.

This "Bottom Up" process is very good when you know small pieces of the overall puzzle, but maybe don’t have enough information yet about the overall concept. Breaking it down in little pieces and exploring with code then helps you slowly grind away at the problem until you’ve solved it.

## Exercise

1. This is a skeleton code.
    ```py
    class Scene():

        def enter(self):
            pass

    class Engine():

        def __init__(self, scene_map):
            pass

        def play(self):
            pass
        pass

    class Death(Scene):

        def enter(self):
            pass
        pass

    class CentralCorridor(Scene):

        def enter(self):
            pass
        pass

    class LaserWeaponArmory(Scene):

        def enter(self):
            pass
        pass

    class TheBridge(Scene):

        def enter(self):
            pass
        pass

    class EscapePod(Scene):

        def enter(self):
            pass
        pass

    class Map():

        def __init__(self, start_scene):
            pass

        def next_scene(self, scene_name):
            pass

        def opening_scene(self):
            pass

    a_map = Map('central_corridor')
    a_game = Engine(a_map)
    a_game.play()
    ```
2. This is the entire code.
    ```py
    from sys import exit
    from random import randint
    from textwrap import dedent

    class Scene():

        def enter(self):
            print("This scene is not yet configured.")
            print("Subclass it and implement enter().")
            exit(1)

    class Engine():

        def __init__(self, scene_map):
            self.scene_map = scene_map

        def play(self):
            current_scene = self.scene_map.opening_scene()
            last_scene = self.scene_map.next_scene('finished')

            while current_scene != last_scene:
                next_scene_name = current_scene.enter()
                current_scene = self.scene_map.next_scene(next_scene_name)

            # be sure to print out the last scene
            current_scene.enter()

    class Death(Scene):

        quips = [
                "You died. You kinda suck at this.",
                "Your Mom would be proud...if she were smarter.",
                "Such a looser.",
                "I have a small puppy that's better at this.",
                "You're worse than your Dad's jokes."
                ]

        def enter(self):
             print(Death.quips[randint(0, len(self.quips) - 1)])
             exit(1)

    class CentralCorridor(Scene):

        def enter(self):
            print(dedent("""
            The Gothons of Planet Percal #25 have invaded your ship and
            destroyed your entire crew. You are the last surviving
            member and your last mission is to get the neutron destruct
            bomb from the Weapons Armory, put it in the bridge, and
            blow the ship up after getting into an escape pod.

            You're running down the central corridor to the Weapons
            Armory when a Gothon jumps out, red scaly skin, dark grimy
            teeth, and evil clown costume flowing around his hate
            filled body. He's blocking the door to the Armory and
            about to pull a weapon to blast you.
             """))

            action = input("> ")

            if action == "shoot!":
                print(dedent("""
                    Quick on the draw you yank out your blaster and fire
                    it at the Gothon. His clown costume is flowing and
                    moving around his body, which throws off your aim.
                    Your laser hits his costume but misses him entirely.
                    This completely ruins his brand new costume his mother
                    bought him, which makes him fly into an insane rage
                    and blast you repeatedly in the face until you are
                    dead. Then he eats you.
                    """))
                return 'death'

            elif action == "dodge!":
                print(dedent("""
                Like a world class boxer you dodge, weave, slip and
                slide right as the Gothon's blaster cranks a laser
                past your head. In the middle of your artful dodge
                your foot slips and you bang your head on the metal
                wall and pass out. you wake up shortly after only to 
                die as the Gothon stomps on your head and eats you.
                """))
                return 'death'

            elif action == "tell a joke":
                print(dedent("""
                Lucky for you they made you learn Gothon insults in
                the academy. You tell the one Gothon joke you know:
                Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr,
                fur fvgf nebhaq gur ubhfr. The Gothon stops, tries
                not to laugh, then busts out laughing and can't move.
                While he's laughing you run up and shoot him square in
                the head putting him down, then jump through the 
                Weapon Armory door.
                """))
                return 'laser_weapon_armory'

            else:
                print("DOES NOT COMPUTE!")
                return 'central_corridor'

    class LaserWeaponArmory(Scene):

        def enter(self):
            print(dedent("""
            You do a dive roll into the Weapon Armory, crouch and scan
            the room for more Gothons that might be hiding. It's dead
            quiet, too quiet. You stand up and run to the far side of
            the room and find the neutron bomb in its container.
            There's a keypad lock on the box and you need the code to
            get the bomb out. If you get the code wrong 10 times then
            the lock closes forever and you can't get the bomb. The
            code is 3 digits.
            """))

            code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
            guess = input("[keypad]> ")
            guesses = 0

            while guess != code and guesses < 10:
                print("BZZZZEDDD!")
                guesses += 1
                guess = input("[keypad]> ")

                if guess == code:
                    print(dedent("""
                    The container clicks open and the seal breaks, letting
                    gas out. You grab the neutron bomb and run as fast as
                    you can to the bridge where you must place it in the
                    right spot.
                    """))
                    return 'the_bridge'

                else:
                    print(dedent("""
                    The lock buzzes one last time and then you hear a
                    sickening melting sound as the mechanism is fused
                    together. You decide to sit there, and finally the
                    Gothons blow up the ship from their ship and you die.
                    """))
                    return 'death'

    class TheBridge(Scene):

        def enter(self):
            print(dedent("""
            You burst onto the Bridge with the netron destruct bomb
            under your arm and surprise 5 Gothons who are trying to
            take control of the ship. Each of them has an even uglier
            clown costume than the last. They haven't pulled their
            weapons out yet, as they see the active bomb under your
            arm and don't want to set it off.
            """))

            action = input("> ")

            if action == "throw the bomb":
                print(dedent("""
                In a panic you throw the bomb at the group of Gothons
                and make a leap for the door. Right as you drop it a
                Gothon shoots you right in the back killing you. As
                you die you see another Gothon frantically try to
                disarm the bomb. You die knowing they will probably
                blow up when it goes off.
                """))
                return 'death'

            elif action == "slowly place the bomb":
                print(dedent("""
                You point your blaster at the bomb under your arm and
                the Gothons put their hands up and start to sweat.
                You inch backward to the door, open it, and then
                carefully place the bomb on the floor, pointing your
                blaster at it. You then jump back through the door,
                punch the close button and blast the lock so the
                Gothons can't get out. Now that the bomb is placed
                you run to the escape pod to get off this tin can.
                """))
                return 'escape_pod'

            else:
                print("DOES NOT COMPUTE!")
                return "the_bridge"

    class EscapePod(Scene):

        def enter(self):
            print(dedent("""
            You rush through the ship desperately trying to make it to
            the escape pod before the whole ship explodes. It seems
            like hardly any Gothons are on the ship, so your run is
            clear of interference. You get to the chamber with the
            escape pods, and now need to pick one to take. Some of
            them could be damaged but you don't have time to look.
            There's 5 pods, which one do you take?
            """))

            good_pod = randint(1,5)
            guess = input("[pod #]> ")

            if int(guess) != good_pod:
                print(dedent("""
                You jump into pod {guess} and hit the eject button.
                The pod escapes out into the void of space, then
                implodes as the hull ruptures, crushing your body into
                jam jelly.
                """))
                return 'death'
            else:
                print(dedent("""
                You jump into pod {guess} and hit the eject button.
                The pod easily slides out into space heading to the
                planet below. As it flies to the planet, you look
                back and see your ship implode then explode like a
                bright star, taking out the Gothon ship at the same
                time. You won!
                """))
                return 'finished'

    class Finished(Scene):

        def enter(self):
            print("You won! Good job.")
            return 'finished'

    class Map():

        scenes = {
                'central_corridor': CentralCorridor(),
                'laser_weapon_armory': LaserWeaponArmory(),
                'the_bridge': TheBridge(),
                'escape_pod': EscapePod(),
                'death': Death(),
                'finished': Finished(),
                }

        def __init__(self, start_scene):
            self.start_scene = start_scene

        def next_scene(self, scene_name):
            val = Map.scenes.get(scene_name)
            return val

        def opening_scene(self):
            return self.next_scene(self.start_scene)

    a_map = Map('central_corridor')
    a_game = Engine(a_map)
    a_game.play()
    ```
3. Run script
    ```
    $ python ex43.py 

    The Gothons of Planet Percal #25 have invaded your ship and
    destroyed your entire crew. You are the last surviving
    member and your last mission is to get the neutron destruct
    bomb from the Weapons Armory, put it in the bridge, and
    blow the ship up after getting into an escape pod.

    You're running down the central corridor to the Weapons
    Armory when a Gothon jumps out, red scaly skin, dark grimy
    teeth, and evil clown costume flowing around his hate
    filled body. He's blocking the door to the Armory and
    about to pull a weapon to blast you.

    > dodge
    DOES NOT COMPUTE!

    The Gothons of Planet Percal #25 have invaded your ship and
    destroyed your entire crew. You are the last surviving
    member and your last mission is to get the neutron destruct
    bomb from the Weapons Armory, put it in the bridge, and
    blow the ship up after getting into an escape pod.

    You're running down the central corridor to the Weapons
    Armory when a Gothon jumps out, red scaly skin, dark grimy
    teeth, and evil clown costume flowing around his hate
    filled body. He's blocking the door to the Armory and
    about to pull a weapon to blast you.

    > dodge!  

    Like a world class boxer you dodge, weave, slip and
    slide right as the Gothon's blaster cranks a laser
    past your head. In the middle of your artful dodge
    your foot slips and you bang your head on the metal
    wall and pass out. you wake up shortly after only to 
    die as the Gothon stomps on your head and eats you.

    You're worse than your Dad's jokes.
    ```

## Note

There are few things that need to add like doing study drill but for now let's move on. As for note

1. `from textwrap import dedent` - dedent help wrapping with multi-line statement `"""`.
    