-- selecting rows with identical values
SELECT score,COUNT(*) AS "number" FROM second_table GROUP BY score ORDER BY number DESC;
