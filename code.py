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

with open('file.sql','a') as file:
    file.write('''
create database uwi2;
USE uwi2;\n\n''')





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

# Create the Teaches table
TeachesTable = '''CREATE TABLE IF NOT EXISTS Teaches (
                LecId INTEGER,
                CourseID VARCHAR(10),
                PRIMARY KEY (LecId, CourseID),
                FOREIGN KEY (LecId) REFERENCES Lecturer(LecId),
                FOREIGN KEY (CourseID) REFERENCES Course(CourseID)
                );'''

# Create the Course table
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
				 FOREIGN KEY (CourseID) REFERENCES Course(CourseID)
				 );'''



if Create_Tables == True:
    with open('file.sql', 'a') as file:
        file.write(LectureTable + '\n\n')
        file.write(StudentTable + '\n\n')
        file.write(TeachesTable + '\n\n')
        file.write(CourseTable + '\n\n')
        file.write(EnrolTable + '\n\n')

        # Eecuting sql
        c.execute(LectureTable[:-1])
        c.execute(StudentTable[:-1])
        c.execute(TeachesTable[:-1])
        c.execute(CourseTable[:-1])
        c.execute(EnrolTable[:-1])




course_codes = [f'{fake.pystr(min_chars=4, max_chars=4).upper()}{str(random.randint(2000, 4000))}' for _ in range(50)]
course_dict = {}
for i, course_code in enumerate(course_codes, start=1):
    course_dict[str(i)] = [course_code, f'Course {i}']





# Define the list of values
lecID_dept_ = {'500000001': 'Humanities', '500000002': 'Linguistics', '500000003': 'Engineering', 
 '500000004': 'Science and Technology', '500000005': 'Geography', '500000006': 'Medical', 
 '500000007': 'Humanities', '500000008': 'Linguistics', '500000009': 'Engineering', 
 '500000010': 'Science and Technology'}

lecID_name_ = {'500000001': ['Lance', 'Mcdonald'], '500000002': ['Jesse', 'Ruiz'], '500000003': ['Claire', 'Moon'], 
               '500000004': ['Brian', 'Brady'], '500000005': ['George', 'Yoder'], '500000006': ['Maureen', 'Fernandez'], 
               '500000007': ['Larry', 'Chan'], '500000008': ['Cheyenne', 'Acevedo'], '500000009': ['Luis', 'Adams'], 
               '500000010': ['Nicole', 'Daniels']}

Student_name = dict()
# # Generate fake names for 10 students
for i in range(620130499, 620130499 + 300):
    Student_name[str(i)] = [fake.first_name(), fake.last_name()]

 

# Student Table funtions
def stu_fName(i):
    i = str(i)
    return Student_name[i][0]
def stu_lName(i):
    i = str(i)
    return Student_name[i][1]

# Funtions Funtion
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




# Populate the Lecturer table with random data
# for i in range(500000001, 500000011):
#     c.execute("INSERT INTO Lecturer (LecId, LecfName, LeclName, Department) VALUES (?, ?, ?, ?)", (i, lec_fName(i), lec_lName(i), lec_dept(i)))

if Insert_Lecturer == True: 
    # Open the file in append mode
    with open('file.sql', 'a') as file:
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
    with open('file.sql', 'a') as file:
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
    with open('file.sql', 'a') as file:
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
    with open('file.sql', 'a') as file:
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
    with open('file.sql', 'a') as file:
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



    
# c.execute("SELECT * FROM Enroll")
c.execute("SELECT * FROM Teaches")
rows = c.fetchall()
for row in rows:
    print(row)

# Commit the changes and close the connection
conn.commit()
conn.close()





