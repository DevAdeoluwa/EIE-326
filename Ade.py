def main():
    # Grade point mapping
    grade_points = {
        'A': 4.0,
        'B': 3.0,
        'C': 2.0,
        'D': 1.0,
        'F': 0.0
    }
    
    grades = []
    
    print("Enter grades for 6 courses:")
    for i in range(6):
        grade = input(f"Course {i + 1} (A, B, C, D, F): ").strip().upper()
        while grade not in grade_points:
            print("Invalid grade. Please enter A, B, C, D, or F.")
            grade = input(f"Course {i + 1} (A, B, C, D, F): ").strip().upper()
        grades.append(grade)

    # Calculate GPA
    total_points = sum(grade_points[grade] for grade in grades)
    gpa = total_points / len(grades)
    
    print(f"Your GPA is: {gpa:.2f}")

if __name__ == "__main__":
    main()