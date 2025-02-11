from sqlalchemy import func, desc
from models import Student, Grade, Subject, Teacher, Group

from connect import Session, session


# 1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
def select_1(session: Session):
    return (
        session.query(Student.name, func.avg(Grade.score).label("avg_score"))
        .join(Grade)
        .group_by(Student.id)
        .order_by(desc("avg_score"))
        .limit(5)
        .all()
    )


# 2. Знайти студента із найвищим середнім балом з певного предмета.
def select_2(session: Session, subject_id: int):
    return (
        session.query(Student.name, func.avg(Grade.score).label("avg_score"))
        .join(Grade)
        .filter(Grade.subject_id == subject_id)
        .group_by(Student.id)
        .order_by(desc("avg_score"))
        .first()
    )


# 3. Знайти середній бал у групах з певного предмета.
def select_3(session: Session, subject_id: int):
    return (
        session.query(Group.name, func.avg(Grade.score).label("avg_score"))
        .select_from(Group)
        .join(Student, Student.group_id == Group.id)
        .join(Grade, Grade.student_id == Student.id)
        .filter(Grade.subject_id == subject_id)
        .group_by(Group.id)
        .all()
    )


# 4. Знайти середній бал на потоці (по всій таблиці оцінок).
def select_4(session: Session):
    return session.query(func.avg(Grade.score).label("avg_score")).scalar()


# 5. Знайти які курси читає певний викладач.
def select_5(session: Session, teacher_id: int):
    return session.query(Subject.name).filter(Subject.teacher_id == teacher_id).all()


# 6. Знайти список студентів у певній групі.
def select_6(session: Session, group_id: int):
    return session.query(Student.name).filter(Student.group_id == group_id).all()


# 7. Знайти оцінки студентів у окремій групі з певного предмета.
def select_7(session: Session, group_id: int, subject_id: int):
    return (
        session.query(Student.name, Grade.score)
        .join(Grade)
        .filter(Student.group_id == group_id, Grade.subject_id == subject_id)
        .all()
    )


# 8. Знайти середній бал, який ставить певний викладач зі своїх предметів.
def select_8(session: Session, teacher_id: int):
    return (
        session.query(func.avg(Grade.score).label("avg_score"))
        .join(Subject)
        .filter(Subject.teacher_id == teacher_id)
        .scalar()
    )


# 9. Знайти список курсів, які відвідує певний студент.
def select_9(session: Session, student_id: int):
    return (
        session.query(Subject.name)
        .join(Grade)
        .filter(Grade.student_id == student_id)
        .group_by(Subject.id)
        .all()
    )


# 10. Список курсів, які певному студенту читає певний викладач.
def select_10(session: Session, student_id: int, teacher_id: int):
    return (
        session.query(Subject.name)
        .join(Grade)
        .filter(Grade.student_id == student_id, Subject.teacher_id == teacher_id)
        .group_by(Subject.id)
        .all()
    )


if __name__ == "__main__":
    print("Топ-5 студентів із найвищим середнім балом:", select_1(session))
    print(
        "Студент із найвищим середнім балом з предмета 1:",
        select_2(session, subject_id=1),
    )
    print("Середній бал у групах для предмета 1:", select_3(session, subject_id=1))
    print("Середній бал на потоці:", select_4(session))
    print("Курси, які читає викладач 1:", select_5(session, teacher_id=1))
    print("Студенти групи 1:", select_6(session, group_id=1))
    print(
        "Оцінки студентів у групі 1 з предмета 1:",
        select_7(session, group_id=1, subject_id=1),
    )
    print("Середній бал викладача 1:", select_8(session, teacher_id=1))
    print("Курси, які відвідує студент 1:", select_9(session, student_id=1))
    print(
        "Курси, які читає викладач 1 для студента 1:",
        select_10(session, student_id=1, teacher_id=1),
    )

    session.close()
