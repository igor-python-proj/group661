import sqlite3


def create_tables(conn):
    conn.execute('''DROP TABLE IF EXISTS students''')
    conn.execute("""
    CREATE TABLE IF NOT EXISTS students (
        name TEXT,
        age INTEGER,
        city TEXT
    )""")

def add_student(conn, name, age, city):
    print("name:", name)
    # добавление данных
    conn.execute("""
    INSERT INTO students VALUES (?, ?, ?)
    """, (name, age, city)
    )
    conn.commit()

def show_students(conn):
    result = conn.execute("SELECT * FROM students")
    return result.fetchall()

if __name__ == "__main__":
    connection = sqlite3.connect("database.db")

    create_tables(connection)

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
        "Elena",
        35,
        "Kant"
    )

    students = show_students(connection)
    print(students)

    connection.close()