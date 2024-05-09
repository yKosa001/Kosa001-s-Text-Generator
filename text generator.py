import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def generate():
    text = entry.get()
    result_text.delete(1.0, tk.END)
    offset = int(offset_entry.get()) if offset_entry.get() else 0
    depth = int(depth_entry.get()) if depth_entry.get() else 1
    repeats = int(repeats_entry.get()) if repeats_entry.get() else 1
    for _ in range(repeats):
        for i in range(depth * 2 - 1):
            if i < depth:
                result_text.insert(tk.END, ' ' * (i + offset * i) + text + '\n')
            else:
                result_text.insert(tk.END, ' ' * ((depth * 2 - 2 - i) + offset * (depth * 2 - 2 - i)) + text + '\n')
            offset_result_text.insert(tk.END, str(offset * i) + '\n')

def copy():
    result_text.clipboard_clear()
    result_text.clipboard_append(result_text.get(1.0, tk.END))

def clear():
    result_text.delete(1.0, tk.END)
    offset_result_text.delete(1.0, tk.END)

def exit_app():
    root.destroy()

root = tk.Tk()
root.title("Kosa001's Text Generator")
root.geometry("700x540")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

entry_label = tk.Label(frame, text="Text:")
entry_label.grid(row=0, column=0, sticky="w")

entry = tk.Entry(frame)
entry.grid(row=0, column=1, padx=5, pady=5)

offset_label = tk.Label(frame, text="Offset:")
offset_label.grid(row=1, column=0, sticky="w")

offset_entry = tk.Entry(frame)
offset_entry.grid(row=1, column=1, padx=5, pady=5)

depth_label = tk.Label(frame, text="Depth:")
depth_label.grid(row=2, column=0, sticky="w")

depth_entry = tk.Entry(frame)
depth_entry.grid(row=2, column=1, padx=5, pady=5)

repeats_label = tk.Label(frame, text="Repetition:")
repeats_label.grid(row=3, column=0, sticky="w")

repeats_entry = tk.Entry(frame)
repeats_entry.grid(row=3, column=1, padx=5, pady=5)

copy_button = ttk.Button(frame, text="Copy", command=copy)
copy_button.grid(row=0, column=2, padx=5, pady=5)

generate_button = ttk.Button(frame, text="Generate", command=generate)
generate_button.grid(row=4, column=0, columnspan=3, pady=10)

clear_button = ttk.Button(frame, text="Clear", command=clear)
clear_button.grid(row=5, column=0, columnspan=3, pady=5)

exit_button = ttk.Button(frame, text="Exit", command=exit_app)
exit_button.grid(row=6, column=0, columnspan=3, pady=5)

result_text = tk.Text(frame, height=10, width=50)
result_text.grid(row=7, column=0, columnspan=3, pady=5)

offset_result_text = tk.Text(frame, height=10, width=15)
offset_result_text.grid(row=7, column=3, pady=5)

version_label = tk.Label(frame, text="Version: 2.0.0")
version_label.grid(row=8, column=0, sticky="w", pady=5)

creator_label = tk.Label(frame, text="Created By: Kosa001")
creator_label.grid(row=9, column=0, sticky="w", pady=5)

zdrojovy_kod = tk.Label(frame, text="Source Code: Source code is fully available for everyone.")
zdrojovy_kod.grid(row=10, column=0, sticky="w", pady=5)

root.mainloop()
