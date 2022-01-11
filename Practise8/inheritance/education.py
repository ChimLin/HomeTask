class Man:

    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname

    def __str__(self):
        return f"Name :{self.__name} Surname: { self.__surname}"


class Teacher(Man):

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def teach(self, subject, *students):
        for student in students:
            student.learn_subjects(subject)


class Student(Man):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.subjects = []

    def learn_subjects(self, subject):
        self.subjects.append(subject)

    def show_subjects(self):
        for item in self.subjects:
            print(item)

class Subject:

    def __init__(self, *subjects):
        self.subjects = list(subjects)
        print(subjects)

    def  list_subjects(self):
        return self.subjects

s = Subject("math", "prhisics")
t = Teacher("Name", "Surname")
s = Student("A", "B")
s2 = Student("C", "D")
s3 = Student("F", "E")

print(f"Teacher: {t}, Students:\n{s}, {s2}, {s3}")
t.teach(s.subjects,s,s2,s3)
print(s.show_subjects())
