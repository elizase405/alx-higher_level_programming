-- -- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each

SELECT tvg.name, COUNT(tvs.title) AS number_of_shows
FROM tv_genres AS tvg
INNER JOIN tv_show_genres AS tvsg
ON tvg.id LIKE tvsg.genre_id
INNER JOIN tv_shows AS tvs
ON tvsg.show_id LIKE tvs.id
GROUP BY tvg.name
ORDER BY number_of_shows DESC;
