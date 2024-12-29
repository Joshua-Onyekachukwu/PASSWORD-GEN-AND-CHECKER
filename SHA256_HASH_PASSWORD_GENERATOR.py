import tkinter as tk
from tkinter import messagebox
import hashlib


# Function to generate SHA-256 hash
def generate_hash():
    password = entry.get()
    if not password:
        messagebox.showwarning("Input Error", "Please enter a password.")
        return

    # Generate SHA-256 hash
    sha_hash = hashlib.sha256(password.encode()).hexdigest()

    # Display the hash
    output_text.set(sha_hash)


# GUI setup
root = tk.Tk()
root.title("SHA-256 Password Generator")

# Input field
tk.Label(root, text="Enter Password:").pack(pady=5)
entry = tk.Entry(root, show="*", width=40)
entry.pack(pady=5)

# Button to generate hash
tk.Button(root, text="Generate SHA-256 Hash", command=generate_hash).pack(pady=10)

# Output field
output_text = tk.StringVar()
tk.Entry(root, textvariable=output_text, width=60, state='readonly').pack(pady=5)

# Run the GUI
root.mainloop()
