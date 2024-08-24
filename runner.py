from ticket import Ticket
from exam import Exam
from subject import Subject
from teacher import Teacher
from student_group import StudentGroup
from student import Student
from people import People
from faker import Faker

# список для генератора тикетов
list_of_lists = [
    ['hello', 'how are you', False],
    ['python', 'is awesome', True],
    ['programming', 'is fun', True],
    ['data science', 'is interesting', False],
    ['machine learning', 'is challenging', True],
    ['artificial intelligence', 'is exciting', False],
    ['computer vision', 'is cool', True],
    ['natural language processing', 'is fascinating', False],
    ['deep learning', 'is powerful', True],
    ['reinforcement learning', 'is rewarding', False]
]
tiket_generator = ((text, question, is_decan_accept) for text, question, is_decan_accept in list_of_lists)
tiket_gen1 = next(tiket_generator)
tiket_gen2 = next(tiket_generator)
print(tiket_gen1)
print(tiket_gen2)

rus_eng = Subject(3, 'русс яз')
ticket1 = Ticket('Текст билета1', 'Доп вопрос-где?', True)
exam1 = Exam('02-12-2000', [ticket1], rus_eng)
fake = Faker()
name1 = fake.name()
name2 = fake.name()
name3 = fake.name()
daniil = Student(name1, 19, 'man')
# Для всего остального тоже фейкер можешь использовать
daniil.read_book()
daniil2 = Student(name2, 20, 'man')
daniil3 = Student(name3, 21, 'man')
people1 = People('den', 20, 'woman')
student_group1 = StudentGroup([daniil3, daniil2, daniil], 'Группа1')
teacher1 = Teacher('Учитель1', 40, 'man', 'Лучший', student_group1, True)
teacher1.сonduct_an_exam(exam1, 4)
x = student_group1.line_of_students()
print(next(x))
print(next(x))
print(next(x))
for i in student_group1:
    print(i)
