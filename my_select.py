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


if __name__ == '__main__':
    result = my_select()
    print(result)