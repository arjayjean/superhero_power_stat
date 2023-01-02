use superhero_power_stat;

CREATE TABLE characters (
    id 				int NOT NULL auto_increment,
    alias			varchar(50),
    name 			varchar(50),
    gender			varchar(6),
    race 			varchar(20),
    side			varchar(8), -- alignment = side
    universe		varchar(20),
    intelligence	tinyint(3),
    strength		tinyint(3),
    speed			tinyint(3),
    durability		tinyint(3),
    power			tinyint(3),
    combat			tinyint(3),
    overall			float,
    primary key(id)
);
    
-- CLEANING: Created a function to change the character's overall rating. Loaded the wrong overall rating.
DELIMITER //
create function overall(intelligence	tinyint(3),
						strength		tinyint(3),
						speed			tinyint(3),
						durability		tinyint(3),
						power			tinyint(3),
						combat			tinyint(3))
	returns  float
	DETERMINISTIC
BEGIN
    
	declare stats float;
	declare overall float;
    declare new_overall float;
    
    set stats = intelligence + strength + speed + durability + power + combat;
	set overall = stats/600;
    set new_overall = overall * 100;
    
	return  round(new_overall, 2);
    
END; //
DELIMITER ;

-- Testing the function to see if the overall function produced the correct overall rating
select alias, overall(intelligence, strength, speed, durability, power, combat) as overall
from characters;

-- CLEANING: Updated the overall rating to have the correct rating for each character
update characters
set overall = overall(intelligence, strength, speed, durability, power, combat);



Select alias, name, gender, race, side, universe 
from characters
where race is null 
	AND universe <> 'Marvel Comics'
    AND gender = 'Male'
    AND side = 'Villain';
    
Select distinct race
from characters
-- where race like 'Cy%'
order by race;


update characters
set race = 'Imskian'
where alias in ('Atom Girl'
                );
            
select * 
from characters
where alias like'Flash';