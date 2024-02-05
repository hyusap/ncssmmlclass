def letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


with open("lab17/grades.txt", "r") as file:
    with open("lab17/output.txt", "w") as output:
        for line in file:
            _, _, student_id, *grades = line.split(",")
            grades = list(map(int, grades))
            avg = sum(grades) / len(grades)
            output.write(f"{student_id},{avg},{letter_grade(avg)}\n")
