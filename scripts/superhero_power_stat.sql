use superhero_power_stat;

CREATE TABLE characters (
    id 				int NOT NULL auto_increment,
    alias			varchar(50),
    name 			varchar(50),
    gender			varchar(6),
    race 			varchar(20),
    side			varchar(7), -- alignment = side
    publisher		varchar(20),
    intelligence	tinyint(3),
    strength		tinyint(3),
    speed			tinyint(3),
    durability		tinyint(3),
    power			tinyint(3),
    combat			tinyint(3),
    overall			float,
    primary key(id)
);

SELECT * FROM characters;


SELECT distinct publisher FROM characters
order by publisher;


update characters
set publisher = 'Marvel Comics'
where publisher like '%Angel%'
	or publisher like 'Anti-%'
    or publisher like 'Spider%'
    or publisher like '%Deadpool%'
    or publisher like 'Power %'
    or publisher = 'Binary'
    or publisher = 'Boom-Boom'
    or publisher = 'Toxin'
    or publisher like 'Venom%'
    or publisher like 'Vindicator%'
    or publisher = 'Tempest'
    or publisher like 'Thor%'
    or publisher = 'Phoenix'
    or publisher = 'Giant-Man'
    or publisher like 'Gemini%'
    or publisher like 'Gemini%';
    


update characters
set publisher = 'DC Comics'
where publisher like 'Batman%'
	or publisher like 'Batgirl%'
    or publisher like '%Robin%'
    or publisher like 'Flash%'
    or publisher like 'Superman%'
    or publisher = 'Red Hood'
    or publisher = 'Black Racer'
    or publisher = 'Wildstorm'
    or publisher = 'Nightwing'
    or publisher = 'Oracle'
    or publisher = 'Spoiler'
    or publisher = 'Speed Demon'
    or publisher = 'Impulse';
    
    
