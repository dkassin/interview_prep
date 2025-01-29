'''You are with your friends in a castle, where there are multiple rooms named after flowers. Some of the rooms contain treasures - we call them the treasure rooms. 

Each room contains a single instruction that tells you which room to go to next.

 *** instructions_1 and treasure_rooms_1 *** 

 lily* ---------      daisy  sunflower
               |        |     |
               v        v     v
 jasmin --> tulip*      violet* ----> rose* -->
            ^    |      ^             ^       |
            |    |      |             |       |
            ------    iris            ---------

* denotes a treasure room, e.g., rose is a treasure room, but jasmin isn't.

This is given as a list of pairs of (source_room, destination_room)

instructions_1 = [ 
    ["jasmin", "tulip"],
    ["lily", "tulip"],
    ["tulip", "tulip"], 
    ["rose", "rose"],
    ["violet", "rose"], 
    ["sunflower", "violet"],
    ["daisy", "violet"],
    ["iris", "violet"]
]

treasure_rooms_1 = ["lily", "tulip", "violet", "rose"]

Write a function that takes two parameters as input:
* a list of instructions represented as pairs of (source_room, destination_room), and
* a list containing the treasure rooms,

and returns a collection of all the rooms that satisfy the following two conditions:
* at least two *other* rooms have instructions pointing to this room
* this room's instruction immediately points to a treasure room 

filter_rooms(instructions_1, treasure_rooms_1) => ["tulip", "violet"]
* tulip can be accessed from rooms lily and jasmin. Tulip's instruction points to a treasure room (tulip itself)
* violet can be accessed from daisy, sunflower and iris. Violet's instruction points to a treasure room (rose)

Additional inputs

treasure_rooms_2 = ["lily", "jasmin", "violet"]  

filter_rooms(instructions_1, treasure_rooms_2) => []
* none of the rooms reachable from tulip or violet are treasure rooms

 *** instructions_2 and treasure_rooms_3 *** 

 lily ---------          --------
              |          |      |
              v          v      |
 jasmin --> tulip ---> violet*--^  

instructions_2 = [ 
    ["jasmin", "tulip"],
    ["lily", "tulip"],
    ["tulip", "violet"],
    ["violet", "violet"]       
]

treasure_rooms_3 = ["violet"]

filter_rooms(instructions_2, treasure_rooms_3) => ["tulip"]
* tulip can be accessed from rooms lily and jasmin. Tulip's instruction points to a treasure room (violet)

All the test cases: 
filter_rooms(instructions_1, treasure_rooms_1)    => ["tulip", "violet"]
filter_rooms(instructions_1, treasure_rooms_2)    => [] 
filter_rooms(instructions_2, treasure_rooms_3)    => ["tulip"]

Complexity Analysis variables:
T: number of treasure rooms
I: number of instructions given'''


instructions_1 = [
	["jasmin", "tulip"],
	["lily", "tulip"],
	["tulip", "tulip"],
	["rose", "rose"],
	["violet", "rose"],
	["sunflower", "violet"],
	["daisy", "violet"],
	["iris", "violet"]
]

instructions_2 = [
	["jasmin", "tulip"],
	["lily", "tulip"],
	["tulip", "violet"],
	["violet", "violet"]
]


treasure_rooms_1 = ["lily", "tulip", "violet", "rose"]
treasure_rooms_2 = ["lily", "jasmin", "violet"]
treasure_rooms_3 = ["violet"]


# * at least two *other* rooms have instructions pointing to this room
# this room's instruction immediately points to a treasure room 
from collections import Counter

def castle_search(inst, tr):
    
    valid_array = []
    remove_invalid = []
    for i in inst:
        if i[0] != i[1]:
            remove_invalid.append(i)
            
    array_of_rooms = [i[1] for i in remove_invalid]
    dict_of_rooms = Counter(array_of_rooms)
    for i in dict_of_rooms.items():
        if i[1] >= 2:
            valid_array.append(i[0])
    win_array = []
    for i in inst:
        if i[0] in valid_array and i[1] in tr:
            win_array.append(i[0])
    return win_array
        
castle_search(instructions_1,treasure_rooms_1)
castle_search(instructions_1,treasure_rooms_2)
castle_search(instructions_2,treasure_rooms_3)

assert castle_search(instructions_1,treasure_rooms_1) == ['tulip', 'violet']
assert castle_search(instructions_1,treasure_rooms_2) == []
assert castle_search(instructions_2,treasure_rooms_3) == ['tulip']