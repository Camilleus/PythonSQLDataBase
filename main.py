from faker import Faker
import random
import sqlite3

fake = Faker()

conn = sqlite3.connect('university.db')
cursor = conn.cursor()



cursor.execute('''
    CREATE TABLE students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        group_id INTEGER
    )
''')

cursor.execute('''
    CREATE TABLE groups (
        id INTEGER PRIMARY KEY,
        name TEXT
    )
''')

cursor.execute('''
    CREATE TABLE professors (
        id INTEGER PRIMARY KEY,
        name TEXT
    )
''')

cursor.execute('''
    CREATE TABLE subjects (
        id INTEGER PRIMARY KEY,
        name TEXT,
        professor_id INTEGER
    )
''')

cursor.execute('''
    CREATE TABLE grades (
        id INTEGER PRIMARY KEY,
        student_id INTEGER,
        subject_id INTEGER,
        grade INTEGER,
        date TEXT
    )
''')