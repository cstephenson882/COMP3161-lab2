CREATE DATABASE IF NOT EXISTS uwi2;
USE uwi2;

CREATE TABLE IF NOT EXISTS Lecturer (
                    LecId INTEGER PRIMARY KEY,
                    LecfName VARCHAR(255),
                    LeclName VARCHAR(255),
                    Department VARCHAR(255)
                    );

CREATE TABLE IF NOT EXISTS Student (
				 StudentID INTEGER PRIMARY KEY,
				 FirstName VARCHAR(55),
				 LastName VARCHAR(55)
				 );

CREATE TABLE IF NOT EXISTS Teaches (
                LecId INTEGER,
                CourseID VARCHAR(10),
                PRIMARY KEY (LecId, CourseID),
                FOREIGN KEY (LecId) REFERENCES Lecturer(LecId),
                FOREIGN KEY (CourseID) REFERENCES Course(CourseID)
                );

CREATE TABLE IF NOT EXISTS Course (
                CourseID VARCHAR(10) PRIMARY KEY,
                CourseCode VARCHAR(55),
                CourseName VARCHAR(55)
                );

CREATE TABLE IF NOT EXISTS Enroll (
				 StudentID INTEGER,
				 CourseID VARCHAR(10),
				 Grade INT(3),
				 PRIMARY KEY (StudentID, CourseID),
				 FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
				 FOREIGN KEY (CourseID) REFERENCES Course(CourseID) ON DELETE RESTRICT
				 );

 
SELECT LecfName, LeclName
FROM Lecturer
WHERE LecId = (
SELECT LecId
FROM Teaches
GROUP BY LecId
ORDER BY COUNT(*) DESC
LIMIT 1);


 
SELECT LecfName, LeclName
FROM Lecturer
WHERE LecId = (
SELECT LecId
FROM Teaches
GROUP BY LecId
ORDER BY COUNT(*) ASC
LIMIT 1);



SELECT Table1.CourseID, Course.CourseName, EnrollCount
FROM
    (SELECT Enroll.CourseID as CourseID, COUNT(*) as EnrollCount 
     FROM Enroll
     GROUP BY CourseID) AS Table1
JOIN Course ON Table1.CourseID = Course.CourseID;




SELECT Table1.CourseID, Course.CourseName, CourseAverage
FROM
    (SELECT Enroll.CourseID, ROUND(AVG(Grade), 1) as CourseAverage
    FROM Enroll
    GROUP BY Enroll.CourseID) as Table1
JOIN Course on Course.CourseID = Table1.CourseID;



SELECT  Table1.StudentID, Student.FirstName, Student.LastName, Average 
FROM
    (SELECT Enroll.StudentID as StudentID , ROUND(AVG(Enroll.Grade) ,1) AS Average 
     FROM Enroll
     GROUP BY Enroll.StudentID ) AS Table1
JOIN Student ON Table1.StudentID = Student.StudentID
ORDER BY Average DESC
LIMIT 1;
 


SELECT * 
FROM
    (SELECT  Table1.StudentID, Student.FirstName, Student.LastName, Average 
    FROM
        (SELECT Enroll.StudentID as StudentID , ROUND(AVG(Enroll.Grade) ,1) AS Average 
        FROM Enroll
        GROUP BY Enroll.StudentID ) AS Table1
    JOIN Student ON Table1.StudentID = Student.StudentID
    ORDER BY Average DESC
    LIMIT 10) AS Table2
ORDER BY Average ASC;

 

