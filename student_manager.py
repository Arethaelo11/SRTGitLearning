class StudentMananger:
    def __init__(self, name, department):
        self.name = name
        self.department = department
        self.score = 0.0
        self.unit = 0
        self.cgpa = 0.0

    def compute_cgpa(self, unit, score):
        self.cgpa = score / unit
