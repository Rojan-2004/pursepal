
import tkinter as tk
import sqlite3

def setup_database():
    conn = sqlite3.connect("login_details.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            mobile_number TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def create_login_interface():
    def handle_login():
        mobile_number = mobile_entry.get()
        password = password_entry.get()

        # Save login details to the SQLite database
        conn = sqlite3.connect("login_details.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (mobile_number, password) VALUES (?, ?)", (mobile_number, password))
        conn.commit()
        conn.close()

        # Clear the entry fields after saving
        mobile_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)

    # Create the main window
    root = tk.Tk()
    root.title("Purse Pal")
    root.geometry("400x400")  # Set the size of the window

    # Define styles
    style = {
        "header": {"bg": "#8B0000", "fg": "white", "font": ("Arial", 16)},
        "label": {"font": ("Arial", 12)},
        "entry": {"font": ("Arial", 12), "width": 20},
        "button": {"font": ("Arial", 12), "width": 15, "bd": 1}
    }

    # Header Frame
    header_frame = tk.Frame(root, bg=style["header"]["bg"])
    header_frame.pack(fill=tk.X)

    # Welcome Label
    welcome_label = tk.Label(header_frame, text="Welcome", **style["header"])
    welcome_label.pack(pady=20)

    # Body Frame
    body_frame = tk.Frame(root)
    body_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

    # Mobile Number Entry
    mobile_label = tk.Label(body_frame, text="Mobile Number", **style["label"])
    mobile_label.grid(row=0, column=0, sticky="w", pady=2)
    mobile_entry = tk.Entry(body_frame, **style["entry"])
    mobile_entry.grid(row=0, column=1, pady=2)

    # Password Entry
    password_label = tk.Label(body_frame, text="Password/MPIN", **style["label"])
    password_label.grid(row=1, column=0, sticky="w", pady=2)
    password_entry = tk.Entry(body_frame, **style["entry"], show="*")
    password_entry.grid(row=1, column=1, pady=2)

    # Buttons Frame
    buttons_frame = tk.Frame(body_frame)
    buttons_frame.grid(row=2, columnspan=2, pady=20)

    # Login Button
    login_button = tk.Button(buttons_frame, text="LOGIN", **style["button"], relief=tk.RAISED, command=handle_login)
    login_button.pack(side=tk.LEFT, padx=5)

    # Forgot Password Button
    forgot_password_button = tk.Button(buttons_frame, text="Forgot Password?", **style["button"], relief=tk.RAISED)
    forgot_password_button.pack(side=tk.LEFT, padx=5)

    # Help and Support Link
    help_support_button = tk.Button(root, text="Help & Support", **style["button"], relief=tk.FLAT)
    help_support_button.pack(pady=(0, 10))

    # Register Link
    register_button = tk.Button(root, text="Register", **style["button"], relief=tk.FLAT)
    register_button.pack()

    root.mainloop()

# Setup the database before starting the interface
setup_database()
# Call the function to create and display the login interface
create_login_interface()