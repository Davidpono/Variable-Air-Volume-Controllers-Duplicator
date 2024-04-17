import tkinter as tk
import os
from tkinter import messagebox
from get_data import get_data

# Define the process_string function
global script_dir
script_dir = os.path.dirname(os.path.abspath(__file__))

    


def display_message(selected_option, selected_option1, selected_option2,selected_option3):
    # Constructing the message
    message = f"Heating And Cooling VAV: {selected_option.get()}\n\nCooling Only VAV: {selected_option1.get()}\n\nSpreadsheets: {selected_option2.get()}"
    print(selected_option1, selected_option)

    # Validating the selected options
    if selected_option.get() == "PY_VAR0" or selected_option1.get() == "PY_VAR1":
        messagebox.showinfo("ERROR", "Please select an option for Everything")
    else:  
        messagebox.showinfo("Parameters",message)
        print(message)


        filename = os.path.join("Spreadsheets", f"{selected_option2.get()}")
        XMLFILESCR=os.path.join("Template VAV SCR Controlers", f"{selected_option.get()}")
        XMLFILECOOLIN = os.path.join("Template Cooling Only VAV Controlers", f"{selected_option1.get()}")
        XMLStageCooling = os.path.join("Template Staged Heating VAV Controlers", f"{selected_option3.get()}")
        print(selected_option,selected_option1,selected_option2)

        num_rows = get_data(filename,XMLFILESCR,XMLFILECOOLIN,XMLStageCooling)

        if num_rows > 0:
            print(f"The CSV file '{filename}' has {num_rows} rows (excluding header).")
        else:
            print(f"Error processing file '{filename}'.")           
def display_files():
    files = os.listdir(script_dir)
    file_list = "\n".join(files)
    status_label.config(text=f"Files in directory:\n{file_list}")
def display_selection(selected_option):
    selected_option.set("Selected option: " + selected_option.get())
   
def show_selected(selected_option):
    selected = selected_option.get()
    print("Selected option:", selected)
def display_selection1(selected_option1):

    selected_option1.set("Selected option: " + selected_option1.get())
def show_selected1(selected_option1):
    selected1 = selected_option1.get()
 
    print("Selected option:", selected1)
def display_selection2(selected_option2):

    selected_option2.set("Selected option: " + selected_option2.get())
def show_selected2(selected_option2):
    selected2 = selected_option2.get()
 
    print("Selected option:", selected2)
def display_selection3(selected_option3):

    selected_option3.set("Selected option: " + selected_option3.get())
def show_selected3(selected_option3):
    selected3 = selected_option3.get()
 
    print("Selected option:", selected3)
def main():
    # Create the main window
    root = tk.Tk()
    root.title("VaV Duplicator")
    
    # Create a label widget
    label = tk.Label(root, text="Duplicate your VAV")
    label.pack()

    # Create a button widget
    button = tk.Button(root, text="Duplicate", command=lambda: display_message(selected_option, selected_option1, selected_option2,selected_option3))
    button.pack()
    button2 = tk.Button(root, text="Display Files", command=display_files)
    button2.pack()
    

    # Create radiobuttons
    selected_option = tk.StringVar()
    selected_option1 = tk.StringVar()
    selected_option2 = tk.StringVar()
    selected_option3 = tk.StringVar()
    

    # Run the main event loop
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    folder_nameforSpreadsheets = "Spreadsheets"
    folder_pathforSpreadsheets = os.path.join(script_dir, folder_nameforSpreadsheets)
    files_in_SpreadsheetsFolder = os.listdir(folder_pathforSpreadsheets)
    folder_nameforSCR = "Template VAV SCR Controlers"
    folder_pathforSCR = os.path.join(script_dir, folder_nameforSCR)
    files_in_SCRFolder = os.listdir(folder_pathforSCR)
    folder_nameforCooling = "Template Cooling Only VAV Controlers"
    folder_pathforCooling = os.path.join(script_dir, folder_nameforCooling)
    files_in_CoolingFolder = os.listdir(folder_pathforCooling)
    folder_nameforstage = "Template Staged Heating VAV Controlers"
    folder_pathforstage = os.path.join(script_dir, folder_nameforstage)
    files_in_stageHeating = os.listdir(folder_pathforstage)

    # Create a status label
    global status_label
    title_label = tk.Label(root, text="Heating And Cooling VAV:")
    title_label.pack(anchor=tk.W)
    display_label = tk.Label(root, textvariable=selected_option)
    display_label.pack()

    options = [("None", "None")]
    options.extend((file_name, file_name) for file_name in files_in_SCRFolder)
    for text, value in options:
        radio_button = tk.Radiobutton(root, text=text, variable=selected_option, value=value, command=display_selection(selected_option))
        radio_button.pack(anchor=tk.W)


    title_label = tk.Label(root, text="Cooling Only VAV:")
    title_label.pack(anchor=tk.W)
    display_label = tk.Label(root, textvariable=selected_option1)
    display_label.pack()
    options1 = [("None", "None")]
    options1.extend((file_name, file_name) for file_name in files_in_CoolingFolder)
    for text1, value1 in options1:
        radio_button = tk.Radiobutton(root, text=text1, variable=selected_option1, value=value1, command=display_selection1(selected_option1))
        radio_button.pack(anchor=tk.W)


    title_label = tk.Label(root, text="Multiple Stage Heating:")
    title_label.pack(anchor=tk.W)
    display_label = tk.Label(root, textvariable=selected_option2)
    display_label.pack()

    options3 = [("None", "None")]
    options3.extend((file_name, file_name) for file_name in files_in_stageHeating)
    for text3, value3 in options3:
        radio_button = tk.Radiobutton(root, text=text3, variable=selected_option3, value=value3, command=display_selection3(selected_option3))
        radio_button.pack(anchor=tk.W)










    
    title_label = tk.Label(root, text="Spreadsheets:")
    title_label.pack(anchor=tk.W)
    display_label = tk.Label(root, textvariable=selected_option2)
    display_label.pack()
    
    options2 = [(file_name, file_name) for file_name in files_in_SpreadsheetsFolder]
    for text2, value2 in options2:
        radio_button2 = tk.Radiobutton(root, text=text2, variable=selected_option2, value=value2, command=display_selection2(selected_option2))
        radio_button2.pack(anchor=tk.W)
        

    status_label = tk.Label(root, text="Click 'Display Files' to show all files in this directory.")
    status_label.pack()
    file_list = "\n".join(files_in_SpreadsheetsFolder)
    status_label.config(text=f"Files in directory:\n{file_list}")
    


    root.mainloop()

if __name__ == "__main__":
    main()