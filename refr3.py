# 17/03/2021 Barnabas

import math  # used for trig and angle conversion methods


def refraction_angle(n=1.5,
                     incidence_angle=40):  # function has default values of index of refraction = 1.5 (air to glass) and incidence angle = 40 degrees
    """Returns the angle of refraction from n (the index of refraction between the two media)
    and the angle of incidence (measured in degrees)."""

    r_angle = math.degrees(math.asin(math.sin(math.radians(
        incidence_angle)) / n))  # rearranged form of Snell's law with angles converted as necessary. asin function works only for radians.

    return round(r_angle, 2)  # rounds to 2 d.p.


def main():
    """Gets user input, calls the refraction_angle function, and displays the output."""

    n = input("Enter the index of refraction between the two media: ")
    incidence_angle = input("Enter the angle of incidence (in degrees): ")
    # ----------------------------------
    # this block allows the user to use the default values of n and incidence angle by just pressing Enter

    if n == '' and incidence_angle == '':  # if user enters nothing (an empty string)
        output = refraction_angle()  # default values will be used
    elif n == '':  # if user leaves n blank
        output = refraction_angle(incidence_angle=float(incidence_angle))
    elif incidence_angle == '':  # if user leaves incidence angle blank
        output = refraction_angle(n=float(n))
    else:  # if the user enters both n and incidence angle
        output = refraction_angle(float(n), float(incidence_angle))
    # ----------------------------------------------------------------------
    print("Angle of refraction:", output, "degrees")

    #Kane Langmead 15/3/2021
#Given m1 is glass and m2 is water
m1=1.5
m2=1.33

#Calculation of critical
u1=m1/m2
sinC=1/u1
C=math.asin(sinC)*180/3.14

#Result of m1/m2
print("Critical angle is", round(C,2),"degree from glass to water")

main()  # calls the main function (that calls everything else)

#github test1

# Barnabas' test: Hey everyone!
# Refraction Project Nikolay Hello
