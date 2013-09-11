from sys import exit
from random import randint

def death():
	quips = ["You died. You kinda suck at this.",
		 "Nice job, you died ...jackass.",
		 "Suck a luser.",
		 "I have a small puppy that's better at this."]

	print quips[randint(0, len(quips)-1)]
	exit(1)

def cnetral_corridor():
	print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
	print "your entire crew. You are the last surviving member and your last"
	print "mission is to get the neutron destruct bomb from the Weapons Armory,"
	print "put it in the bridge, and blow the ship up after getting an "
	print "escape pod."
	print "\n"
	print "Youre running down the central corridor to the Weapons Armory when"
	print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
	print "flowing around his hate filled body. He's blocking the door to the"
	print "Armory and about to pull a weapon to blast you."

	action = raw_input("> ")
	
	if action == "shoot!":
		print "Quick on the draw you yank out your blaster and fire it at the Gothon."
		print "His clown costume is flowing and moving around his body, which throws"
		print "off your aim. Your laser hits his costume but misses him entirely. This"
		print "completely ruins his brand new costume his mother bought him, which"
		print "makes him fly into an insane rage and blast you repeatedly in the face until"
		print "you are dead. THen he eats you."
		return 'death'

	elif action == "dodge!":
		print "Like a world class bower you dodge, weave, slip and slide right"
		print "as the Gothon's blaster cranks a laser past your head."
		return 'death'
	
	elif action == "tell a joke":
		print "Lucky for you they made you learn Gothon insults in the academy."
		return 'laser_weapon_armory'

	else:
		print "DOES NOT COMPUTE!"
		return 'central_corridor'

def laser_weapon_armory():
	print "you do a dive roll into the Weapon Armory, crouch and scan the room"
	print "for more Gothons that might be hiding. It's dead quiet, too quiet."
	code = "%d" % (randint(1,9))
	guess = raw_input("[keypard]> ")
	guesses = 0

	while guess != code and guesses <10:
		print "BZZZZEDDD!"
		guesses += 1
		guess = raw_input("[keypad]> ")

	if guess == code:
		print "The container clicks open and the seal breaks, letting gas out."
		print "You grab the neutron bomb and run as fast as you can to the"
		return 'the_bridge'
	else:
		print "The lock buzzes one last time and then you hear a sickening"
		print "melting sound as the mechanism is fused together."
		return 'death'

def the_bridge():
	print "You burst onto the Bridge with the netron destruct bomb"
	print "under your arm and surprise 5 Gothons who are trying to"
	
	action = raw_input("> ")
	
	if action == "throw the bomb":
		print "In a panic you throw the bomb at the group of Gothons"
		print "and make a leap for the door."
		return 'death'
	
	elif action == "slowly place the bomb":
		print "You point your blaster at the bomb under your arm"
		print "and the Gothons put their hands up and start to sweat."
		return 'escape_pod'
	else:
		print "DOES NOT COMPUTE!"
		return "the_bridge"

def escape_pod():
	print "You rush through the ship desperately trying to make it to"
	print "the escape pod before the whole ship explodes. It seems like"
	print "hardly any Gothons are on the ship, so your run is clear of"
	
	good_pod = randint(1,5)
	guess = raw_input("[pod #]> ")

	if int(guess) != good_pod:
		print "You jump into pod %s and hit the eject button." % guess
		return 'death'
	else:
		print "You jump into pod %s and hit the eject button." % guess
		print "The pod easily slides out into space heading to"
	exit(0)

ROOMS = {
	'death': death,
	'central_corridor': laser_weapon_armory,
	'the_bridge': the_bridge,
	'escape_pod': escape_pod
}

def runner(map, start):
	next = start

	while True:
		room = map[next]
		print "\n========="
		next = room()

runner(ROOMS, 'central_corridor')
