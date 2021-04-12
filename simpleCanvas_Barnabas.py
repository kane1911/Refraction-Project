# Updated 08/04/2021 by Barnabas using Kane's Combobox code
import tkinter
from tkinter import ttk
import math
import tkinter.messagebox

root = tkinter.Tk()
root.title("Calculating Angle of Refraction")
root.geometry("400x400")

def refraction_angle(n=1.5,
                     incidence_angle=40):  # function has default values of index of refraction = 1.5 (air to glass) and incidence angle = 40 degrees
    """Returns the angle of refraction from n (the index of refraction between the two media)
    and the angle of incidence (measured in degrees)."""

    try:
        r_angle = math.degrees(math.asin(math.sin(math.radians(incidence_angle)) / n))  # rearranged form of Snell's law with angles converted as necessary. asin function works only for radians.
        
        return round(r_angle, 2)  # rounds to 2 d.p.
    except ValueError:
        tkinter.messagebox.showerror(title="Domain error", message="Invalid combination of incidence angle and index of refraction.")



def main():
    """Gets user input, calls the refraction_angle function, and displays the output."""

    n = index_input.get()
    incidence_angle = incidence_input.get()

    if n.isalpha() or incidence_angle.isalpha(): # if either of the inputs are letters
        tkinter.messagebox.showerror(title="Letter(s) entered", message="Please enter valid numbers for the incidence angle and index of refraction.") # displays warning pop-up window
    
    else: # if both inputs are digits or decimals
        try:
            output = refraction_angle(float(n), float(incidence_angle))

            calc = tkinter.Label(root, text = output)
            calc.grid(row = 6, column = 2)
        except ValueError:
            tkinter.messagebox.showerror(title="Space or symbol entered", message="Invalid input.") # displays warning pop-up window


# -------------Window widgets and layout ---------------------------    
incidence_label = tkinter.Label(root, text = "Incidence Angle:")
incidence_label.grid(row = 1, column = 1, sticky = "E")
incidence_input = tkinter.Spinbox(root, from_=0, to=90, wrap=True) # Spinbox only accepts from a certain range of inputs (0 to 90 degrees)
incidence_input.grid(row = 1, column = 2)

index_label = tkinter.Label(root, text = "Index of Refraction:")
index_label.grid(row = 2, column = 1, sticky = "E")
index_input = tkinter.Spinbox(root, from_=0.1, to=100, increment=0.1, wrap=True) # # Spinbox only accepts from a certain range of inputs of index of refraction (0 to 100 in increments of 0.1)
index_input.grid(row = 2, column = 2)

# --------Combobox drop down list-----
ttk.Label(text="Select Index Medium:").grid(column=1,row=3, sticky="E")
n1 = tkinter.StringVar()
indexmedium1 = ttk.Combobox(root, width=18, textvariable=n1)
indexmedium1['values'] = ('Air', 'Glass', 'Water')
indexmedium1['state'] = 'readonly' # means the user cannot directly enter a value into the combobx see:https://www.pythontutorial.net/tkinter/tkinter-combobox/
indexmedium1.grid(column=2, row=3)
indexmedium1.current(1) # Shows Air as default



ttk.Label(text="Select Refraction Medium:").grid(column=1,row=4, sticky="E")
n2 = tkinter.StringVar()
indexmedium2 = ttk.Combobox(root, width=18, textvariable=n2)
indexmedium2['values'] = ('Air', 'Glass', 'Water', 'Amber', 'Diamond')
indexmedium2['state'] = 'readonly' # means the user cannot directly enter a value into the combobx see:https://www.pythontutorial.net/tkinter/tkinter-combobox/
indexmedium2.grid(column=2, row=4)
indexmedium2.current(0) # Shows Glass as default


calculate_button = tkinter.Button(root, text = "Calculate", command = main)
calculate_button.grid(row = 5, column = 2)

refraction_label = tkinter.Label(root, text="Angle of Refraction (degrees):")
refraction_label.grid(row=6, column=1, sticky = "E")



# First attempt at creating a drop-down menu:

# i_medium_label = tkinter.Label(root, text="Incidence Medium:")
# i_medium_label.grid(row=5, column=1)

# variable = tkinter.StringVar(root)
# variable.set("Incidence Medium")
# i_medium_input = tkinter.OptionMenu(root, variable, "Air", "Water", "Glass")
# i_medium_input.grid(row=5, column=2)

# i_med = tkinter.Label(root, text=variable.get())
# i_med.grid(row=6,column=2)
# ------------------------------------------

root.mainloop()
