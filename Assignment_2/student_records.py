import csv

filename = "students.csv"


def create_file():
    try:
        # "x" creates a new file without overwriting an existing one
        with open(filename, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Roll Number", "Name", "Marks"])

        print("File created.")
    except FileExistsError:
        print("File already exists.")


def add_student():
    roll = input("Enter roll number: ").strip()
    name = input("Enter student name: ").strip()

    if roll == "" or name == "":
        print("Roll number and name cannot be empty.")
        return

    try:
        marks = float(input("Enter marks out of 100: "))
    except ValueError:
        print("Enter valid marks.")
        return

    if not 0 <= marks <= 100:
        print("Marks must be between 0 and 100.")
        return

    # Check whether the roll number is already saved
    try:
        with open(filename, "r", newline="") as file:
            reader = csv.reader(file)
            next(reader, None)

            for row in reader:
                if row and row[0] == roll:
                    print("Roll number already exists.")
                    return
    except FileNotFoundError:
        create_file()

    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([roll, name, marks])

    print("Record added.")


def read_students():
    try:
        with open(filename, "r", newline="") as file:
            reader = csv.reader(file)
            next(reader, None)

            found = False
            print("\nRoll Number | Name | Marks")

            for row in reader:
                if row:
                    print(row[0], "|", row[1], "|", row[2])
                    found = True

            if not found:
                print("No records added yet.")
    except FileNotFoundError:
        print("Create the file first.")


while True:
    print("\n1. Create file")
    print("2. Add student")
    print("3. Read records")
    print("4. Exit")

    choice = input("Enter your choice: ").strip()

    try:
        if choice == "1":
            create_file()
        elif choice == "2":
            add_student()
        elif choice == "3":
            read_students()
        elif choice == "4":
            print("Program closed.")
            break
        else:
            print("Invalid choice.")
    except OSError:
        print("Unable to access the file.")
