def read_numbers(file_name):
    numbers = []
    with open(file_name, "r") as file:
        for line in file:
            numbers.append(int(line.strip()))
    return numbers


def compute_stats(numbers):
    total_values = len(numbers)
    total_sum = sum(numbers)
    average = total_sum / total_values
    return total_values, total_sum, average


def write_log(message):
    with open("results.log", "a") as log:
        log.write(message + "\n")


def main():
    write_log("Program started")

    try:
        write_log("Opening numbers file")
        numbers = read_numbers("numbers.txt")
        write_log(f"Read {len(numbers)} numbers")

        total, total_sum, avg = compute_stats(numbers)
        write_log(f"Sum: {total_sum}")
        write_log(f"Average: {avg}")

        write_log("Processing completed")

    except FileNotFoundError:
        write_log("Error: numbers.txt file not found")


main()
