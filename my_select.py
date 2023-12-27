from models import Session, Student, Group, Professor, Subject, Grade
from sqlalchemy import func


def select_1(session):
    # Znajdź 5 studentów z najwyższą średnią ocen ze wszystkich przedmiotów.
    result = (
        session.query(Student.name, func.avg(Grade.value).label('average'))
        .join(Grade, Student.id == Grade.student_id)
        .group_by(Student.id)
        .order_by(func.avg(Grade.value).desc())
        .limit(5)
        .all()
    )
    return result

def select_2(session, subject_name):
    # Znajdź studenta z najwyższą średnią ocen z określonego przedmiotu.
    result = (
        session.query(Student.name, func.avg(Grade.value).label('average'))
        .join(Grade, Student.id == Grade.student_id)
        .join(Subject, Grade.subject_id == Subject.id)
        .filter(Subject.name == subject_name)
        .group_by(Student.id)
        .order_by(func.avg(Grade.value).desc())
        .first()
    )
    return result

def select_3(session, subject_name):
    # Znajdź średni wynik w grupach dla określonego przedmiotu.
    result = (
        session.query(Group.name, func.avg(Grade.value).label('average'))
        .join(Student, Group.id == Student.group_id)
        .join(Grade, Student.id == Grade.student_id)
        .join(Subject, Grade.subject_id == Subject.id)
        .filter(Subject.name == subject_name)
        .group_by(Group.id)
        .all()
    )
    return result

my_select = input("What data do you want to receive?")

if __name__ == '__main__':
    result = my_select()
    print(result)