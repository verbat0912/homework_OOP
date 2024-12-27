from colorama import Fore

# Создать класс студент с необходимыми атрибутами
class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.study_courses = []
        self.grades = {}
        self.average_rating = float()
        self.number_stud = int()

    def rate_lecturer(self, lecturer, courses, grade_lecturer):
        if (isinstance(lecturer, Lecturer) and courses in lecturer.teach_courses
                and courses in self.study_courses and 0 <= grade_lecturer <= 10):
            if courses in lecturer.lecturer_grade:
                lecturer.lecturer_grade[courses] += [grade_lecturer]
            else:
                lecturer.lecturer_grade[courses] = [grade_lecturer]
        else:
            return 'ошибка'

    def __str__(self):
        count_grades = 0
        courses_in_progress = ", ".join(self.study_courses)
        fin_courses = ", ".join(self.finished_courses)
        for grade in self.grades:
            count_grades += len(self.grades[grade])
        self.average_rating = round(sum(map(sum, self.grades.values())) / count_grades, 1)
        print(f'Студент: {self.name}')
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'                
                f'Средняя оценка за домашние задания по курсу: {self.average_rating}\n'
                f'Курсы в процессе изучения: {courses_in_progress}\n'
                f'Завершенные курсы: {fin_courses}\n')

    def __eq__(self, other):
        return self.average_rating == other.average_rating

    def __gt__(self, other):
        return self.average_rating > other.average_rating

    def __ge__(self, other):
        return self.average_rating >= other.average_rating


# Создать класс ментор с необходимыми атрибутами
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.teach_courses = []



# Создаем подкласс Reviewer
class Reviewer(Mentor):
    def rate_students(self, student, courses, grade):
        if (isinstance(student, Student) and courses in student.study_courses
                and courses in self.teach_courses and 0 <= grade <= 10):
            if courses in student.grades:
                student.grades[courses] += [grade]
            else:
                student.grades[courses] = [grade]
        else:
            return 'ошибка'

    def __str__(self):
        print(f'Проверяющий: {self.name}')
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n')


# Создаем подкласс Lecturer
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecturer_grade = {}
        self.lecturer_average_rating = float()

    def __str__(self):
        count_lecturer_grade = 0
        for grade in self.lecturer_grade:
            count_lecturer_grade += len(self.lecturer_grade[grade])
        self.lecturer_average_rating = round((sum(map(sum,self.lecturer_grade.values()))
                                              / count_lecturer_grade),1)
        print(f'Лектор: {self.name}')
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'                
                f'Средняя оценка за лекции: {self.lecturer_average_rating}\n')

    def __eq__(self, other):
        return self.lecturer_average_rating == other.lecturer_average_rating

    def __gt__(self, other):
        return self.lecturer_average_rating > other.lecturer_average_rating

    def __ge__(self, other):
        return self.lecturer_average_rating >= other.lecturer_average_rating

# Создадим базу студентов, привяжем к изучаемым курсам,спиcки пройденных курсов
student1 = Student('Clark','Kent')
student1.study_courses += ['Python']
student1.finished_courses += ['Основы python', 'Системы исчисления']

student2 = Student('Bruce','Wayne')
student2.study_courses += ['JavaScr']
student2.finished_courses += ['Основы python', 'git']

student3 = Student('Barry','Allen')
student3.study_courses += ['git']
student3.finished_courses += ['Qbasic', '1c']

student4 = Student('Diana','Prince')
student4.study_courses += ['Python']
student4.finished_courses += ['Основы Java']

# Создадим базу Менторов и определим на каких курсах они преподают
# Менторы(Проверяющие)
Mentor1_rev = Reviewer('Alexandr','Luthor')
Mentor1_rev.teach_courses += ['Python']

Mentor2_rev = Reviewer('Джек Освальд','Уайт')
Mentor2_rev.teach_courses += ['JavaScr']

Mentor3_rev = Reviewer('Eobard','Thawne')
Mentor3_rev.teach_courses += ['git']

# Менторы (Лекторы)
Mentor4_lect = Lecturer('Tony','Stark')
Mentor4_lect.teach_courses += ['Python']

Mentor5_lect = Lecturer('Bruce','Banner')
Mentor5_lect.teach_courses += ['JavaScr']

Mentor6_lect = Lecturer('Steve','Rogers')
Mentor6_lect.teach_courses += ['git']

# Проверяющие выставляют оценки студентам за домашние задания

Mentor1_rev.rate_students(student1,'Python',8)
Mentor1_rev.rate_students(student1,'Python',10)
Mentor1_rev.rate_students(student1,'Python',9)
Mentor1_rev.rate_students(student4,'Python',7)
Mentor1_rev.rate_students(student4,'Python',8)
Mentor1_rev.rate_students(student4,'Python',5)

Mentor2_rev.rate_students(student2,'JavaScr',7)
Mentor2_rev.rate_students(student2,'JavaScr',10)
Mentor2_rev.rate_students(student2,'JavaScr',6)

Mentor3_rev.rate_students(student3,'git',9)
Mentor3_rev.rate_students(student3,'git',7)
Mentor3_rev.rate_students(student3,'git',10)

# выводим информацию о студентах
print(Fore.RED + "СТУДЕНТЫ:")
print(student1)
print()
print(student2)
print()
print(student3)
print()
print(student4)
print()

# Студенты выставляют оценки лекторам за лекции
student1.rate_lecturer(Mentor4_lect, 'Python', 10)
student1.rate_lecturer(Mentor4_lect, 'Python', 9)
student1.rate_lecturer(Mentor4_lect, 'Python', 9)

student2.rate_lecturer(Mentor5_lect, 'JavaScr', 9)
student2.rate_lecturer(Mentor5_lect, 'JavaScr', 8)
student2.rate_lecturer(Mentor5_lect, 'JavaScr', 10)

student3.rate_lecturer(Mentor6_lect, 'git', 8)
student3.rate_lecturer(Mentor6_lect, 'git', 7)
student3.rate_lecturer(Mentor6_lect, 'git', 9)

# Выводим информацию по Лекторам
print(Fore.GREEN + "Менторы(Лекторы):")
print(Mentor4_lect)
print()
print(Mentor5_lect)
print()
print(Mentor6_lect)
print()

# Выводим информацию по Проверяющим
print(Fore.BLUE + "Менторы(Проверяющие):")
print(Mentor1_rev)
print()
print(Mentor2_rev)
print()
print(Mentor3_rev)
print()
print(Fore.MAGENTA + "Сравнение средних оценок Студентов и Лекторов:")
print()
print(f'У стундента {str(student1.name)} средняя оценка за домашние задания '
      f'выше чем у студента {str(student4.name)}: {str(student1 > student2)}' )
print()
print(f'У лектора {str(Mentor5_lect.name)} средняя оценка за лекции '
      f'выше чем у лектора {str(Mentor6_lect.name)}: {str(Mentor5_lect > Mentor6_lect)}' )
print()
print()
print(Fore.WHITE + "Расчет средней оценки всех студентов за домашние задания в рамках одного курса:")
print()
# создаем список студетов
student_list = [student1, student2, student3, student4]
# создаем функцию расчета средней оценки за ДЗ всех студентов в рамках одного курса
def average_grade_students(student_list, course_name):
    all_student_count = 0
    sum_average_grade = 0
    for stud in student_list:
        if stud.study_courses == [course_name]:
           sum_average_grade += stud.average_rating
           all_student_count += 1
    average_grade_all = round(sum_average_grade / all_student_count, 1)
    return average_grade_all
print (Fore.CYAN + f'Средняя оценка за домашние задания всех студентов'
                   f' в рамках курса {'Python'}: '
                   f'{average_grade_students(student_list, 'Python')}')
print()
print()
print(Fore.WHITE + "Расчет средней оценки всех лекторов за лекции в рамках одного курса:")
print()
# создаем список Лекторов
lecturer_list = [Mentor4_lect, Mentor5_lect, Mentor6_lect]
# создаем функцию расчета средней оценки за лекции всех лекторов в рамках одного курса
def average_grade_lect(lecturer_list, course_name):
    all_lect_count = 0
    sum_average_grade = 0
    for lect in lecturer_list:
        if lect.teach_courses == [course_name]:
           sum_average_grade += lect.lecturer_average_rating
           all_lect_count += 1
    average_grade_all = round(sum_average_grade / all_lect_count, 1)
    return average_grade_all
print (Fore.YELLOW + f'Средняя оценка за лекции всех лекторов'
                   f' в рамках курса {'Python'}: '
                   f'{average_grade_lect(lecturer_list, 'Python')}')