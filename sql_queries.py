"""
File: sql_queries.py is a form of py sql script.
Objective: This file contain queries to create/drop tables, handle data insertion, and create aggregation data.

    Arguments: 
     - CREATE TABLE IF NOT EXIST will evaluate the table to see if it is existed or not. If not create one with specific name.
     - NOT NULL: will evalutate the data to see if it is NULL. If it is not NULL, inlcuded the data.
     - SERIAL: is a data type that will auto-increment everytime the row is added.
     - varchar or variable character: is a data type that can hold number, letters, and special character. 
       Using varchar to widen the range of data restriction.
     - INSERT INTO: use to insert data into specific column and table.
     - ON CONFLICT: will handle data that are duplicate or conflict with some action. In this case, DO NOTHING.
"""

# DROP TABLES

songplay_table_drop = "drop table if exists songplays"
user_table_drop = "drop table if exists users"
song_table_drop = "drop table if exists songs"
artist_table_drop = "drop table if exists artists"
time_table_drop = "drop table if exists time"

# CREATE TABLES
songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays
    (songplay_id SERIAL PRIMARY KEY, 
    start_time bigint NOT NULL, 
    user_id int NOT NULL, 
    level varchar, 
    song_id varchar , 
    artist_id varchar , 
    session_id int, 
    location varchar, 
    user_agent varchar)
    
""")
    
user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users
    (user_id int PRIMARY KEY, 
    first_name varchar NOT NULL, 
    last_name varchar NOT NULL, 
    gender varchar, 
    level varchar
    )
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs
    (song_id varchar PRIMARY KEY, 
    title varchar NOT NULL, 
    artist_id varchar NOT NULL,
    year int, 
    duration float NOT NULL )
    """)


artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists
    (artist_id varchar PRIMARY KEY,
     name varchar NOT NULL, 
     location varchar, 
     lattitude float, 
     longitude float)
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time
    (start_time date PRIMARY KEY,
     hour int, 
     day int, 
     week int, 
     month int, 
     year int, 
     weekday varchar)
""")

# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO songplays
    (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (songplay_id) DO NOTHING;
""")

user_table_insert = ("""
    INSERT INTO users
    (user_id, first_name, last_name, gender, level)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (user_id) DO UPDATE SET level=EXCLUDED.level;
""")

song_table_insert = ("""
    INSERT INTO songs(song_id, title, artist_id, year, duration) 
    VALUES(DEFAULT, %s, %s, %s, %s, %s) 
    ON CONFLICT(song_id) DO NOTHING;
""")

artist_table_insert = ("""
    INSERT INTO artists
    (artist_id, name, location, lattitude, longitude)
    VALUES (DEFAULT, %s, %s, %s, %s, %s)
    ON CONFLICT (artist_id) DO NOTHING;
""")


time_table_insert = ("""
    INSERT INTO time
    (start_time, hour, day, week, month, year, weekday)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (start_time) DO NOTHING;
""")

# FIND SONGS

song_select = ("""
    SELECT song_id, artists.artist_id
    FROM songs JOIN artists ON songs.artist_id = artists.artist_id
    WHERE songs.title = %s
    AND artists.name = %s
    AND songs.duration = %s
""")

# QUERY LISTS

create_table_queries = [user_table_create, artist_table_create, song_table_create, time_table_create, songplay_table_create]
drop_table_queries = [user_table_drop, artist_table_drop, song_table_drop, time_table_drop, songplay_table_drop]