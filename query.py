
import sqlite3
# Connect to the SQLite database
conn = sqlite3.connect('uwi2.db')
c = conn.cursor()






c.execute(''' 
SELECT LecfName, LeclName
FROM Lecturer
WHERE LecId = (
SELECT LecId
FROM Teaches
GROUP BY LecId
ORDER BY COUNT(*) DESC
LIMIT 1
);''')

c.execute(''' 
SELECT LecfName, LeclName
FROM Lecturer
WHERE LecId = (
SELECT LecId
FROM Teaches
GROUP BY LecId
ORDER BY COUNT(*) ASC
LIMIT 1
);''')


rows = c.fetchall()
for row in rows:
    print(row)