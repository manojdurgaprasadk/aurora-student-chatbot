from rapidfuzz import fuzz
import sqlite3

def get_response(user_question):

    conn = sqlite3.connect("college.db")
    cursor = conn.cursor()

    cursor.execute("SELECT question, answer FROM college_info")
    data = cursor.fetchall()

    best_score = 0
    best_answer = "Sorry, I could not understand your question."

    for question, answer in data:

        score = fuzz.ratio(user_question.lower(), question.lower())

        if score > best_score:
            best_score = score
            best_answer = answer

    conn.close()

    if best_score > 60:
        return best_answer
    else:
        return "Please ask about college related queries."