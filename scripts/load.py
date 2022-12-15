from sqlalchemy import create_engine, Column, Integer, String, Table, MetaData
from sqlalchemy.orm import Session
import subprocess

subprocess.run('clear')

engine = create_engine(
    "mysql+pymysql://root:Arjay1717@localhost:3306/superhero_power_stat",    
    echo=True
    )

# Check connection
# print(f'\n')
# connection = engine.connect()
# print(f'\n')

metadata = MetaData()

characters = Table('characters', metadata, autoload=True, autoload_with=engine)

print(f'\n')
print(characters.columns.keys())
# print(repr(characters))
# Shows a list of tables
# print(engine.table_names())


