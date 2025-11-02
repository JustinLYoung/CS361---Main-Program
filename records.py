import json
from json import loads, dumps
bench = 0
squat = 0
deadlift = 0

# Open json file for bench
file_path = "bench.json"

try:
    with open(file_path, 'r') as f:
        bench = json.load(f)
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")

# open json file for squat
file_path = "squat.json"

try:
    with open(file_path, 'r') as f:
        squat = json.load(f)
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")

# open json file for deadlift
file_path = "deadlift.json"

try:
    with open(file_path, 'r') as f:
        deadlift = json.load(f)
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")


def bench_record():
    global bench
    while True:
        print("1 - Bench - 0 to return to previous menu")
        print("-------------------------------------")
        print(f"Current Record {bench} lbs")
        print("1 - To clear record")

        json_data = '{"Bench": 0}'
        python_dictionary = loads(json_data)
        user_select = int(input("Enter new record or 0 to return to previous menu "))
        if user_select == 0:
            break
        elif user_select == 1:
            python_dictionary["Bench"] = 0
            bench = dumps(python_dictionary)
        else:
            python_dictionary["Bench"] = user_select
            bench = dumps(python_dictionary)

        file_path = "bench.json"
        with open(file_path, 'w') as f:
            json.dump(bench, f, indent=4)


def squat_record():
    global squat
    while True:
        print("2 - Squat - 0 to return to previous menu")
        print("-------------------------------------")
        print(f"Current Record {squat} lbs")
        print("1 - To clear record")

        json_data = '{"Squat": 0}'
        python_dictionary = loads(json_data)
        user_select = int(input("Enter new record or 0 to return to previous menu "))
        if user_select == 0:
            break
        elif user_select == 1:
            python_dictionary["Squat"] = 0
            squat = dumps(python_dictionary)
        else:
            python_dictionary["Squat"] = user_select
            squat = dumps(python_dictionary)

        file_path = "squat.json"
        with open(file_path, 'w') as f:
            json.dump(squat, f, indent=4)


def deadlift_record():
    global deadlift
    while True:
        print("3 - Deadlift - 0 to return to previous menu")
        print("-------------------------------------")
        print(f"Current Record {deadlift} lbs")
        print("1 - To clear record")

        json_data = '{"Deadlift": 0}'
        python_dictionary = loads(json_data)
        user_select = int(input("Enter new record or 0 to return to previous menu "))
        if user_select == 0:
            break
        elif user_select == 1:
            python_dictionary["Deadlift"] = 0
            deadlift = dumps(python_dictionary)
        else:
            python_dictionary["Deadlift"] = user_select
            deadlift = dumps(python_dictionary)

        file_path = "deadlift.json"
        with open(file_path, 'w') as f:
            json.dump(deadlift, f, indent=4)