-- Create database hbtn_0d_2 and user user_0d_2 with SELECT privilege
-- This script creates the database hbtn_0d_2 and the user user_0d_2 with SELECT privileges on the hbtn_0d_2 database.
-- The password for user_0d_2 is set to user_0d_2_pwd.

-- Create database hbtn_0d_2 if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create user user_0d_2 if it does not exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege on hbtn_0d_2 to user_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Apply the changes
FLUSH PRIVILEGES;
