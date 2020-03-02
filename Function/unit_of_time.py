def calculate_seconds(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + seconds


def main():
    hours = int(input("Enter hours: "))
    minutes = int(input("Enter minutes: "))
    seconds = int(input("Enter seconds: "))
    total_seconds = calculate_seconds(
        hours, minutes, seconds)
    print(f"Total number of seconds = {total_seconds}.")


main()
