# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays 
                (songplay_id serial PRIMARY KEY, 
                start_time bigint NOT NULL,
                user_id int NOT NULL, 
                level varchar, 
                song_id varchar,
                artist_id varchar, 
                session_id int, 
                location varchar, 
                user_agent varchar,
                FOREIGN KEY (start_time) REFERENCES time (start_time),
                FOREIGN KEY (user_id) REFERENCES users (user_id),
                FOREIGN KEY (song_id) REFERENCES songs (song_id),
                FOREIGN KEY (artist_id) REFERENCES artists (artist_id));
""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users
                (user_id int NOT NULL PRIMARY KEY, 
                first_name varchar, 
                last_name varchar,\
                gender varchar(1), 
                level varchar);
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs
                (song_id varchar NOT NULL PRIMARY KEY, 
                title varchar NOT NULL, 
                artist_id varchar NOT NULL,
                year int NOT NULL, 
                duration numeric NOT NULL);
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists
                (artist_id varchar NOT NULL PRIMARY KEY, 
                name varchar NOT NULL, 
                location varchar,
                latitude numeric, 
                longitude numeric);
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time
                (start_time bigint NOT NULL PRIMARY KEY, 
                hour int, 
                day int,
                week int, 
                month int, 
                year int, 
                weekday int);
""")




# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays ( start_time, user_id, level,
                song_id, artist_id, session_id, location, user_agent)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""INSERT INTO users (user_id, first_name, last_name, gender, level)
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (user_id) DO UPDATE SET level=EXCLUDED.level
""")

song_table_insert = ("""INSERT INTO songs (song_id, title, artist_id, year,duration)
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (song_id) DO NOTHING
""")

artist_table_insert = ("""INSERT INTO artists (artist_id, name, location, latitude, longitude)
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (artist_id) DO NOTHING
""")


time_table_insert = ("""INSERT INTO time (start_time, hour, day, week, month, year, weekday)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (start_time) DO NOTHING
""")

# FIND SONGS
# Implement the song_select query in sql_queries.py to find the song ID and artist ID based on the title, artist name, and
# duration of a song
# get the song ID and artist ID by querying the songs and artists tables to find matches based on song title, artist name, 
# and song duration time.

song_select = ("""SELECT song_id, songs.artist_id
                FROM songs
                JOIN artists
                ON songs.artist_id = artists.artist_id
                WHERE songs.title = %s
                AND artists.name = %s
                AND songs.duration = %s;
""")

# QUERY LISTS

create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]