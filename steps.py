import csv
from datetime import datetime

def enter_steps(steps):
    today = datetime.now().strftime("%Y-%m-%d")
    filename = "daily_steps.csv"
    data = {}
    try:
        with open(filename, 'r', newline='') as f:
            read = csv.reader(f)
            for line in read:
                if line:
                    data[line[0]] = int(line[1])
    except FileNotFoundError:
        pass 

    data[today] = steps

    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        for date, step_count in data.items():
            writer.writerow([date, step_count])


def view_steps():
    filename = "daily_steps.csv"
    try:
        with open(filename, 'r', newline='') as f:
            read = csv.reader(f)
            for line in read:
                if line:
                    print(f"Date: {line[0]}, Steps: {line[1]}")
    except FileNotFoundError:
        print("No data yet")