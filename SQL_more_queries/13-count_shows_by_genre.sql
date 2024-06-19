-- List all genres and the number of shows linked to each genre
-- This script lists all genres from the database hbtn_0d_tvshows and displays the number of shows linked to each.
-- Each record displays the genre and the number of shows linked to it.
-- The results are sorted in descending order by the number of shows linked.

-- Select genre and count of shows linked, grouped by genre
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
HAVING COUNT(tv_show_genres.show_id) > 0
ORDER BY number_of_shows DESC;
