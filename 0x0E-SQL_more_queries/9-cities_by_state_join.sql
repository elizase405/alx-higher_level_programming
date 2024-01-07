-- lists all cities contained in the database hbtn_0d_usa
SELECT id, c.name, s.name AS name
FROM cities AS c
INNER JOIN states AS s
USING (id)
ORDER BY c.id;
