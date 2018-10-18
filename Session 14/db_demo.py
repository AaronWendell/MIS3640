import dbm
import random

ROSTER = ('Aaron Wendell',
          'Alden Pexton',
          'Allison Fernandez',
          'Angela Tsung',
          'Christian Thompson',
          'Christine Lee',
          'Connie Li',
          'Defne Ikiz',
          'Dong Hyun Kim',
          'Ha Min Ko',
          'Ho Wang Alastair Ng',
          'Jingyu He',
          'Jonathan Beltran',
          'Jonghyun Park',
          'Kyle Lawson',
          'Matthew Michalke',
          'Pranjal Joshi',
          'Qinyi Li',
          'Sarah Zazyczny',
          'Shiyue (Shirley) Zong',
          'Shriya Rathi',
          'Siddhanth Goyal',
          'Waylon Ryan',
          'Zirui Jiao')

GRADES = ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-']

db = dbm.open('db_student', 'c')

for student in ROSTER:
    db[student] = random.choice(GRADES)

for key in db:
    print(key, db[key])


db.close()
