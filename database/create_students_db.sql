SHOW databases;
CREATE database IF NOT EXISTS students_db;
SHOW databases;

USE students_db;

-- create all neceseary tables in database
CREATE table IF NOT EXISTS students(
	student_id integer PRIMARY KEY AUTO_INCREMENT,
	name varchar(50) NOT NULL,
	surname varchar(50) NOT NULL);


/* 
AUTO_INCREMENT makes sense if there are a lot of students.
For other tables it's better to manually control indexes
names.
*/

CREATE table IF NOT EXISTS courses(
	course_id varchar(10) PRIMARY KEY NOT NULL,
	course_name varchar(150) NOT NULL,
    description text DEFAULT null);

    
CREATE table IF NOT EXISTS exercises(
	exercise_id varchar(10) PRIMARY KEY NOT NULL,
    name varchar(150) NOT NULL,
    max_points float NOT NULL,
	course_id varchar(10) NOT NULL,
    description text DEFAULT null);

   
CREATE table IF NOT EXISTS tasks(
	task_id varchar(10) PRIMARY KEY NOT NULL,
    name varchar(150) NOT NULL,
    max_points float NOT NULL,
	exercise_id varchar(10) NOT NULL,
    description text DEFAULT null);
    
    
CREATE table IF NOT EXISTS marks(
	student_id int NOT NULL,
    task_id varchar(10) NOT NULL,
    student_points float NOT NULL,
    private_comment text DEFAULT null,
    student_comment text DEFAULT null);


-- DROP table marks;
-- DROP table tasks;
-- DROP table exercises;
-- DROP table courses;
-- DROP table students;	

/*
DROP table IF EXISTS marks;
DROP table IF EXISTS tasks;
DROP table IF EXISTS exercises;
DROP table IF EXISTS courses;
DROP table IF EXISTS students;	
*/
    
-- SHOW tables;
-- DESCRIBE tasks;

-- add relations between databases
ALTER table exercises
ADD CONSTRAINT FK_exercises
FOREIGN KEY (course_id) REFERENCES courses(course_id);

-- DESCRIBE exercises;

ALTER table tasks
ADD CONSTRAINT FK_tasks
FOREIGN KEY (exercise_id) REFERENCES exercises(exercise_id);

ALTER table marks
ADD CONSTRAINT FK_marks
FOREIGN KEY (task_id) REFERENCES tasks(task_id);

SHOW tables;

-- DESCRIBE courses;
-- DESCRIBE exercises;
-- DESCRIBE tasks;
-- DESCRIBE marks;
-- select * from INFORMATION_SCHEMA.TABLE_CONSTRAINTS where CONSTRAINT_TYPE = 'FOREIGN KEY' ;