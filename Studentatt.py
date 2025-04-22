import csv
from datetime import datetime

STUDENT_FILE = 'students.csv'
ATTENDANCE_FILE = 'attendance.csv'

# Initialize files if they don't exist
def init_files():
    for file, header in [(STUDENT_FILE, ['ID', 'Name']), (ATTENDANCE_FILE, ['Date', 'ID', 'Status'])]:
        try:
            with open(file, 'x', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(header)
        except FileExistsError:
            pass

# Add a new student
def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    with open(STUDENT_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([student_id, name])
    print("Student added successfully.\n")

# List all students
def list_students():
    with open(STUDENT_FILE, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        print("Student List:")
        for row in reader:
            print(f"ID: {row[0]}, Name: {row[1]}")
    print()

# Mark attendance for today
def mark_attendance():
    date_today = datetime.now().strftime("%Y-%m-%d")
    print(f"\nMarking attendance for: {date_today}")
    with open(STUDENT_FILE, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        with open(ATTENDANCE_FILE, 'a', newline='') as att_file:
            writer = csv.writer(att_file)
            for row in reader:
                status = input(f"Is {row[1]} (ID: {row[0]}) present? (y/n): ").lower()
                status = 'Present' if status == 'y' else 'Absent'
                writer.writerow([date_today, row[0], status])
    print("Attendance marked.\n")

# View attendance report
def view_report():
    print("\nAttendance Report:")
    with open(ATTENDANCE_FILE, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            print(f"Date: {row[0]}, Student ID: {row[1]}, Status: {row[2]}")
    print()

# Main Menu
def main():
    init_files()
    while True:
        print("=== Student Attendance System ===")
        print("1. Add Student")
        print("2. List Students")
        print("3. Mark Attendance")
        print("4. View Attendance Report")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            list_students()
        elif choice == '3':
            mark_attendance()
        elif choice == '4':
            view_report()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
