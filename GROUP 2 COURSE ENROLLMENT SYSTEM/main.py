from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import json
import os


def main_window():
    window = Tk()
    window.title("Course enrollment")
    window.geometry("1000x600")
    window.resizable(False, False)



    # Load data when program starts
    try:
        with open("database.json", "r") as file:
            data = json.load(file)

        students_database = data.get("students", [])
        courses_database = data.get("courses", [])
        enrollments_database = data.get("enrollments", [])

    except (FileNotFoundError, json.JSONDecodeError):
        students_database = []
        courses_database = []
        enrollments_database = []

    # Rest of your Tkinter program...
    def save_data():
        data_in_tuples = {
            "students": students_database,
            "courses": courses_database,
            "enrollments": enrollments_database
        }

        with open("database.json", "w") as file:
            json.dump(data_in_tuples, file, indent=4)


    # notebook
    notebook = ttk.Notebook(window)
    tab1 = ttk.Frame(notebook)
    tab2 = ttk.Frame(notebook)
    tab3 = ttk.Frame(notebook)
    notebook.pack(expand=   True,fill="both")

    notebook.add(tab1, text="STUDENTS")
    notebook.add(tab2, text="COURSES")
    notebook.add(tab3, text="ENROLLMENTS")

    #  students are now done
    def delete():

        selected = table_tab1.selection()

        if not selected:
            messagebox.showwarning("Warning", "Select a student first.")
            return

        confirm = messagebox.askyesno("Delete", "Are you sure you want to delete this record?")

        if confirm:
            # Also remove from students list
            for item in selected:
                values = table_tab1.item(item, 'values')
                for student_delete in students_database[:]:
                    if student_delete[0] == values[0]:  # Match by Student ID
                        students_database.remove(student_delete)

                table_tab1.delete(item)
                save_data()

            # Refresh student combo in tab3
            refresh_student_combo()
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
        old_values = table_tab1.item(selected[0], 'values')

        for student_update in students_database:
            if student_update[0] == old_values[0]:
                student_update[0] = entry_id.get()
                student_update[1] = entry_name.get()
                student_update[2] = entry_gmail.get()
                student_update[3] = combo_course.get()
                break

        save_data()
        table_tab1.item(selected, values=values)


        # Refresh student combo in tab3
        refresh_student_combo()
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
        program = combo_course.get()

        if student_id == "" or name == "" or age == ""  or program == "":
            messagebox.showerror("Error", "Please complete all fields.")
            return
        for student_loop in students_database:
            if student_loop[0] == student_id:
                messagebox.showerror("Error", "Student ID already exists!")
                return

        data_insert = [student_id, name, age, program]
        students_database.append(data_insert)
        save_data()


        table_tab1.insert('', tk.END, values=data_insert)

        refresh_student_combo()
        messagebox.showinfo("Success", "Student enrolled successfully!")
        clear()




    style = ttk.Style()

    # Change Notebook Tab Font
    style.configure(
        "TNotebook.Tab",
        font=("Arial", 12, "bold"),
    )



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
    for student in students_database:
        table_tab1.insert('', tk.END, values=student)

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
            messagebox.showwarning("Warning", "Select a course first.")
            return

        confirm = messagebox.askyesno("Delete", "Are you sure you want to delete this record?")

        if confirm:
            # Also remove from courses list
            for item in selected:

                values = table_tab2.item(item, 'values')
                for course_loop in courses_database[:]:
                    if course_loop[0] == values[0]:  # Match by Course Code
                        courses_database.remove(course_loop)
                table_tab2.delete(item)
                save_data()

            # Refresh course combo in tab3
            refresh_course_combo()
            messagebox.showinfo("Deleted", "Record deleted successfully.")

            clear_tab2()


    def update_tab2():
        selected = table_tab2.selection()

        if not selected:
            messagebox.showwarning("Warning", "Select a course first.")
            return

        code = Course_code_tab2.get()
        name = Course_name_tab2.get()
        units = spinbox_units_tab2.get()
        maxs = spinbox_maxs_tab2.get()

        if not code or not name or not units or not maxs:
            messagebox.showerror("Error", "Please complete all fields.")
            return

        # 1. UPDATE LIST FIRST (IMPORTANT FIX)
        old_values = table_tab2.item(selected[0], 'values')

        for course_list in courses_database:
            if course_list[0] == old_values[0]:
                course_list[0] = code
                course_list[1] = name
                course_list[2] = units
                course_list[3] = maxs
                break
        current_values = table_tab2.item(selected[0], 'values')

        table_tab2.item(
            selected[0],
            values=(code, name, units, maxs, current_values[4]),
        )

        save_data()

        refresh_course_combo()
        messagebox.showinfo("Updated", "Course information updated.")
        clear_tab2()


    def clear_tab2():
        Course_code_tab2.delete(0, tk.END)
        Course_name_tab2.delete(0, tk.END)
        spinbox_units_tab2.delete(0, "end")
        spinbox_maxs_tab2.delete(0, "end")

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
        code = Course_code_tab2.get()
        coursed = Course_name_tab2.get()
        units = spinbox_units_tab2.get()
        maxs = spinbox_maxs_tab2.get()

        if code == "" or coursed == "" or units == "" or maxs == "":
            messagebox.showerror("Error", "Please complete all fields.")
            return

        for existing_course in courses_database:
            if existing_course[0] == code:
                messagebox.showerror("Error", "Course code already exists!")
                return

        datas = [code, coursed, units, maxs, "0"]
        courses_database.append(datas)
        save_data()

        table_tab2.insert('', tk.END, values=datas)

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
    for course in courses_database:
        table_tab2.insert('', tk.END, values=course)
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
        student_list = [f"{s[0]} - {s[1]}" for s in students_database]
        combo_students['values'] = student_list
        combo_students.set('')  # always reset selection

    def refresh_course_combo():
        course_list = [f"{c[0]} - {c[1]}" for c in courses_database]
        combo_Courses_to_enroll['values'] = course_list
        combo_Courses_to_enroll.set('')  # always reset selection



    def enroll_student():
        #enroll a student
        student_selection = combo_students.get()
        course_selection = combo_Courses_to_enroll.get()

        if not student_selection or not course_selection:
            messagebox.showwarning("Warning", "Please select both a student and a course.")
            return

        # Extract IDs from selections
        student_id = student_selection.split(" - ")[0]
        course_code = course_selection.split(" - ")[0]

        # Find student name
        student_name = ""
        for student in students_database:
            if student[0] == student_id:
                student_name = student[1]
                break

        # Find course name
        course_name = ""
        max_capacity = 0
        for course_find in courses_database:
            if course_find[0] == course_code:
                course_name = course_find[1]
                max_capacity = int(course_find[3])
                break

        # Check if already enrolled
        for enrollment_find in enrollments_database:
            if enrollment_find[0] == student_id and enrollment_find[2] == course_code:
                messagebox.showerror("Error", "Student is already enrolled in this course!")
                return

        # Check capacity
        enrolled_count = sum(1 for e in enrollments_database if e[2] == course_code)
        if enrolled_count >= max_capacity:
            messagebox.showerror("Error", f"Course has reached maximum capacity ({max_capacity} students)!")
            return

        # Add enrollment
        enrollment_data = [student_id, student_name, course_code, course_name, "Enrolled"]
        enrollments_database.append(enrollment_data)

        # Add to table
        table_tab3.insert('', tk.END, values=enrollment_data)

        # Update enrolled count in courses table
        update_enrolled_count(course_code)

        messagebox.showinfo("Success", f"{student_name} successfully enrolled in {course_name}!")

        # Clear selections
        combo_students.set('')
        combo_Courses_to_enroll.set('')

    # update the dode
    def update_enrolled_count(course_code):
        enrolled_count = sum(1 for e in enrollments_database if e[2] == course_code)

        for item in table_tab2.get_children():
            values = list(table_tab2.item(item, 'values'))

            if values[0] == course_code:
                values[4] = str(enrolled_count)
                table_tab2.item(item, values=values)

                for course in courses_database:
                    if course[0] == course_code:
                        course[4] = str(enrolled_count)
                        break

                save_data()
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
                for enrollment_loop2 in enrollments_database[:]:
                    if enrollment_loop2[0] == values[0] and enrollment_loop2[2] == values[2]:
                        enrollments_database.remove(enrollment_loop2)
                        # Update enrolled count for that course
                        update_enrolled_count(values[2])
                        break
                save_data()
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

    combo_Courses_to_enroll = ttk.Combobox(
        tab3,
        width=30,
        font=("Arial", 10)
    )
    combo_Courses_to_enroll.place(x=470, y=50)

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

    for enrollment in enrollments_database:
        table_tab3.insert('', tk.END, values=enrollment)

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