from faker import Faker
class People:

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


class Student(People):

    def __init__(self, name: str, age: int, sex: str):
        super().__init__(name, age, sex)
        self.exp = 0
        self.grade = []
        self.score = {}
        self.group = None

    def read_book(self):
        self.exp += 1

    def check_my_exp(self):
        print(f"Ваш опыт - {self.exp}")

    def check_score(self, subject):
        if subject.title in self.score:
            counter = 0
            for i in self.score[subject.title]:
                counter += i
            print(f'Ваша средняя оценка по предмету {subject.title} - {counter//len(self.score[subject.title])}')
        else:
            print(f'Вы еще не посещяли предмет {subject.title}')

    def check_grade(self):
        if len(self.grade) != 0:
            print(f'Вы изучили такие предметы как:{self.grade}, ваш ученический опыт - {self.exp}')
        else:
            print('Неуч, иди подучись ка!!!')

    def kick_me(self):
        self.group = None



#Сравниваем экземпляры одного класса - student == student1
    def __eq__(self, other):
        if not isinstance(other, (int, Student)):
            raise TypeError("Операнд справа должен иметь тип int или Clock")

        otherxp = other if isinstance(other, int) else other.exp
        return self.exp == otherxp

    def __lt__(self, other):
        if not isinstance(other, (int, Student)):
            raise TypeError("Операнд справа должен иметь тип int или Clock")

        otherxp = other if isinstance(other, int) else other.exp
        return self.exp < otherxp

    def __le__(self, other):
        if not isinstance(other, (int, Student)):
            raise TypeError("Операнд справа должен иметь тип int или Clock")

        otherxp = other if isinstance(other, int) else other.exp
        return self.exp <= otherxp

    def __str__(self):
        return f"Это ученик, его зовут {self.name}, ему {self.age} лет"


class StudentGroup:
#Взаимодействовать с полями не напрямую , а через методы
    def __init__(self, list_students: list, group_name: str):
        self.list_students = list_students
        self.group_name = group_name
        for student in list_students:
            student.group = group_name


    def kick_all_students(self):
        for student in self.list_students:
            student.kick_me()

    def lecture(self):
        for student in self.list_students:
            student.read_book()


    def __iter__(self):
        return self.list_students

    def __contains__(self, item):
        if item in self.list_students:
            return True
        else:
            return False

    def __len__(self):
        return len(self.list_students)

class Teacher(People):

    def __init__(self, name, age, sex,skill_teacher: str, my_group, decan: bool):
        super().__init__(name, age, sex)
        self.skill_teacher = skill_teacher
        self.my_group = my_group
        self.decan = decan

    def sign_a_ticket(self, ticket):
        if self.decan:
            ticket.decan_accept = True
        else:
            print('Вы не декан, вы не можете подписать билет')


    def teaching_a_student(self, student, subject, score):
        if subject.title in student.grade:
            student.exp += subject.hard
            student.score[subject.title].append(score)
        else:
            student.grade.append(subject.title)
            student.exp += subject.hard
            student.score[subject.title] = [score]

    def teachin_group(self, group, subject, score):
        for student in group.list_students:
            if subject.title in student.grade:
                student.exp += subject.hard
                student.score[subject.title].append(score)
            else:
                student.grade.append(subject.title)
                student.exp += subject.hard
                student.score[subject.title] = [score]

    def teaching_my_group(self, subject, score):
        for student in self.my_group.list_students:
            if subject.title in student.grade:
                student.exp += subject.hard
                student.score[subject.title].append(score)
            else:
                student.grade.append(subject.title)
                student.exp += subject.hard
                student.score[subject.title] = [score]

    def сonduct_an_exam(self, exam, score):
        for student in self.my_group.list_students:
            if exam.subject.title in student.grade:
                student.exp += exam.subject.hard
                student.score[exam.subject.title].append(score)
            else:
                student.grade.append(exam.subject.title)
                student.exp += exam.subject.hard
                student.score[exam.subject.title] = [score]


    def __str__(self):
        return f"Это учитель, его зовут {self.name}, ему {self.age} лет, он преподает {self.skill_teacher}"


class Subject:

    def __init__(self, hard, title):
        self.hard = hard
        self.title = title


class Exam:

    def __init__(self,date, list_bilet, subject):
        self.date = date
        self.colvobilet = len(list_bilet)
        self.list_bilet = list_bilet
        self.subject = subject


class Ticket:

    def __init__(self,text, question, decan_accept: bool):
        self.text = text
        self.question = question
        self.decan_accept = decan_accept





if __name__ == '__main__':
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




