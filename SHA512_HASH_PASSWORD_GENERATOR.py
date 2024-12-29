import tkinter as tk
from tkinter import messagebox
import hashlib


# Function to generate SHA-512 hash
def generate_sha512_hash():
    password = entry.get()
    if not password:
        messagebox.showwarning("Input Error", "Please enter a password.")
        return

    # Generate SHA-512 hash
    sha512_hash = hashlib.sha512(password.encode()).hexdigest()

    # Display the hash
    output_text.set(sha512_hash)


# GUI setup
root = tk.Tk()
root.title("SHA-512 Password Hash Generator")

# Input field for password
tk.Label(root, text="Enter Password:").pack(pady=5)
entry = tk.Entry(root, show="*", width=40)
entry.pack(pady=5)

# Button to generate the hash
tk.Button(root, text="Generate SHA-512 Hash", command=generate_sha512_hash).pack(pady=10)

# Output field for the hash result
output_text = tk.StringVar()
tk.Entry(root, textvariable=output_text, width=80, state='readonly').pack(pady=5)

# Run the GUI loop
root.mainloop()
