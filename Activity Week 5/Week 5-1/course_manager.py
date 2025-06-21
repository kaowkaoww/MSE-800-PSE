from database import create_connection
import sqlite3

def add_course(course_code, course_name):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO course (course_name, course_code) VALUES (?, ?)", (course_name, course_code))
        conn.commit()
        print(" Course added successfully.")
    except sqlite3.IntegrityError:
        print(" Course must be unique.")
    conn.close()

def search_course(course_code, course_name):
    conn = create_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM course WHERE 1=1" 
    params = []

    if course_name:
        query += " AND course_name LIKE ? "
        params.append(f"%{course_name}%")

    if course_code:
        query += " AND course_code LIKE ? "
        params.append(f"%{course_code}%")



    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("No course found matching the search criteria.")
    return rows 
