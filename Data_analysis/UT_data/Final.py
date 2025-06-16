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
    #print(f"'{type(selected_file)}' is '{selected_file}'",)
    #print(type(selected_folder))

# Create the main application window
root = tk.Tk()
root.title("Unit Test utility")

# Label for the first text entry
label1 = tk.Label(root, text="Enter path of Axivion report ")
label1.pack(pady=(10, 0))

# First text entry
entry1 = tk.Entry(root, width=60)
entry1.pack(pady=5)
entry1.bind("<Double-Button-1>", lambda event: select_file(event, entry1, 1))

# Label for the first text entry
label1 = tk.Label(root, text="Enter the file where you want to save report ")
label1.pack(pady=(10, 0))

# Create and place the second text entry
entry2 = tk.Entry(root, width=60)
entry2.pack(pady=10)
entry2.bind("<Double-Button-1>", lambda event: select_folder(event, entry2))


# Create and place the utility button
button = tk.Button(root, text="Create status sheet", command=process_data)
button.pack(pady=20)

# Run the application
root.mainloop()