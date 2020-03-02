def seconds_to_hours_minutes_and_seconds(total_seconds):
    hours = total_seconds // 3600
    # minutes = (hours * 3600) - (seconds // 60) if  hours > 0 else seconds // 60
    minutes = (total_seconds - hours * 3600) // 60
    seconds = total_seconds - (hours * 3600 + minutes * 60)

    return hours, minutes, seconds


def main():
    total_seconds = int(input("Enter number of seconds: "))
    hours, minutes, seconds = seconds_to_hours_minutes_and_seconds(
        total_seconds)
    message = f"{hours}:{minutes}:{seconds}"
    print(message)


main()
