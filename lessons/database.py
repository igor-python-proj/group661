import sqlite3
from colorama import Fore

def create_tables(conn):
    conn.execute('''DROP TABLE IF EXISTS students''')
    conn.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        city TEXT
    )""")

# CRUD - create(добавление данных) read(получение данных)
# update(изменение данных) delete(удаление данных)
def add_student(conn, name, age, city):
    print("name:", name)
    # добавление данных
    conn.execute("""
    INSERT INTO students (name, age, city) VALUES (?, ?, ?)
    """, (name, age, city)
    )
    conn.commit()

def show_students(conn):
    result = conn.execute("SELECT * FROM students")
    # result = conn.execute("SELECT name, age FROM students LIMIT 2")
    # возвращаем список кортежей
    return result.fetchall()

def get_student_by_name(conn, name):
    result = conn.execute("""
        SELECT * FROM students 
        WHERE name = ?""",
    (name,))
    return result.fetchall()

def get_student_by_id(conn, student_id):
    result = conn.execute("""
        SELECT * FROM students 
        WHERE id = ?""",
    (student_id,))
    return result.fetchone()

def delete_student(conn, student_id):
    conn.execute("""
        DELETE FROM students
        WHERE id = ?""",
    (student_id,))
    conn.commit()

def delete_by_city(conn, city):
    conn.execute("""
        DELETE FROM students
        WHERE city = ?
    """, (city,))
    conn.commit()


def change_student(conn, name, age, city, student_id):
    conn.execute("""
    UPDATE students 
    SET name = ?, age = ?, city = ?
    WHERE id = ?""",
    (name, age, city, student_id))
    conn.commit()


if __name__ == "__main__":
    connection = sqlite3.connect("database.db")

    create_tables(connection)
    print(Fore.RED + 'Работа с базой данных')
    add_student(
        connection,
        "Kurmanbek",
        20,
        "Bishkek"
    )
    add_student(
        connection,
        "Altynai",
        25,
        "Karakol"
    )
    add_student(
        connection,
        "Almaz",
        24,
        "Karakol"
    )
    add_student(
        connection,
        "Elena",
        35,
        "Kant"
    )

    students = show_students(connection)
    print(students)

    print("=== filtering ===")
    students2 = get_student_by_name(connection, "Elena")
    print(students2)
    student = get_student_by_id(connection, 1)
    print(student)

    print("=== deleting ===")
    delete_student(connection, 1)
    delete_by_city(connection, "Karakol")
    students = show_students(connection)
    print(students)

    print("=== updating ===")
    change_student(
        connection,
        "Elena",
        35,
        "Bishkek",
        4,
    )
    students = show_students(connection)
    print(students)

    connection.close()