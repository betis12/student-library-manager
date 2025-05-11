import studentOperation as So
from rich.console import Console

console = Console()

while True:
    console.print("--------'A' to add student --------", style="bold #98fc03")
    console.print("--------'F' to find student --------", style="bold #98fc03")
    console.print("--------'D' to delete student --------",
                  style="bold #98fc03")
    console.print(
        "--------'G' to change one student courses --------", style="bold #98fc03")
    console.print("--------'L' to list all students --------",
                  style="bold #98fc03")
    console.print("--------'S' to save students --------",
                  style="bold #98fc03")
    console.print("--------'Q' to exit --------   :", style="bold #98fc03")
    choice = input("").upper()
    if choice == 'A':
        So.add_student()
    elif choice == 'D':
        So.del_student()
    elif choice == 'F':
        So.find_student()
    elif choice == 'L':
        So.show_students()
    elif choice == 'S':
        So.save_students()
    elif choice == 'G':
        So.change_courses()
    elif choice == 'Q':
        break
