from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox

window = Tk()
window.title("Course enrollment")
window.geometry("1000x600")
window.resizable(False, False)

students = []
courses = []
enrollments = []

#  students are now done

def delete():
    selected = table_tab1.selection()

    if not selected:
        messagebox.showwarning("Warning", "Select a student first.")
        return

    confirm = messagebox.askyesno("Delete", "Are you sure you want to delete this record?")

    if confirm:
        table_tab1.delete(selected)
        messagebox.showinfo("Deleted", "Record deleted successfully.")
        clear()


def update():

    selected = table_tab1.selection()

    if not selected:
        messagebox.showwarning("Warning", "Select a student first.")
        return

    values = (
        entry_id.get(),
        entry_name.get(),
        entry_gmail.get(),
        combo_course.get(),
    )


    table_tab1.item(selected, values=values)

    messagebox.showinfo("Updated", "Student information updated.")

    clear()

# update students

def clear():
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_gmail.delete(0, tk.END)
    combo_course.set("Select")



def record(event):
    selected = table_tab1.selection()

    if selected:
        values = table_tab1.item(selected, 'values')

        clear()

        entry_id.insert(0, values[0])
        entry_name.insert(0, values[1])
        entry_gmail.insert(0, values[2])
        combo_course.set(values[3])



def insert_student():
    student_id = entry_id.get()
    name = entry_name.get()
    age = entry_gmail.get()
    course = combo_course.get()

    if student_id == "" or name == "" or age == ""  or course == "" or course == "":
        messagebox.showerror("Error", "Please complete all fields.")
        return
    for student in students:
        if student[0] == student_id:
            messagebox.showerror("Error", "Student ID already exists!")
            return

    data = [student_id, name, age, course]
    students.append(data)

    table_tab1.insert('', tk.END, values=data)

    refresh_student_combo()
    messagebox.showinfo("Success", "Student enrolled successfully!")
    clear()




style = ttk.Style()

# Change Notebook Tab Font
style.configure(
    "TNotebook.Tab",
    font=("Arial", 12, "bold"),
)

notebook = ttk.Notebook(window)
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)
notebook.pack(expand=   True,fill="both")

notebook.add(tab1, text="STUDENTS")
notebook.add(tab2, text="COURSES")
notebook.add(tab3, text="ENROLLMENTS")

Label(tab1,text="STUDENTS INFO",font=("Arial", 12, "bold")).place(x=10, y=50)
Label(tab1,text="Student ID: ",font=("Arial", 10, "bold")).place(x=10, y=150)
Label(tab1,text="Full Name: ",font=("Arial", 10, "bold")).place(x=10, y=200)
Label(tab1,text="Email: ",font=("Arial", 10, "bold")).place(x=10, y=250)
Label(tab1,text="Program: ",font=("Arial", 10, "bold")).place(x=10, y=300)



entry_id = Entry(tab1, font=("Arial", 10))
entry_id.place(x=100, y=150)
entry_name = Entry(tab1, font=("Arial", 10))
entry_name.place(x=100, y=200)
entry_gmail = Entry(tab1, font=("Arial", 10))
entry_gmail.place(x=100, y=250)


style = ttk.Style()

style.configure(
    "TCombobox",
    font=("Arial", 14),
    padding=8
)

combo_course = ttk.Combobox(
    tab1,
    values=[
    "BSChE",
     "BSEE",
     "BSECE",
     "BSGE",
     "BSME",
     "BSIE",
     "BSIT",
    ],
    state="readonly",
    font=("Times New Roman", 13, "bold"),
    width=15,
)
combo_course.place(x=100, y=300)
combo_course.option_add("*TCombobox*Listbox.font", ("Courier New", 10))



table_frame_tab1 = Frame(tab1, bg="white", bd=2, relief="ridge")
table_frame_tab1.place(x=330, y=20, width=645, height=380)

style = ttk.Style()
style.theme_use("default")

style.configure(
    "Treeview",
    font=("Arial", 10),
    rowheight=28,

)

style.configure(
    "Treeview.Heading",
    font=("Arial", 10, "bold"),
)

columns = (
    "Student ID",
    "Full name",
    "Email",
    "Program",

)

table_tab1 = ttk.Treeview(table_frame_tab1, columns=columns, show="headings")

for col in columns:
    table_tab1.heading(col, text=col)
    table_tab1.column(col, width=80)

# Custom Widths
table_tab1.column("Email", width=150)
table_tab1.column("Full name", width=150)
table_tab1.column("Student ID", width=50)
table_tab1.column("Program", width=5,)

table_tab1.pack(fill="both", expand=True)
table_tab1.bind("<<TreeviewSelect>>",record)


Button(tab1,
       text="ADD STUDENTS",
       font=("arial",15,"bold"),
       command=insert_student
       ).place(x=80, y=420)
Button(tab1,
       text="UPDATE",
       font=("arial",15,"bold"),
       command=update
       ).place(x=270, y=420)
Button(tab1,
       text="DELETE",
       font=("arial",15,"bold"),
       command=delete
       ).place(x=390, y=420)
Button(tab1,
       text="CLEAR",
       font=("arial",15,"bold"),
       command=clear
       ).place(x=500, y=420)

# tab2

def delete_tab2():
    selected = table_tab2.selection()

    if not selected:
        messagebox.showwarning("Warning", "Select a student first.")
        return

    confirm = messagebox.askyesno("Delete", "Are you sure you want to delete this record?")

    if confirm:
        table_tab2.delete(selected)
        messagebox.showinfo("Deleted", "Record deleted successfully.")
        clear_tab2()


def update_tab2():

    selected = table_tab2.selection()

    if not selected:
        messagebox.showwarning("Warning", "Select a student first.")
        return

    values = (
    Course_code_tab2.get(),
    Course_name_tab2.get(),
    spinbox_units_tab2.get(),
    spinbox_maxs_tab2.get(),
    )


    table_tab2.item(selected, values=values)

    messagebox.showinfo("Updated", "Student information updated.")

    clear_tab2()

# update students

def clear_tab2():
    Course_code_tab2.delete(0, tk.END)
    Course_name_tab2.delete(0, tk.END)
    spinbox_units_tab2.delete(0, tk.END)
    spinbox_maxs_tab2.delete(0, tk.END)


def record_tab2(event):
    selected = table_tab2.selection()

    if selected:
        values = table_tab2.item(selected[0], 'values')

        clear_tab2()

        Course_code_tab2.insert(0, values[0])
        Course_name_tab2.insert(0, values[1])
        spinbox_units_tab2.delete(0, "end")
        spinbox_units_tab2.insert(0, values[2])
        spinbox_maxs_tab2.delete(0, "end")
        spinbox_maxs_tab2.insert(0, values[3])


def insert_course_tab2():
    code=Course_code_tab2.get()
    course=Course_name_tab2.get()
    units=spinbox_units_tab2.get()
    maxs=spinbox_maxs_tab2.get()

    if code == "" or course == "" or units == ""  or maxs== "":
        messagebox.showerror("Error", "Please complete all fields.")
        return
    for existing_course in courses:
        if existing_course[0] == code:
            messagebox.showerror("Error", "Course code already exists!")
            return

    data = [code, course, units, maxs]
    courses.append(data)

    table_tab2.insert('', tk.END, values=data)


    refresh_course_combo()
    messagebox.showinfo("Success", "Course added successfully!")
    clear_tab2()
# tab 2

Label(tab2,text="COURSE INFO",font=("Arial", 12, "bold")).place(x=10, y=50)
Label(tab2,text="Course Code:",font=("Arial", 10, "bold")).place(x=10, y=150)
Label(tab2,text="Course Name:",font=("Arial", 10, "bold")).place(x=10, y=200)
Label(tab2,text="Units:",font=("Arial", 10, "bold")).place(x=10, y=250)
Label(tab2,text="Maximum Students:",font=("Arial", 10, "bold")).place(x=10, y=300)


Course_code_tab2 = Entry(tab2, font=("Arial", 10))
Course_code_tab2.place(x=120, y=150)
Course_name_tab2 = Entry(tab2, font=("Arial", 10))
Course_name_tab2.place(x=120, y=200)

spinbox_units_tab2 = Spinbox(
    tab2,
    from_=0,
    to=100,
    width=10,
    font=("Arial", 12)
)
spinbox_units_tab2.place(x=80, y=250)
spinbox_maxs_tab2 = Spinbox(
    tab2,
    from_=0,
    to=100,
    width=10,
    font=("Arial", 12)
)

spinbox_maxs_tab2.place(x=150, y=300)


table_frame_tab2 = Frame(tab2, bg="white", bd=2, relief="ridge")
table_frame_tab2.place(x=330, y=20, width=645, height=380)

style = ttk.Style()
style.theme_use("default")

style.configure(
    "Treeview",
    font=("Arial", 10),
    rowheight=28
)

style.configure(
    "Treeview.Heading",
    font=("Arial", 10, "bold")
)

columns = (
    "Course Code",
    "Course Name",
    "Units",
    "Max Capacity",
    "Enrolled",


)

table_tab2 = ttk.Treeview(table_frame_tab2, columns=columns, show="headings")
table_tab2.bind("<<TreeviewSelect>>",record_tab2)

for col in columns:
    table_tab2.heading(col, text=col)
    table_tab2.column(col, width=80)

# Custom Widths
table_tab2.column("Course Code", width=150)
table_tab2.column("Course Name", width=150)
table_tab2.column("Units", width=24)
table_tab2.column("Max Capacity", width=50,)
table_tab2.column("Enrolled", width=50,)

table_tab2.pack(fill="both", expand=True)

Button(tab2,
       text="ADD COURSE",
       font=("arial",15,"bold"),
       command=insert_course_tab2
       ).place(x=80, y=420)
Button(tab2,
       text="UPDATE",
       font=("arial",15,"bold"),
       command=update_tab2
       ).place(x=270, y=420)
Button(tab2,
       text="DELETE",
       font=("arial",15,"bold"),
       command=delete_tab2
       ).place(x=390, y=420)
Button(tab2,
       text="CLEAR",
       font=("arial",15,"bold"),
       command=clear_tab2
       ).place(x=500, y=420)


#tab3



def refresh_student_combo():
    # refresh tghe student combo with idk
    student_list = [f"{s[0]} - {s[1]}" for s in students]
    combo_students['values'] = student_list
    if student_list:
        combo_students.set('')
    else:
        combo_students.set('')


def refresh_course_combo():
    #  refresh teh course bombo
    course_list = [f"{c[0]} - {c[1]}" for c in courses]
    combo_Courses['values'] = course_list
    if course_list:
        combo_Courses.set('')
    else:
        combo_Courses.set('')


def enroll_student():
    #enroll a student
    student_selection = combo_students.get()
    course_selection = combo_Courses.get()

    if not student_selection or not course_selection:
        messagebox.showwarning("Warning", "Please select both a student and a course.")
        return

    # Extract IDs from selections
    student_id = student_selection.split(" - ")[0]
    course_code = course_selection.split(" - ")[0]

    # Find student name
    student_name = ""
    for student in students:
        if student[0] == student_id:
            student_name = student[1]
            break

    # Find course name
    course_name = ""
    max_capacity = 0
    for course in courses:
        if course[0] == course_code:
            course_name = course[1]
            max_capacity = int(course[3])
            break

    # Check if already enrolled
    for enrollment in enrollments:
        if enrollment[0] == student_id and enrollment[2] == course_code:
            messagebox.showerror("Error", "Student is already enrolled in this course!")
            return

    # Check capacity
    enrolled_count = sum(1 for e in enrollments if e[2] == course_code)
    if enrolled_count >= max_capacity:
        messagebox.showerror("Error", f"Course has reached maximum capacity ({max_capacity} students)!")
        return

    # Add enrollment
    enrollment_data = [student_id, student_name, course_code, course_name, "Enrolled"]
    enrollments.append(enrollment_data)

    # Add to table
    table_tab3.insert('', tk.END, values=enrollment_data)

    # Update enrolled count in courses table
    update_enrolled_count(course_code)

    messagebox.showinfo("Success", f"{student_name} successfully enrolled in {course_name}!")

    # Clear selections
    combo_students.set('')
    combo_Courses.set('')

# update the dode
def update_enrolled_count(course_code):

    enrolled_count = sum(1 for e in enrollments if e[2] == course_code)

    # Find and update the course in the treeview
    for item in table_tab2.get_children():
        values = table_tab2.item(item, 'values')
        if values[0] == course_code:
            # Update the Enrolled column (index 4)
            new_values = list(values)
            new_values[3] = str(enrolled_count)
            table_tab2.item(item, values=new_values)
            break


def delete_enrollment():
    # delete a table
    selected = table_tab3.selection()

    if not selected:
        messagebox.showwarning("Warning", "Please select an enrollment to delete.")
        return

    confirm = messagebox.askyesno("Delete", "Are you sure you want to delete this enrollment?")

    if confirm:
        for item in selected:
            values = table_tab3.item(item, 'values')
            # Remove from enrollments list
            for enrollment in enrollments[:]:
                if enrollment[0] == values[0] and enrollment[2] == values[2]:
                    enrollments.remove(enrollment)
                    # Update enrolled count for that course
                    update_enrolled_count(values[2])
                    break
            table_tab3.delete(item)

        messagebox.showinfo("Success", "Enrollment(s) deleted successfully!")


Label(tab3, text="Students:", font=("Arial", 12, "bold")).place(x=10, y=50)
Label(tab3, text="Course:", font=("Arial", 12, "bold")).place(x=400, y=50)
Label(tab3, text="All Enrollments", font=("Arial", 12, "bold")).place(x=10, y=150)

combo_students = ttk.Combobox(
    tab3,
    width=30,
    font=("Arial", 10)
)
combo_students.place(x=100, y=50)

combo_Courses = ttk.Combobox(
    tab3,
    width=30,
    font=("Arial", 10)
)
combo_Courses.place(x=470, y=50)

Button(tab3,
       text="Enroll",
       font=("arial", 12, "bold"),
       command=enroll_student
       ).place(x=700, y=45)

Button(tab3,
       text="Delete Enrollment",
       font=("arial", 12, "bold"),
       command=delete_enrollment,
       ).place(x=800, y=45)

table_frame_tab3 = Frame(tab3, bg="white", bd=2, relief="ridge")
table_frame_tab3.place(x=20, y=200, width=950, height=350)

style = ttk.Style()
style.theme_use("default")

style.configure(
    "Treeview",
    font=("Arial", 10),
    rowheight=28
)

style.configure(
    "Treeview.Heading",
    font=("Arial", 10, "bold")
)

columns = (
    "Student ID",
    "Student Name",
    "Course Code",
    "Course Name",
    "Status"
)

table_tab3 = ttk.Treeview(table_frame_tab3, columns=columns, show="headings")

for col in columns:
    table_tab3.heading(col, text=col)
    if col == "Student Name" or col == "Course Name":
        table_tab3.column(col, width=200)
    else:
        table_tab3.column(col, width=120)

table_tab3.pack(fill="both", expand=True)


refresh_student_combo()
refresh_course_combo()

window.mainloop()