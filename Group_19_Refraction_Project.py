import tkinter
from tkinter import ttk
import math
from tkinter import messagebox
import sys
import os
import webbrowser
import matplotlib.pyplot as plt


root = tkinter.Tk()
root.title("Group 19: Angle of Refraction Calculator")
root.geometry("1200x700")  # window size


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

        scrollbar.set(0)  # sets scrollbar to 0 degrees


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
    v_formatted = round(v / (10 ** 6), 1)  # reformats the velocity. 300000000 m/s becomes 300.0 x 10^6 m/s
    return v_formatted


def draw_coord_axes():
    """Draws the x and y coordinate axes."""
    my_canvas.create_line(250, 0, 250, 500)  # y-axis
    my_canvas.create_line(0, 250, 500, 250)  # x-axis


def clear_canvas():
    """Clears canvas and redraws coordinate axes."""
    my_canvas.delete(tkinter.ALL)

    draw_coord_axes()  # redraws axes


def medium_colour(medium):
    """Returns the colour of the refraction medium as an appropriate string. The r_medium parameter must be set to indexmedium2.get()."""
    medium_colours = {'Air': 'snow', 'Glass': 'light blue', 'Water': 'royal blue', 'Amber': 'goldenrod1',
                      'Diamond': 'light grey'}  # tkinter colour chart: http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter
    colour = medium_colours[medium]
    return colour


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

        else:  # if both inputs are digits or decimals between 0° and 90°
            r_angle = refraction_angle(n, float(incidence_angle))

            calculated_angle = tkinter.Label(frame, text=str(r_angle) + "°")  # concatenates degree symbol to
            calculated_angle.grid(row=5, column=2)

    except ValueError:
        tkinter.messagebox.showerror(title="Space or symbol entered",
                                     message="Invalid input.")  # displays warning pop-up window

    # ------------------
    my_canvas.create_rectangle(0, 0, 500, 500, fill=medium_colour(indexmedium1.get()),
                               outline='')  # draws a rectangle with the colour of the incidence medium

    my_canvas.create_arc(250 - 100, 250 - 100, 250 + 100, 250 + 100, start=0, extent=-180, fill=medium_colour(
        indexmedium2.get()))  # draws semicircle with the colour of the selected refraction medium

    draw_coord_axes()  # redraws axes

    # -------------Draws laser on canvas -------------
    my_canvas.create_line(ind_laser_x(float(scrollbar.get()), 1.25), ind_laser_y(float(scrollbar.get()), 1.25),
                          ind_laser_x(float(scrollbar.get())), ind_laser_y(float(scrollbar.get())),
                          width=12)  # the laser itself

    my_canvas.create_line(ind_laser_x(float(scrollbar.get())), ind_laser_y(float(scrollbar.get())), 250, 250,
                          fill="red", width=2)  # incidence ray ending at our origin (250,250)

    my_canvas.create_line(250, 250, refr_laser_x(r_angle), refr_laser_y(r_angle),
                          width=2)  # refracted ray beginning at our origin (0,0)

    tkinter.Button(frame, text="i", command=open_info_index).grid(row=6,
                                                                  column=4)  # shows button when 'calculat' is pressed
    tkinter.Button(frame, text="i", command=open_info_velocity1).grid(row=7,
                                                                      column=4)  # shows button when 'calculat' is pressed
    tkinter.Button(frame, text="i", command=open_info_velocity2).grid(row=8,
                                                                      column=4)  # shows button when 'calculat' is pressed

    # ----------Widgets showing additional calculations

    index_label = tkinter.Label(frame,
                                text="Refractive index from {} to {}:".format(indexmedium1.get(), indexmedium2.get()))
    index_label.grid(row=6, column=1, sticky="E")

    n_label = tkinter.Label(frame, text=str(n))  # displays the index of refractin between the two selected media
    n_label.grid(row=6, column=2)

    i_medium_v_label = tkinter.Label(frame, text="Velocity of light in {}:".format(indexmedium1.get()))
    i_medium_v_label.grid(row=7, column=1, sticky="E")

    i_medium_v = tkinter.Label(frame, text=str(find_v(find_abs_n(
        indexmedium1.get()))) + " x 10^6 m/s")  # displays the velocity of light in the incidence medium based on its absolute refractive index
    i_medium_v.grid(row=7, column=2)

    i_medium_v_label = tkinter.Label(frame, text="Velocity of light in {}:".format(indexmedium2.get()))
    i_medium_v_label.grid(row=8, column=1, sticky="E")

    i_medium_v = tkinter.Label(frame, text=str(find_v(find_abs_n(
        indexmedium2.get()))) + " x 10^6 m/s")  # displays the velocity of light in the refraction medium based on its absolute refractive index
    i_medium_v.grid(row=8, column=2)


# ------Canvas and scrollbar--------------------------------------------------------------------------------------------------------------------

my_canvas = tkinter.Canvas(root, width=500, height=500, background="white")  # canvas
my_canvas.grid(row=0, column=1)
scrollbar = tkinter.Scale(root, from_=-90, to=90, length=500, tickinterval=20, orient="horizontal",
                          command=scroll_bar)  # see https://www.python-course.eu/tkinter_sliders.php
scrollbar.grid(row=1, column=1)

scrollbar_label = tkinter.Label(root, text="Degrees")
scrollbar_label.grid(row=2, column=1)

draw_coord_axes()  # draws axes


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

    clear_canvas()  # clears canvas

    n = index_of_refraction(i_medium=indexmedium1.get(),
                            r_medium=indexmedium2.get())  # gets the index of refraction between the 2 selected media
    incidence_angle = incidence_input.get()  # gets incidence angle from the user's input in the Spinbox

    try:
        if not (-90 <= float(incidence_angle) <= 90):  # if the incidence angle entered is not in the interval [-90, 90]
            tkinter.messagebox.showerror(title="Angle out of range",
                                         message="Please enter an incidence angle between -90° and 90°.")  # displays warning pop-up window
        else:
            if incidence_angle.isalpha():  # if the angle input contains letters
                tkinter.messagebox.showerror(title="Letter(s) entered",
                                             message="Please enter a valid incidence angle.")  # displays error pop-up window

            else:  # if both inputs are digits or decimals between 0° and 90°
                r_angle = refraction_angle(n, float(incidence_angle))

                calculated_angle = tkinter.Label(frame, text=str(r_angle) + "°")  # concatenates degree symbol to
                calculated_angle.grid(row=5, column=2)

            # --------------------------
            scrollbar.set(incidence_angle)  # sets the scrollbar to the angle entered by the user in the spinbox
            my_canvas.create_rectangle(0, 0, 500, 500, fill=medium_colour(indexmedium1.get()),
                                       outline='')  # draws a rectangle with the colour of the incidence medium

            my_canvas.create_arc(250 - 100, 250 - 100, 250 + 100, 250 + 100, start=0, extent=-180, fill=medium_colour(
                indexmedium2.get()))  # draws semicircle with the colour of the selected refraction medium

            draw_coord_axes()  # redraws axes
            # -------------Draws laser on canvas -------------
            my_canvas.create_line(ind_laser_x(float(incidence_input.get()), 1.25),
                                  ind_laser_y(float(incidence_input.get()), 1.25),
                                  ind_laser_x(float(incidence_input.get())),
                                  ind_laser_y(float(incidence_input.get())), width=12)  # the laser itself

            my_canvas.create_line(ind_laser_x(float(incidence_input.get())), ind_laser_y(float(incidence_input.get())),
                                  250,
                                  250, fill="red", width=2)  # incidence ray ending at our origin (250,250)

            my_canvas.create_line(250, 250, refr_laser_x(r_angle), refr_laser_y(r_angle),
                                  width=2)  # refracted ray beginning at our origin (0,0)

            # ----------Widgets showing additional calculations that only display when the Calculate button is pressed:

            index_label = tkinter.Label(frame,
                                        text="Refractive index from {} to {}:".format(indexmedium1.get(),
                                                                                      indexmedium2.get()))
            index_label.grid(row=6, column=1, sticky="E")

            n_label = tkinter.Label(frame,
                                    text=str(n))  # displays the index of refractin between the two selected media
            n_label.grid(row=6, column=2)

            i_medium_v_label = tkinter.Label(frame, text="Velocity of light in {}:".format(indexmedium1.get()))
            i_medium_v_label.grid(row=7, column=1, sticky="E")

            i_medium_v = tkinter.Label(frame, text=str(find_v(find_abs_n(
                indexmedium1.get()))) + " x 10^6 m/s")  # displays the velocity of light in the incidence medium based on its absolute refractive index
            i_medium_v.grid(row=7, column=2)

            i_medium_v_label = tkinter.Label(frame, text="Velocity of light in {}:".format(indexmedium2.get()))
            i_medium_v_label.grid(row=8, column=1, sticky="E")

            i_medium_v = tkinter.Label(frame, text=str(find_v(find_abs_n(
                indexmedium2.get()))) + " x 10^6 m/s")  # displays the velocity of light in the refraction medium based on its absolute refractive index
            i_medium_v.grid(row=8, column=2)

    except ValueError:
        tkinter.messagebox.showerror(title="Space or symbol entered",
                                     message="Invalid input.")  # displays warning pop-up window


# -------------Window widgets in frame:

frame = tkinter.Frame(
    root)  # creates a frame for the other widgets. see: https://stackoverflow.com/questions/20149483/python-canvas-and-grid-tkinter
frame.grid(row=0, column=0, sticky="n", padx=40)  # sticky = "n" moves aligns widgets to the top of the window

scrollbar_angle = tkinter.StringVar(frame)
scrollbar_angle.set(str(scrollbar.get()))  # sets spinbox angle to the angle of the scrollbar

incidence_label = tkinter.Label(frame, text="Incidence Angle (°):")
incidence_label.grid(row=1, column=1, sticky="E")
incidence_input = tkinter.Spinbox(frame, from_=-90, to=90, wrap=True,
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

calculate_button = tkinter.Button(frame, text="Calculate",
                                  command=lambda: [main(), button_info_index(), button_info_velocity1(),
                                                   button_info_velocity2()])  # Calculate button runs the main() function
calculate_button.grid(row=4, column=2)

refraction_label = tkinter.Label(frame, text="Angle of Refraction:")
refraction_label.grid(row=5, column=1, sticky="E")
quit_button = tkinter.Button(frame, text="Quit app", command=root.destroy)  # quit button
quit_button.grid(row=12, column=2, pady=5)


#Resetting the canvas and default values

def myDelete():
    python = sys.executable
    os.execl(python, python, *sys.argv)

#delete button
DeleteButton = tkinter.Button(frame, text="Reset", command=lambda:[clear_canvas(),myDelete()])
DeleteButton.grid(row=11, column=2, pady=5)


#Added More info button that hyperlinks to physics classroom to learn more about refraction
def open():
    webbrowser.open("https://www.physicsclassroom.com/class/refrn/Lesson-2/Snell-s-Law")

More_label = tkinter.Label(frame, text="Learn more about refraction from physicsclassroom.com: ")
More_label.grid(row=10, column=1)
InfoButton = tkinter.Button(frame, text="More Info", command=open)
InfoButton.grid(row=10, column=2, pady=5)


# info buttons to show calculations

def open_info_angle():
    plt.figure("Refractive Angle Info")
    plt.text(0.5, 0.95, "The Refractive index is a material property that describes\n "
                   "how the material affects the speed of light travelling through it.\n Refractive index is usually represented by the symbol n,\n "
                   "or sometimes " + r"$\mathbf{\mu}$" + ".", fontsize=11, fontstyle='italic', weight='bold', ha='center', va='center', linespacing=2)
    plt.text(-0.1, 0.55, r"$\Rightarrow$" + "by rearranging the formula for the index of refraction one can \n  calculate the refraction angle:", fontsize=11, fontstyle='italic', linespacing=2)
    plt.text(0.325, 0.35, r"$\mathbf{\theta_r}$" + " = " + "arcsin(" + r"$\frac{\mathbf{sin}(\mathbf{\theta_i})}{\mathbf{n}}$" + ")", fontsize=14, weight='bold', bbox=dict(boxstyle = "square", facecolor = "white"))
    plt.axis(False)
    plt.show()


tkinter.Button(frame, text="i", command=open_info_angle).grid(row=5, column=4)

def button_info_index():
    tkinter.Button(frame, text="i", command=open_info_index).grid(row=6, column=4) # shows butten when calculate is pressed

def open_info_index():
    plt.figure("Refractive Index Info")
    plt.text(0.5, 1, "The angle made by a refracted ray perpendicular to \n the refracting surface", fontsize=11, fontstyle='italic', weight='bold', ha='center', va='center', linespacing=2)
    plt.text(-0.1, 0.75, r"$\Rightarrow$" + "when both the incidence angle (" + r"$\theta_i$" + ") and refractive angle are given (" + r"$\theta_r$" + "):", fontsize=11, fontstyle='italic')
    plt.text(0.375, 0.6, r"$\frac{\mathbf{sin}(\mathbf{\theta_i})}{\mathbf{sin}(\mathbf{\theta_r})}$" + " = " + "n", fontsize=14, weight='bold', bbox=dict(boxstyle = "square", facecolor = "white"))
    plt.text(-0.1, 0.25, r"$\Rightarrow$" + "when indices of both media are given:", fontsize=11, fontstyle='italic')
    plt.text(0.395, 0.1, r"$\frac{\mathbf{n_i}}{\mathbf{n_r}}$" + " = " + "n", fontsize=14, weight='bold', bbox=dict(boxstyle = "square", facecolor = "white"))
    plt.axis(False)
    plt.show()



def button_info_velocity1():
    tkinter.Button(frame, text="i", command=open_info_velocity1).grid(row=7,
                                                                      column=4)  # shows button when 'calculat' is pressed


def open_info_velocity1():
    plt.figure("Velocity of Light Info")
    plt.text(0.5, 0.95, "The velocity of light varies depending on the material of the medium, \n"
                        " the optically denser it gets the faster the waves travel.\n"
                        " This causes the ray to bend at an angle,\n"
                        " a phenomenon known as refraction.", fontsize=11, fontstyle='italic', weight='bold',
             ha='center',
             va='center', linespacing=2)
    plt.text(-0.1, 0.6,
             r"$\Rightarrow$" + "The velocity can be calculate using the index of refraction (n) of the given\n"
                                " medium and the speed of light through a vacuum (c = " + r"$300 \times 10^{6}$" + " m " + r"$s^{-1}$" + "):",
             fontsize=11, fontstyle='italic')
    plt.text(0.45, 0.45, "v = " + r"$\frac{\mathbf{c}}{\mathbf{n}}$",
             fontsize=14, weight='bold', bbox=dict(boxstyle="square", facecolor="white"))
    plt.axis(False)
    plt.show()


def button_info_velocity2():
    tkinter.Button(frame, text="i", command=open_info_velocity2).grid(row=8,
                                                                      column=4)  # shows button when 'calculat' is pressed


def open_info_velocity2():
    plt.figure("Velocity of Light Info")
    plt.text(0.5, 0.95, "The velocity of light varies depending on the material of the medium, \n"
                        " the optically denser it gets the faster the waves travel.\n"
                        " This causes the ray to bend at an angle,\n"
                        " a phenomenon known as refraction.", fontsize=11, fontstyle='italic', weight='bold',
             ha='center',
             va='center', linespacing=2)
    plt.text(-0.1, 0.6,
             r"$\Rightarrow$" + "The velocity can be calculate using the index of refraction (n) of the given\n"
                                " medium and the speed of light through a vacuum (c = " + r"$300 \times 10^{6}$" + " m " + r"$s^{-1}$" + "):",
             fontsize=11, fontstyle='italic')
    plt.text(0.45, 0.45, "v = " + r"$\frac{\mathbf{c}}{\mathbf{n}}$",
             fontsize=14, weight='bold', bbox=dict(boxstyle="square", facecolor="white"))
    plt.axis(False)
    plt.show()


root.mainloop()