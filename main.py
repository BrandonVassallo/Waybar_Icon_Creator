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
waybar_pos = "LEFT"
color = 0

def prompt_user():

    ###############################
    ### Define Button Functions ###
    ###############################


    def color_picker():
        global color
        color = colorchooser.askcolor(title="Choose Icon Color")

        # The color is represneted as a tuple: ((R, G, B), "#rrbbgg")
        if color[1] is not None:
            selected_color.config(text=f"Selected Color is: {color[1]}", bg=color[1])

        color = color[1]

    def set_way_left():
        global waybar_pos
        waybar_pos = "LEFT"
        update_waybar_buttons()

    def set_way_right():
        global waybar_pos
        waybar_pos = "RIGHT"
        update_waybar_buttons()

    def set_way_center():
        global waybar_pos
        waybar_pos = "CENTER"
        update_waybar_buttons()

    def update_waybar_buttons():
        if waybar_pos == "LEFT":
            way_left.config(bg="Green")
            way_center.config(bg="White")
            way_right.config(bg="White")

        elif waybar_pos == "CENTER":
            way_left.config(bg="White")
            way_center.config(bg="Green")
            way_right.config(bg="White")

        elif waybar_pos == "RIGHT":
            way_left.config(bg="White")
            way_center.config(bg="White")
            way_right.config(bg="Green")

    def update_tooltip_bool():
        if tool_bool.get() == False:
            # Turn off tooltip entry
            tool_label.grid_remove()
            tool_entry.grid_remove()
        else:
            # Turn on tooltip entry
            tool_label.grid()
            tool_entry.grid()

    def update_dropdown_bool():
        if drop_bool.get() == False:
            # Turn off tooltip entry
            drop_label.grid_remove()
            drop_entry.grid_remove()
        else:
            # Turn on tooltip entry
            drop_label.grid()
            drop_entry.grid()

    def check_exit():
        if icon_name.get() != "" and nerd_icon.get() != "" and command.get() != "" and color != 0:
            # RUN CONFORMATION CODE
            root.destroy()
        else:
            if icon_name.get() == "":
                icon_name_label.config(fg="Red")
            else:
                icon_name_label.config(fg="Black")

            if nerd_icon.get() == "":
                nerd_label.config(fg="Red")
            else:
                nerd_label.config(fg="Black")

            if command.get() == "":
                command_label.config(fg="Red")
            else:
                command_label.config(fg="Black")

            if color == 0:
                color_label.config(fg="Red")
            else:
                color_label.config(fg="Black")
                

    ########################
    ### Open User Window ###
    ########################

    root = ttk.Tk()
    window = ttk.Frame(root, padx=10, pady=10)
    window.grid()

    # ROW 0 - Spacing
    ttk.Label(window, text="    ").grid(column=0, row=0)

    # ROW 1 - Icon Decleration
    icon_name = StringVar()
    icon_name_label = ttk.Label(window, text="Icon Decleration Name*")
    icon_name_label.grid(column=0,row=1, sticky=E)
    icon_name_entry = ttk.Entry(window, width=20, textvariable=icon_name)
    icon_name_entry.grid(column=1, row=1, sticky=W)


    # ROW 2 - Nerd Font Icon
    nerd_font = font.Font(family="JetBrainsMono Nerd Font")
    nerd_icon = StringVar()
    nerd_label = ttk.Label(window, text="Nerd Font Icon*")
    nerd_label.grid(column=0,row=2, sticky=E)
    nerd_font_entry = ttk.Entry(window, font=nerd_font, width=3, textvariable=nerd_icon)
    nerd_font_entry.grid(column=1, row=2, sticky=W)

    # ROW 3 - Command
    command = StringVar()
    command_label = ttk.Label(window, text="Command to be run*")
    command_label.grid(column=0,row=3, sticky=E)
    command_entry = ttk.Entry(window, width=40, textvariable=command)
    command_entry.grid(column=1, row=3, sticky=W)

    # ROW 4 - Icon Color
    color_label = ttk.Label(window, text="Choose Icon Color:*")
    color_label.grid(column=0,row=4, sticky=E)
    selected_color = ttk.Label(window, text="No color selected")
    selected_color.grid(column=2, row=4, sticky=E)
    ttk.Button(window, text="Pick a Color", command=lambda: color_picker()).grid(column=1, row=4, sticky=W)

    # ROW 5 - EMPTY
    ttk.Label(window, text=" ").grid(column=0, row=5)

    # ROW 6,7,8 - Waybar Position
    ttk.Label(window, text="Choose Icon Position:").grid(column=0,row=6, sticky=E)

    way_left = ttk.Button(window, text="Left", command=set_way_left)
    way_center = ttk.Button(window, text="Center", command=set_way_center)
    way_right = ttk.Button(window, text="Right", command=set_way_right)

    way_left.grid(column=1, row=6, sticky=W)
    way_center.grid(column=1, row=7, sticky=W)
    way_right.grid(column=1, row=8, sticky=W)

    update_waybar_buttons()

    # ROW 9 - EMPTY
    ttk.Label(window, text=" ").grid(column=0, row=9)

    # ROW 10 - Tooltip?
    tool_bool = ttk.BooleanVar(value=False)
    tool_label = ttk.Label(window, text="Tooltip:")                 # In ROW 11, but needs to be defined before update_tooltip_bool
    tooltip = ttk.StringVar()
    tool_entry = ttk.Entry(window, width=40, textvariable=tooltip)  # In ROW 11, but needs to be defined before update_tooltip_bool


    ttk.Label(window, text="Include a Tooltip?").grid(column=0,row=10, sticky=E)
    tool_check_box = ttk.Checkbutton(window, variable=tool_bool, command=update_tooltip_bool)
    tool_check_box.grid(column=1, row=10, sticky=W)

    # ROW 11 - Tooltip Label
    tool_label.grid(column=0, row=11, sticky=E)
    tool_entry.grid(column=1, row=11, sticky=W)

    update_tooltip_bool()

    # ROW 12 - Dropdown?
    drop_bool = ttk.BooleanVar(value=False)
    drop_label = ttk.Label(window, text="Dropdown Number:")                 # In ROW 13, but needs to be defined before update_tooltip_bool
    drop_num = ttk.StringVar()
    drop_entry = ttk.Entry(window, width=6, textvariable=drop_num)                      # In ROW 13, but needs to be defined before update_tooltip_bool

    ttk.Label(window, text="Include a Dropdown?").grid(column=0,row=12, sticky=E)
    drop_check_box = ttk.Checkbutton(window, variable=drop_bool, command=update_dropdown_bool)
    drop_check_box.grid(column=1, row=12, sticky=W)

    # ROW 13 - Number of dropdown elements
    drop_entry.grid(column=1, row=13, sticky=W)
    drop_label.grid(column=0, row=13, sticky=E)

    update_dropdown_bool()

    # ROW 14 - Empty
    ttk.Label(window, text=" ").grid(column=0, row=14)

    # ROW 15 - Exit Button
    ttk.Button(window, text="Finished?", command=check_exit).grid(column=0, row=15)
    ttk.Button(window, text="Cancel", command=root.destroy).grid(column=1, row=15)

    window.mainloop()

def main():
    prompt_user()

main()

