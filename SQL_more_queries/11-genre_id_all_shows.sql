-- List all shows with their corresponding genre ids
-- This script lists all shows in the database hbtn_0d_tvshows with their corresponding genre ids.
-- Each record displays tv_shows.title and tv_show_genres.genre_id.
-- If a show doesn’t have a genre, display NULL.
-- The results are sorted in ascending order by tv_shows.title and tv_show_genres.genre_id.

-- Select tv_shows.title and tv_show_genres.genre_id using a LEFT JOIN
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
