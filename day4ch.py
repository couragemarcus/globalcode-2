from flask import Flask, jsonify

app = Flask(__name__)

students = [
    {
        'id': 1,
        'name': 'John Doe',
        'age': 20,
        'program': 'Computer Science'
    },
    {
        'id': 2,
        'name': 'Jane Smith',
        'age': 32,
        'program': 'ICT'
    },
    {
        'id': 3,
        'name': 'Smoke',
        'age': 42,
        'program': 'Fashion'
    },
    {
        'id': 4,
        'name': 'Smith',
        'age': 12,
        'program': 'BT'
    },
    {
        'id': 5,
        'name': 'Jane',
        'age': 22,
        'program': 'Belook'
    }
]


@app.route('/api/students', methods=['GET'])
def get_students():
    return jsonify(students)


@app.route('/api/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = next(
        (student for student in students if student['id'] == student_id),
        None
    )

    if student is None:
        return jsonify({'message': 'Student not found'}), 404

    return jsonify(student)


if __name__ == '__main__':
    app.run(debug=True)

