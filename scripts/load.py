from sqlalchemy import create_engine, Column, Integer, String, Table, MetaData
from sqlalchemy.orm import Session
import subprocess
import transform

subprocess.run('clear')

database = "mysql+pymysql://root:Arjay1717@localhost:3306/superhero_power_stat"
engine = create_engine(database, echo=True)
connection = engine.connect()

# Check connection
# print(f'\n')
# print(f'\n')

metadata = MetaData()

characters = Table('characters', metadata, autoload=True, autoload_with=engine)

length = transform.length
stat_sheet = transform.stat_sheet



def insert_into(data):
    # data = ()
    for n in range(length):
        
        query = f"""
        INSERT INTO characters (alias, name, gender, race, side, publisher, intelligence, strength, speed, durability, power, combat, overall)
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        
        connection.execute(query, data[n])

insert_into(stat_sheet)

# {alias[n]}, {name[n]}, {gender[n]}, {race[n]}, {side[n]}, {publisher[n]}, {intelligence[n]}, {strength[n]}, {speed[n]}, {durability[n]}, {power[n]}, {combat[n]}, {overall[n]}
# data = (alias[n], name[n], gender[n], race[n], side[n], publisher[n], intelligence[n], strength[n], speed[n], durability[n], power[n], combat[n], overall[n])
print(f'\n')
# print(stat_sheet[0])
print(f'\n')
# print(characters.columns.keys())
# print(repr(characters))
# Shows a list of tables
# print(engine.table_names())


