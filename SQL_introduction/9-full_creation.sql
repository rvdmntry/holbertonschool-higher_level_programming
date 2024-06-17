-- Create the table second_table if it does not exist
-- This query creates a table named second_table with columns id, name, and score
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- Insert records into the table second_table
-- This query inserts the specified records into second_table
INSERT INTO second_table (id, name, score) VALUES
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);
