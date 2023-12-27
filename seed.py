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