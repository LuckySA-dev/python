# // 1st Version // 

with open('employees.txt', 'r') as emp_file:
    count = 0
    for emp in emp_file:
        emp = emp.strip()
        if count == 0:
            print(f'Name : {emp}')
            count += 1
        elif count == 1:
            print(f'ID Number : {emp}')
            count += 1
        else:
            print(f'Dept : {emp}\n')
            count = 0

# // 2st Version //

def load_employee(file_path: str) -> list[dict]:

    employees = []
    fields = ["Name", "ID Number", "Dept"]

    with open(file_path, "r") as emp_temp:
        lines = [line.strip() for line in emp_temp if line.strip()]

    for i in range(0, len(lines), 3):
        employee = dict(zip(fields, lines[i : i + 3]))
        employees.append(employee)

    return employees


def main():
    employee = load_employee("employees.txt")

    for emp in employee:
        print(f"Name : {emp['Name']}")
        print(f"ID Number : {emp['ID Number']}")
        print(f"Dept : {emp['Dept']}")
        print("-" * 30)

if __name__ == "__main__":
    main()