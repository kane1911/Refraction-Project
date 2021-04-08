import math
import tkinter

root = tkinter.Tk()
my_canvas = tkinter.Canvas(root, width = 500, height = 500)
my_canvas.grid(row = 1, column = 3)

x1 = 250
x2 = 250
y1 = 0
y2 = 500

my_canvas.create_line(x1, y1, x2, y2) # y-axis

x3 = 0
x4 = 500
y3 = 250
y4 = 250

my_canvas.create_line(x3, y3, x4, y4) # x-axis

# incident angle laser

def ind_laser_x(ind_angle):
    x = 250 - (math.sin(math.radians(ind_angle)) * 250) # switched cos to sin so the angle of incidence is relative to the normal

    return x


def ind_laser_y(ind_angle):
    y = 250 - (math.cos(math.radians(ind_angle)) * 250) # switched to cos so the angle of incidence is relative to the normal

    return y

my_canvas.create_line(ind_laser_x(40), ind_laser_y(40), 250, 250) # incidence ray ending at our origin (250,250)

# refraction angle laser

def refr_laser_x(refr_angle):
    x = 250 + (math.sin(math.radians(refr_angle)) * 250) # switched cos to sin so that the refraction angle is relative to the normal

    return x

def refr_laser_y(refr_angle):
    y = 250 + (math.cos(math.radians(refr_angle)) * 250) # switched cos to sin so that the refraction angle is relative to the normal

    return y

my_canvas.create_line(250, 250, refr_laser_x(25.37), refr_laser_y(25.37)) # refracted ray beginning at our origin (0,0)


def start_laser():
    pass
    

root.mainloop()

