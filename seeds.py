from faker import Faker
from models import Group, Student, Teacher, Subject, Grade
import random
from datetime import datetime

from connect import session

fake = Faker()


def seed_data():
    groups = [Group(name=f"Group {i}") for i in range(1, 4)]
    session.add_all(groups)
    session.commit()

    students = [
        Student(name=fake.name(), group=random.choice(groups)) for _ in range(50)
    ]
    session.add_all(students)
    session.commit()

    teachers = [Teacher(name=fake.name()) for _ in range(5)]
    session.add_all(teachers)
    session.commit()

    subjects = [
        Subject(name=f"Subject {i}", teacher=random.choice(teachers))
        for i in range(1, 9)
    ]
    session.add_all(subjects)
    session.commit()

    for student in students:
        for subject in subjects:
            for _ in range(20):
                grade = Grade(
                    student=student,
                    subject=subject,
                    score=random.uniform(50, 100),
                    date=fake.date_this_year(),
                )
                session.add(grade)
    session.commit()


if __name__ == "__main__":
    seed_data()
    session.close()
