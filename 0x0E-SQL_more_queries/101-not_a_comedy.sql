-- lists all shows without the genre Comedy in the database hbtn_0d_tvshows

SELECT DISTINCT title
FROM tv_shows AS tvs
LEFT JOIN tv_show_genres AS tvsg
ON show_id LIKE tvs.id
LEFT JOIN tv_genres AS tvg
ON tvg.id LIKE genre_id
WHERE title NOT IN (
        SELECT title
        FROM tv_shows AS tvs
        INNER JOIN tv_show_genres AS tvsg
        ON show_id LIKE tvs.id
        INNER JOIN tv_genres AS tvg
        ON tvg.id LIKE genre_id
        WHERE name LIKE "COMEDY"
)
ORDER BY title;
