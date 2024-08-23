class StudentGroup:
#Взаимодействовать с полями не напрямую , а через методы
    def __init__(self, list_students: list, group_name: str):
        self.list_students = list_students
        self.group_name = group_name
        self.index = 0
        for student in list_students:
            student.group = group_name


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
        return iter(self.list_students)

    def __contains__(self, item):
        if item in self.list_students:
            return True
        else:
            return False

    def __len__(self):
        return len(self.list_students)

