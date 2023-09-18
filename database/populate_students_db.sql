-- populate students_db with examples
USE students_db;

INSERT INTO students (name, surname)
VALUES 
	('Ala','Adamowicz'),
	('Bartosz','Barkowski'),
	('Cecylia','Ciarkowska'),
	('Danuta','Donut'),
	('Edward','Ekierka'),
	('Franek','Foryszak'),
	('Grzesiek','Gajak'),
	('Henrietta','Hartman'),
	('Ilona','Iksinska')
;


INSERT INTO courses (course_id, course_name, description)
VALUES 
	('b2km', 'Bioinformatyka 2 kurs maly', 'Kurs dla biotechu i biofizyki'),
	('b2', 'Bioinformatyka 2', 'Homologiczne i Modeller'),
	('mm', 'Modelowanie Molekularne', 'Biotechnologia'),
	('py', 'Python', null),
	('C', 'C', null);

-- SELECT *  FROM courses;
-- DELETE FROM courses;

INSERT INTO exercises (exercise_id, name, max_points, course_id)
VALUES 
	('bali', 'BaliBase', 4, 'b2km'),
	('filo', 'filogeneza', 4, 'b2km'),
	('rna', 'struktury RNA', 4, 'b2km'),
	('mikro', 'mikromacierze', 4, 'b2km'),
	('homo', 'modelowanie homologiczne', 4, 'b2km'),
	('kol', 'kolokwium', 20, 'b2km'),
	('homo_d', 'modelowanie homologiczne', 5, 'b2'),
	('itasser', 'ITASSER', 5, 'b2'),
	('py','pymol',5,'mm'),
	('gro', 'gromacs',5,'mm'),
	('prom', 'teoria',5,'mm'),
	('kol_mm','kolokwium',10,'mm')
;

SELECT * FROM exercises;

SELECT * FROM tasks;

INSERT INTO tasks (task_id, name, max_points, exercise_id, description)
VALUES 
    ('blast', 'Dopasowanie dwóch sekwencji', 1, 'bali', 'Przypomnienie'),
    ('bali','sopasowanie wielosekwencyjne', 1, 'bali', null)
;

INSERT INTO tasks (task_id, name, max_points, exercise_id, description)
VALUES 
    ('msa','Dopasowanie wielosekwencyjne', 1, 'filo', 'odniesienie do balibase'),
    ('matrix', 'Macierz odległości', 1, 'filo', null),
    ('tree', 'Drzewa filogenetyczne', 2, 'filo', null)
;


SELECT *
FROM courses;

SELECT c.course_id, c.course_name, e.exercise_id, e.name, t.task_id, t.name
FROM tasks AS t
INNER JOIN
    exercises AS e ON t.exercise_id = e.exercise_id
INNER JOIN
    courses AS c ON e.course_id = c.course_id;

INSERT INTO marks (student_id, task_id, student_points, private_comment, student_comment)
VALUES 
	(1,'blast', 1, null, null),
	(1,'bali', 1, null, null),
	(2,'blast', 1, null, null),
	(2,'bali', 0.5, null, null),
	(3,'blast', 1, null, null),
	(3,'bali', 0.3, null, null),
;

INSERT INTO marks (student_id, task_id, student_points, private_comment, student_comment)
VALUES 
	(1,'msa', 1, null, null),
	(1,'matrix', 1, null, null),
	(1,'tree', 1.5, null, null),
	(2,'msa', 1, null, null),
	(2,'matrix', 0.5, null, null),
	(2,'tree', 1, null, null),
	(3,'msa', 1, null, null),
	(3,'matrix', 0.5, null, null),
	(3,'tree', 0.3, null, null),
;