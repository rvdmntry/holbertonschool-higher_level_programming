-- Create database hbtn_0d_usa and table cities
-- This script creates the database hbtn_0d_usa and the table cities with id, state_id, and name columns.
-- The id column is unique, auto-generated, cannot be null, and is the primary key.
-- The state_id column cannot be null and must be a foreign key referencing the id of the states table.
-- The name column cannot be null.
-- If the database hbtn_0d_usa already exists, the script will not fail.
-- If the table cities already exists, the script will not fail.

-- Create database hbtn_0d_usa if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the created or existing database
USE hbtn_0d_usa;

-- Create table states if it does not exist (required for foreign key constraint)
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT UNIQUE NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);

-- Create table cities if it does not exist
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT UNIQUE NOT NULL,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id)
);
