-- Create table unique_id
-- This script creates the table unique_id with id and name columns.
-- The id column has a default value of 1 and must be unique.
-- The table will be created in the specified database.
-- If the table unique_id already exists, the script will not fail.

-- Create table unique_id if it does not exist
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
