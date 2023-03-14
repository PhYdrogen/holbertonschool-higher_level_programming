-- A script that lists all cities contained in the database
SELECT cities.id, cities.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id;
