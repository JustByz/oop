students_list = []
lecturers_list = []


class Student:
    
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        students_list.append(self)
        
    def rate_l(self, lecture, course, grade):
        if isinstance(lecture, Lecture) and course in self.courses_in_progress and course in lecture.courses_attached and 0 < grade <= 10:
            if course in lecture.grades:
                lecture.grades[course] += [grade]
            else:
                lecture.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def average_all_courses(self):
        count = 0
        grade = 0
        for course in list(self.grades.keys()):
            if self.grades.get(course) != None:
                count += len(self.grades[course])
                grade += sum(self.grades[course])
            else:
                continue
        grade = '{:.2f}'.format(grade / count)
        return grade
    
    def average_simple_course(self, course):
        grade = '{:.2f}'.format(sum(self.grades[course]) / len(self.grades[course]))
        return grade
    
    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_all_courses() < other.average_all_courses()
        else:
            return 'Ошибка'
    
    def __str__(self):
        text = f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {Student.average_all_courses(self)}
Курсы в процессе изучения: {', '.join(self.courses_in_progress)}
Завершенные курсы: {', '.join(self.finished_courses)}
'''
        return text
        
        
class Mentor:
    
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
          

class Lecture(Mentor):
    
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}  
        lecturers_list.append(self)
        
    def average_all_courses(self):
        count = 0
        grade = 0
        for course in list(self.grades.keys()):
            if self.grades.get(course) != None:
                count += len(self.grades[course])
                grade += sum(self.grades[course])
            else:
                continue
        grade = '{:.2f}'.format(grade / count)
        return grade
    
    def average_simple_course(self, course):
        grade = '{:.2f}'.format(sum(self.grades[course]) / len(self.grades[course]))
        return grade
    
    def rate_hw(self, student, course, grade):
        print('Лектор не может выставлять оценки.\n')
    
    def __lt__(self, other):
        if isinstance(other, Lecture):
            return self.average_all_courses() < other.average_all_courses()
        else:
            return 'Ошибка'
    
    def __str__(self):
        text = f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {Lecture.average_all_courses(self)}
'''
        return text
    
    
class Reviewer(Mentor):
    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress and 0 < grade <= 10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        text = f'''Имя: {self.name}
Фамилия: {self.surname}
'''
        return text
    
def course_average_students(stud_list, course):
    total = []
    counter = 0
    for student in stud_list:
        if course in student.courses_in_progress:
            total += student.grades[course]
            counter += 1
    if counter == 0:
        return 'Этот курс никто не изучает.'
    else:
        average_students = '{:.2f}'.format(sum(total) / len(total))
        return f'Средний балл всех студентов на курсе "{course}": {average_students}\n'
    
def course_average_lecturers(lect_list, course):
    total = []
    counter = 0
    for lecturer in lect_list:
        if course in lecturer.courses_attached:
            total += lecturer.grades[course]
            counter += 1
    if counter == 0:
        return 'Этот курс никто не читает.'
    else:
        average_lecturers = '{:.2f}'.format(sum(total) / len(total))
        return f'Средний балл всех лекторов на курсе "{course}": {average_lecturers}\n'
    
    
 
best_student = Student('Александр', 'Зайцев', 'мужчина')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Основы программирования']
best_student.courses_in_progress += ['Высшая математика']
best_student.courses_in_progress += ['Алгоритмы']

medium_student = Student('Максим', 'Стрельцов', 'male')
medium_student.courses_in_progress += ['Python']
medium_student.courses_in_progress += ['Основы программирования']
medium_student.courses_in_progress += ['Высшая математика']
medium_student.courses_in_progress += ['Алгоритмы']
 
cool_mentor = Reviewer('Николай', 'Губанов')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['Основы программирования']

cool_reviewer = Reviewer('Никита', 'Лушин')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Основы программирования']

math_lecturer = Lecture('Владимир', 'Семенов')
math_lecturer.courses_attached += ['Высшая математика']
math_lecturer.courses_attached += ['Алгоритмы']
math_lecturer.courses_attached += ['Основы программирования']

prog_lecturer = Lecture('Степан', 'Разин')
prog_lecturer.courses_attached += ['Python']
prog_lecturer.courses_attached += ['Основы программирования']
prog_lecturer.courses_attached += ['Алгоритмы']

best_student.rate_l(math_lecturer, 'Высшая математика', 9)
best_student.rate_l(math_lecturer, 'Высшая математика', 9)
best_student.rate_l(math_lecturer, 'Высшая математика', 10)

medium_student.rate_l(math_lecturer, 'Алгоритмы', 8)
medium_student.rate_l(math_lecturer, 'Алгоритмы', 9)
medium_student.rate_l(math_lecturer, 'Алгоритмы', 7)

best_student.rate_l(prog_lecturer, 'Python', 8)
best_student.rate_l(prog_lecturer, 'Python', 9)
best_student.rate_l(prog_lecturer, 'Python', 8)

medium_student.rate_l(prog_lecturer, 'Основы программирования', 8)
medium_student.rate_l(prog_lecturer, 'Основы программирования', 10)
medium_student.rate_l(prog_lecturer, 'Основы программирования', 7)

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 9)
cool_mentor.rate_hw(best_student, 'Python', 8)
cool_mentor.rate_hw(best_student, 'Основы программирования', 9)
cool_mentor.rate_hw(best_student, 'Основы программирования', 8)
cool_mentor.rate_hw(best_student, 'Основы программирования', 8)

cool_reviewer.rate_hw(medium_student, 'Python', 9)
cool_reviewer.rate_hw(medium_student, 'Python', 8)
cool_reviewer.rate_hw(medium_student, 'Python', 7)
cool_reviewer.rate_hw(medium_student, 'Основы программирования', 9)
cool_reviewer.rate_hw(medium_student, 'Основы программирования', 9)
cool_reviewer.rate_hw(medium_student, 'Основы программирования', 7)

prog_lecturer.rate_hw(medium_student, 'Основы программирования', 9)
print(cool_mentor)
print(math_lecturer)
print(prog_lecturer)
print(best_student)
print(medium_student)
print('Сравнение студентов:')
print(best_student > medium_student)
print()
print('Сравнение лекторов:')
print(math_lecturer > prog_lecturer)
print(course_average_students(students_list, 'Основы программирования'))
print(course_average_lecturers(lecturers_list, 'Высшая математика'))