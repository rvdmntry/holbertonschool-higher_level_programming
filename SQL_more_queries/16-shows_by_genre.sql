-- List all shows and all genres linked to that show
-- This script lists all shows and all genres linked to each show from the database hbtn_0d_tvshows.
-- If a show doesn’t have a genre, display NULL in the genre column.
-- Each record displays tv_shows.title and tv_genres.name.
-- The results are sorted in ascending order by the show title and genre name.

-- Select titles and genres of all shows
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
