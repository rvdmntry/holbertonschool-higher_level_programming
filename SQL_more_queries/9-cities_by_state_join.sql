-- List all cities with their corresponding state names
-- This script lists all cities in the database hbtn_0d_usa with their corresponding state names.
-- The results are sorted in ascending order by cities.id.

-- Select cities.id, cities.name, and states.name using a join
SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
