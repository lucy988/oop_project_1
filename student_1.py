class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_courses(self, course_name):
        self.finished_courses.append(course_name) 

    def rate_lector(self, lector, course, grade):
        if course in self.courses_in_progress and course in lector.courses_attached:
            if course in lector.lector_grades:
                lector.lector_grades[course].append(grade)
            else:
                lector.lector_grades[course] = [grade]

    def __str__(self):
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)
            if all_grades:
                avg_grade = sum(all_grades) / len(all_grades)
            else:
                avg_grade = 0
        return (f'Имя: {self.name} \n' +
                f'Фамилия: {self.surname} \n' +
                f'Средняя оценка за домашние задания: {avg_grade} \n' +
                f'Курсы в процессе изучения: {self.courses_in_progress} \n' +
                f'Завершенные курсы: {self.finished_courses}')
    
    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.get_avg_grade() < other.get_avg_grade()
    
    def __le__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.get_avg_grade() <= other.get_avg_grade()
    
    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.get_avg_grade() == other.get_avg_grade()
    
    def get_avg_grade(self):
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)
        return sum(all_grades) / len(all_grades) if all_grades else 0

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
                return 'Ошибка'
        
    def __str__(self):
        return (f'Имя: {self.name} \n' +
                f'Фамилия: {self.surname}')
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lector_grades = {}

    def __str__(self):
        all_grades = []
        for grades in self.lector_grades.values():
            for grade in grades:
                all_grades.append(grade)
        if all_grades:
            avg_grade = sum(all_grades) / len(all_grades)
        else:
            avg_grade = 0
        return (f'Имя: {self.name}\n' +
                f'Фамилия: {self.surname}\n' +
                f'Средняя оценка за лекции: {self.get_avg_grade()}')
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.get_avg_grade() < other.get_avg_grade()
    
    def __le__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.get_avg_grade() <= other.get_avg_grade()
    
    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.get_avg_grade() == other.get_avg_grade()
    
    def get_avg_grade(self):
        all_grades = []
        for grades in self.lector_grades.values():
            all_grades.extend(grades)
        return sum(all_grades) / len(all_grades) if all_grades else 0

# Проверка задания 2.1: выставление оценки студенту проверяющим
some_student = Student('Иван', 'Иванов', 'мужской')
some_student.courses_in_progress += ['Python']

some_reviewer = Reviewer('Питон', 'Питонов')
some_reviewer.courses_attached += ['Python']

some_reviewer.rate_hw(some_student, 'Python', 7)
some_reviewer.rate_hw(some_student, 'Python', 8)

print()
print(f'Проверка задания 2.1: выставление оценки студенту проверяющим')
print(f'Оценки студента: {some_student.grades}')

# Проверка задания 2.2: выставление оценок студентом лектору
some_lecturer = Lecturer('Джав', 'Джавов')
some_lecturer.courses_attached += ['Java']

some_student.courses_in_progress += ['Java']
some_student.rate_lector(some_lecturer, 'Java', 9)
some_student.rate_lector(some_lecturer, 'Java', 10)

print()
print(f'Проверка задания 2.2: выставление оценок студентом лектору')
print(some_lecturer.lector_grades)

# Проверка задания 3.1: метод __str__
print()
print(f'Проверка задания 3: метод __str__')
print()
print(some_reviewer)
print()
print(some_lecturer)
print()
some_student.finished_courses += ['Введение в программирование']
print(some_student)
print()

# Проверка задания 3.2: сравнение
print("Проверка сравнения:")

# Создаем еще одного студента и лектора для сравнения
another_student = Student('Петр', 'Петров', 'мужской')
another_student.courses_in_progress += ['Python']
some_reviewer.rate_hw(another_student, 'Python', 9)
some_reviewer.rate_hw(another_student, 'Python', 9)

another_lecturer = Lecturer('Си', 'Плюсов')
another_lecturer.courses_attached += ['C++']
some_student.courses_in_progress += ['C++']
some_student.rate_lector(another_lecturer, 'C++', 8)
some_student.rate_lector(another_lecturer, 'C++', 8)

print("\nСравнение студентов:")
print(f"Средний балл some_student: {some_student.get_avg_grade()}")
print(f"Средний балл another_student: {another_student.get_avg_grade()}")
print(f"some_student < another_student: {some_student < another_student}")
print(f"some_student == another_student: {some_student == another_student}")

print("\nСравнение лекторов:")
print(f"Средний балл some_lecturer: {some_lecturer.get_avg_grade()}")
print(f"Средний балл another_lecturer: {another_lecturer.get_avg_grade()}")
print(f"some_lecturer > another_lecturer: {some_lecturer > another_lecturer}")
print(f"some_lecturer == another_lecturer: {some_lecturer == another_lecturer}")