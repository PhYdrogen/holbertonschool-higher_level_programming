-- my genre
-- SELECT *
-- FROM tv_shows
-- WHERE tv_shows.title = "Dexter"

SELECT tv_genres.name as name
FROM tv_genres
INNER JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_show_genres.show_id = 10