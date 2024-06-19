-- Create table id_not_null
-- This script creates the table id_not_null with id and name columns.
-- The id column has a default value of 1.
-- The table will be created in the specified database.
-- If the table id_not_null already exists, the script will not fail.

-- Create table id_not_null if it does not exist
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
