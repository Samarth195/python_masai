def greet(name):
    return f"Hello, {name}!"


def calculate_stats(scores):
    count = len(scores)
    average = sum(scores) / count
    return count, average


def result(avg):
    if avg >= 50:
        return "Pass"
    else:
        return "Fail"


def main():
    name = input("What is your name? ")
    print(greet(name))

    n = int(input("Enter the number of subjects: "))
    scores = []

    for i in range(n):
        marks = int(input(f"Enter marks for subject {i+1}: "))
        scores.append(marks)

    subjects, avg = calculate_stats(scores)
    status = result(avg)

    print("\n--- Student Evaluation ---")
    print("Subjects:", subjects)
    print("Average Score:", avg)
    print("Result:", status)


main()
