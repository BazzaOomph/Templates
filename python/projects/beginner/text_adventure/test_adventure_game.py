import json
import pprint

with open("D:\\Coding\\Github\\Templates\\python\\projects\\beginner\\text_adventure\\rooms.json") as f:
    rooms = json.load(f)

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
pprint.pprint(rooms)


#Text adventure game in Python


#Able to define a room.
#Rooms have exits: North, East, South, West. Not all the exits are available in each room.
#Map is a matrix of rooms. Rooms have objects.
#The player can interact with objects in order to solve puzzles.
#Puzzles must be solved before they can complete the game.

#Game idea:
#It's a school. You're a student.
#As a student you have to go to classes in a linear order. Classes are held in rooms.
#When you get to the right room in the right order, the class starts.

#You are given a challenge, where you play a mini-game until the level is over, at which point you're released from the room
#and allowed to go to the next room.

#Once you have completed all the challenges in all the rooms, you're allowed to catch the bus home.

#How do I "define a room?"
#How do I create a map of all the rooms?
#How do I keep track of where the player is in these rooms?

#The player has the following things:
#A location (which contains the ID number of the room they're in)
#An inventory (which contains object IDs)
#A number indicating how much life they have left

#----------------------
#the map consists of 10 * 3 "rooms". "Outside" is the bus stop at 1x2

#FFFRWRWRWW
#BPDHHHHHHW
#FFFRWRWRWW

# 2021-07-26 
#F = Fence (cannot pass)
#W = Wall (cannot pass)
#B = Bus Stop
#P = Pathway
#D = Main door into the school
#H = Hallway
#R = Room

# 2021-07-26 How do I store the map? Lists? 
#----------------------

#Rooms
# 2021-07-26 Rooms have a Room ID, a location number, an inventory of objects in the room and Directions you can leave.
#Direction you can leave could be four separate bools: exit_north, exit_east_, exit_south, exit_west
#Alternatively for exits, I could have the exits make you "teleport" into a room number.. This would
#Allow for more varied travel!
# 2021-07-27 
#So, I think having a list which contains all the rooms is a good idea. Each room is an object with a few different parameters and potentially methods,
#one of the parameters will be the exits out of this room and which rooms they go to. I haven't quite figured
#out how to store that information.. Obviously I need one field which stores all the exits, so it will most likely be a list.
#Each exit needs to have the following information about it:
#The "direction" the person must type in order to use that exist
#   Eg: North, South, Elevator, Transporter
#A "description" of the 'direction' or exit point.
#   eg: Looking North you see a pathway.
#   eg: Look Transporter you see that it appears to be bigger on the inside
#The room number you'll be transported to when you travel in that direction
#   eg: 3

#Should I be storing the map file separately? Like in a JSON file? Probably. Let's get a few rooms working first and go from there.

#######
#How to start? 
#Create a list of rooms, with hard-coded descriptions
#The player can move from room 1, to room 2, to room 3. 

#Create each room as a dict



# rooms = [
#     {'room_number':1, 'room_description':'Room 1'},
#     {'room_number':2, 'room_description':'Room 3'},
#     {'room_number':3, 'room_description':'Room 4'}
# ]

# roomlist = [1,2,3]
# playerLocation = 1

# while True:
#     print(roomlist[playerLocation])
#     playerDirection = input("What direction do you want to go?")
#     if playerDirection == "e":
#         playerLocation+=1
#     if playerDirection == "w":
#         playerLocation-=1

