import random
import pandas as pd
import os

os.makedirs("input", exist_ok=True)

employees = [
    ("101", "Aman", "Sales"),
    ("102", "Priya", "Sales"),
    ("103", "Rahul", "Marketing"),
    ("104", "Neha", "Finance"),
    ("105", "Arjun", "Sales"),
    ("106", "Riya", "HR"),
    ("107", "Karan", "IT"),
    ("108", "Sneha", "Marketing"),
    ("109", "Vikas", "Finance"),
    ("110", "Anjali", "Sales")
]

months = ["jan", "feb", "mar"]

for month in months:

    data = []

    for emp in employees:

        sales = random.randint(30000, 100000)

        data.append({
            "Employee ID": emp[0],
            "Employee Name": emp[1],
            "Department": emp[2],
            "Sales": sales
        })

    # Add duplicate row
    data.append(data[3].copy())

    # Make one Sales value blank
    data[5]["Sales"] = None

    df = pd.DataFrame(data)

    df.to_excel(f"input/sales_{month}.xlsx", index=False)

print("Sample Excel files generated successfully!")
