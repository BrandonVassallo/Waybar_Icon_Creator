import tkinter as ttk
from tkinter import *
from tkinter import font
from tkinter import colorchooser

import write_xml
import manage_config
import manage_style

'''
setup:s

1) Open tkinter UI                                              (Variable names)
    - Obtain User input:    (? = Not Required)
        - Waybar position (Left, Center, Right)                 (waybar_pos)
        - Icon name (for config/style decleration)              (icon_name)
        - Nerd font icon                                        (nerd_icon)
        - Icon Color                                            (icon_color)
        - Tooltip?                                              (tool_bool)
            - Tooltip                                           (tooltip)
        - Command to run                                        (command)
        - Dropdown?
            - Dropdown Element Names, Labels, and commands      (dropdown_elements[] = [(name0, command0), ...])

2) Create xml file for dropdown if necessary
    - See write_xml.py

3) Modify config.json
    - See manage_config.py
'''

def prompt_user():

    ###############################
    ### Define Button Functions ###
    ###############################


    def color_picker():
        color = colorchooser.askcolor(title="Choose Icon Color")

        # The color is represneted as a tuple: ((R, G, B), "#rrbbgg")
        if color[1] is not None:
            selected_color.config(text=f"Selected Color is: {color[1]}", bg=color[1])

        color = color[1]


    ########################
    ### Open User Window ###
    ########################

    root = ttk.Tk()
    window = ttk.Frame(root)
    window.grid()

    # ROW 0 - Spacing
    ttk.Label(window, text="    ").grid(column=0, row=0)

    # ROW 1 - Icon Decleration
    icon_name = StringVar()
    ttk.Label(window, text="Icon Decleration Name").grid(column=0,row=1, sticky=E)
    icon_name_entry = ttk.Entry(window, width=20, textvariable=icon_name)
    icon_name_entry.grid(column=1, row=1, sticky=W)


    # ROW 2 - Nerd Font Icon
    nerd_font = font.Font(family="JetBrainsMono Nerd Font")
    nerd_icon = StringVar()
    ttk.Label(window, text="Nerd Font Icon").grid(column=0,row=2, sticky=E)
    nerd_font_entry = ttk.Entry(window, font=nerd_font, width=3, textvariable=nerd_icon)
    nerd_font_entry.grid(column=1, row=2, sticky=W)

    # ROW 3 - Command
    command = StringVar()
    ttk.Label(window, text="Command to be run").grid(column=0,row=3, sticky=E)
    command_entry = ttk.Entry(window, width=40, textvariable=command)
    command_entry.grid(column=1, row=3, sticky=W)

    # ROW 4 - Icon Color
    color = ""

    ttk.Label(window, text="Choose Icon Color:").grid(column=0,row=4, sticky=E)
    ttk.Button(window, text="Pick a Color", command=lambda: color_picker()).grid(column=1, row=4, sticky=W)
    selected_color = ttk.Label(window, text="No color selected")
    selected_color.grid(column=2, row=4, sticky=E)

    # ROW 5 - Waybar Position

    # ROW 6 - Tooltip?

    # ROW 7 - Tooltip Label

    # ROW 8 - Dropdown?

    # ROW 9 - Exit Button



    window.mainloop()

def main():
    prompt_user()

main()

