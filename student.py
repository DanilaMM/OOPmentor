from people import People


class Student(People):
    # Не хватает __str__ __repr__ методов у студента

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
            return subject.title - (counter//len(self.score[subject.title]))
        else:
            return None

    def check_grade(self):
        if len(self.grade) != 0:
            print(f'Вы изучили такие предметы как:{self.grade}, ваш ученический опыт - {self.exp}')
        else:
            print('Неуч, иди подучись ка!!!')

    def kick_me(self):
        self.group = None

    def __repr__(self):
        return f"Student('{self.name}', '{self.age}', {self.exp})"

    def __str__(self):
        return f"Это студент, его зовут {self.name}, ему {self.age} лет, его опыт равен {self.exp}"

    def __eq__(self, other):
        if isinstance(other, Student):
            return (self.name == other.name and
                    self.age == other.age and
                    self.sex == other.sex)
        return False

    def __lt__(self, other):
        if not isinstance(other, Student):
            raise TypeError(f"unsupported operator < for Student and {other}")

        otherxp = other if isinstance(other, int) else other.exp
        return self.exp < otherxp

    def __le__(self, other):
        if not isinstance(other, (int, Student)):
            raise TypeError(f"unsupported operator > for Student and {other}")

        otherxp = other if isinstance(other, int) else other.exp
        return self.exp <= otherxp

    def __str__(self):
        return f"Это ученик, его зовут {self.name}, ему {self.age} лет"