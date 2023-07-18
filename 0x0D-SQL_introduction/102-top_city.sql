-- Import in hbtn_0c_0 database
-- displays the top 3 of cities
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month=7 OR month=8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;