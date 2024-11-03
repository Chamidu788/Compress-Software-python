# Zip priject Python

**Description**: මෙහිදී ඔබගේ Python කේතය EXE ගොනුවක් බවට පත් කිරීමට අදාළ තොරතුරු සහ විධාන තිබේ.

## Requirements

- Python 3.x
- `pyinstaller` (EXE එකක් සාදන්න)

### Installation

1. **Python ස්ථාපනය කරන්න**: [Python Downloads](https://www.python.org/downloads/)

2. (` ``` import tkinter as tk
from tkinter import filedialog, messagebox
import zipfile
import os

def compress_file():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
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
    extract_dir = os.path.splitext(file_path)[0]
    try:
        with zipfile.ZipFile(file_path, 'r') as zip_file:
            zip_file.extractall(extract_dir)  # Extract all files
        messagebox.showinfo("Success", f"File decompressed to {extract_dir}")
    except Exception as e:
        messagebox.showerror("Error", str(e))
root = tk.Tk()
root.title("Simple Compressor")
compress_button = tk.Button(root, text="Compress File", command=compress_file)
compress_button.pack(pady=20)

decompress_button = tk.Button(root, text="Decompress File", command=decompress_file)
decompress_button.pack(pady=20)
root.mainloop() `)

3. **pyinstaller ස්ථාපනය කරන්න**:
   ```bash
   pip install pyinstaller
   ```

## Creating the Executable

1. **පළමුව** ඔබගේ Python කේතය `.py` ගොනුවක් ලෙස සුරකින්න. (උදාහරණයක් ලෙස, `your_script.py`)


3. **පසුබැසීමේ අවශ්‍ය විධානය ක්‍රියාත්මක කරන්න**:
   ```bash
   pyinstaller --onefile your_script.py
   ```

4. **EXE ගොනුව සොයාගන්න**: `dist` ෆොල්ඩරය තුළ ඔබට EXE ගොනුව සොයාගන්න පුළුවන්.

## Download Executable

**Download the EXE file** from the [dts folder](./dts/).

[Download EXE](./dts/Zip.exe)

## YouTube Video

**Watch the tutorial on YouTube**: [Your Video Title](https://www.youtube.com/your_video_link)
