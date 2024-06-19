-- Create table force_name
-- This script creates the table force_name with id and name columns.
-- The table will be created in the specified database.
-- If the table force_name already exists, the script will not fail.

-- Create table force_name if it does not exist
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
