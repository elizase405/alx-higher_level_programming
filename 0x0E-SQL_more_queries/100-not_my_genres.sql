-- list all genres not linked to the show Dexter

SELECT DISTINCT tvg.name
FROM tv_genres AS tvg
INNER JOIN tv_show_genres AS tvsg
ON tvg.id LIKE tvsg.genre_id
INNER JOIN tv_shows AS tvs
ON tvs.id LIKE tvsg.show_id
WHERE tvsg.genre_id NOT IN
	( SELECT tvsg.genre_id
	FROM tv_show_genres AS tvsg
	INNER JOIN tv_shows as tvs
	ON tvsg.show_id LIKE tvs.id
	WHERE tvs.title LIKE "Dexter")
ORDER BY name;
