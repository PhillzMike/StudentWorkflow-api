from flask import Flask, request
import database
from marshmallow import Schema, fields
from models import Course

app = Flask(__name__)


class CourseSchema(Schema):
    id = fields.String()

    class Meta:
        additional = ('code', 'title', 'lecturer', 'status', 'level')


courseSchema = CourseSchema()


@app.route('/course', methods=["POST"])
def add_course():
    title = request.json['title']
    code = request.json['code']
    lecturer = request.json['lecturer']
    status = request.json['status']
    level = request.json['level']

    course = Course(code=code, title=title, lecturer=lecturer, status=status, level=level)
    course = course.save()
    print(course.id)
    jsonify = courseSchema.dump(course)
    return jsonify


@app.route('/courses', methods=["GET"])
def get_courses():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
