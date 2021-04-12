
def find_n():
    '''This function will calculate the value of n by taking the value of v by the user'''


    print("\n:: Find N ::")
    #input v value from user
    v_value = input("Please enter value of V (m/s) : ")

    #Test if value is numeric
    done = True
    while not done:
        try:
            v_value = float(v_value)
            done=True
        except:
            print("Please enter a number only! ")
            v_value = input("Please enter value of V (m/s) : ")
            done=False

    #Calculate n
    n = round(300000000 / float(v_value),3)


    #print answer
    print(f"V-value : {v_value}")
    print(f"C-value : 300000 km/s")
    print("--The Answer : \n")
    print(f"N-value : {n}")
    return
def find_v():
    '''This function will calculate the value of v by taking the value of n by the user'''


    print("\n:: Find V ::")
    # input n value from user
    n_value = input("Please enter value of N : ")


    # Test if value is numeric
    done = True
    while not done:
        try:
            n_value = float(n_value)
            done = True
        except:
            print("Please enter a number only! ")
            n_value = input("Please enter value of N : ")
            done = False

    # Calculate v
    v = round(300000000 / float(n_value), 3)

    print(f"N-value : {n_value}")
    print(f"C-value : 300000 km/s")
    print("--The Answer : \n")
    print(f"V-value : {v} m/s")
    return


def main():
    '''This is the function where user can choose which function to run according to his requirement of finding n or v.'''

    
    print("\n:: Menu ::")
    print("(1) Find N (input V)")
    print("(2) Find V (input N)")

    #Take input from user to choose which function to run
    user_choice = input("Please choose between 1 or 2 : ")
    while user_choice not in ["1","2"]:
        print("Please only choose between 1 or 2!")
        user_choice = input("Please choose between 1 or 2 : ")
    if user_choice=="1":
        find_n()
    else:
        find_v()
    return

if __name__ == '__main__':
    print("--------------Refractive Index--------------")
    print("Equation :    N = C/V")
    print("N : Refractive Index")
    print("C : Speed of Light (Vacuum)")
    print("V : Phase Velocity of Light")
    user_input = "y"

    #Loop until the user presses y, if user presses n then quit
    while user_input!="n":
        main()
        user_input = input("\n\nDo you want to calculate again? ( y/n ) : ")
        while user_input.lower() not in ["y","n","yes","no"]:
            print("Please enter correct answer i.e. y or n.")
            user_input = input("Do you want to calculate again? ( y/n ) : ")
        if user_input.lower()=="y" or user_input.lower()=="yes":
            pass
        else:
            print("\nGoodbye :)")
            break