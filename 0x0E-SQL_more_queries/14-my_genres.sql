-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter

SELECT tvg.name
FROM tv_genres AS tvg
INNER JOIN tv_show_genres AS tvsg
ON tvsg.genre_id LIKE tvg.id
INNER JOIN tv_shows AS tvs
ON tvsg.show_id LIKE tvs.id
WHERE tvs.title LIKE "Dexter"
ORDER BY tvg.name;
