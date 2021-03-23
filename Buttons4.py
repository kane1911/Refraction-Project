# Updated 23/3/21 by Kane
import tkinter
from tkinter import ttk
import math
import tkinter.messagebox

root = tkinter.Tk()
root.title("Calculating Angle of Refraction")
root.geometry("400x400")
# Attempt at creating a drop-down menu:

# i_medium_label = tkinter.Label(root, text="Incidence Medium:")
# i_medium_label.grid(row=5, column=1)

# variable = tkinter.StringVar(root)
# variable.set("Incidence Medium")
# i_medium_input = tkinter.OptionMenu(root, variable, "Air", "Water", "Glass")
# i_medium_input.grid(row=5, column=2)

# i_med = tkinter.Label(root, text=variable.get())
# i_med.grid(row=6,column=2)
# ------------------------------------------

incidence_label = tkinter.Label(root, text="Incidence Angle:")
incidence_label.grid(row=1, column=1, sticky="E")
incidence_input = tkinter.Spinbox(root, from_=0, to=90,
                                  wrap=True)  # Spinbox only accepts from a certain range of inputs (0 to 90 degrees)
incidence_input.grid(row=1, column=2)

index_label = tkinter.Label(root, text="Index of Refraction:")
index_label.grid(row=2, column=1, sticky="E")
index_input = tkinter.Spinbox(root, from_=0.1, to=100, increment=0.1,
                              wrap=True)  # # Spinbox only accepts from a certain range of inputs of index of refraction (0 to 100 in increments of 0.1)
index_input.grid(row=2, column=2)

refraction_label = tkinter.Label(root, text="Angle of Refraction (degrees):")
refraction_label.grid(row=10, column=1, sticky="E")


def refraction_angle(n=1.5,
                     incidence_angle=40):  # function has default values of index of refraction = 1.5 (air to glass) and incidence angle = 40 degrees
    """Returns the angle of refraction from n (the index of refraction between the two media)
    and the angle of incidence (measured in degrees)."""

    try:
        r_angle = math.degrees(math.asin(math.sin(math.radians(
            incidence_angle)) / n))  # rearranged form of Snell's law with angles converted as necessary. asin function works only for radians.

        return round(r_angle, 2)  # rounds to 2 d.p.
    except ValueError:
        tkinter.messagebox.showerror(title="Domain error",
                                     message="Invalid combination of incidence angle and index of refraction.")


def main():
    """Gets user input, calls the refraction_angle function, and displays the output."""

    n = index_input.get()
    incidence_angle = incidence_input.get()

    if n.isalpha() or incidence_angle.isalpha():  # if either of the inputs are letters
        tkinter.messagebox.showerror(title="Letter(s) entered",
                                     message="Please enter valid numbers for the incidence angle and index of refraction.")  # displays warning pop-up window

    else:  # if both inputs are digits or decimals
        try:
            output = refraction_angle(float(n), float(incidence_angle))

            calc = tkinter.Label(root, text=output)
            calc.grid(row=10, column=2)
        except ValueError:
            tkinter.messagebox.showerror(title="Space or symbol entered",
                                         message="Invalid input.")  # displays warning pop-up window


calculate_button = tkinter.Button(root, text="Calculate Refraction Angle", command=main)
calculate_button.grid(row=7, column=2)

# Label
ttk.Label(text="Select Index Medium :",
          font=("Times New Roman", 10)).grid(column=1,
                                             row=3,)

n = tkinter.StringVar()
indexmedium = ttk.Combobox(width=18,
                            textvariable=n)

# Adding combobox drop down list
indexmedium['values'] = (' Glass',
                          ' Air',
                          ' Water',
                          )

indexmedium.grid(column=2, row=3)

# Shows Glass as default
indexmedium.current(0)


root.mainloop()
