# DROP TABLES
songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays 
  ( 
     songplay_id VARCHAR PRIMARY KEY, 
     start_time  TIME NOT NULL, 
     user_id     VARCHAR, 
     level       VARCHAR NOT NULL, 
     song_id     VARCHAR, 
     artist_id   VARCHAR, 
     session_id  VARCHAR NOT NULL, 
     location    VARCHAR, 
     user_agent  VARCHAR 
  ); 
""")


user_table_create = ("""CREATE TABLE IF NOT EXISTS users 
  ( 
     user_id    VARCHAR PRIMARY KEY, 
     first_name VARCHAR , 
     last_name  VARCHAR , 
     gender     VARCHAR, 
     level      VARCHAR NOT NULL
  ); """)

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs 
  ( 
     song_id   VARCHAR PRIMARY KEY, 
     title     VARCHAR NOT NULL, 
     artist_id VARCHAR NOT NULL, 
     year      INT, 
     duration  FLOAT 
  ); """)

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists 
  ( 
     artist_id VARCHAR PRIMARY KEY, 
     name      VARCHAR NOT NULL, 
     location  VARCHAR, 
     latitude  VARCHAR, 
     longitude VARCHAR 
  ); """)

time_table_create = ("""CREATE TABLE IF NOT EXISTS time 
  ( 
     start_time TIME NOT NULL, 
     hour       INT NOT NULL, 
     day        INT NOT NULL, 
     week       INT NOT NULL, 
     month      INT NOT NULL, 
     year       INT NOT NULL, 
     weekday    VARCHAR NOT NULL 
  ); """)

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays(songplay_id, start_time, user_id, level, song_id, artist_id, session_id , location , user_agent) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s) 
ON CONFLICT (songplay_id) DO NOTHING;""")

user_table_insert = ("""INSERT INTO users(user_id, first_name, last_name, gender, level) 
VALUES(%s,%s,%s,%s,%s)  
ON CONFLICT(user_id) DO UPDATE
    SET --first_name = excluded.first_name,
        --last_name = excluded.last_name,
        --gender = excluded.gender,
        level = excluded.level;
""")

song_table_insert = ("""INSERT INTO songs(song_id, title, artist_id , year , duration ) 
VALUES(%s,%s,%s,%s,%s) 
ON CONFLICT (song_id) DO NOTHING;""")

artist_table_insert = ("""INSERT INTO artists(artist_id, name, location, latitude, longitude) 
VALUES(%s,%s,%s,%s,%s) 
ON CONFLICT (artist_id) DO NOTHING;""")

time_table_insert = ("""INSERT INTO time(start_time, hour, day, week, month , year , weekday) 
VALUES(%s,%s,%s,%s,%s,%s,%s);""")

# FIND SONGS

song_select = (""" 
SELECT DISTINCT s.song_id,
                a.artist_id
FROM artists a
JOIN songs s ON a.artist_id=s.artist_id
WHERE 1=1
  AND (a.artist_id IS NOT NULL
       OR a.artist_id<>'')
  AND (s.artist_id IS NOT NULL
       OR s.artist_id<>'')
  AND s.title=(%s)
  AND a.name=(%s)
  AND s.duration=(%s)
""")


# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]