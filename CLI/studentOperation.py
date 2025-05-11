# imported modules
from datetime import datetime as dt
import pickle
from rich.console import Console
from rich.table import Table
from rich.columns import Columns
from rich.panel import Panel
# imported modules


# read database
try:
    with open("ActiveStudent.db", "rb") as file:
        Students = pickle.load(file)
except:
    Students = []

try:
    with open("GraduatedStudent.db", "rb") as file:
        graduated_student = pickle.load(file)
except:
    graduated_student = []
# functions


# building rich text ready
console = Console()
# building rich text ready


def change_courses():
    result, chosen_one = find_student_logical()
    if not result:
        return
    while True:
        choice = input(
            "do you want to add course or remove a course or get out a/r/g :").upper()
        if choice == 'A':
            course = input("enter course name :")
            grade = input("enter grade for this course :")
            Students[chosen_one]["courses"].append(course)
            Students[chosen_one]["grades"].append(grade)
            console.print("course successfully added", style="bold yellow")
        elif choice == 'R':
            course = input("enter course name :")
            course_index = Students[chosen_one]["courses"].index(course)
            Students[chosen_one]["courses"].pop(course_index)
            Students[chosen_one]["grades"].pop(course_index)
            console.print("course successfully deleted", style="bold red")
        elif choice == 'G':
            break


def add_student():
    first_name = input("please enter first name :")
    last_name = input("please enter last name :")
    birthday = is_it_date()
    code_melli = validation_code(
        "enter code melli :", length=10, topic="code_melli")
    student_code = validation_code(
        "please enter student code :", topic="student_code", length=8)
    courses, grades = add_course_grade()
    student = {
        "first_name": first_name,
        "last_name": last_name,
        "birthday": birthday,
        "code_melli": code_melli,
        "student_code": student_code,
        "courses": courses,
        "grades": grades
    }
    Students.append(student)


def save_students():
    global Students
    with open("ActiveStudent.db", 'wb') as file:
        pickle.dump(Students, file)
    with open("GraduatedStudent.db", 'wb') as graduate_file:
        pickle.dump(graduated_student, graduate_file)
    print("students saved")


def del_student():
    result, student_index = find_student_logical()
    if result:
        answer = input(
            "do you want to move student to Graduated students y/n :").upper()
        if answer == 'Y':
            graduated_student.append(Students.pop(student_index))
            console.print("student has graduated congratulation",
                          style="bold green")
        elif answer == 'N':
            Students.pop(student_index)
            console.print("student has gone!", style="bold red")
    return


def show_students():
    for Student in Students:
        show_one_student(Student)
    show_graduated_students()


def find_student():
    result, student_index = find_student_logical()
    if result:
        show_one_student(Students[student_index])
    return


def find_student_logical():
    topic_length = 10
    topic = input(
        "do you want to Find student by code melli or Find by student code c/s :").upper()
    if topic == 'C':
        topic = "code_melli"
    elif topic == 'S':
        topic = "student_code"
        topic_length = 8
    while True:
        number = is_it_number(f"enter your {topic} :", topic_length)
        for student in Students:
            if str(number) == student[topic]:
                return [True, Students.index(student)]
        else:
            print("", end="\n")
            print("there is no this student", end="\n")
            return [False, 0]


def check_unique(number, topic):
    for student in Students:
        if number == student[topic]:
            print(f"there is a student with this {topic}!")
            return False
    else:
        return True


def add_course_grade():
    courses = []
    grades = []
    while True:
        choice = input("do you want to add courses y/n :").upper()
        if choice == 'N':
            break
        elif choice == 'Y':
            courses.append(input("enter course name :"))
            grades.append(input("enter grade :"))
    return [courses, grades]


def show_courses(student):
    content_panel = []
    if len(student["courses"]) != 0:
        print(f"all of {student['first_name']} {student['last_name']} courses")
        for course in student["courses"]:
            index = student["courses"].index(course)
            content_panel.append(
                Panel(f"[b]{course}[/b]\n[yellow]{student['grades'][index]}", expand=True))
        console.print(Columns(content_panel))
    else:
        return


def validation_code(message, length, topic):
    number = ""
    while len(number) != length and check_unique(number=number, topic=topic):
        number = str(is_it_number(message, length))
        if len(number) < length:
            for i in range(0, length - len(number)):
                number = '0' + number
    return number


def show_one_student(student):
    table_student = Table(
        title=f"{student['first_name']} {student['last_name']}", expand=True,
        caption="")
    table_student.add_column("first name", justify="center")
    table_student.add_column("last name", justify="center")
    table_student.add_column("birthday", justify="center")
    table_student.add_column("code melli", justify="center")
    table_student.add_column("student code", justify="center")
    table_student.add_row(student["first_name"], student["last_name"],
                          str(student["birthday"].strftime(
                              "%A %d. %B %Y")), student["code_melli"],
                          student["student_code"])
    console.print(table_student)
    print("", end="\n")
    show_courses(student)
    print("", end="\n")


def show_graduated_students():
    if len(graduated_student) != 0:
        console.print("graduated students", style="bold green")
    for student in graduated_student:
        show_one_student(student)


def is_it_date():
    while True:
        try:
            birthday = dt.strptime(
                input("enter birthday date like 'yy mm dd' :"), '%y %m %d')
            break
        except:
            pass
    return birthday


def is_it_number(message, length):
    while True:
        try:
            number = input(message)
            if len(number) == length:
                number = int(number)
                break
        except:
            pass
    return number


def prepare_string_length(string, length):
    result = ''
    if len(string) < length:
        for i in range(0, length - len(string)):
            result = '0' + result
        return result
    else:
        return string
