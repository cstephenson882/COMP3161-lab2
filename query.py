import sqlite3
# Connect to the SQLite database
conn = sqlite3.connect('uwi2.db')
c = conn.cursor()

# Question 1a to 1f

q1a = ''' 
SELECT LecfName, LeclName
FROM Lecturer
WHERE LecId = (
SELECT LecId
FROM Teaches
GROUP BY LecId
ORDER BY COUNT(*) DESC
LIMIT 1);
'''

q1b = ''' 
SELECT LecfName, LeclName
FROM Lecturer
WHERE LecId = (
SELECT LecId
FROM Teaches
GROUP BY LecId
ORDER BY COUNT(*) ASC
LIMIT 1);
'''

q1c = '''
SELECT Table1.CourseID, Course.CourseName, EnrollCount
FROM
    (SELECT Enroll.CourseID as CourseID, COUNT(*) as EnrollCount 
     FROM Enroll
     GROUP BY CourseID) AS 'Table1'
JOIN Course ON Table1.CourseID = Course.CourseID;

'''

q1d = '''
SELECT Table1.CourseID, Course.CourseName, CourseAverage
FROM
    (SELECT Enroll.CourseID, ROUND(AVG(Grade), 1) as CourseAverage
    FROM Enroll
    GROUP BY Enroll.CourseID) as 'Table1'
JOIN Course on Course.CourseID = Table1.CourseID;
'''


q1e = '''
SELECT  Table1.StudentID, Student.FirstName, Student.LastName, Average 
FROM
    (SELECT Enroll.StudentID as StudentID , ROUND(AVG(Enroll.Grade) ,1) AS Average 
     FROM Enroll
     GROUP BY Enroll.StudentID ) AS 'Table1'
JOIN Student ON Table1.StudentID = Student.StudentID
ORDER BY Average DESC
LIMIT 1;
 '''

q1f = '''
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

 '''
def runQuery(str_):
    c.execute(str_)
    rows = c.fetchall()
    for row in rows:
        print(row)


# with open('schemaXqueries.sql', 'a') as file:
#     file.write(q1a + '\n\n')
#     file.write(q1b + '\n\n')
#     file.write(q1c + '\n\n')
#     file.write(q1d + '\n\n')
#     file.write(q1e + '\n\n')
#     file.write(q1f + '\n\n')

# runQuery(q1a)
# runQuery(q1b)
# runQuery(q1c)
# runQuery(q1d)
# runQuery(q1e)
runQuery(q1f)


# Commit the changes and close the connection
conn.commit()
conn.close()
