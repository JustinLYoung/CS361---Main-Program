import json
from json import loads, dumps


"""This is a file used for suggested workout prompts."""

def chest():
    while True:
        print("\n")
        print("""    1 - Chest
        -------------------------------------
        Bench Press     3 X 8-10
        Pec Deck        3 x 8-10
        Incline Press   3 x 8-10
        Cable Flies     3 x 8-10
        -------------------------------------
        Have a great workout!""")
        user_select = int(input("Enter 0 for previous screen "))
        if user_select == 0:
            break


def back():
    while True:
        print("\n")
        print("""2 - Back
        -------------------------------------
        Pull-ups        3 x to failure
        Bent over Row   3 X 8-10
        Lat Pulldown    3 x 8-10
        Seated Row      3 x 8-10
        Deadlift        3 x 6-8
        Reverse Flies   3 x 10-12
        -------------------------------------
        Have a great workout!""")
        user_select = int(input("Enter 0 for previous screen "))
        if user_select == 0:
            break

def biceps():
    while True:
        print("\n")
        print("""3 - Biceps
    -------------------------------------
    Barbell/Dumbell curl  3 X 8-10
    Hammer curl           3 X 8-10
    Preacher curl         3 x 8-10
    Cable curl            3 x 8-10
    Concentraction curl   3 x 8-10
    -------------------------------------
        Have a great workout!""")
        user_select = int(input("Enter 0 for previous screen "))
        if user_select == 0:
            break

def triceps():
    while True:
        print("\n")
        print("""4 - Triceps - 0 to return to main
    -------------------------------------
    Cable pulldown   3 X 8-10
    Overhead rope    3 X 8-10
    Skull crushers   3 x 8-10
    Dips             3 x 8-10
    Cable kickbacks  3 x 8-10
    -------------------------------------
        Have a great workout!""")
        user_select = int(input("Enter 0 for previous screen "))
        if user_select == 0:
            break

def shoulders():
    while True:
        print("\n")
        print("""5 - Shoulders - 0 to return to main
    -------------------------------------
    Overhead Press   3 X 8-10
    Side Laterals    3 X 8-10
    Read Delt Fly    3 x 8-10
    Shrugs           3 x 8-10
    Facepulls        3 x 10-12
    -------------------------------------
        Have a great workout!""")
        user_select = int(input("Enter 0 for previous screen "))
        if user_select == 0:
            break

def legs():
    while True:
        print("\n")
        print("""6 - Legs - 0 to return to main
    -------------------------------------
    Squats           3 X 6-8
    Legs Extensions  3 X 8-10
    Hamstring Curls  3 x 8-10
    Calf Raises      3 x 8-10
    Lunges           3 x 10-12
    -------------------------------------
        Have a great workout!""")
        user_select = int(input("Enter 0 for previous screen "))
        if user_select == 0:
            break

def ab():
    while True:
        print("\n")
        print("""7 - Abs - 0 to return to main
    -------------------------------------
    Cable crunch    3 X 12-15
    Leg Raises      3 X 8-10
    Plank           30s - 1 min
    Reverse crunch  3 x 8-10
    Russian Twist   3 x 10-12
    --------------------------------------
        Have a great workout!""")
        user_select = int(input("Enter 0 for previous screen "))
        if user_select == 0:
            break

def body_upper():
    while True:
        print("\n")
        print("""    1 - Upper Body
        -------------------------------------
        Push Up           3 X 8-10
        Bench Dip         3 x 8-10
        Incline Push Up   3 x 8-10
        Wide-Grip Push up 3 x 8-10
        Forearm Plank     Until failure
        Diamond Push Up   3 x 8-10
        -------------------------------------
        Have a great workout!""")
        user_select = int(input("Enter 0 for previous screen "))
        if user_select == 0:
            break

def body_lower():
    while True:
        print("\n")
        print("""    2 - Lower Body
        -------------------------------------
        Air Squat         3 X 8-10
        Lunges            3 x 8-10
        Burpee            3 x 8-10
        Jump Squat        3 x 8-10
        Calf Raises       3 x 12-15
        -------------------------------------
        Have a great workout!""")
        user_select = int(input("Enter 0 for previous screen "))
        if user_select == 0:
            break
