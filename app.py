from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

def connect_db():
    return sqlite3.connect("database.db")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/entry', methods=['POST'])
def entry():

    data = request.get_json()

    student_id = data.get("student_id")
    rc = data.get("rc")
    licence = data.get("licence")

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE id=?",
        (student_id,)
    )

    student = cursor.fetchone()

    cursor.execute(
        "SELECT * FROM vehicles WHERE rc_number=? AND student_id=?",
        (rc, student_id)
    )

    vehicle = cursor.fetchone()

    cursor.execute(
        "SELECT * FROM licences WHERE licence_number=? AND student_id=?",
        (licence, student_id)
    )

    lic = cursor.fetchone()

    conn.close()

    if student and vehicle and lic:

        return jsonify({
            "status": "Access Granted"
        })

    return jsonify({
        "status": "Access Denied"
    })

if __name__ == "__main__":
    app.run(debug=True)
