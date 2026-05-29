import main
import tkinter as tk

from tkinter import messagebox

window = tk.Tk()

window.title("Login")
window.geometry("600x300")
window.resizable(False, False)

def toggle_password():
    if show_var.get():        # If checkbox is checked
        password.config(show="")      # Show password
    else:
        password.config(show="*")     # Hide password

def hi():
    usernames = user.get().strip()
    passwords = password.get().strip()

    # ←←← Change this with your actual login logic later
    if usernames == "admin" and passwords == "123":
        messagebox.showinfo("Success", "Login Successful!")
        window.destroy()
        main.main_window()


    else:
        messagebox.showerror("Failed", "Invalid username or password!\nPlease try again.")
        # Login window stays open for retry

label = tk.Label(window,
    text="USERNAME",
    font=("Arial", 10))
label.place(x = 30, y = 50)

user = tk.Entry(
    window,
    width= 20,
    font=("Arial", 20)
)
user.place(x = 130, y = 40)


label = tk.Label(window,
    text="PASSWORD",
    font=("Arial", 10),
    )
label.place(x = 30, y = 90)

password = tk.Entry(window, width=20, font=("Arial", 20), show="*")
password.place(x=130, y=85)

show_var = tk.BooleanVar()

checkbox = tk.Checkbutton(
    window,
    text="Show Password",
    variable=show_var,
    command=toggle_password,
    bg="white",
    activebackground="white",
    font=("Arial", 10)
)
checkbox.place(x=440, y=91)

btn = tk.Button(window,
    text="LOGIN",
    command=hi,
    font=("Arial", 20, "bold"),
    bg = "#7f00ff",
    fg = "black",
    activebackground="#7f00ff",
    activeforeground="black",
)
btn.place(x = 250, y = 150)





window.mainloop()