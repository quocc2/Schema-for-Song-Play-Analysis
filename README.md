# Data Modeling with Postgres

## Overview:

This project is to build a PostgreSQL data base which utilizes the data of user's activities and songs metadata. The data base helps to analyze user's activities and song play.

## Data and File:

*Song's metadata source* [Million Song Dataset] (https://labrosa.ee.columbia.edu/millionsong/).
*Song metadata* is a collection of JSON files that describes the song data such as: tiletl, artist name, year, album...etc.
*User activities source* [eventsim] (https://github.com/Interana/eventsim).
*Log data* is a collection of JSON files that logs user's activi

## Database Structure:

Database build by optimizing tables around efficient reads that will serve complex queries.
To achieve this task, a **START** schema is used with dimensional modeling to take advantages of its usage: Denormalized tables, Simplied queries, and fast for aggregation.

-Song plays as fact table.
-Songs, artist, uers, and time are dimentions tables.

## Project Structure:

1. 'sql_queries.py' contains all queries needed to create tables, drop tables, and other queries to get song_id and artist_id from different tables that are not provided in the log dataset.
2. 'create_tables.py' contains scripts that create database, create connection to database, or drop table using sql_queries scripts.
3. 'etl.py' extract data from JSON files. Transformation of dta and insert them to the corresponding tables. For example, timestamp data.

### How project executed:

1. Run the 'create_table.py' to create table and connection.
2. Run the 'elt.py' to create database, tables, and data pipeline.
3. Run 'test.ipynb' to test 'sql_queries.py'
4. Restart the execution from step (1) to (3) each script test or script changes tests.

## Example Output:

### queries
%sql SELECT * FROM users LIMIT 5;

 * postgresql://student:***@127.0.0.1/sparkifydb
5 rows affected.
user_id	first_name	last_name	gender	level
91	Jayden	Bell	M	free
73	Jacob	Klein	M	paid
86	Aiden	Hess	M	free
24	Layla	Griffin	F	paid
26	Ryan	Smith	M	free



