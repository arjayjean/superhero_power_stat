import subprocess
import requests
import time
import os
import json
import sys
import extract
# import data

file = open('data/superhero_api.json', 'r')
data = file.read()
character = json.loads(data)

length = len(character)

# Character's alias/codename
alias = [character[n]['name'] for n in range(length)]


# Character's name
name = [character[n]['biography']['fullName'] for n in range(length)]


# Character's gender
gender = [character[n]['appearance']['gender'] for n in range(length)]


# Character's race
race = [character[n]['appearance']['race'] for n in range(length)]


# Character's side/alignment
side = [character[n]['biography']['alignment'] for n in range(length)]


# Publishing companmy that created the character
publisher = [character[n]['biography']['publisher'] for n in range(length)]


# List to hold all of the character's stats
character_stat = []

def powerstats(*stats):

    for i in range(length):
        # List to hold each individual character's stat
        individual_stat = []
        for stat in stats:
            num = character[i]['powerstats'][f'{stat}']
            individual_stat.append(num)
        overall = round( ((sum(individual_stat)/length) * 100), 2)
        individual_stat.append(overall)
        character_stat.append(individual_stat)

powerstats('intelligence', 'strength', 'speed', 'durability', 'power', 'combat')


print(character_stat)
# print(f'\n{len(race)}')


# def unique(list):
 
#     unique_list = []

#     for x in list:
#         if x not in unique_list:
#             unique_list.append(x)

#     for i in unique_list:
#         print(i)

# unique(race)

print('\n')



# print(  )
# print(character_stat)