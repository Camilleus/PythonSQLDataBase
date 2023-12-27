from models import Session, Student, Group, Professor, Subject, Grade
from sqlalchemy import func


def select_1(session):
    # 5 studentów z najwyższą średnią ocen ze wszystkich przedmiotów.
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
    # Student z najwyższą średnią ocen z określonego przedmiotu.
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
    # Średni wynik w grupach dla określonego przedmiotu.
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

def select_4(session):
    # Średni wynik w grupie (w całej tabeli ocen).
    result = (
        session.query(func.avg(Grade.value).label('average'))
        .scalar()
    )
    return result

def select_5(session, professor_name):
    # Przedmioty, których uczy określony wykładowca.
    result = (
        session.query(Subject.name)
        .join(Grade, Subject.id == Grade.subject_id)
        .join(Professor, Grade.professor_id == Professor.id)
        .filter(Professor.name == professor_name)
        .distinct()
        .all()
    )
    return result

def select_6(session, group_name):
    # Lista studentów w określonej grupie.
    result = (
        session.query(Student.name)
        .join(Group, Student.group_id == Group.id)
        .filter(Group.name == group_name)
        .all()
    )
    return result

def select_7(session, group_name, subject_name):
    # Oceny studentów w określonej grupie z danego przedmiotu.
    result = (
        session.query(Student.name, Grade.value)
        .join(Group, Student.group_id == Group.id)
        .join(Grade, Student.id == Grade.student_id)
        .join(Subject, Grade.subject_id == Subject.id)
        .filter(Group.name == group_name, Subject.name == subject_name)
        .all()
    )
    return result

def select_8(session, professor_name):
    # Średnia ocena wystawiona przez określonego wykładowcę z jego przedmiotów.
    result = (
        session.query(func.avg(Grade.value).label('average'))
        .join(Professor, Grade.professor_id == Professor.id)
        .filter(Professor.name == professor_name)
        .scalar()
    )
    return result

def select_9(session, student_name):
    # Lista przedmiotów zaliczonych przez danego studenta.
    result = (
        session.query(Subject.name)
        .join(Grade, Subject.id == Grade.subject_id)
        .join(Student, Grade.student_id == Student.id)
        .filter(Student.name == student_name, Grade.value >= 3)
        .distinct()
        .all()
    )
    return result

def select_10(session, professor_name, student_name):
    # Lista kursów prowadzonych przez określonego wykładowcę dla określonego studenta.
    result = (
        session.query(Subject.name)
        .join(Grade, Subject.id == Grade.subject_id)
        .join(Professor, Grade.professor_id == Professor.id)
        .join(Student, Grade.student_id == Student.id)
        .filter(Professor.name == professor_name, Student.name == student_name)
        .distinct()
        .all()
    )
    return result

def select_11(session, professor_name, student_name):
    # Średnia ocena, jaką określony wykładowca wystawił pewnemu studentowi.
    result = (
        session.query(func.avg(Grade.value).label('average'))
        .join(Student, Grade.student_id == Student.id)
        .join(Subject, Grade.subject_id == Subject.id)
        .join(Professor, Grade.professor_id == Professor.id)
        .filter(Professor.name == professor_name, Student.name == student_name)
        .group_by(Professor.id, Student.id)
        .first()
    )
    return result


my_select = input("What data do you want to receive?")

if __name__ == '__main__':
    result = my_select()
    print(result)