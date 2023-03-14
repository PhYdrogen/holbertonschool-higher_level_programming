-- use hbtn_0d_tvshows;
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows, tv_show_genres
ORDER BY tv_show_genres.genre_id ASC, tv_shows.title ASC;
