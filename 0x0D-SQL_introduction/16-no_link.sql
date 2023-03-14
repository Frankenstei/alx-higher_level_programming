-- shows all records with name
SELECT score, name FROM second_table WHERE name IS NOT null GROUP BY score DESC;
