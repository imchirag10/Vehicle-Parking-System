from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

students = {
    "1": {
        "rc": "RC123",
        "licence": "LIC123"
    }
}

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/entry', methods=['POST'])
def entry():

    data = request.json

    student_id = data['student_id']
    rc = data['rc']
    licence = data['licence']

    if student_id in students:
        if students[student_id]["rc"] == rc and students[student_id]["licence"] == licence:
            return jsonify({"status": "Access Granted"})
    
    return jsonify({"status": "Access Denied"})

if __name__ == "__main__":
    app.run(debug=True)
   
