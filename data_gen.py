import csv
import random
import time

x_cm = 0
y_cm = 0

fieldnames = ["x_cm", "y_cm"]


with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:

    with open('data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            "x_cm": x_cm,
            "y_cm": y_cm
        }

        csv_writer.writerow(info)
        print(x_cm, y_cm)

        x_rand=random.randint(0,1)
        x_cm += (10*x_rand)
        y_rand=random.randint(0, 1)
        y_cm += 10*y_rand
        
        if(x_cm > 300):
            x_cm = 0
            y_cm = 0

    time.sleep(0.5)