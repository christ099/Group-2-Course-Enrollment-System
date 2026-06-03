from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import json


def main_window():
    """Main function that creates and runs the Course Enrollment Application."""

    window = Tk()
    window.title("Course Enrollment System")
    window.geometry("1000x600")
    window.resizable(False, False)

    # ====================== DATABASE LOADING ======================
    # Load existing data from JSON file or initialize empty lists if file doesn't exist
    try:
        with open("database.json", "r") as file:
            data = json.load(file)

        students_database = data.get("students", [])
        courses_database = data.get("courses", [])
        enrollments_database = data.get("enrollments", [])

    except (FileNotFoundError, json.JSONDecodeError):
        # If file not found or corrupted, start with fresh databases
        students_database = []
        courses_database = []
        enrollments_database = []

    # ====================== SAVE FUNCTION ======================
    def save_data():
        """Save all current data (students, courses, enrollments) to database.json."""
        data_in_tuples = {
            "students": students_database,
            "courses": courses_database,
            "enrollments": enrollments_database
        }

        with open("database.json", "w") as files:
            json.dump(data_in_tuples, files, indent=4)

    # ====================== GUI STYLING ======================
    style = ttk.Style()
    style.theme_use("default")

    # Notebook (Tab) Styling
    style.configure("TNotebook", background="#F3F0F7", borderwidth=0)
    style.configure("TNotebook.Tab", font=("arial", 10, "bold"), padding=[20, 8],
                    background="#E0DBEC", foreground="#2e1a47")
    style.map("TNotebook.Tab",
              background=[("selected", "#2e1a47")],
              foreground=[("selected", "white")])

    notebook = ttk.Notebook(window)
    notebook.pack(expand=True, fill="both")

    # Create tabs
    tab1 = Frame(notebook)  # Students Tab
    tab2 = Frame(notebook)  # Courses Tab
    tab3 = Frame(notebook)  # Enrollments Tab

    notebook.add(tab1, text="STUDENTS")
    notebook.add(tab2, text="COURSES")
    notebook.add(tab3, text="ENROLLMENTS")

    # ====================== TAB 1: STUDENTS ======================

    # Delete selected student
    def delete():
        """Delete selected student from table and database."""
        selected = table_tab1.selection()

        if not selected:
            messagebox.showwarning("Warning", "Select a student first.")
            return

        confirm = messagebox.askyesno("Delete", "Are you sure you want to delete this record?")

        if confirm:
            for item in selected:
                values = table_tab1.item(item, 'values')
                # Remove from students_database list
                for student_delete in students_database[:]:
                    if student_delete[0] == values[0]:
                        students_database.remove(student_delete)

                table_tab1.delete(item)
                save_data()

            refresh_student_combo()
            messagebox.showinfo("Deleted", "Record deleted successfully.")
            clear()

    # Update student information
    def update():
        """Update selected student's information."""
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

        # Update in database list
        for student_update in students_database:
            if student_update[0] == old_values[0]:
                student_update[0] = entry_id.get()
                student_update[1] = entry_name.get()
                student_update[2] = entry_gmail.get()
                student_update[3] = combo_course.get()
                break

        save_data()
        table_tab1.item(selected, values=values)

        refresh_student_combo()
        messagebox.showinfo("Updated", "Student information updated.")
        clear()

    def clear():
        """Clear all input fields in Students tab."""
        entry_id.delete(0, tk.END)
        entry_name.delete(0, tk.END)
        entry_gmail.delete(0, tk.END)
        combo_course.set("Select")

    def record(event):
        """Load selected student data into input fields when clicked in table."""
        selected = table_tab1.selection()

        if selected:
            values = table_tab1.item(selected, 'values')
            entry_id.insert(0, values[0])
            entry_name.insert(0, values[1])
            entry_gmail.insert(0, values[2])
            combo_course.set(values[3])

    def insert_student():
        """Add a new student to the database and table."""
        student_id = entry_id.get()
        name = entry_name.get()
        email = entry_gmail.get()
        program = combo_course.get()

        if student_id == "" or name == "" or email == "" or program == "Select" or program == "":
            messagebox.showerror("Error", "Please complete all fields.")
            return

        # Check for duplicate Student ID
        for student_loop in students_database:
            if student_loop[0] == student_id:
                messagebox.showerror("Error", "Student ID already exists!")
                return

        data_insert = [student_id, name, email, program]
        students_database.append(data_insert)
        save_data()
        table_tab1.insert('', tk.END, values=data_insert)
        refresh_student_combo()
        messagebox.showinfo("Success", "Student added successfully!")
        clear()

    # ====================== STUDENTS TAB UI ======================
    Label(tab1, text="STUDENTS INFO", font=("Arial", 15, "bold"), pady=15, padx=90,
          bg="#2e1a47", fg="white").place(x=0, y=50)

    Label(tab1, text="Student ID: ", font=("Arial", 10, "bold")).place(x=10, y=150)
    Label(tab1, text="Full Name: ", font=("Arial", 10, "bold")).place(x=10, y=200)
    Label(tab1, text="Email: ", font=("Arial", 10, "bold")).place(x=10, y=250)
    Label(tab1, text="Program: ", font=("Arial", 10, "bold")).place(x=10, y=300)

    entry_id = Entry(tab1, font=("Arial", 10),width=30)
    entry_id.place(x=100, y=150)

    entry_name = Entry(tab1, font=("Arial", 10),width=30)
    entry_name.place(x=100, y=200)

    entry_gmail = Entry(tab1, font=("Arial", 10), width=30)
    entry_gmail.place(x=100, y=250)

    combo_course = ttk.Combobox(tab1,
                            values=["BSChE",
                                    "BSEE",
                                    "BSECE",
                                    "BSGE",
                                    "BSME",
                                    "BSIE",
                                    "BSIT"
                                    ],
                                state="readonly", font=("Times New Roman", 15, "bold"), width=15)
    combo_course.place(x=100, y=300)
    combo_course.set("Select")

    # Students Table
    table_frame_tab1 = Frame(tab1, bg="white", bd=2, relief="ridge")
    table_frame_tab1.place(x=330, y=20, width=645, height=380)

    columns = ("Student ID",
               "Full name",
               "Email",
               "Program")
    table_tab1 = ttk.Treeview(table_frame_tab1, columns=columns, show="headings")

    # Load existing students
    for student in students_database:
        table_tab1.insert('', tk.END, values=student)

    for col in columns:
        table_tab1.heading(col, text=col)
        table_tab1.column(col, width=80)

    # Adjust column widths
    table_tab1.column("Email", width=150)
    table_tab1.column("Full name", width=150)
    table_tab1.column("Student ID", width=80)
    table_tab1.column("Program", width=100)

    table_tab1.pack(fill="both", expand=True)
    table_tab1.bind("<<TreeviewSelect>>", record)

    # Buttons
    Button(tab1, text="ADD STUDENTS", font=("arial", 15, "bold"), command=insert_student,
           fg="white", bg="green").place(x=350, y=420)

    Button(tab1, text="UPDATE", font=("arial", 15, "bold"), command=update,
           fg="white", bg="blue").place(x=530, y=420)

    Button(tab1, text="DELETE", font=("arial", 15, "bold"), command=delete,
           fg="white", bg="red").place(x=635, y=420)

    Button(tab1, text="CLEAR", font=("arial", 15, "bold"), command=clear,
           fg="white", bg="orange").place(x=740, y=420)

    # ====================== TAB 2: COURSES ======================

    def delete_tab2():
        """Delete selected course."""
        selected = table_tab2.selection()
        if not selected:
            messagebox.showwarning("Warning", "Select a course first.")
            return

        if messagebox.askyesno("Delete", "Are you sure you want to delete this record?"):
            for item in selected:
                values = table_tab2.item(item, 'values')
                for course_loop in courses_database[:]:
                    if course_loop[0] == values[0]:
                        courses_database.remove(course_loop)
                table_tab2.delete(item)
                save_data()

            refresh_course_combo()
            messagebox.showinfo("Deleted", "Record deleted successfully.")
            clear_tab2()

    def update_tab2():
        """Update selected course information."""
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

        old_values = table_tab2.item(selected[0], 'values')

        # Update in database
        for course_list in courses_database:
            if course_list[0] == old_values[0]:
                course_list[0] = code
                course_list[1] = name
                course_list[2] = units
                course_list[3] = maxs
                break

        table_tab2.item(selected[0], values=(code, name, units, maxs, old_values[4]))
        save_data()
        refresh_course_combo()
        messagebox.showinfo("Updated", "Course information updated.")
        clear_tab2()

    def clear_tab2():
        """Clear course input fields."""
        Course_code_tab2.delete(0, tk.END)
        Course_name_tab2.delete(0, tk.END)
        spinbox_units_tab2.delete(0, "end")
        spinbox_maxs_tab2.delete(0, "end")

    def record_tab2(event):
        """Load selected course data into input fields."""
        selected = table_tab2.selection()
        if selected:
            values = table_tab2.item(selected[0], 'values')
            clear_tab2()
            Course_code_tab2.insert(0, values[0])
            Course_name_tab2.insert(0, values[1])
            spinbox_units_tab2.insert(0, values[2])
            spinbox_maxs_tab2.insert(0, values[3])

    def insert_course_tab2():
        """Add a new course."""
        code = Course_code_tab2.get()
        name = Course_name_tab2.get()
        units = spinbox_units_tab2.get()
        maxs = spinbox_maxs_tab2.get()

        if not code or not name or not units or not maxs:
            messagebox.showerror("Error", "Please complete all fields.")
            return

        for existing_course in courses_database:
            if existing_course[0] == code:
                messagebox.showerror("Error", "Course code already exists!")
                return

        datas = [code, name, units, maxs, "0"]
        courses_database.append(datas)
        save_data()
        table_tab2.insert('', tk.END, values=datas)
        refresh_course_combo()
        messagebox.showinfo("Success", "Course added successfully!")
        clear_tab2()

    # ====================== COURSES TAB UI ======================
    Label(tab2, text="COURSE INFO", font=("Arial", 15, "bold"), pady=15, padx=100,
          bg="#2e1a47", fg="white").place(x=0, y=50)

    Label(tab2, text="Course Code:", font=("Arial", 10, "bold")).place(x=10, y=150)
    Label(tab2, text="Course Name:", font=("Arial", 10, "bold")).place(x=10, y=200)
    Label(tab2, text="Units:", font=("Arial", 10, "bold")).place(x=10, y=250)
    Label(tab2, text="Maximum Students:", font=("Arial", 10, "bold")).place(x=10, y=300)

    Course_code_tab2 = Entry(tab2, font=("Arial", 10),width=28)
    Course_code_tab2.place(x=120, y=150)

    Course_name_tab2 = Entry(tab2, font=("Arial", 10),width=28)
    Course_name_tab2.place(x=120, y=200)

    spinbox_units_tab2 = Spinbox(tab2, from_=0, to=100, width=10, font=("Arial", 14))
    spinbox_units_tab2.place(x=150, y=240)

    spinbox_maxs_tab2 = Spinbox(tab2, from_=0, to=100, width=10, font=("Arial", 14))
    spinbox_maxs_tab2.place(x=150, y=300)

    # Courses Table
    table_frame_tab2 = Frame(tab2, bg="white", bd=2, relief="ridge")
    table_frame_tab2.place(x=330, y=20, width=645, height=380)

    columns = ("Course Code",
               "Course Name",
               "Units",
               "Max Capacity",
               "Enrolled")
    table_tab2 = ttk.Treeview(table_frame_tab2, columns=columns, show="headings")
    table_tab2.bind("<<TreeviewSelect>>", record_tab2)

    for course in courses_database:
        table_tab2.insert('', tk.END, values=course)

    for col in columns:
        table_tab2.heading(col, text=col)
        table_tab2.column(col, width=80)

    table_tab2.column("Course Code", width=150)
    table_tab2.column("Course Name", width=150)
    table_tab2.column("Units", width=80)
    table_tab2.column("Max Capacity", width=100)
    table_tab2.column("Enrolled", width=80)

    table_tab2.pack(fill="both", expand=True)

    # Course Buttons
    Button(tab2, text="ADD COURSE", font=("arial", 15, "bold"), command=insert_course_tab2,
           fg="white", bg="green").place(x=375, y=420)
    Button(tab2, text="UPDATE", font=("arial", 15, "bold"), command=update_tab2,
           fg="white", bg="blue").place(x=530, y=420)
    Button(tab2, text="DELETE", font=("arial", 15, "bold"), command=delete_tab2,
           fg="white", bg="red").place(x=635, y=420)
    Button(tab2, text="CLEAR", font=("arial", 15, "bold"), command=clear_tab2,
           fg="white", bg="orange").place(x=740, y=420)

    # ====================== TAB 3: ENROLLMENTS ======================

    def refresh_student_combo():
        """Refresh student dropdown with current students."""
        student_list = [f"{s[0]} - {s[1]}" for s in students_database]
        combo_students['values'] = student_list
        combo_students.set('')

    def refresh_course_combo():
        """Refresh course dropdown with current courses."""
        course_list = [f"{c[0]} - {c[1]}" for c in courses_database]
        combo_Courses_to_enroll['values'] = course_list
        combo_Courses_to_enroll.set('')

    def enroll_student():
        """Enroll a student in a course with validation."""
        student_selection = combo_students.get()
        course_selection = combo_Courses_to_enroll.get()

        if not student_selection or not course_selection:
            messagebox.showwarning("Warning", "Please select both a student and a course.")
            return

        student_id = student_selection.split(" - ")[0]
        course_code = course_selection.split(" - ")[0]

        # Get student and course details
        student_name = next((s[1] for s in students_database if s[0] == student_id), "")
        course_info = next((c for c in courses_database if c[0] == course_code), None)

        if not course_info:
            return

        course_name = course_info[1]
        max_capacity = int(course_info[3])

        # Check if already enrolled
        if any(e[0] == student_id and e[2] == course_code for e in enrollments_database):
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
        table_tab3.insert('', tk.END, values=enrollment_data)

        update_enrolled_count(course_code)
        messagebox.showinfo("Success", f"{student_name} successfully enrolled in {course_name}!")

        combo_students.set('')
        combo_Courses_to_enroll.set('')

    def update_enrolled_count(course_code):
        """Update the enrolled count for a course in both table and database."""
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
        """Drop (delete) a student's enrollment."""
        selected = table_tab3.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select an enrollment to delete.")
            return

        if messagebox.askyesno("Delete", "Are you sure you want to drop this enrollment?"):
            for item in selected:
                values = table_tab3.item(item, 'values')
                for enrollment in enrollments_database[:]:
                    if enrollment[0] == values[0] and enrollment[2] == values[2]:
                        enrollments_database.remove(enrollment)
                        update_enrolled_count(values[2])
                        break
                table_tab3.delete(item)
            save_data()
            messagebox.showinfo("Success", "Enrollment(s) dropped successfully!")

    # ====================== ENROLLMENTS TAB UI ======================
    Label(tab3, text="ENROLLED STUDENTS", font=("Arial", 15, "bold"), pady=15, padx=362,
          bg="#2e1a47", fg="white").place(x=20, y=143)

    Label(tab3, text="Students:", font=("Arial", 12, "bold")).place(x=10, y=50)
    Label(tab3, text="Course:", font=("Arial", 12, "bold")).place(x=400, y=50)

    combo_students = ttk.Combobox(tab3, width=30, font=("Arial", 10))
    combo_students.place(x=100, y=50)

    combo_Courses_to_enroll = ttk.Combobox(tab3, width=30, font=("Arial", 10))
    combo_Courses_to_enroll.place(x=470, y=50)

    # button to enroll the student
    Button(tab3, text="ENROLL", font=("arial", 12, "bold"), command=enroll_student,
           bg="green").place(x=700, y=45)
    # button to drop the student
    Button(tab3, text="DROP STUDENT", font=("arial", 12, "bold"), command=delete_enrollment,
           bg="red").place(x=800, y=45)

    # Enrollments Table
    table_frame_tab3 = Frame(tab3, bg="white", bd=2, relief="ridge")
    table_frame_tab3.place(x=20, y=200, width=950, height=350)

    columns = ("Student ID",
               "Student Name",
               "Course Code",
               "Course Name",
               "Status")
    table_tab3 = ttk.Treeview(table_frame_tab3, columns=columns, show="headings")

    for enrollment in enrollments_database:
        table_tab3.insert('', tk.END, values=enrollment)

    for col in columns:
        table_tab3.heading(col, text=col)
        if col in ["Student Name", "Course Name"]:
            table_tab3.column(col, width=200)
        else:
            table_tab3.column(col, width=120)

    table_tab3.pack(fill="both", expand=True)

    # Refresh dropdowns
    refresh_student_combo()
    refresh_course_combo()

    window.mainloop()
