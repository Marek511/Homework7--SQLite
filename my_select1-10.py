from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from models import Student, Group, Lecturer, Subject, Grade

engine = create_engine('sqlite:///my_database.db')
Session = sessionmaker(bind=engine)


def select_1():
    with Session() as session:
        score = session.query(Student, func.avg(Grade.grade).label('avg_score')) \
            .join(Grade).group_by(Student.id).order_by(func.avg(Grade.grade).desc()).limit(5).all()
    return score


def select_2(subject_name):
    with Session() as session:
        score = session.query(Student, func.avg(Grade.grade).label('avg_score')) \
            .join(Grade).join(Subject).filter(Subject.name.is_(subject_name)) \
            .group_by(Student.id).order_by(func.avg(Grade.grade).desc()).first()
    return score


def select_3(subject_name):
    with Session() as session:
        score = session.query(Group, func.avg(Grade.grade).label('avg_score')) \
            .join(Student).join(Grade).join(Subject).filter(Subject.name.is_(subject_name)) \
            .group_by(Group.id).all()
    return score


def select_4():
    with Session() as session:
        score = session.query(func.avg(Grade.grade).label('avg_score')).first()
    return score


def select_5(teacher_name):
    with Session() as session:
        score = session.query(Subject).join(Lecturer).filter(Lecturer.name.is_(teacher_name)).all()
    return score


def select_6(group_name):
    with Session() as session:
        score = session.query(Student).join(Group).filter(Group.name.is_(group_name)).all()
    return score


def select_7(group_name, subject_name):
    with Session() as session:
        score = session.query(Student, Grade) \
            .join(Group).join(Grade).join(Subject) \
            .filter(Group.name.is_(group_name), Subject.name.is_(subject_name)).all()
    return score


def select_8(teacher_name):
    with Session() as session:
        score = session.query(func.avg(Grade.grade).label('avg_score')) \
            .join(Subject).join(Lecturer).filter(Lecturer.name.is_(teacher_name)).first()
    return score


def select_9(student_id):
    with Session() as session:
        score = session.query(Subject).join(Grade).filter(Grade.student_id.is_(student_id), Grade.grade >= 3.0).all()
    return score


def select_10(teacher_name, student_id):
    with Session() as session:
        score = session.query(Subject).join(Lecturer).join(Grade) \
            .filter(Lecturer.name.is_(teacher_name), Grade.student_id.is_(student_id).all())
    return score


result = select_1()

for student, avg_score in result:
    print(f"Student ID: {student.id}, Name: {student.name}, Average Score: {avg_score}")
