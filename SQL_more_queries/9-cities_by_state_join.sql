-- A script that lists all cities contained in the database
SELECT cities.id, cities.name, states.name
FROM cities, states
ORDER BY cities.id;
