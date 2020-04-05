import pymongo
from faker import Faker


class Manager:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://db")
        self.client.drop_database('staff_assessment')
        self.db = self.client['staff_assessment']
        self.student = self.db['student']
        self.ta = self.db['ta']
        self.prof = self.db['professor']
        self.feedback = self.db['feedback']
        self.course = self.db['course']
        self.admin = self.db['admin']

    def get_student(self, email):
        q = {"email": email}
        ans = self.student.find(q)
        return ans

    def get_all_students(self):
        return self.student.find()

    def set_student(self, first_name, last_name, email, courses):
        data = {"first_name": first_name,
                "last_name":  last_name,
                "email":      email,
                "courses":    courses}
        self.student.insert_one(data)

    def get_professor(self, email):
        q = {"email": email}
        ans = self.prof.find(q)
        return ans

    def set_professor(self, first_name, last_name, email, courses):
        data = {"first_name": first_name,
                "last_name":  last_name,
                "email":      email,
                "courses":    courses}
        self.prof.insert_one(data)

    def get_ta(self, email):
        q = {"email": email}
        ans = self.ta.find(q)
        return ans

    def set_ta(self, first_name, last_name, email, courses):
        data = {"first_name": first_name,
                "last_name": last_name,
                "email": email,
                "courses": courses
                }
        self.ta.insert_one(data)

    def get_admin(self, email):
        q = {"email": email}
        ans = self.admin.find(q)
        return ans

    def set_admin(self, first_name, last_name, email):
        data = {"first_name": first_name,
                "last_name": last_name,
                "email": email,
                }
        self.admin.insert_one(data)

    def get_course(self, year, name):
        q = {"name": name, "year": year}
        ans = self.course.find(q)
        return ans

    def set_course(self, name, year, prof_id, students):
        data = {
            "year": year,
            "name": name,
            "professor_id": prof_id,
            "students": students
        }
        self.course.insert_one(data)

    def get_feedback(self, course_id, f_type):
        q = {"course_id": course_id, 'feedback_type':f_type}
        ans = self.feedback.find(q)
        return ans

    def set_feedback(self, course_id, f_type, feedback):
        data = {
            'course_id': course_id,
            'f_type': f_type,
            'feedback': feedback
        }
        self.feedback.insert_one(data)


if __name__ == '__main__':
    fake = Faker()

    # random students
    m = Manager()
    for i in range(20):
        n = fake.name().split(' ')
        m.set_student(n[0], n[1], f'{n[0][0].lower()}'
                                  f'.{n[1].lower()}@innopolis.ru', [])
    s = m.get_all_students()
    for x in s:
        print(x)
