import tkinter as ttk
from tkinter import *
from tkinter import font

def confirm(parent: Tk, icon_name: StringVar, nerd_icon: StringVar, command: StringVar, color: str, position: str, tool_bool: BooleanVar, tooltip: StringVar, drop_bool: BooleanVar, drop_num: StringVar):

    status = ttk.BooleanVar(value=False)

    def accept():
        status.set(True)
        print(f"STATUS SET TO: {status.get()}")
        root.destroy()
        
    
    def deny():
        status.set(False)
        print(f"STATUS SET TO: {status.get()}")
        root.destroy()
        

    root = ttk.Toplevel(parent)
    root.title("Confirm Details")
    root.grab_set()

    window = ttk.Frame(root, padx=10, pady=10)
    window.grid()

    # ROW 0 - Spacing 
    ttk.Label(window, text="    ").grid(column=0, row=0)

    # ROW 1 - Title
    title = ttk.Label(window, text="CONFIRM DETAILS BELOW", font=("Arial", 12, "bold"))
    title.grid(column=1, row=1, sticky=W)

    # ROW 2 - Spacing
    ttk.Label(window, text="    ").grid(column=1, row=2, sticky=W)

    # ROW 3 - Icon Name
    ttk.Label(window, text="ICON NAME: ").grid(column=0, row=3, sticky=E)
    ttk.Label(window, text=icon_name.get()).grid(column=1, row=3, sticky=W)

    # ROW 4 - Nerd Icon
    ttk.Label(window, text="NERD ICON: ").grid(column=0, row=4, sticky=E)
    ttk.Label(window, text=nerd_icon.get()).grid(column=1, row=4, sticky=W)

    # ROW 5 - Command
    ttk.Label(window, text="COMMAND: ").grid(column=0, row=5, sticky=E)
    ttk.Label(window, text=command.get()).grid(column=1, row=5, sticky=W)

    # ROW 6 - Color
    ttk.Label(window, text="COLOR: ").grid(column=0, row=6, sticky=E)
    ttk.Label(window, text=color, fg=color).grid(column=1, row=6, sticky=W)

    # ROW 7 - Tooltip Selected
    ttk.Label(window, text="TOOLTIP? ").grid(column=0, row=7, sticky=E)
    if tool_bool.get():
        ttk.Label(window, text="YES").grid(column=1, row=7, sticky=W)
    else:
        ttk.Label(window, text="NO").grid(column=1, row=7, sticky=W)

    # ROW 8 - Tooltip
    if tool_bool.get():
        ttk.Label(window, text="TOOLTIP: ").grid(column=0, row=8, sticky=E)
        ttk.Label(window, text=tooltip.get()).grid(column=1, row=8, sticky=W)

    # ROW 9 - Dropdown Selected
    ttk.Label(window, text="DROPDOWN? ").grid(column=0, row=9, sticky=E)
    if drop_bool.get():
        ttk.Label(window, text="YES").grid(column=1, row=9, sticky=W)
    else:
        ttk.Label(window, text="NO").grid(column=1, row=9, sticky=W)

    # ROW 10 - Dropdown
    if drop_bool.get():
        ttk.Label(window, text="DROPDOWN NUM: ").grid(column=0, row=10, sticky=E)
        ttk.Label(window, text=drop_num.get()).grid(column=1, row=10, sticky=W)

    # ROW 11 - Spacing
    ttk.Label(window, text="    ").grid(column=0, row=11)

    # ROW 12 - Confirm/Deny
    ttk.Button(window, text="CONFIRM", command=accept, fg="Green").grid(column=0, row=12, sticky=E)
    ttk.Button(window, text="DENY", command=deny, fg="Red").grid(column=1, row=12, sticky=W)

    parent.wait_window(root)

    return status.get()

