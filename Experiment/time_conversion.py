'''
This function need correcting.
def count_minutes(minutes, seconds):
    This function converts number of minutes and seconds into
    equivalent number of minutes

    # Conversion for seconds to minutes
    remaining_seconds = seconds % 60
    minutes_in_seconds = (seconds - remaining_seconds) // 60
    # Conversion of Seconds and minutes in total minutes
    minutes = minutes + minutes_in_seconds
    return minutes

    # return f"{minutes} minute and {remaining_seconds} second"
'''


def count_seconds(minutes, seconds, hours=None):
    '''This function convert minutes and seconds
    into total number of seconds'''
    if hours:
        return hours * 3600 + minutes * 60 + seconds
    return minutes * 60 + seconds


def count_hours_minutes_seconds(seconds):
    '''This function counts how many hours,minutes and seconds
    in given number of seconds'''
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds


def main(time_series):
    '''This function calculate the complete time and return hours minutes and seconds'''

    sec_container = []
    for minute, second, hours in time_series:
        seconds = count_seconds(minute, second, hours)
        sec_container.append(seconds)

    total_sec = sum(sec_container)
    return count_hours_minutes_seconds(total_sec)


time_series_flask_false = [(15, 32), (20, 27), (45, 45), (9, 0), (38, 47), (45, 56), (31, 17), (35, 41),
                           (26, 7), (53, 15), (37, 1), (25, 4), (60, 0), (22, 0), (27, 18), (20, 47), (26, 25), (53, 31)]

time_series_flask = [(17, 9), (31, 42), (48, 16), (29, 58), (20, 38), (47, 15), (42, 15),
                     (48, 13), (31, 22), (42, 12), (42, 43), (12, 45), (60, 0), (15, 0), (24, 0), (17, 14)]

time_series_Django = [(15, 32), (20, 27), (45, 45), (9, 0), (38, 47), (45, 56), (31, 17), (35, 41),
                      (26, 7), (53, 15), (37, 1), (25, 4), (60, 0), (22, 1), (27, 18), (20, 47), (26, 35), (53, 31)]


time_serires_Krish_naik_complete_ml = [(19, 5), (5, 15), (21, 49), (16, 5), (26, 24), (16, 49), (29, 32), (19, 13),
                                       (25, 55), (21, 43), (10, 54), (10, 5), (13, 39), (6, 3), (4,
                                                                                                 46), (3, 58), (8, 8), (10, 25), (12, 2), (5, 1), (14, 28),
                                       (13, 11), (4, 42), (15, 53), (11, 59), (7, 52), (24, 16), (20,
                                                                                                  17), (9, 51), (16, 0), (17, 16), (11, 45), (12, 1), (20, 2),
                                       (14, 9), (24, 12), (12, 40), (28, 17), (6, 39), (8, 52), (12,
                                                                                                 40), (11, 13), (6, 11), (23, 29), (19, 48), (14, 12), (13, 54),
                                       (8, 3), (9, 49), (6, 2), (20, 6), (6, 27), (10, 18), (13, 1), (10,
                                                                                                      59), (14, 55), (14, 6), (17, 23), (8, 39), (14, 36), (6, 12),
                                       (18, 32), (7, 37), (19, 6), (12, 30), (18, 15)]
cs50_web_programming = [(27, 43, 3), (45, 47, 1), (30, 55, 3),
                        (34, 10, 3), (41, 15, 1), (2, 20, 3), (41, 14, 2)]
cs50_react_native = [(14, 56, 3), (59, 22, 7), (39, 33, 1),
                     (46, 56, 1), (35, 1, 3), (24, 17, 3)]


'''
# print(second)
for minute, second in time_series_flask:
    seconds = count_seconds(minute, second)
    sec_container.append(seconds)

total_sec = sum(sec_container)

minut = count_hours_minutes_seconds(total_sec)
print(minut)

# Flask time = (8, 50, 42)
# Django time = (9, 54, 4)
# Krish niak complete ml = (15, 19, 16)
# CS50's Web Programming with Python and JavaScript = (19, 43, 24)
# CS50's Mobile App Development with React Native = (21, 40, 5)
'''
print(main(cs50_react_native))
