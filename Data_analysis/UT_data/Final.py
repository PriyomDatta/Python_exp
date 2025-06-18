import os
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from Final_1 import pros


# Global variables to store selected file paths
selected_file = ''
selected_folder = ''

# Function to open file dialog and store selected file path
def select_file(event, entry, file_index):
    global selected_file
    file_selected = filedialog.askopenfilename()
    if file_selected:
        entry.delete(0, tk.END)
        entry.insert(0, file_selected)
        if file_index == 1:
            selected_file = file_selected

# Function to open folder dialog and insert selected path into the entry
def select_folder(event, entry):
    global selected_folder
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        entry.delete(0, tk.END)
        entry.insert(0, folder_selected)
        selected_folder = folder_selected


# Function to concatenate text from both entries and show in a message box
def process_data():
    os.system('cls')
    pros(selected_file,selected_folder,1)
    pros(selected_file,selected_folder,2)
    root.destroy()
    #print(f"'{type(selected_file)}' is '{selected_file}'",)
    #print(type(selected_folder))

#Start of Impl.
# Create the main application window
root = tk.Tk()
root.title("Status sheet generator")
root.configure(bg="#e6e6fa") # Light lavender background

# Set window size and center it
window_width = 800
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width / 2) - (window_width / 2))
y_cordinate = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

# Font styles
title_font = ("Georgia", 16, "bold")
label_font = ("Helvetica", 10, "bold")
entry_font = ("Helvetica", 10, "bold")

# Title label inside the window
title_label = tk.Label(root, text="Status sheet generator", bg="#e6e6fa",font=title_font, fg="#333366")
title_label.pack(pady=(10, 10))

# Label and entry for Axivion report path
label1 = tk.Label(root, text="Enter path of Axivion report:", bg="#e6e6fa", font=label_font)
label1.pack(pady=(5, 5))
entry1 = tk.Entry(root, width=100, font=entry_font)
entry1.pack(pady=5)
entry1.bind("<Double-Button-1>", lambda event: select_file(event, entry1, 1))

# Label and entry for output file path
label2 = tk.Label(root, text="Enter the folder to save the report:", bg="#e6e6fa", font=label_font)
label2.pack(pady=(15, 5))
entry2 = tk.Entry(root, width=80, font=entry_font)
entry2.pack(pady=5)
entry2.bind("<Double-Button-1>", lambda event: select_folder(event, entry2))

# Create and place the utility button
button = tk.Button(root, text="Create Status Sheet", command=process_data,bg="#4CAF50", fg="white", font=label_font, padx=10, pady=5)
button.pack(pady=20)

# Footer label at bottom-right corner
footer_label = tk.Label(root, text="developed by dattapr",bg="#e6e6fa", font=("Helvetica", 8), fg="#666666")
footer_label.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)

# Run the application
root.mainloop()
