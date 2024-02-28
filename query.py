
import sqlite3
# Connect to the SQLite database
conn = sqlite3.connect('uwi2.db')
c = conn.cursor()






# c.execute(''' 
# SELECT LecfName, LeclName
# FROM Lecturer
# WHERE LecId = (
# SELECT LecId
# FROM Teaches
# GROUP BY LecId
# ORDER BY COUNT(*) DESC
# LIMIT 1;
# )''')

# c.execute(''' 
# SELECT LecfName, LeclName
# FROM Lecturer
# WHERE LecId = (
# SELECT LecId
# FROM Teaches
# GROUP BY LecId
# ORDER BY COUNT(*) ASC
# LIMIT 1;
# )''')

# c.execute('''
# SELECT Table1.CourseID, Course.CourseName, EnrollCount
# FROM
#     (SELECT Enroll.CourseID as CourseID, COUNT(*) as EnrollCount 
#      FROM Enroll
#      GROUP BY CourseID) AS 'Table1'
# JOIN Course ON Table1.CourseID = Course.CourseID;

# ''')

c.execute('''
SELECT Table1.CourseID, Course.CourseName, Average
FROM
    (SELECT Enroll.CourseID, CAST(AVG(Grade) AS INT) as Average
    FROM Enroll
    GROUP BY Enroll.CourseID) as 'Table1'
JOIN Course on Course.CourseID = Table1.CourseID


'''
)


rows = c.fetchall()
for row in rows:
    print(row)

# Commit the changes and close the connection
conn.commit()
conn.close()
