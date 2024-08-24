from student import Student


class StudentGroup:
    def __init__(self, list_students: list, group_name: str):
        for stud in list_students:
            if isinstance(stud, Student):
                pass
            else:
                raise ValueError(f"The class group of students accepts only students")

        self.list_students = list_students
        self.group_name = group_name
        self.index = 0

    def enroll_students(self):
        for student in self.list_students:
            student.group = self.group_name

    def line_of_students(self):
        '''Используется на физкультуре , что бы пересчитать всех студентов'''
        for index, student in enumerate(self.list_students):
            print(id(student))
            print(self.list_students.index(student))
            if index % 2 == 0:
                yield [student, 'Первый']
            else:
                yield [student, 'Второй']

    def kick_all_students(self):
        for student in self.list_students:
            student.kick_me()

    def lecture(self):
        for student in self.list_students:
            student.read_book()

    def __next__(self):
        if self.index < len(self.list_students):
            self.index += 1
            return self.list_students[self.index]
        else:
            raise StopIteration

    def __iter__(self):
        # Когда создаешь новый итерабельный объект не забывай обнулять self.index, так как сразу получишь StopIteration при повторном цикле
        return iter(self.list_students)

    def __contains__(self, item):
        return item in self.list_students

    def __len__(self):
        return len(self.list_students)
