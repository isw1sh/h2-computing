import sqlite3
from datetime import date 

#Task 4.2 second part 
class Person:
    def __init__(self, full_name , date_of_birth):
        self.full_name = full_name
        self.date_of_birth = date_of_birth 

    def is_adult(self):
        birth_year = int(self.date_of_birth[:4])
        year = date.today().year
        return (year - birth_year) >= 18
    
    def screen_name(self):
        name = ''
        for char in self.full_name:
            if char.isalpha():
                name = name + char
        month = self.date_of_birth[5:7]
        day = self.date_of_birth[8:10]
        return name + month + day 
    
class Staff(Person):
    
    def screen_name(self):
        name = super().screen_name() + "Staff"
        return name 
    
    def is_adult(self):
        return True
    
class Student(Person):
    def is_adult(self):
        return False

    


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
            person = Staff(full_name , date_of_birth)

        elif person_type == "Student":
            person = Student(full_name, date_of_birth)

        else:
            person = Person(full_name, date_of_birth)

        people.append(person)


conn = sqlite3.connect('school.db')
cursor = conn.cursor()

for p in people:
    cursor.execute(
                   'INSERT INTO People (FullName , DateOfBirth , ScreenName , IsAdult) VALUES (?,?,?,?) ' ,
                   (p.full_name , p.date_of_birth , p.screen_name() , int(p.is_adult()))
                   
    )
    
conn.commit()
conn.close()


