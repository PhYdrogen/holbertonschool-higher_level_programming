-- A script that lists all Comedy shows in the database
SELECT tv_shows.title
FROM tv_show_genres
JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id = 5