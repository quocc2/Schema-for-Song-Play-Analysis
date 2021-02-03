import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *

def process_song_file(cur, filepath):
    """
    This function responsible for reading song data, 
    insert data such as song_id, title, year, and play duration.
    
    Arguments:
        df.values.tolist() that convert Pandas data frame to Python list: song data and artist data convert to python lists.
        df = pd.read_json(filepath, lines=True) to read data if True.
    """
    # open and read song file
    df = pd.read_json(filepath , lines = True)

    # Insert song's record
    song_data = df[['song_id', 'title', 'artist_id', 'year', 'duration']].values[0].tolist()
    cur.execute(song_table_insert, song_data)
    
    # Insert artist's record
    artist_data = df[['artist_id', 'artist_name', 'artist_location', 'artist_latitude', 'artist_longitude']].values[0].tolist()
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    """
    This function read and convert data in log file, 
    and performing filter by next song action,
    then convert timestamp to datetime. Insert data record and time data.
    """
    # open and read log file
    df = pd.read_json(filepath, lines=True)

    # Create filter by NextSong action
    df = df[df.page == 'NextSong']

    # Convert timestamp column to datetime
    t = pd.to_datetime(df['ts'] , unit='ms')

    # Insert data record and time
    time_data = (t, t.dt.hour, t.dt.day, t.dt.week , t.dt.month, t.dt.year, t.dt.weekday)
    column_labels = ('timestamp', 'hour', 'day', 'week of year', 'month', 'year', 'weekday')
    time_df = pd.DataFrame.from_dict(dict(zip(column_labels,time_data)))

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # Load user id
    user_df = df[['userId', 'firstName', 'lastName', 'gender', 'level']]

    # Insert user record
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # Insert songplay records
    for index, row in df.iterrows():
        
        # From song and artist tables get data
        results = cur.execute(song_select, (row.song, row.artist, row.length))
        songid, artistid = results if results else None, None
    
        # Insert songplay
        songplay_data = (index, row.ts, row.userId, row.level, songid, artistid, row.sessionId, row.location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    """
    This function will process insert data. Listing file  in a directory,
    and then executing  each file according to the function
    that performs the transformation to save it to the database.
    """
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()