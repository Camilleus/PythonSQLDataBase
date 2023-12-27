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
        group = Group(name=fake.worf())
        groups.append(group)
        session.add(group)
    session.commit()
    
def create_subjects(session, num_subjects):
    subjects = []
    for _ in range(num_subjects):   
        subject = Subject(name=fake.worf())
        subjects.append(subject)
        session.add(subject)
    session.commit()
    
def create_teachers(session, num_teachers):
    teachers = []
    for _ in range(num_teachers):
        teacher = Teacher(name=fake.name())
        teachers.append(teacher)
        session.add(teacher)
    session.commit()