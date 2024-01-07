-- lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT id, name from cities
WHERE state_id LIKE (SELECT id FROM states WHERE name LIKE "California")
ORDER BY id;
