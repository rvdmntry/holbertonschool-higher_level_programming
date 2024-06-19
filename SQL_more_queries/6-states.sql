-- Create database hbtn_0d_usa and table states
-- This script creates the database hbtn_0d_usa and the table states with id and name columns.
-- The id column is unique, auto-generated, cannot be null, and is the primary key.
-- The name column cannot be null.
-- If the database hbtn_0d_usa already exists, the script will not fail.
-- If the table states already exists, the script will not fail.

-- Create database hbtn_0d_usa if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the created or existing database
USE hbtn_0d_usa;

-- Create table states if it does not exist
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT UNIQUE NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
