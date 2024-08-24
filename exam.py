
class Exam:

    def __init__(self,date, list_bilet, subject):
        # лучше не использовать транслит в проекте, исключительно английский язык, даже в выбрасываемых исключениях
        self.date = date
        self.colvobilet = len(list_bilet)
        self.list_bilet = list_bilet
        self.subject = subject