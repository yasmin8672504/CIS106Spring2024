# Assignment 7

import csv

def compute_gross_pay(hours, rate):
    if hours <= 40:
        return hours * rate
    else:
        return (40 * rate) + ((hours - 40) * (rate * 1.5))

def format_email(first_name, last_name):
    return f"{first_name[0].lower()}{last_name.lower()}@gm.com"

try:
    with open('EmpData.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        with open('NewEmpData.csv', 'w', newline='') as NewFile:
            fieldnames = ['Last_Name', 'First_Name', 'Gross_Pay', 'Email']
            csv_writer = csv.DictWriter(NewFile, fieldnames=fieldnames)
            csv_writer.writeheader()
            for row in csv_reader:
                gross_pay = compute_gross_pay(float(row['Hours']), float(row['Rate']))
                email = format_email(row['First_Name'], row['Last_Name'])
                csv_writer.writerow({'Last_Name': row['Last_Name'], 'First_Name': row['First_Name'],
                                 'Gross_Pay': f'${gross_pay:.2f}', 'Email': email})
except IOError:
    print("Unable to open file.")
except:
    print("Unexpected error")
