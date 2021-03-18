import tkinter
import math

root = tkinter.Tk()
root.title("Calculating Angle of Refraction")

incidence_label = tkinter.Label(root, text = "Incidence Angle:")
incidence_label.grid(row = 1, column = 1, sticky = "E")
incidence_input = tkinter.Entry(root)
incidence_input.grid(row = 1, column = 2)

index_label = tkinter.Label(root, text = "Index of Refraction:")
index_label.grid(row = 2, column = 1, sticky = "E")
index_input = tkinter.Entry(root)
index_input.grid(row = 2, column = 2)

def refraction_angle(n=1.5,
                     incidence_angle=40):  # function has default values of index of refraction = 1.5 (air to glass) and incidence angle = 40 degrees
    """Returns the angle of refraction from n (the index of refraction between the two media)
    and the angle of incidence (measured in degrees)."""

    r_angle = math.degrees(math.asin(math.sin(math.radians(
        incidence_angle)) / n))  # rearranged form of Snell's law with angles converted as necessary. asin function works only for radians.

    return round(r_angle, 2)  # rounds to 2 d.p.

def main():
    """Gets user input, calls the refraction_angle function, and displays the output."""

    n = index_input.get()
    incidence_angle = incidence_input.get()

    output = refraction_angle(float(n), float(incidence_angle))

    calc = tkinter.Label(root, text = output)
    calc.grid(row = 3, column = 3)


calculate_button = tkinter.Button(root, text = "Calculate Refraction Angle", command = main())
calculate_button.grid(row = 3, column = 2)


root.mainloop()