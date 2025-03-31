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

    def get_avg_grade(self):
        all_grades = []
        avg_grade = 0
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)
            if all_grades:
                avg_grade = sum(all_grades) / len(all_grades)
            else:
                avg_grade = 0
        return avg_grade  

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

    def __str__(self):
        return (f'Имя: {self.name} \n' +
                f'Фамилия: {self.surname} \n' +
                f'Средняя оценка за домашние задания: {self.get_avg_grade()} \n' +
                f'Курсы в процессе изучения: {self.courses_in_progress} \n' +
                f'Завершенные курсы: {self.finished_courses}')

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

    def get_avg_grade(self):
        all_grades = []
        avg_grade = 0
        for grades in self.lector_grades.values():
            for grade in grades:
                all_grades.append(grade)
        if all_grades:
            avg_grade = sum(all_grades) / len(all_grades)
        else:
            avg_grade = 0
        return avg_grade
    
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

    def __str__(self):

        return (f'Имя: {self.name}\n' +
                f'Фамилия: {self.surname}\n' +
                f'Средняя оценка за лекции: {self.get_avg_grade()}')

# Добавление данных

some_student_1 = Student('Иван', 'Иванов', 'мужской')
some_student_1.courses_in_progress += ['Python']
some_student_1.courses_in_progress += ['Java']
some_student_1.finished_courses += ['Введение в программирование']

some_student_2 = Student('Пётр', 'Петров', 'мужской')
some_student_2.courses_in_progress += ['Python']
some_student_2.courses_in_progress += ['Java']
some_student_2.finished_courses += ['Введение в программирование']

some_lecturer_1 = Lecturer('Джав', 'Джавов')
some_lecturer_1.courses_attached += ['Java']

some_lecturer_2 = Lecturer('Питон', 'Питонов')
some_lecturer_2.courses_attached += ['Python']

some_reviewer_1 = Reviewer('Питон', 'Питонов')
some_reviewer_1.courses_attached += ['Python']

some_reviewer_1.rate_hw(some_student_1, 'Python', 9)
some_reviewer_1.rate_hw(some_student_1, 'Python', 9)

some_reviewer_1.rate_hw(some_student_2, 'Python', 10)
some_reviewer_1.rate_hw(some_student_2, 'Python', 9)

some_student_1.rate_lector(some_lecturer_1, 'Java', 9)
some_student_1.rate_lector(some_lecturer_1, 'Java', 9)

some_student_2.rate_lector(some_lecturer_2, 'Python', 10)
some_student_2.rate_lector(some_lecturer_2, 'Python', 9)

# Проверка задания 2.1: выставление оценки студенту проверяющим

print()
print(f'Проверка задания 2.1: выставление оценки студенту проверяющим')
print(f'Оценки студента: {some_student_1.grades}')

# Проверка задания 2.2: выставление оценок студентом лектору

print()
print(f'Проверка задания 2.2: выставление оценок студентом лектору')
print(some_lecturer_1.lector_grades)

# Проверка задания 3.1: метод __str__

print()
print(f'Проверка задания 3: метод __str__')
print()
print(some_reviewer_1)
print()
print(some_lecturer_1)
print()
print(some_student_1)
print()

# Проверка задания 3.2: сравнение

print(f'Проверка задания 3.2: сравнение')
print()
print(some_student_2)
# print(best_student)
print()
print(some_lecturer_2)
# print(best_lecturer)
print()

if some_student_1 == some_student_2:
    print("Все студенты молодцы! Средние оценки одинаковые!\n")
else:
    if some_student_1 > some_student_2:
        best_student = some_student_1
    else:
        best_student = some_student_2
    print(f'Лучший студент! \n{best_student}\n')

if some_lecturer_1 == some_lecturer_2:
    print("Все лекторы супер! Средние оценки одинаковые!\n")
else:
    if some_lecturer_1 > some_lecturer_2:
        best_lecturer = some_lecturer_1
    else:
        best_lecturer = some_lecturer_2
    print(f'Лучший лектор! \n{best_lecturer}\n')

# Проверка задания 4.1: подсчёт средней оценки студентов

def students_sr_course_grade(students, course_name):
    all_grades = list()
    for st in students:
        if course_name in st.grades and st.grades[course_name]:
            st_course_grades = st_course_grades = st.grades[course_name]
            all_grades.append(sum(st_course_grades) / len(st_course_grades))
    return round(sum(all_grades)/len(all_grades), 2) if all_grades else None

input_course_name = "Python"
print(f"Средняя оценка студентов, обучающихся на курсе {input_course_name}: {students_sr_course_grade([some_student_1, some_student_2], input_course_name)}")


# Проверка задания 4.2: подсчёт средней оценки лекторов

def lecturers_sr_course_grade(lecturers, course_name):
    all_grades = list()
    for lc in lecturers:
        if course_name in lc.lector_grades and lc.lector_grades[course_name]:
            lc_course_grades = lc.lector_grades[course_name]
            all_grades.append(sum(lc_course_grades) / len(lc_course_grades))
    return round(sum(all_grades)/len(all_grades), 2) if all_grades else None

input_course_name = "Python"
print(f"Средняя оценка лекторов, преподающих на курсе {input_course_name}: {lecturers_sr_course_grade([some_lecturer_1, some_lecturer_2], input_course_name)}")





