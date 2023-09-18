-- to remonve duplicate courses - modify for other tables

-- are there any duplicates?
SELECT course_name, COUNT(course_name) AS CNT
FROM courses
GROUP BY course_name
HAVING CNT>1;


-- this deletoin method won't work in MySQL
/*
DELETE FROM courses
WHERE course_id NOT IN
	(
    SELECT MIN(course_id)
    FROM courses
    GROUP BY course_name
    )
;
*/

-- remember to turn on safe updates adter removing duplicates

SET SQL_SAFE_UPDATES = 0;

-- short version of inner join delete
/*
DELETE crs1
FROM 
	courses crs1,
    courses crs2
WHERE 
	(
    crs1.course_id > crs2.course_id AND
    crs1.course_name = crs2.course_name
    )
;
*/

-- longer version of inner join delete
DELETE crs1
FROM 
	courses AS crs1
INNER JOIN
    courses AS crs2
WHERE 
	(
    crs1.course_id > crs2.course_id AND
    crs1.course_name = crs2.course_name
    )
;

SET SQL_SAFE_UPDATES = 1;