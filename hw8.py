import sqlite3

conn = sqlite3.connect('my_database2.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    grade INTEGER,
    subject TEXT
)
''')
conn.commit()

def add_student(first_name, last_name, grade, subject):
    cursor.execute('''
        INSERT INTO students (first_name, last_name, grade, subject)
        VALUES (?, ?, ?, ?)
    ''', (first_name, last_name, grade, subject))
    conn.commit()
    print(f"Студент {first_name} {last_name} добавлен!!")

def get_students():
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    for s in students:
        print(s)
    return students

def update_student(student_id, new_first_name, new_last_name):
    cursor.execute('''
        UPDATE students
        SET first_name = ?, last_name = ?
        WHERE id = ?
    ''', (new_first_name, new_last_name, student_id))
    conn.commit()
    print(f"Студент с ID {student_id} обнавлен!")

def delete_student(student_id):
    cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))
    conn.commit()
    print(f"Студент с ID {student_id} удален!")

if __name__ == "__main__":
    add_student("Pin", "Granovich", 11, "math")
    add_student("Lina", "Krasnova", 10, "music")

    print("\nВсе студенты:")
    get_students()

    update_student(1, "Pin", "Timurovich")
    print("\nПосле обновления:")
    get_students()

    delete_student(2)
    print("\nПосле удаления:")
    get_students()

conn.close()