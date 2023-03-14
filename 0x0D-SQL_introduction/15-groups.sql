-- displays records with same score
SELECT score, count(score) as number FROM second_table GROUP BY score DESC;
