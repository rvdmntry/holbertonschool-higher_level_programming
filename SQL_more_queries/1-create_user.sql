-- Create MySQL server user user_0d_1 with all privileges
-- This script creates the user user_0d_1 with all privileges on the MySQL server and sets the password to user_0d_1_pwd.

-- Create user user_0d_1 if it does not exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to user_0d_1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Apply the changes
FLUSH PRIVILEGES;
