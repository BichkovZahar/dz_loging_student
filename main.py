import logging
class StudentProcessor:
    def __init__(self):
        self.students = []
        self.logger = logging.getLogger('hello')
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(logging.StreamHandler())
    def add_student(self , student):
        self.students.append(student)
        self.logger.info(f"{student} був доданий до списку")
    def remove_student(self , student):
        try:
          self.students.remove(student)
          self.logger.info(f"{student} був видалений зі списку")
        except:
          print(f"{student} не було знайдено в списку")
    def process_students(self):
        print()
        print("Студенти")
        for item in self.students:
            print(f"{item} студент")
finish = StudentProcessor()
finish.add_student("Захар")
finish.add_student("Женя")
finish.add_student("Даша")
finish.remove_student("Даша")
finish.process_students()
