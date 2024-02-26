def average(lst):
    return sum(lst) / len(lst)


def to_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def get_input():
    scores = []
    while True:
        score = int(input("Enter a score (or negative number to quit): "))
        if score < 0:
            break
        scores.append(score)
    return scores


def main():
    scores = get_input()
    print("Average score:", average(scores))
    print("Letter grade:", to_letter_grade(average(scores)))


main()
