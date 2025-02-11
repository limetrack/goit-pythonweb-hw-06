# **Student Management System**

A simple project to manage students, groups, teachers, subjects, and grades using Python, SQLAlchemy, PostgreSQL, and Alembic.

---

## **Requirements**
- Python 3.8+
- Docker
- Poetry

---

## **Setup Instructions**

### **1. Clone the repository**
```
git clone <repository-url>
cd <repository-folder>
```

### **2. Start PostgreSQL with Docker**
```docker run --name hw6_postgres -p 5432:5432 -e POSTGRES_PASSWORD=pwd -d postgres```

### **3. Install dependencies**
```poetry install```

### **4. Initialize the database**
```poetry run alembic upgrade head```

### **5. Seed the database**
```poetry run python seeds.py```

### **6. Run queries**
Use my_select.py to perform queries. For example:
```
poetry run python
>>> from my_select import *
>>> from connect import session
>>> print(select_1(session))  # Example query
>>> session.close()
```

## **Project Structure**
models.py: SQLAlchemy models for the database.
seeds.py: Script to populate the database with sample data.
my_select.py: Predefined queries for the database.
migrations/: Alembic configuration for database migrations.

## **Useful Commands**
Start Poetry Shell:
```poetry shell```
Stop PostgreSQL Container:
```docker stop hw6_postgres```
Restart PostgreSQL Container:
```docker start hw6_postgres```
