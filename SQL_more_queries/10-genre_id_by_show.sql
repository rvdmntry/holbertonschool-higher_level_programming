-- List all shows with at least one genre linked
-- This script lists all shows in the database hbtn_0d_tvshows that have at least one genre linked.
-- Each record displays tv_shows.title and tv_show_genres.genre_id.
-- The results are sorted in ascending order by tv_shows.title and tv_show_genres.genre_id.

-- Select tv_shows.title and tv_show_genres.genre_id
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows, tv_show_genres
WHERE tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
