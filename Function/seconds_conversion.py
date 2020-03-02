def convert_second(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds


def main():
    print("Enter number of seconds: ")
    seconds = int(input(">"))
    hours, minutes, remaining_seconds = convert_second(seconds)
    message = "Hours = " + str(hours) + "\n" + "Minutes = " + str(minutes) + \
        "\n" + "seconds = " + str(remaining_seconds)

    print(message)


main()
