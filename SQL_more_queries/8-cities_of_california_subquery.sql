-- A script that lists all the cities of California that can be found in the database
SELECT cities.id, cities.name
	FROM states, cities
	WHERE states.id = state_id
	ORDER BY cities.id;
