import sqlite3

def fetch_questions():

    conn = sqlite3.connect("college.db")

    cursor = conn.cursor()

    cursor.execute("SELECT question, answer FROM college_info")

    rows = cursor.fetchall()

    conn.close()

    return rows