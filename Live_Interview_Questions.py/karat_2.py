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

# I should have written this out beforehand

## Plan to solve
#1 Find all instructions that have at least two other rooms pointing at themselves
#1a Remove all instructions that point to themselves
#1b Take count of all rooms present after remove the rooms that point to themselves
#1c Remove all rooms that have a count less then 2
#2 Select rooms that are both valid rooms and point to a treasure room
#3 Return the selected rooms

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

## Math Section Questions
#1 Confusion matrix
## Calculate precision, accuracy and recall

#2 A population has a disease that is present 0.1, if a test has a 10% false positive and a 1% false negative
#What is the percentage that if someone has the disease.

#3 What distribution model would you use for the given situations
# percentage of emails opened in 1000 emails

#4 what does a p < .05 mean?
# What are two examples of this? or something like this

## SQL PROBLEM


# Here is the SQL problem adapted specifically for PostgreSQL:

# SQL Problem: Highest Salesperson in December
# Schema Definition
# sql
# Copy
# Edit
# CREATE TABLE salesperson (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100) NOT NULL
# );

# CREATE TABLE sales (
#     id SERIAL PRIMARY KEY,
#     salesperson_id INT REFERENCES salesperson(id),
#     amount DECIMAL(10,2) NOT NULL,
#     date DATE NOT NULL
# );
# Problem Constraints
# The salesperson table has 5 unique salespeople.
# The sales table contains 10 sales transactions, assigned across the 5 salespersons.
# The sales.date column includes dates from December and January.

# The goal is to find the salesperson with the highest total sales in December, returning the following columns:
# name	month	year	amount
# John	12	2024	5000.00


# ChatGPT solution 
# 
# WITH DecemberSales AS (
#     SELECT 
#         salesperson_id,
#         EXTRACT(MONTH FROM date) AS month,
#         EXTRACT(YEAR FROM date) AS year,
#         SUM(amount) AS total_amount
#     FROM sales
#     WHERE EXTRACT(MONTH FROM date) = 12
#     GROUP BY salesperson_id, EXTRACT(YEAR FROM date)
# )
# SELECT 
#     sp.name,
#     ds.month,
#     ds.year,
#     ds.total_amount AS amount
# FROM DecemberSales ds
# JOIN salesperson sp ON ds.salesperson_id = sp.id
# ORDER BY ds.total_amount DESC
# LIMIT 1; 