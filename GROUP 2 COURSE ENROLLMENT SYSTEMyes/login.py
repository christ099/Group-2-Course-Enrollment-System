import main
import tkinter as tk
from tkinter import *
from tkinter import messagebox


window = tk.Tk()

window.title("Login")

# window.attributes('-fullscreen', True)
window.resizable(False, False)
window_width = 400
window_height = 500
# Calculate coordinates: (screen_dimension - window_dimension) / 2
center_x = int((window.winfo_screenwidth() - window_width) / 2)
center_y = int((window.winfo_screenheight() - window_height) / 4)
# Apply geometry: WidthxHeight+X+Y
window.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")


canvas =tk.Canvas(window, width=400, height=500, bg="white")
canvas.place(x=0, y=0)

purple_box = canvas.create_rectangle(
    20, 20,                    # top-left corner of box
    400-20,500-20,  # bottom-right corner of box
    fill="#2e1a47",
    outline="#2e1a47",
    width=4
)
purple_box = canvas.create_rectangle(
    50, 150,                    # top-left corner of box
    365-20,450-20,  # bottom-right corner of box
    fill="white",
    outline="white",
    width=4
)

canvas.create_oval(
    175, 30,   # top-left corner (x1, y1)
    225, 80,   # bottom-right corner (x2, y2)
    fill="black",
    outline="white",
    width=3
)


def toggle_password():
    if show_var.get():        # If checkbox is checked
        password.config(show="")      # Show password
    else:
        password.config(show="*")     # Hide password

def get_theinfo():
    usernames = user.get().strip()
    passwords = password.get().strip()

    # ←←← Change this with your actual login logic later
    if usernames == "4" and passwords == "4":
        window.destroy()
        main.main_window()
    else:
        messagebox.showerror("Failed", "Invalid username or password!\nPlease try again.")


label = tk.Label(window,
    text="USERNAME",
    font=("Arial", 10,"bold"),
    fg="black",
    bg="white",
                 )
label.place(x = 75, y = 200)

user = tk.Entry(
    window,
    width= 20,
    font=("Arial", 10),
)
user.place(x=75, y=225)


label = tk.Label(window,
    text="PASSWORD",
    font=("Arial", 10, "bold"),
    fg="black",
    bg="white",
    )
label.place(x = 75, y = 250)

password = tk.Entry(window, width=20, font=("Arial", 10), show="*")
password.place(x=75, y=275)

show_var = tk.BooleanVar()



checkbox = tk.Checkbutton(
    window,
    text="Show Password",
    variable=show_var,
    command=toggle_password,
    foreground="black",
    bg="white",
    activebackground="#2e1a47",
    font=("Arial", 8),

)
checkbox.place(x=225, y=275)

btn = tk.Button(window,
    text="LOGIN",
    command=get_theinfo,
    font=("Arial", 14, "bold"),
    bg="#7B2CBF",
    fg="#FFFFFF",
    activebackground="#9D4EDD",
    activeforeground="#FFFFFF",

)
btn.place(x = 150, y = 300)





window.mainloop()