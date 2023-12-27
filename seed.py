import random
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Session, Student, Group, Professor, Subject, Grade

fake = Faker()

def create_students(session, num_students):
    students = []
    for _ in range(num_students):
        student = Student(
            name=fake.name(),
            email=fake.email(),
            group_id=random.choice(session.query(Group.id).all())[0]
        )
        students.append(student)
        session.add(student)
    session.commit()
    
def create_groups(session, num_groups):
    groups = []
    for _ in range(num_groups):
        group = Group(name=fake.word())
        groups.append(group)
        session.add(group)
    session.commit()
    
def create_subjects(session, num_subjects):
    subjects = []
    for _ in range(num_subjects):   
        subject = Subject(name=fake.word())
        subjects.append(subject)
        session.add(subject)
    session.commit()
    
def create_Professors(session, num_Professors):
    Professors = []
    for _ in range(num_Professors):
        Professor = Professor(name=fake.name())
        Professors.append(Professor)
        session.add(Professor)
    session.commit()
    
def create_grades(session, num_grades):
    students = session.query(Student).all()
    subjects = session.query(Subject).all()
    Professors = session.query(Professor).all()

    for _ in range(num_grades):
        grade = Grade(
            value=random.randint(2, 5),
            student_id=random.choice(students).id,
            subject_id=random.choice(subjects).id,
            Professor_id=random.choice(Professors).id
        )
        session.add(grade)
    session.commit()
