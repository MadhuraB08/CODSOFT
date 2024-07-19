import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate the password
def generate_password():
    try:
        length = int(entry.get())
        if length <= 0:
            raise ValueError("Length should be a positive number.")
        if length > 13:
            messagebox.showwarning("Warning", "Password length should not exceed 13 characters.")
            return
        all_characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(all_characters) for _ in range(length))
        password_display.config(text=password)
    except ValueError as ve:
        messagebox.showerror("Invalid input", str(ve))

# Setting up the main window
root = tk.Tk()
root.title("🔐 Password Generator")
root.geometry("600x300")
root.resizable(False, False)
root.config(bg="#2e2e2e")

# Title label
title_label = tk.Label(root, text="🔐 Password Generator", font=("Helvetica", 24, "bold"), fg="#ffcc00", bg="#2e2e2e")
title_label.pack(pady=20)

# Frame for user input
input_frame = tk.Frame(root, bg="#4d4d4d", bd=2, relief="sunken")
input_frame.pack(pady=20, padx=20, fill="x")

# Label and entry for password length
length_label = tk.Label(input_frame, text="Password Length:", font=("Helvetica", 16), fg="#ffffff", bg="#4d4d4d")
length_label.grid(row=0, column=0, padx=10, pady=10)
entry = tk.Entry(input_frame, width=5, font=("Helvetica", 16))
entry.grid(row=0, column=1, padx=10, pady=10)

# Button to generate password
generate_button = tk.Button(input_frame, text="Generate", font=("Helvetica", 16), bg="#ffcc00", fg="#000000", command=generate_password)
generate_button.grid(row=0, column=2, padx=10, pady=10)

# Label to display generated password
password_display = tk.Label(root, text="", font=("Helvetica", 18, "bold"), fg="#00ff00", bg="#2e2e2e")
password_display.pack(pady=20)

# Run the application
root.mainloop()
