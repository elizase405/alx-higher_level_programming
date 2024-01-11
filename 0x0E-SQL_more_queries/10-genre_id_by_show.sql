-- script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked

SELECT tvs.title, tvsg.genre_id
FROM tv_shows AS tvs
INNER JOIN tv_show_genres AS tvsg
WHERE tvs.id LIKE tvsg.show_id
ORDER BY tvs.title, tvsg.genre_id;
