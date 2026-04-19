# This File is responsible for modifying the config.json file

import tkinter as tk
from tkinter import *

'''
HOW TO:

    - Add the string: "custom/{icon_name}" to the specified Waybar position
    - Add the below config decleration (can be appended)

    // NO DROPDOWN //
    "custom/{icon_name}": {
        "format": "{nerd_icon}",
        "on-click": "{command}",
        "tooltip": {tool_bool}},
        "tooltip-format": "{tooltip}}",     # Depending on tool_bool 
    },

    // DROPDOWN //
    "custom/{icon_name}": {
        "tooltip": {tool_bool},
        "tooltip-format": "{tooltip}",     # Depending on tool_bool 
        "menu": "on-click",
        "menu-file": "~/.config/waybar/{icon_name}_menu.xml",
        "menu-actions": {
	        "{label1}": "{menu_cmd_1}",
            "{label2}": "{menu_cmd_2}",
	        "{label3}": "{menu_cmd_3}",
            ...etc...
    },
    "format": "{nerd_icon}",
  },


Variables

icon_name
    - the name of the icon for decleration purposes only

nerd_icon
    - the nerd icon for display

command
    - the command to be executed when selected

tool_bool
    - A bool representing if a tooltip is necessary

tooltip
    - The actual tooltip to be displayed

labelX
    - From the dropdown_elements[] array tuple of (name0, label0, command0)
    - The label decleration to help the config file point to the xml menu file

menu_cmd_X
    - From the dropdown_elements[] array tuple of (name0, label0, command0)
    - The command executed when the dropdown element is selected

'''


'''
Creates the dropdown UI entrance
'''
def dropdown_UI(drop_num):
    drop_array = []     # Used to store all of the Dropdown elements

    '''
    Debugging function for the Finished? button
    '''
    def print_out():
        j = 1
        for tup in drop_array:
            print(f"ELEMENT: {j}")
            print(f"NAME: {tup[0].get()}")
            print(f"LABEL: {tup[1].get()}")
            print(f"COMMAND: {tup[2].get()}\n")
            j += 1

        root.destroy()     

    root = tk.Tk()
    window = tk.Frame(root, padx=10, pady=10)
    window.grid()

    # ROW 0 - Spacing
    tk.Label(window, text="    ").grid(column=0, row=0)

    # ROW 1 - Label

    tk.Label(window, text="Display Name").grid(column=0, row=1)
    tk.Label(window, text="Label (For code)").grid(column=1, row=1)
    tk.Label(window, text="Command").grid(column=2, row=1)

    for i in range(drop_num):       # Move through each row, adding each entry label
        # DROPDOWN NAME ENTRIES
        drop_name_temp = tk.StringVar()
        drop_name_entry = tk.Entry(window, width=30, textvariable=drop_name_temp)
        drop_name_entry.grid(row=i+2, column=0)

        # DROPDOWN LABEL ENTRIES
        drop_label_temp = tk.StringVar()
        drop_label_entry = tk.Entry(window, width=30, textvariable=drop_label_temp)
        drop_label_entry.grid(row=i+2, column=1)

        # DROPDOWN COMMAND ENTRIES
        drop_command_temp = tk.StringVar()
        drop_command_entry = tk.Entry(window, width=30, textvariable=drop_command_temp)
        drop_command_entry.grid(row=i+2, column=2)

        # Tuple format is always (DISPLAY NAME, LABEL, COMMAND)
        drop_tupple = (drop_name_temp, drop_label_temp, drop_command_temp)

        drop_array.append(drop_tupple)      # Add each tuple to the drop array

    tk.Button(window, text="Finished?", command=root.destroy).grid(column=0, row=drop_num+2, sticky=E)

    root.mainloop()
    
    return drop_array

def manage_config(icon_name, nerd_icon, command, tool_bool, tooltip, dropdown_elements):
    # Input the stuff into the config file
    pass

# Debugging:
# d_num = 2
# dropdown_UI(d_num)