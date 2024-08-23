from People import People


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