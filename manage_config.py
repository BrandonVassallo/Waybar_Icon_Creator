# This File is responsible for modifying the config.json file

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