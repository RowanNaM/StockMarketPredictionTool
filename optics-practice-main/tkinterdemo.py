import gc
import sys
import tkinter as tk
import numpy as np
import pandas as pd
from tkinter import ttk
    # themed tkinter import as ttk

def save_to_file(button_text, selected_option):
    with open("OUTPUTFILE.xlsx", "a") as file:
        # NEW INFO --> "f" string is a formatted string literal which can embed expressions inside string literals in python
        file.write(f"Button '{button_text}' clicked! Selected Option: {selected_option}\n")

def on_button_click(button_text, selected_option):
    print(f"Button '{button_text}' clicked! Selected Option: {selected_option}")
    # When button is clicked, print that the given button was clicked in the console
    save_to_file(button_text, selected_option)
    # Calls the function defined below

def text_data_analysis(text_entry):
    input_file_path = "/Users/romax/Desktop/Programming Projects/optics-practice-main/INPUTFILE.xlsx"
    # try multiple different engines to run the program (WHY IS MacOS WACK)
    try:
        data_frame = pd.read_excel(input_file_path, engine="xlrd")
    except Exception as e1:
        try: 
            # Try reading with 'openpyxl' engine if 'xlrd' fails
            data_frame = pd.read_excel(input_file_path, engine='openpyxl')
        except Exception as e2:
            # Print an error message if both engines fail
            print(f"Error reading Excel file: {e1}\n{e2}")
            return
    root = root_content()
    entered_text = text_entry.get()
    # TODO --> "user_input" must contain the parameter for the query meaning that there must BE A PARAMETER to query
    data_frame.query(f'name.str.contains("{entered_text}")', engine="python")

def perform_search(text_entry, selected_option):
    entered_text = text_entry.get()
    text_data_analysis(entered_text, selected_option.get())

def root_content():
        # instantiate root as tk window
    root = tk.Tk()
        # sizing
    root.geometry("800x800")
        # file title
    root.title("Tkinter GUI Optics and Photonics")
        # Dropdown menu
    label = tk.Label(root, text="Select an option:")
        # vertical padding added for readability
    label.pack(pady=10)
        # return root to be used in main
    return root

def main():
        # Create the main window
    root = root_content()
    options = ["Geometry", "History", "Biology", "Geography", "Historiography"]
        #TODO --> Implement Pandas Library and display options DYNAMICALLY based on the desired cols/rows
    selected_option = tk.StringVar(root)
        # Creates StringVar Object Associated with the current Tk Window
        # NOTE TO SELF --> StringVar is SPECIAL to TKinter and links to the attribute/state of a widget to set that value elsewhere
    dropdown = ttk.Combobox(root, textvariable=selected_option, values=options)
    search_box = ttk.Scrollbar(root)
        # NOTE TO SELF --> Combo box is the TTK drop down widget
    dropdown.pack(pady=10)
    dropdown.set(options[0])  # Set the default selection to "Geometry"

    # Text Entry Portion
    text_entry = tk.Entry(root, width=30)
    text_entry.pack(pady=10)
        # TODO --> Implement the parsing/query process WITH the text_data_analysis function where the text_entry is passed

    search_button = tk.Button(root, text="Search", command=lambda: perform_search(text_entry, selected_option))
    search_button.pack(pady=10)

    # Buttons
    button_frame = tk.Frame(root)

    button_texts = ["Optics Sub A", "Optics Sub B", "Optics Sub C", "Optics Sub D", "Optics Sub E"]
        # Later TODO --> Dynamically change the buttons in button_texts to reflect the rows/cols in the excel file.
        # df.iloc() allows a passed row which could be used for this :D
    for button_text in button_texts:
        button = tk.Button(button_frame, text=button_text, command=lambda text=button_text, option=selected_option: on_button_click(text, option))
        button.pack(side=tk.LEFT, padx=5)

    button_frame.pack(pady=20)
    download_button = tk.Button(root, text="Download", command=lambda: save_to_file("Download Button", selected_option.get()))
    download_button.pack(pady=10)
    # on a click of the download button, the lambda fnctn calls the save_to_file fnctn and fills in "button_text" with the selected dropdown

    # Run the GUI (and hope nothing is broken)
    root.mainloop()

if __name__ == "__main__":
    main()