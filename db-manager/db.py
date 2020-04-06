import pymongo
import random as rm
from faker import Faker


class Manager:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://db")
        self.db = self.client['staff_assessment']
        self.student = self.db['student']
        self.ta = self.db['ta']
        self.prof = self.db['professor']
        self.feedback = self.db['feedback']
        self.course = self.db['course']
        self.admin = self.db['admin']

    def drop_db(self):
        self.client.drop_database('staff_assessment')

    def get_student(self, email):
        x = self.student.find_one({'email': email})
        return x

    def get_all_students(self):
        arr = []
        res = self.student.find()
        for _ in res:
            arr.append(_)
        return arr

    def set_student(self, first_name, last_name, email, courses):
        data = {"first_name": first_name,
                "last_name": last_name,
                "email": email,
                "courses": courses}
        self.student.insert_one(data)

    def get_professor(self, email):
        x = self.prof.find_one({'email': email})
        return x

    def get_all_prof(self):
        arr = []
        res = self.prof.find()
        for _ in res:
            arr.append(_)
        return arr

    def set_professor(self, first_name, last_name, email, courses):
        data = {"first_name": first_name,
                "last_name": last_name,
                "email": email,
                "courses": courses}
        self.prof.insert_one(data)

    def get_ta(self, email):
        x = self.ta.find_one({'email': email})
        return x

    def get_all_ta(self):
        arr = []
        res = self.ta.find()
        for _ in res:
            arr.append(_)
        return arr

    def set_ta(self, first_name, last_name, email, courses):
        data = {"first_name": first_name,
                "last_name": last_name,
                "email": email,
                "courses": courses
                }
        self.ta.insert_one(data)

    def get_admin(self, email):
        x = self.admin.find_one({'email': email})
        return x

    def get_all_admin(self):
        arr = []
        res = self.admin.find()
        for _ in res:
            arr.append(_)
        return arr

    def set_admin(self, first_name, last_name, email):
        data = {"first_name": first_name,
                "last_name": last_name,
                "email": email,
                }
        self.admin.insert_one(data)

    def get_course(self, name, year):
        x = self.course.find_one({"name": name, "year": year})
        return x

    def get_all_courses(self):
        arr = []
        res = self.course.find()
        for _ in res:
            arr.append(_)
        return arr

    def set_course(self, name, year, prof_id, ta_id):
        data = {
            "year": year,
            "name": name,
            "professor_id": prof_id,
            "ta_id": ta_id
        }
        self.course.insert_one(data)

    def get_feedback(self, course_id, f_type):
        q = {"course_id": course_id, 'feedback_type': f_type}
        x = self.feedback.find_one(q)
        return x

    def get_all_feedback(self):
        arr = []
        res = self.feedback.find()
        for _ in res:
            arr.append(_)
        return arr

    def set_feedback(self, course_id, f_type, feedback):
        # 0 - course
        # 1 - prof
        # 2 - TA
        data = {
            'course_id': course_id,
            'f_type': f_type,
            'feedback': feedback
        }
        self.feedback.insert_one(data)

    def generator(self):
        fake = Faker()
        self.drop_db()

        student_emails = []
        for i in range(20):
            n = fake.name().split(' ')
            email = f'{n[0][0].lower()}.{n[1].lower()}@innopolis.university.ru'
            student_emails.append(email)
            self.set_student(n[0], n[1], email, [])

        prof_emails = []
        for i in range(20):
            n = fake.name().split(' ')
            email = f'{n[0][0].lower()}.{n[1].lower()}@innopolis.ru'
            prof_emails.append(email)
            self.set_professor(n[0], n[1], email, [])

        ta_emails = []
        for i in range(20):
            n = fake.name().split(' ')
            email = f'{n[0][0].lower()}.{n[1].lower()}@innopolis.ru'
            ta_emails.append(email)
            self.set_ta(n[0], n[1], email, [])

        def gen_course(name, year, professor, ta, students):
            professor = self.get_professor(professor)
            tas_data = []
            tas_id = []
            for ta_email in ta:
                tas_data.append(self.get_ta(ta_email))
                tas_id.append(tas_data[len(tas_data) - 1]['_id'])
            self.set_course(name, year, professor['_id'], tas_id)
            c = self.get_course(name, year)
            professor['courses'].append(c['_id'])
            result = self.prof.replace_one({'_id': professor['_id']},
                                        professor)

            for t in tas_data:
                t['courses'].append(c['_id'])
                result = self.ta.replace_one({'_id': t['_id']}, t)

            for s in students:
                student = self.get_student(s)
                student['courses'].append(c['_id'])
                result = self.student.replace_one({'_id': student['_id']},
                                               student)

        info_courses = [('Maths', 2020), ('Sowftware Project', 2020),
                        ('English', 2019), ('Linear Algebra', 2019)]

        for course in info_courses:
            cur_prof = rm.choice(prof_emails)
            cur_ta = [rm.choice(ta_emails) for _ in range(4)]
            cur_stu = [rm.choice(student_emails) for _ in range(10)]
            gen_course(course[0], course[1], cur_prof, cur_ta, cur_stu)

if __name__ == '__main__':
    m = Manager()
    m.generator()