import sqlite3

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS People')

cursor.execute('''
CREATE TABLE People (
    PersonID INTEGER PRIMARY KEY AUTOINCREMENT ,
    FullName TEXT , 
    DateOfBirth TEXT , 
    ScreenName TEXT , 
    IsAdult INTEGER
)
''' )

conn.commit()
conn.close()
print("DB Created")

#Task 4.2 continued (not finished)
people = []
with open('people.txt' , 'r') as file:
    for line in file:
        line = line.strip()
        if line == '':
            continue 
        full_name , date_of_birth , person_type = line.split(',')

        if person_type == "Staff":
            person = Staff()