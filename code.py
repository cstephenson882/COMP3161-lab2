import sqlite3
import random
from faker import Faker


fake = Faker()
runAll = True
Insert_Lecturer = runAll
Insert_Student = runAll
Insert_Teaches = runAll 
Insert_Course = runAll 
Insert_Enrol = runAll 

Create_Tables = True

# Connect to the SQLite database
conn = sqlite3.connect('uwi2.db')
c = conn.cursor()
create_ = True



# Create the tables
LectureTable = '''CREATE TABLE IF NOT EXISTS Lecturer (
                    LecId INTEGER PRIMARY KEY,
                    LecfName VARCHAR(255),
                    LeclName VARCHAR(255),
                    Department VARCHAR(255)
                    );'''

StudentTable = '''CREATE TABLE IF NOT EXISTS Student (
				 StudentID INTEGER PRIMARY KEY,
				 FirstName VARCHAR(55),
				 LastName VARCHAR(55)
				 );'''

TeachesTable = '''CREATE TABLE IF NOT EXISTS Teaches (
                LecId INTEGER,
                CourseID VARCHAR(10),
                PRIMARY KEY (LecId, CourseID),
                FOREIGN KEY (LecId) REFERENCES Lecturer(LecId),
                FOREIGN KEY (CourseID) REFERENCES Course(CourseID)
                );'''

CourseTable = '''CREATE TABLE IF NOT EXISTS Course (
                CourseID VARCHAR(10) PRIMARY KEY,
                CourseCode VARCHAR(55),
                CourseName VARCHAR(55)
                );'''

EnrolTable = '''CREATE TABLE IF NOT EXISTS Enroll (
				 StudentID INTEGER,
				 CourseID VARCHAR(10),
				 Grade INT(3),
				 PRIMARY KEY (StudentID, CourseID),
				 FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
				 FOREIGN KEY (CourseID) REFERENCES Course(CourseID) ON DELETE RESTRICT
				 );'''



if Create_Tables == True:
    with open('schemaXqueries.sql', 'a') as file:
        file.write('''CREATE DATABASE IF NOT EXISTS uwi2;\n''')
        file.write('''USE uwi2;\n\n''')
        file.write(LectureTable + '\n\n')
        file.write(StudentTable + '\n\n')
        file.write(TeachesTable + '\n\n')
        file.write(CourseTable + '\n\n')
        file.write(EnrolTable + '\n\n')

        # Executing sql
        c.execute(LectureTable[:-1])
        c.execute(StudentTable[:-1])
        c.execute(TeachesTable[:-1])
        c.execute(CourseTable[:-1])
        c.execute(EnrolTable[:-1])



# Generating Fake Data

# Fake Course: A mapping from a course's ID to the Course code and name
course_codes = [f'{fake.pystr(min_chars=4, max_chars=4).upper()}{str(random.randint(2000, 4000))}' for _ in range(50)]
course_dict = {}
for i, course_code in enumerate(course_codes, start=1):
    course_dict[str(i)] = [course_code, f'Course {i}']


# Fake Dept: A mapping from the lecture IDs to a department
lecID_dept_ = {'500000001': 'Humanities', '500000002': 'Linguistics', '500000003': 'Engineering', 
 '500000004': 'Science and Technology', '500000005': 'Geography', '500000006': 'Medical', 
 '500000007': 'Humanities', '500000008': 'Linguistics', '500000009': 'Engineering', 
 '500000010': 'Science and Technology'}

# Fake LecName: A mapping from the lecture IDs to a lecture names
lecID_name_ = {'500000001': ['Lance', 'Mcdonald'], '500000002': ['Jesse', 'Ruiz'], '500000003': ['Claire', 'Moon'], 
               '500000004': ['Brian', 'Brady'], '500000005': ['George', 'Yoder'], '500000006': ['Maureen', 'Fernandez'], 
               '500000007': ['Larry', 'Chan'], '500000008': ['Cheyenne', 'Acevedo'], '500000009': ['Luis', 'Adams'], 
               '500000010': ['Nicole', 'Daniels']}

# Fake StudentNames: A mapping from the Student IDs to names
Student_name = dict()
for i in range(620130499, 620130499 + 300):
    Student_name[str(i)] = [fake.first_name(), fake.last_name()]

# Student Table funtions
def stu_fName(i):
    i = str(i)
    return Student_name[i][0]
def stu_lName(i):
    i = str(i)
    return Student_name[i][1]

# Lecture Table funtions
def lec_fName(i):
    i = str(i)
    return lecID_name_[i][0]
def lec_lName(i):
    i = str(i)
    return lecID_name_[i][1]
def lec_dept(i):
    i = str(i)
    return lecID_dept_[i]

# Course table funtions
def cCode(i):
    return course_dict[str(i)][0]
def cName(i):
    return course_dict[str(i)][1]



# INSERT queries
if Insert_Lecturer == True: 
    # Open the file in append mode
    with open('insert.sql', 'a') as file:
        # Populate the Lecturer table with random data
        Lecturer_insert = f"INSERT INTO Lecturer (LecId, LecfName, LeclName, Department) VALUES "
        for i in range(500000001, 500000011):
            # Create the SQL command
            sql_command = "INSERT INTO Lecturer (LecId, LecfName, LeclName, Department) VALUES (?, ?, ?, ?)"
            c.execute(sql_command, (i, lec_fName(i), lec_lName(i), lec_dept(i)))
            # Write the SQL command to the file
            Lecturer_insert += f"\n({i}, '{lec_fName(i)}', '{lec_lName(i)}', '{lec_dept(i)}'),"
        file.write(Lecturer_insert[:-1] + ';\n\n')

if Insert_Student == True:
    # Open the file in append mode
    with open('insert.sql', 'a') as file:
        # Populate the Lecturer table with random data
        Student_insert = f"INSERT INTO Student (StudentID, FirstName, LastName) VALUES "
        for i in range(620130499, 620130499 + 300):
            # Create the SQL command
            sql_command = "INSERT INTO Student (StudentID, FirstName, LastName) VALUES (?, ?, ?)"
            c.execute(sql_command, (i, stu_fName(i), stu_lName(i)))
            
            # Write the SQL command to the file
            Student_insert  += f"\n({i}, '{stu_fName(i)}', '{stu_lName(i)}'),"
        file.write(Student_insert [:-1] + ';\n\n')

if Insert_Course == True: 
    # Open the file in append mode
    with open('insert.sql', 'a') as file:
        # Populate the Lecturer table with random data
        Course_insert = f"INSERT INTO Course (CourseID, CourseCode, CourseName) VALUES "
        for i in range(1, 51):
            # Create the SQL command
            sql_command = "INSERT INTO Course (CourseID, CourseCode, CourseName) VALUES (?, ?, ?)"
            c.execute(sql_command, (i, cCode(i), cName(i)))
            # Write the SQL command to the file
            Course_insert += f"\n({i}, '{cCode(i)}', '{cName(i)}'),"
        file.write(Course_insert[:-1] + ';\n\n')



if Insert_Teaches == True:
    with open('insert.sql', 'a') as file:
        sql_command = '''INSERT INTO TEACHES (LecID, CourseID) VALUES '''
        unique_constraint = dict()
        courses = [i for i in range(1,51)]
        u=0
        while u < 8 != 0 :
            for i in range(500000001+u,500000011):
                if courses == []:
                    break
                index_ = random.randint(0, len(courses)-1)
                CourseID_ = courses[index_]
                LectID_ = i
                sql_command += f"\n( {LectID_}, {CourseID_} ),"
                unique_constraint[(LectID_,CourseID_)] = ''
                courses.pop(index_)
            u+=1 
        
        file.write(sql_command[:-1] + ';\n\n')

        c.execute(sql_command[:-1])

if Insert_Enrol == True:
    with open('insert.sql', 'a') as file:
        sql_command = '''INSERT INTO Enroll (StudentID, CourseID,Grade) VALUES'''
        unique_constraint = dict()
        enrolCount = dict()
        for i in range(620130499, 620130499+200):
            StuID_ = i
            for j in range(random.randint(3,6)):
                CourseID_ = random.randint(1, 50)
                Grade_ = random.randint(0, 99)
                if (StuID_,CourseID_) in unique_constraint:
                    j-=1
                else:
                    sql_command += f"\n({StuID_}, {CourseID_},{Grade_}),"
                    # enrolCount[StuID_]+=1
                    unique_constraint[(StuID_,CourseID_)] =''

        file.write(sql_command[:-1] + ';\n\n')
        c.execute(sql_command[:-1])


# Question Queries

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
     GROUP BY CourseID) AS Table1
JOIN Course ON Table1.CourseID = Course.CourseID;

'''

q1d = '''
SELECT Table1.CourseID, Course.CourseName, CourseAverage
FROM
    (SELECT Enroll.CourseID, ROUND(AVG(Grade), 1) as CourseAverage
    FROM Enroll
    GROUP BY Enroll.CourseID) as Table1
JOIN Course on Course.CourseID = Table1.CourseID;
'''


q1e = '''
SELECT  Table1.StudentID, Student.FirstName, Student.LastName, Average 
FROM
    (SELECT Enroll.StudentID as StudentID , ROUND(AVG(Enroll.Grade) ,1) AS Average 
     FROM Enroll
     GROUP BY Enroll.StudentID ) AS Table1
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


with open('schemaXqueries.sql', 'a') as file:
    file.write(q1a + '\n\n')
    file.write(q1b + '\n\n')
    file.write(q1c + '\n\n')
    file.write(q1d + '\n\n')
    file.write(q1e + '\n\n')
    file.write(q1f + '\n\n')

# runQuery(q1a)
# runQuery(q1b)
# runQuery(q1c)
# runQuery(q1d)
# runQuery(q1e)
# runQuery(q1f)

  

# Commiting the changes and close the connection
conn.commit()
conn.close()





