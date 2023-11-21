total_working_days = int(input("Enter total number of working days: "))
total_absent_days = int(input("Enter total number of days absent: "))

attendance_percentage = (
    (total_working_days - total_absent_days) / total_working_days) * 100

if attendance_percentage < 75:
    print("Attendance Percentage:", attendance_percentage, "%")
    print("Student cannot sit in the exam due to low attendance.")

else:
    print("Attendance Percentage:", attendance_percentage, "%")

    marks = []
    for i in range(5):
        subject_marks = float(input(f"Enter marks for subject {i+1}: "))
        marks.append(subject_marks)

    for i in range(5):
        print(f"subject {i+1} marks: {marks[i]}")

