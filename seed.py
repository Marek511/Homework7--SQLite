import random
from faker import Faker
from models import Student, Group, Lecturer, Subject, Grade
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import timedelta, datetime

engine = create_engine('sqlite:///my_database.db')

Session = sessionmaker(bind=engine)

with Session() as session:
    faker = Faker()

    group_names = ['A', 'B', 'C']
    groups = [Group(name=group_name) for group_name in group_names]
    session.add_all(groups)

    lecturer_names = [faker.name() for _ in range(random.randint(3, 5))]
    lecturers = [Lecturer(name=name) for name in lecturer_names]
    session.add_all(lecturers)
    session.commit()

    subject_names = ['Biology', 'Mathematics', 'History', 'Physics', 'Chemistry', 'Literature', 'Geography',
                     'Computer Science']
    subjects = [Subject(name=name, lecturer_id=random.choice(lecturers).id) for name in subject_names]
    session.add_all(subjects)

    for _ in range(random.randint(30, 50)):
        student = Student(
            name=faker.name(),
            group_id=random.choice(groups).id,
            grades=[]
        )

        session.add(student)
        session.flush()

        for _ in range(min(20, random.randint(5, 20))):
            subject_id = random.choice(subjects).id
            start_date = datetime(2023, 1, 1)
            end_date = datetime(2023, 12, 31)

            days_difference = (end_date - start_date).days
            random_days = random.randint(0, days_difference)

            grade_date = start_date + timedelta(days=random_days)
            grade_value = random.randint(1, 6)

            grade = Grade(
                student_id=student.id,
                subject_id=subject_id,
                date=grade_date,
                grade=grade_value,
            )

            student.grades.append(grade)

    session.commit()
