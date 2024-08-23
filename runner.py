from Ticket import Ticket
from Exam import Exam
from Subject import Subject
from Teacher import Teacher
from StudentGroup import StudentGroup
from Student import Student
from People import People
from faker import Faker

rus_eng = Subject(3, 'русс яз')
ticket1 = Ticket('Текст билета1', 'Доп вопрос-где?', True)
exam1 = Exam('02-12-2000', [ticket1], rus_eng)
fake = Faker()
name1 = fake.name()
name2 = fake.name()
name3 = fake.name()
daniil = Student(name1, 19, 'man')
daniil.read_book()
daniil2 = Student(name2, 20, 'man')
daniil3 = Student(name3, 21, 'man')
student_group1 = StudentGroup([daniil3, daniil2, daniil], 'Группа1')
teacher1 = Teacher('Учитель1', 40, 'man', 'Лучший', student_group1, True)
teacher1.сonduct_an_exam(exam1, 4)

for i in student_group1:
    print(i)
