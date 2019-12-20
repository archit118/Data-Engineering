# Drop Tables

songplay_drop = "DROP table songplays"
user_drop = "DROP table users"
song_drop = "DROP table songs"
artist_drop = "DROP table artists"
time_drop = "DROP table time"


# Create Tables

songplay_create = "CREATE TABLE IF NOT EXISTS songplays (songplay_id text, start_time timestamp, user_id text, level text, song_id text, artist_id text, session_id int, location text, user_agent text)"
user_create = "CREATE TABLE IF NOT EXISTS users (user_id int, first_name text, last_name text, gender text, level text)"
song_create = "CREATE TABLE IF NOT EXISTS songs (song_id text, title text, artist_id text, year int, duration float)"
artist_create = "CREATE TABLE IF NOT EXISTS artists (artist_id text, name text, location text, lattitude text, longitude text)"
time_create = "CREATE TABLE IF NOT EXISTS time (start_time timestamp, hour int, day int, week int, month int, year int, weekday text)"

# Insert Records

songplay_insert = "INSERT INTO songplays (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
user_insert = "INSERT INTO users (user_id, first_name, last_name, gender, level) VALUES (%s, %s, %s, %s, %s)"
song_insert = "INSERT INTO songs (song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s)"
artist_insert = "INSERT INTO artists (artist_id, name, location, lattitude, longitude) VALUES (%s, %s, %s, %s, %s)"
time_insert = "INSERT INTO time (start_time, hour, day, week, month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s)"


# FIND SONGS

song_select = "SELECT songs.song_id, artists.artist_id FROM songs JOIN artists ON songs.artist_id = artists.artist_id WHERE songs.title = %s AND artists.name=%s AND songs.duration=%s" 


# QUERY LISTS

create_queries = [songplay_create, user_create, song_create, artist_create, time_create]
drop_queries = [songplay_drop, user_drop, song_drop, artist_drop, time_drop]