from flask import Flask, jsonify, request


def create_app():
    app = Flask(__name__)

    students = [
        {
            "id": 1,
            "name": "Ava Johnson",
            "email": "ava.johnson@example.com",
            "course": "Computer Science",
        },
        {
            "id": 2,
            "name": "Liam Chen",
            "email": "liam.chen@example.com",
            "course": "Information Technology",
        },
    ]

    @app.get("/students")
    def get_students():
        return jsonify(students), 200

    @app.get("/students/<int:student_id>")
    def get_student(student_id):
        student = next((item for item in students if item["id"] == student_id), None)
        if student is None:
            return jsonify({"error": "Student not found"}), 404
        return jsonify(student), 200

    @app.post("/students")
    def add_student():
        payload = request.get_json(silent=True)
        if not isinstance(payload, dict):
            return jsonify({"error": "Request body must be a JSON object"}), 400

        required_fields = ("name", "email", "course")
        missing_fields = [
            field for field in required_fields
            if not isinstance(payload.get(field), str) or not payload[field].strip()
        ]
        if missing_fields:
            return jsonify({
                "error": "Fields name, email, and course are required",
                "missing_fields": missing_fields,
            }), 400

        if "@" not in payload["email"]:
            return jsonify({"error": "Email must be valid"}), 400

        new_student = {
            "id": max((student["id"] for student in students), default=0) + 1,
            "name": payload["name"].strip(),
            "email": payload["email"].strip(),
            "course": payload["course"].strip(),
        }
        students.append(new_student)
        return jsonify(new_student), 201

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
