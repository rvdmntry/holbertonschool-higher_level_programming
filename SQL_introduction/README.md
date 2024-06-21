# MySQL Database Scripts

This project contains SQL scripts for managing a MySQL database. The scripts include operations such as listing databases, creating a new database, using a specific database, creating tables, and inserting and retrieving data.

## Prerequisites

- MySQL 8.0 (version 8.0.25) installed on Ubuntu 20.04 LTS

## Installation

  1. Update your package list:
    ```sh
    $sudo apt update
    ```

  2. Install MySQL server:

```sh
    $ sudo apt install mysql-server
    ```

3. Verify the installation:
    ```sh
    $ mysql --version
    ```

## Usage

1. Start the MySQL service:
    ```sh
    $ sudo service mysql start
    ```

2. Connect to the MySQL server:
    ```sh
    $ sudo mysql
    ```

3. Run SQL scripts:
    ```sh
    $ cat script_name.sql | mysql -uroot -p
    ```

## Files

- `0-list_databases.sql`: Lists all databases in the MySQL server.
- `1-create_database.sql`: Creates a new database named 'school'.
- `2-create_table.sql`: Creates a 'students' table in the 'school' database.
- `3-insert_data.sql`: Inserts sample data into the 'students' table.
- `4-retrieve_data.sql`: Retrieves the first 3 students in batch ID 3.

## Comments

All SQL scripts contain comments describing the tasks performed by each query. SQL keywords are written in uppercase for readability.

## Testing

The length of the files can be tested using the `wc` command:
    ```sh
    $ wc -l script_name.sql
    ```
