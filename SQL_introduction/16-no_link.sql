-- List all records of the table second_table with a name value
-- This query retrieves all rows with a non-null name value from second_table, displaying score and name, ordered by score in descending order
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
