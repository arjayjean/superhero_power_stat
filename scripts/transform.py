import json
import subprocess

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


# List to hold all of the character's skill rating
skill_rating = []

def skills(*rates):

    for i in range(length):
        # List to hold each individual character's skill rating
        rating = []
        for rate in rates:
            num = character[i]['powerstats'][f'{rate}']
            rating.append(num)
        overall = round( ((sum(rating)/length) * 100), 2)
        rating.append(overall)
        skill_rating.append(rating)

skills('intelligence', 'strength', 'speed', 'durability', 'power', 'combat')

intelligence = [skill_rating[n][0] for n in range(length)]
strength = [skill_rating[n][1] for n in range(length)]
speed = [skill_rating[n][2] for n in range(length)]
durability = [skill_rating[n][3] for n in range(length)]
power = [skill_rating[n][4] for n in range(length)]
combat = [skill_rating[n][5] for n in range(length)]
overall = [skill_rating[n][6] for n in range(length)]


subprocess.run('clear')

# List that stores all the characters stats
stat_sheet = []

def character_data(*data):

    for n in range(length):
        # List that hold the individual stat for each character
        sheet = []
        
        for info in data:
            stat =  info[n]
            sheet.append(stat)
        
        stat_sheet.append(tuple(sheet))

character_data(alias, name, gender, race, side, publisher, intelligence, strength, speed, durability, power, combat, overall)


print(f'\n')
print(stat_sheet[0])
print(f'\n')



# print(  )
# print(skill_rating)