# TV Shows and Genres Database Queries

This project contains SQL scripts to interact with the `hbtn_0d_tvshows` database. The scripts are designed to perform various queries on TV shows and their associated genres.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All SQL scripts should be executed on Ubuntu 20.04 LTS using MySQL 8.0
- All files should end with a new line
- All SQL queries should have a comment just before them
- All files should start with a comment describing the task
- All SQL keywords should be in uppercase (e.g., `SELECT`, `WHERE`)
- A `README.md` file at the root of the project folder is mandatory

## Database Import

To import the database dump, run the following commands:

```sh
curl -s -o hbtn_0d_tvshows.sql "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql"
mysql -uroot -p < hbtn_0d_tvshows.sql
