-- List all shows without a genre linked
-- This script lists all shows in the database hbtn_0d_tvshows without a genre linked.
-- Each record displays tv_shows.title and tv_show_genres.genre_id (which will be NULL).
-- The results are sorted in ascending order by tv_shows.title and tv_show_genres.genre_id.

-- Select tv_shows.title and tv_show_genres.genre_id using a LEFT JOIN and filtering for NULL genres
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
