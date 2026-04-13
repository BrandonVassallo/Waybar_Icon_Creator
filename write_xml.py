# This File is responsible for writing the xml file for any dropdowns if selected

'''

The file name will be: "{icon_name}_menu.xml"

Structure:  (2-space scope changes)

<?xml version="1.0" encoding="UTF-8"?>
<interface>
  <object class="GtkMenu" id="menu">
    ...
    <child>
        <object class="GtkMenuItem" id="{name0}">
			<property name="label">{label0}</property>
        </object>
	</child>
    ...
    <child>
      <object class="GtkSeparatorMenuItem" id="delimiter{delimiter_count}"/>
    </child>
    ...
  </object>
</interface>



Variables:

delimiter_count
    - Amount of specified delimiters to avoid decleration name matching

name0
    - From the dropdown_elements[] array tuple of (name0, label0, command0)
    - The decleration name of the dropdown selection
        - Not shown in the dropdown, soley for decleration

label0
    - From the dropdown_elements[] array tuple of (name0, label0, command0)
    - The label shown in the dropdown menu
        - Is shown in the dropdown

'''