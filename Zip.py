import tkinter as tk
from tkinter import filedialog, messagebox
import zipfile
import os

def compress_file():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    # Create a new zip file
    zip_file_path = file_path + '.zip'
    try:
        with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            zip_file.write(file_path, os.path.basename(file_path))  # Add the file to the zip

        messagebox.showinfo("Success", f"File compressed to {zip_file_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def decompress_file():
    file_path = filedialog.askopenfilename()
    if not file_path or not file_path.endswith('.zip'):
        messagebox.showerror("Error", "Please select a valid zip file.")
        return

    # Create a directory to extract to
    extract_dir = os.path.splitext(file_path)[0]
    try:
        with zipfile.ZipFile(file_path, 'r') as zip_file:
            zip_file.extractall(extract_dir)  # Extract all files

        messagebox.showinfo("Success", f"File decompressed to {extract_dir}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Creating main window
root = tk.Tk()
root.title("Simple Compressor")

# Creating buttons
compress_button = tk.Button(root, text="Compress File", command=compress_file)
compress_button.pack(pady=20)

decompress_button = tk.Button(root, text="Decompress File", command=decompress_file)
decompress_button.pack(pady=20)

# Run the application
root.mainloop()
