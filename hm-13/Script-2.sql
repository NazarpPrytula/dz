SELECT MAX(rating) AS best_rating FROM courses c, school s 
WHERE lang = 'python' AND c.id = s.course_id


SELECT COUNT(*) AS PYTHON_STUDENT
FROM school s ,courses c
WHERE lang = 'C#' and c.id = s.course_id

SELECT COUNT(*) AS STUDENT, lang 
FROM school s ,courses c
WHERE  c.id = s.course_id 
GROUP BY lang


SELECT COUNT(*) AS STUDENT, lang 
FROM school s ,courses c
WHERE  c.id = s.course_id 
GROUP BY lang 
ORDER BY STUDENT DESC



SELECT COUNT(*) AS STUDENT, lang 
FROM school s ,courses c
WHERE  c.id = s.course_id 
GROUP BY lang 
ORDER BY STUDENT DESC ,lang

SELECT c.title  FROM  pupils p, school s, courses c
WHERE gender = 2 AND p.id = s.pupil_id AND s.course_id = c.id;

SELECT c.title  
  FROM  pupils p, school s, courses c
 WHERE gender = 2 
   AND p.id = s.pupil_id 
   AND s.course_id = c.id;

SELECT c.title
    FROM pupils p
    INNER JOIN school s ON p.id = s.pupil_id
   INNER JOIN courses c  ON s.course_id = c.id
   WHERE gender = 2
   
  
   
   DELETE FROM school
WHERE pupil_id IN (SELECT  id FROM pupils 
 WHERE name = 'Maksim')








