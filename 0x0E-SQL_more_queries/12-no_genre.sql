-- lists all shows contained in hbtn_0d_tvshows without a genre linked.

SELECT tvs.title, tvsg.genre_id
FROM tv_shows AS tvs
LEFT JOIN tv_show_genres AS tvsg
ON tvs.id LIKE tvsg.show_id
WHERE tvsg.genre_id IS NULL
ORDER BY tvs.title, tvsg.genre_id;
