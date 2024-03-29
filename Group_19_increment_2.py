import tkinter
from tkinter import ttk
import math
import tkinter.messagebox

root = tkinter.Tk()
root.title("Group 19: Angle of Refraction Calculator")
root.geometry("400x400") # window size


def refraction_angle(n, incidence_angle):
    """Returns the angle of refraction from n (the index of refraction between the two media)
    and the angle of incidence (measured in degrees)."""

    try:
        r_angle = math.degrees(math.asin(math.sin(math.radians(incidence_angle)) / n))  # rearranged form of Snell's law with angles converted as necessary. asin function works only for radians.
        
        return round(r_angle, 2)  # rounds to 2 d.p.
    except ValueError:
        tkinter.messagebox.showerror(title="Domain error", message="Invalid combination of incidence angle and index of refraction.")


def index_of_refraction(i_medium, r_medium):
    """Returns the index of refraction between the incidence medium (i_medium) and the refraction medium (r_medium)."""

    abs_index = {'Air': 1, 'Glass': 1.5, 'Water': 1.333, 'Amber': 1.55, 'Diamond': 2.417} # obtained from: https://en.wikipedia.org/wiki/List_of_refractive_indices

    n_i = abs_index[i_medium]  # finds the index of refraction of the incidence medium from the key provided from the drop down menu
    n_r = abs_index[r_medium] # finds the index of refraction of the refraction medium from the key provided from the drop down menu
    i_n_r = round(n_r/n_i, 3) # calcs the relative index of refraction between the media
    return i_n_r

def find_abs_n(medium):
    """Returns the absoulute refracive index of the given medium."""
    abs_index = {'Air': 1, 'Glass': 1.5, 'Water': 1.333, 'Amber': 1.55, 'Diamond': 2.417} # obtained from: https://en.wikipedia.org/wiki/List_of_refractive_indices
    abs_n = abs_index[medium]
    return abs_n


def find_v(abs_n):
    '''This function will calculate the v (velocity of light) by taking the absolute refractive index from the user's medium selections.'''
    # Calculate v
    v = round(300000000 / float(abs_n), 3) 
    return v



def main():
    """Combines user input from the Spinbox and Comboboxes (drop-down menus) with the refraction_angle function, and displays the output."""

    n = index_of_refraction(i_medium = indexmedium1.get(), r_medium = indexmedium2.get()) # gets the index of refraction between the 2 selected media
    incidence_angle = incidence_input.get() # gets incidence angle from the user's input in the Spinbox

    try:
        if incidence_angle.isalpha(): # if the angle input contains letters
            tkinter.messagebox.showerror(title="Letter(s) entered", message="Please enter a valid incidence angle.") # displays error pop-up window
        
        elif not (-90 <= float(incidence_angle) <= 90): # if the incidence angle entered is not in the interval [-90, 90]
            tkinter.messagebox.showerror(title="Angle out of range", message="Please enter an incidence angle between -90° and 90°.") # displays warning pop-up window
        
        else: # if both inputs are digits or decimals between -90° and 90°
            r_angle = refraction_angle(n, float(incidence_angle))

            calculated_angle = tkinter.Label(root, text = str(r_angle) + "°") # concatenates degree symbol to
            calculated_angle.grid(row = 5, column = 2)

    except ValueError:
        tkinter.messagebox.showerror(title="Space or symbol entered", message="Invalid input.") # displays warning pop-up window
    
    # ----------Widgets showing additional calculations that only display when the Calculate button is pressed:
    
    index_label = tkinter.Label(root, text="Refractive index from {} to {}:".format(indexmedium1.get(), indexmedium2.get())) 
    index_label.grid(row=6, column=1)

    n_label = tkinter.Label(root, text=str(n)) # displays the index of refractin between the two selected media
    n_label.grid(row=6, column=2)

    i_medium_v_label = tkinter.Label(root, text="Velocity of light in {}:".format(indexmedium1.get())) 
    i_medium_v_label.grid(row=7, column = 1, sticky = "E")

    i_medium_v = tkinter.Label(root, text= str(find_v(find_abs_n(indexmedium1.get()))) + " m/s") # displays the velocity of light in the incidence medium based on its absolute refractive index
    i_medium_v.grid(row=7, column = 2)

    i_medium_v_label = tkinter.Label(root, text="Velocity of light in {}:".format(indexmedium2.get())) 
    i_medium_v_label.grid(row=8, column = 1, sticky = "E")

    i_medium_v = tkinter.Label(root, text= str(find_v(find_abs_n(indexmedium2.get()))) + " m/s") # displays the velocity of light in the refraction medium based on its absolute refractive index
    i_medium_v.grid(row=8, column = 2)



# -------------Window widgets and grid layout:   

incidence_label = tkinter.Label(root, text = "Incidence Angle (°):")
incidence_label.grid(row = 1, column = 1, sticky = "E")
incidence_input = tkinter.Spinbox(root, from_=-90, to=90, wrap=True) # Spinbox only accepts from a certain range of inputs (-90 to 90 degrees)
incidence_input.grid(row = 1, column = 2)

ttk.Label(text="Select Incidence Medium:").grid(row=2, column=1, sticky="E") # incidence medium drop down menu
n1 = tkinter.StringVar()
indexmedium1 = ttk.Combobox(root, width=18, textvariable=n1)
indexmedium1['values'] = ('Air', 'Glass', 'Water')
indexmedium1['state'] = 'readonly' # means the user cannot directly enter a value into the combobx see:https://www.pythontutorial.net/tkinter/tkinter-combobox/
indexmedium1.grid(row=2, column=2)
indexmedium1.current(0) # Shows Air as default

ttk.Label(text="Select Refraction Medium:").grid(row=3, column=1, sticky="E") # refraction medium drop down menu
n2 = tkinter.StringVar()
indexmedium2 = ttk.Combobox(root, width=18, textvariable=n2)
indexmedium2['values'] = ('Air', 'Glass', 'Water', 'Amber', 'Diamond')
indexmedium2['state'] = 'readonly' # means the user cannot directly enter a value into the combobx see:https://www.pythontutorial.net/tkinter/tkinter-combobox/
indexmedium2.grid(row=3, column=2)
indexmedium2.current(1) # Shows Glass as default


calculate_button = tkinter.Button(root, text = "Calculate", command = main) # Calculate button runs the main() function
calculate_button.grid(row = 4, column = 2)

refraction_label = tkinter.Label(root, text="Angle of Refraction:")
refraction_label.grid(row=5, column=1, sticky = "E")


root.mainloop()