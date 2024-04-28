use mis_db
INSERT INTO student (s_id, password, name, dept_name, totCred) VALUES ('S10058', 'password123', 'John Doe', 'Computer Science', 120);
INSERT INTO student (s_id, password, name, dept_name, totCred) VALUES ('215100481', '1111', 'SUjan Mujawar', 'Computer Science', 120);
INSERT INTO instructor (id, password, name, dept_name, salary) VALUES ('2', '1111', 'Alice', 'HR', 50000);
INSERT INTO student (s_id, password, name, dept_name, totCred) VALUES ('21510019', '1111', 'Harshada Shinde', 'Computer Science', 120);

select * from instructor;
select * from student;