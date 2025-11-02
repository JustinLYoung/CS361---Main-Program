# prompts for suggested workouts
from prompts import *
from records import *
from json import loads, dumps
from steps import *
import datetime
import subprocess

# global variable to store goals
goal_list = []


# Open Goal_list File
try:
    infile = open("goal_list.txt", "r")
    line = infile.readline()
    while line:
        goal_list.append(line.rstrip("\n").split(","))
        line = infile.readline()
    infile.close()
except FileNotFoundError:
    print("No Goals Set")


def intro():
    print("\n")
    print("""Welcome To Your Fitness Journey      
------------------------------------
Multifunctional App to help you on your fitness journey.  
Keep track of your progress and provide suggested workout 
routines.  
By checking in, your day will be recorded.
------------------------------------
Enter 1 to check-in
Enter 0 to exit
------------------------------------""")
    choice = int(input("Please make selection: "))
    return choice
            

def main_menu():
    today = datetime.date.today()
    with open("check_in_log.txt", "a") as f:
        f.write(f"{today}\n")
    print("\n")
    print("""1 - Check in (Main)
------------------------------------""")
    print(f"You are checked in for {today}")
    print("You can view each category by selecting a number.")
    print("Entering 0 will always take you back 1 screen.")
    print("""------------------------------------
    1 - Goals
    2 - Suggested Workouts (requires weights)
    3 - Bodyweighted Workouts
    4 - Step Count
    5 - Progress
    6 - Peronal Records
    7 - Erase Data
    0 - Return to previous screen
-------------------------------------""")
    choice = int(input("Please make selection: "))
    return choice


def goals():
    while True:
        print("\n")
        print("""1 - Goals
-------------------------------------
You can set personal goals for yourself by
selecting 2 and typing in your own goal.
To review the goals you have set you can select
1 to view your goals.
-------------------------------------
1 - View goals
2 - Enter New Goal
0 - Return to previous screen
-------------------------------------""")
        choice = int(input("Please make selection: "))
        if choice == 1:
            print("\n")
            print("Here are your goals: ")
            print(goal_list)
        elif choice == 2:
            goal = input("My goal: ")
            goal_list.append([goal])
            outfile = open("goal_list.txt", "w")
            for goal in goal_list:
                outfile.write("".join(goal) + "\n")
            outfile.close()
            print(goal_list)
        elif choice == 0:
            break

def suggested_workouts():
    while True:
        print("\n")
        print("""2 - Suggested Workouts
-------------------------------------
1 - Chest
2 - Back
3 - Biceps
4 - Triceps
5 - Shoulders
6 - Legs
7 - Abs
8 - Open Website (Addition Exercises)
0 - Return to previous screen
-------------------------------------""")
        choice = int(input("Please make selection: "))
        if choice == 1:
            chest()
        elif choice == 2:
            back()
        elif choice == 3:
            biceps()
        elif choice == 4:
            triceps()
        elif choice == 5:
            shoulders()
        elif choice == 6:
            legs()
        elif choice == 7:
            ab()
        elif choice == 8:
            url = "https://www.muscleandstrength.com/workouts/6-day-powerbuilding-split-meal-plan"
            subprocess.run(["xdg-open", url])
        elif choice == 0:
            break

def personal_records():
    while True:
        print("\n")
        print("""6 - Personal Records
-------------------------------------
1 - Bench Press
2 - Squat
3 - Deadlift
0 - Return to previous screen
-------------------------------------""")
        choice = int(input("Please make selection: "))
        if choice == 1:
            bench_record()
        elif choice == 2:
            squat_record()
        elif choice == 3:
            deadlift_record()
        elif choice == 0:
            break

def step_count():
    while True:
        print("\n")
        print("""4 - Step Count
-------------------------------------
1 - Enter Daily Steps
2 - View Step History
0 - Return to previous menu
-------------------------------------""")
        choice = int(input("Please make selection: "))
        if choice == 1:
            user_steps = input("Enter number of steps: ")
            enter_steps(user_steps)
        elif choice == 2:
            view_steps()
        elif choice == 0:
            break

def daily_progress():
    used_dates = set()
    try:
        with open("check_in_log.txt", "r") as f:
            for line in f:
                date_str = line.strip()
                if date_str:
                    used_dates.add(date_str)
    except FileNotFoundError:
        pass
    return len(used_dates)

def progress():
    while True:
        print("\n")
        print("""5 - Progress
-------------------------------------
1 - View Progress
0 - Return to previous screen
-------------------------------------""")
        choice = int(input("Please make selection: "))
        if choice == 1:
            days = daily_progress()
            print(f"You have worked out for {days} day(s)! \n")
        if choice == 0:
            break

def erase():
    # >>>>>>>>>>>>>>NEED TO DELTE ALL FILES - NOT WORKING YET.<<<<<<<<<<<<<<<<<<<<<<
    while True:
        print("\n")
        print("""7 - Erase data 
-------------------------------------
1 - Confirm Erase (data will be lost)
0 - Return to previous menu
-------------------------------------""")
        choice = int(input("Please make selection: "))
        if choice == 1:
            print("Are you sure you want to delete all data?")
            choice = int(input("1 to delete, 0 to previous menu "))
            if choice == 1:
                print("Data has been deleted")
            elif choice == 0:
                break
        elif choice == 0:
            break

def body_weight():
    while True:
        print("\n")
        print("""3 - Body Weight Workouts
-------------------------------------
1 - Upper Body
2 - Lower Body
3 - Open Website (Addition Exercises)
0 - Return to previous screen
-------------------------------------""")
        choice = int(input("Please make selection: "))
        if choice == 1:
            body_upper()
        elif choice == 2:
            body_lower()
        elif choice == 2:
            url = "https://www.nerdfitness.com/blog/beginner-body-weight-workout-burn-fat-build-muscle/"
            subprocess.run(["xdg-open", url])

        elif choice == 0:
            break


while True:
    app_start = intro()
    if app_start == 1:
        while True:
            main_start = main_menu()
            # Exits to main menu
            if main_start == 0:
                break
            elif main_start == 1:
                goals()
            elif main_start == 2:
                suggested_workouts()
            elif main_start == 3:
                body_weight()
            elif main_start == 4:
                step_count()
            elif main_start == 5:
                progress()
            elif main_start == 6:
                personal_records()
            elif main_start == 7:
                erase()
    elif app_start == 0:
        print("Thank you for using the fitness app")
        break
                
                
            