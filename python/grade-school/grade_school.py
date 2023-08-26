import bisect


class School:
    def __init__(self):
        self.grades = [[] for _ in range(7)]
        self.status = []

    def add_student(self, name, grade):
        if name not in self.roster():
            bisect.insort(self.grades[grade - 1], name)
            self.status.append(True)
        else:
            self.status.append(False)

    def roster(self):
        result = []
        for i in range(len(self.grades)):
            result += self.grades[i]
        return result

    def grade(self, grade_number):
        return self.grades[grade_number - 1]

    def added(self):
        return self.status
