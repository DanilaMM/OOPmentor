from People import People


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
            raise Exception('Вы не декан, вы не можете подписать билет')


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