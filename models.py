from mongoengine import Document, StringField, ListField, ReferenceField, IntField


class User(Document):
    name = StringField()
    roles = ListField(StringField())
    email = StringField()
    password = StringField()
    level = IntField()


class Course(Document):
    code = StringField()
    title = StringField()
    lecturer = StringField()
    status = StringField()
    level = IntField()


class CourseReg(Document):
    student = ReferenceField(User)
    course = ReferenceField(Course)
    status = StringField()
    message = StringField()


class Result(Document):
    student = ReferenceField(User)
    course = ReferenceField(Course)
    test1 = IntField()
    test2 = IntField()
    test3 = IntField()
    exam = IntField()
