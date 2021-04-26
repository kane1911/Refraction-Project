import tkinter
from tkinter import ttk
import math
from tkinter import messagebox
import matplotlib.pyplot as plt

root = tkinter.Tk()
root.title("Group 19: Angle of Refraction Calculator")
root.geometry("950x600")  # window size



def refraction_angle(n, incidence_angle):
    """Returns the angle of refraction from n (the index of refraction between the two media)
    and the angle of incidence (measured in degrees)."""

    try:
        r_angle = math.degrees(math.asin(math.sin(math.radians(
            incidence_angle)) / n))  # rearranged form of Snell's law with angles converted as necessary. asin function works only for radians.

        return round(r_angle, 2)  # rounds to 2 d.p.
    except ValueError:
        tkinter.messagebox.showerror(title="Domain error",
                                     message="Invalid combination of incidence angle and index of refraction.")


def index_of_refraction(i_medium, r_medium):
    """Returns the index of refraction between the incidence medium (i_medium) and the refraction medium (r_medium)."""

    abs_index = {'Air': 1, 'Glass': 1.5, 'Water': 1.333, 'Amber': 1.55,
                 'Diamond': 2.417}  # obtained from: https://en.wikipedia.org/wiki/List_of_refractive_indices

    n_i = abs_index[
        i_medium]  # finds the index of refraction of the incidence medium from the key provided from the drop down menu
    n_r = abs_index[
        r_medium]  # finds the index of refraction of the refraction medium from the key provided from the drop down menu
    i_n_r = round(n_r / n_i, 3)  # calcs the relative index of refraction between the media
    return i_n_r


def find_abs_n(medium):
    """Returns the absoulute refracive index of the given medium."""
    abs_index = {'Air': 1, 'Glass': 1.5, 'Water': 1.333, 'Amber': 1.55,
                 'Diamond': 2.417}  # obtained from: https://en.wikipedia.org/wiki/List_of_refractive_indices
    abs_n = abs_index[medium]
    return abs_n


def find_v(abs_n):
    '''This function will calculate the v (velocity of light) by taking the absolute refractive index from the user's medium selections.'''
    # Calculate v
    v = round(300000000 / float(abs_n), 3)
    v_formatted = round(v/(10**6), 1) # reformats the velocity. 300000000 m/s becomes 300.0 x 10^6 m/s
    return v_formatted


def clear_canvas():
    """Clears canvas and redraws coordinate axes."""
    my_canvas.delete(tkinter.ALL)

    my_canvas.create_arc(250 - 100, 250 - 100, 250 + 100, 250 + 100, start=0, extent=-180,
                         fill="light blue")  # refraction medium
    my_canvas.create_line(250, 0, 250, 500)  # y-axis
    my_canvas.create_line(0, 250, 500, 250)  # x-axis



def scroll_bar(angle):
    """FUnction called each time the scrollbar is moved. the angle parameter does nothing, but has to be there else there is this error:
    'TypeError: scroll_bar() takes 0 positional arguments but 1 was given'."""

    scrollbar_angle.set(str(scrollbar.get()))  # sets the spinbox with the value of the scrollbar
    clear_canvas()  # calls the function that clears the canvas and draws the axes

    n = index_of_refraction(i_medium=indexmedium1.get(),
                            r_medium=indexmedium2.get())  # gets the index of refraction between the 2 selected media
    incidence_angle = str(scrollbar.get())  # gets incidence angle from the scrollbar

    try:
        if incidence_angle.isalpha():  # if the angle input contains letters
            tkinter.messagebox.showerror(title="Letter(s) entered",
                                         message="Please enter a valid incidence angle.")  # displays error pop-up window

        elif not (0 <= float(incidence_angle) <= 90):  # if the incidence angle entered is not in the interval [0, 90]
            tkinter.messagebox.showerror(title="Angle out of range",
                                         message="Please enter an incidence angle between 0° and 90°.")  # displays warning pop-up window

        else:  # if both inputs are digits or decimals between 0° and 90°
            r_angle = refraction_angle(n, float(incidence_angle))

            calculated_angle = tkinter.Label(frame, text=str(r_angle) + "°")  # concatenates degree symbol to
            calculated_angle.grid(row=5, column=2)

    except ValueError:
        tkinter.messagebox.showerror(title="Space or symbol entered",
                                     message="Invalid input.")  # displays warning pop-up window





 # -------------Draws laser on canvas -------------
    my_canvas.create_line(ind_laser_x(float(scrollbar.get()), 1.25), ind_laser_y(float(scrollbar.get()), 1.25),
                          ind_laser_x(float(scrollbar.get())), ind_laser_y(float(scrollbar.get())),
                          width=12)  # the laser itself

    my_canvas.create_line(ind_laser_x(float(scrollbar.get())), ind_laser_y(float(scrollbar.get())), 250, 250,
                          fill="red", width=2)  # incidence ray ending at our origin (250,250)

    my_canvas.create_line(250, 250, refr_laser_x(r_angle), refr_laser_y(r_angle),
                          width=2)  # refracted ray beginning at our origin (0,0)

    tkinter.Button(frame, text="i", command=open_info_index).grid(row=6, column=4)  # shows button when 'calculat' is pressed
    tkinter.Button(frame, text="i", command=open_info_velocity1).grid(row=7,
                                                                      column=4)  # shows button when 'calculat' is pressed
    tkinter.Button(frame, text="i", command=open_info_velocity2).grid(row=8,
                                                                      column=4)  # shows button when 'calculat' is pressed

    # ----------Widgets showing additional calculations

    index_label = tkinter.Label(frame,
                                text="Refractive index from {} to {}:".format(indexmedium1.get(), indexmedium2.get()))
    index_label.grid(row=6, column=1)

    n_label = tkinter.Label(frame, text=str(n))  # displays the index of refractin between the two selected media
    n_label.grid(row=6, column=2)

    i_medium_v_label = tkinter.Label(frame, text="Velocity of light in {}:".format(indexmedium1.get()))
    i_medium_v_label.grid(row=7, column=1, sticky="E")

    i_medium_v = tkinter.Label(frame, text=str(find_v(find_abs_n(
        indexmedium1.get()))) + " m/s")  # displays the velocity of light in the incidence medium based on its absolute refractive index
    i_medium_v.grid(row=7, column=2)

    i_medium_v_label = tkinter.Label(frame, text="Velocity of light in {}:".format(indexmedium2.get()))
    i_medium_v_label.grid(row=8, column=1, sticky="E")

    i_medium_v = tkinter.Label(frame, text=str(find_v(find_abs_n(
        indexmedium2.get()))) + " m/s")  # displays the velocity of light in the refraction medium based on its absolute refractive index
    i_medium_v.grid(row=8, column=2)


# ------Canvas and scrollbar--------------------------------------------------------------------------------------------------------------------

my_canvas = tkinter.Canvas(root, width = 500, height = 500, background = "white") # canvas
my_canvas.grid(row = 0, column = 1)
scrollbar = tkinter.Scale(root, from_=0, to=90, length=500, tickinterval=10, orient="horizontal", command=scroll_bar) #see https://www.python-course.eu/tkinter_sliders.php
scrollbar.grid(row=1, column = 1)

# semi-circle as refraction medium

my_canvas.create_arc(250-100, 250-100, 250+100, 250+100, start=0, extent=-180, fill="light blue")


x1 = 250
x2 = 250
y1 = 0
y2 = 500
my_canvas.create_line(x1, y1, x2, y2)  # y-axis

x3 = 0
x4 = 500
y3 = 250
y4 = 250
my_canvas.create_line(x3, y3, x4, y4)  # x-axis


def ind_laser_x(ind_angle, scale=1):
    """Calcs incident angle laser x-coord. The scale parameter is used to draw the laser source."""
    x = 250 - (math.sin(math.radians(ind_angle)) * 200 * scale)
    return x


def ind_laser_y(ind_angle, scale=1):
    """Calcs incident angle laser y-coord. The scale parameter is used to draw the laser source."""
    y = 250 - (math.cos(math.radians(ind_angle)) * 200 * scale)
    return y


def refr_laser_x(refr_angle):
    """Calcs refraction angle laser x-coord."""
    x = 250 + (math.sin(math.radians(refr_angle)) * 200)
    return x


def refr_laser_y(refr_angle):
    """Calcs refraction angle laser y-coord."""
    y = 250 + (math.cos(math.radians(refr_angle)) * 200)
    return y


# ----------------------------------------------------------------------------------------------------------------------------------------------------

def main():
    """Combines user input from the Spinbox and Comboboxes (drop-down menus) with the refraction_angle function, and displays the output."""

    n = index_of_refraction(i_medium=indexmedium1.get(),
                            r_medium=indexmedium2.get())  # gets the index of refraction between the 2 selected media
    incidence_angle = incidence_input.get()  # gets incidence angle from the user's input in the Spinbox

    try:
        if incidence_angle.isalpha():  # if the angle input contains letters
            tkinter.messagebox.showerror(title="Letter(s) entered",
                                         message="Please enter a valid incidence angle.")  # displays error pop-up window

        elif not (0 <= float(incidence_angle) <= 90):  # if the incidence angle entered is not in the interval [0, 90]
            tkinter.messagebox.showerror(title="Angle out of range",
                                         message="Please enter an incidence angle between 0° and 90°.")  # displays warning pop-up window

        else:  # if both inputs are digits or decimals between 0° and 90°
            r_angle = refraction_angle(n, float(incidence_angle))

            calculated_angle = tkinter.Label(frame, text=str(r_angle) + "°")  # concatenates degree symbol to
            calculated_angle.grid(row=5, column=2)

    except ValueError:
        tkinter.messagebox.showerror(title="Space or symbol entered",
                                     message="Invalid input.")  # displays warning pop-up window


    # -------------Draws laser on canvas -------------
    my_canvas.create_line(ind_laser_x(float(incidence_input.get()), 1.25),
                          ind_laser_y(float(incidence_input.get()), 1.25), ind_laser_x(float(incidence_input.get())),
                          ind_laser_y(float(incidence_input.get())), width=12)  # the laser itself

    my_canvas.create_line(ind_laser_x(float(incidence_input.get())), ind_laser_y(float(incidence_input.get())), 250,
                          250, fill="red", width=2)  # incidence ray ending at our origin (250,250)

    my_canvas.create_line(250, 250, refr_laser_x(r_angle), refr_laser_y(r_angle),
                          width=2)  # refracted ray beginning at our origin (0,0)

    # ----------Widgets showing additional calculations that only display when the Calculate button is pressed:

    index_label = tkinter.Label(frame,
                                text="Refractive index from {} to {}:".format(indexmedium1.get(), indexmedium2.get()))
    index_label.grid(row=6, column=1)

    n_label = tkinter.Label(frame, text=str(n))  # displays the index of refractin between the two selected media
    n_label.grid(row=6, column=2)

    i_medium_v_label = tkinter.Label(frame, text="Velocity of light in {}:".format(indexmedium1.get()))
    i_medium_v_label.grid(row=7, column=1, sticky="E")

    i_medium_v = tkinter.Label(frame, text=str(find_v(find_abs_n(indexmedium1.get()))) + " x 10^6 m/s")  # displays the velocity of light in the incidence medium based on its absolute refractive index
    i_medium_v.grid(row=7, column=2)

    i_medium_v_label = tkinter.Label(frame, text="Velocity of light in {}:".format(indexmedium2.get()))
    i_medium_v_label.grid(row=8, column=1, sticky="E")

    i_medium_v = tkinter.Label(frame, text=str(find_v(find_abs_n(indexmedium2.get()))) + " x 10^6 m/s")  # displays the velocity of light in the refraction medium based on its absolute refractive index
    i_medium_v.grid(row=8, column=2)


# -------------Window widgets in frame:

frame = tkinter.Frame(
    root)  # creates a frame for the other widgets. see: https://stackoverflow.com/questions/20149483/python-canvas-and-grid-tkinter
frame.grid(row=0, column=0, sticky="n")  # sticky = "n" moves aligns widgets to the top of the window

scrollbar_angle = tkinter.StringVar(frame)
scrollbar_angle.set(str(scrollbar.get()))  # sets spinbox angle to the angle of the scrollbar

incidence_label = tkinter.Label(frame, text="Incidence Angle (°):")
incidence_label.grid(row=1, column=1, sticky="E")
incidence_input = tkinter.Spinbox(frame, from_=0, to=90, wrap=True,
                                  textvariable=scrollbar_angle)  # Spinbox only accepts from a certain range of inputs (0 to 90 degrees)
incidence_input.grid(row=1, column=2)

ttk.Label(frame, text="Select Incidence Medium:").grid(row=2, column=1, sticky="E")  # incidence medium drop down menu
n1 = tkinter.StringVar()
indexmedium1 = ttk.Combobox(frame, width=18, textvariable=n1)
indexmedium1['values'] = ('Air', 'Glass', 'Water')
indexmedium1[
    'state'] = 'readonly'  # means the user cannot directly enter a value into the combobx see:https://www.pythontutorial.net/tkinter/tkinter-combobox/
indexmedium1.grid(row=2, column=2)
indexmedium1.current(0)  # Shows Air as default

ttk.Label(frame, text="Select Refraction Medium:").grid(row=3, column=1, sticky="E")  # refraction medium drop down menu
n2 = tkinter.StringVar()
indexmedium2 = ttk.Combobox(frame, width=18, textvariable=n2)
indexmedium2['values'] = ('Air', 'Glass', 'Water', 'Amber', 'Diamond')
indexmedium2[
    'state'] = 'readonly'  # means the user cannot directly enter a value into the combobx see:https://www.pythontutorial.net/tkinter/tkinter-combobox/
indexmedium2.grid(row=3, column=2)
indexmedium2.current(1)  # Shows Glass as default

calculate_button = tkinter.Button(frame, text="Calculate", command=lambda:[main(), button_info_index(), button_info_velocity1(), button_info_velocity2()])  # Calculate button runs the main() function
calculate_button.grid(row=4, column=2)

refraction_label = tkinter.Label(frame, text="Angle of Refraction:")
refraction_label.grid(row=5, column=1, sticky="E")

clear_button = tkinter.Button(frame, text="Clear canvas", command=clear_canvas)
clear_button.grid(row=9, column=2)

# info buttons to show calculations

def open_info_angle():
    messagebox.showinfo("Calculations", "Hello info")

tkinter.Button(frame, text = "i", command = open_info_angle).grid(row = 5, column = 4)



def button_info_index():
    tkinter.Button(frame, text = "i", command = open_info_index).grid(row = 6, column = 4) # shows button when 'calculat' is pressed

def open_info_index():
    plt.figure()
    plt.text(0.5, 0.5, r"$\frac{\sin(\theta_i)}{\sin(\theta_r)}$" + " = " r"$\frac{c_i}{c_r}$" + " = " + "n", fontsize=20)
    plt.text(1, 1, r"$\frac{n_i}{n_r}$" + " = " + r"$\ _i$" + r"$\n_r$", fontsize = 20)
    plt.axis(False)
    plt.show()





def button_info_velocity1():
    tkinter.Button(frame, text="i", command=open_info_velocity1).grid(row=7, column=4) # shows button when 'calculat' is pressed

def open_info_velocity1():
    messagebox.showinfo("Calculations", "Hello info")


def button_info_velocity2():
    tkinter.Button(frame, text="i", command=open_info_velocity2).grid(row=8, column=4) # shows button when 'calculat' is pressed

def open_info_velocity2():
    messagebox.showinfo("Calculations", "Hello info")





root.mainloop()