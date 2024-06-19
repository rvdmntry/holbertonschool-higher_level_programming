-- List all cities of California
-- This script lists all the cities of California from the database hbtn_0d_usa.
-- The results are sorted in ascending order by cities.id.

-- Select cities of California using a subquery to find the state_id
SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY id ASC;
