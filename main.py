import tkinter as tk

# Function to show the login form
def show_login_form():
    # Hide the registration widgets
    username_label.pack_forget()
    username_entry.pack_forget()
    password_label.pack_forget()
    password_entry.pack_forget()
    register_button.pack_forget()

    # Show the login widgets
    login_label.pack()
    login_username_entry.pack()
    login_password_label.pack()
    login_password_entry.pack()
    login_button.pack()


# Function to register a new user
def register():
    username = username_entry.get()
    password = password_entry.get()

    with open("user_db.txt", "a") as file:
        file.write(f"{username}:{password}\n")

    result_label.config(text="Registration successful!")

    # Show the login form after registration
    show_login_form()

# Function to log in a user
def login():
    username = login_username_entry.get()
    password = login_password_entry.get()

    with open("user_db.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        stored_username, stored_password = line.strip().split(":")
        if username == stored_username and password == stored_password:
            result_label.config(text="Login successful!")

            return

    result_label.config(text="Login failed. Please check your username and password.")

# Create the main window
window = tk.Tk()
window.geometry("200x200")
window.title("Register and Login System")

# Create and configure widgets
username_label = tk.Label(window, text="Username:")
password_label = tk.Label(window, text="Password:")
username_entry = tk.Entry(window)
password_entry = tk.Entry(window, show="*")  # Hide password
register_button = tk.Button(window, text="Register", command=register)
login_label = tk.Label(window, text="Login")
login_username_entry = tk.Entry(window)
login_password_label = tk.Label(window, text="Password:")
login_password_entry = tk.Entry(window, show="*")
login_button = tk.Button(window, text="Login", command=login)
result_label = tk.Label(window, text="", fg="red")

# Place widgets in the window
username_label.pack()
username_entry.pack()
password_label.pack()
password_entry.pack()
register_button.pack()
result_label.pack()

# Main loop
window.mainloop()
