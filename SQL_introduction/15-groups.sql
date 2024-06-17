-- List the number of records with the same score in the table second_table
-- This query retrieves the score and the count of records for each score, labeled as number, sorted by number in descending order
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
