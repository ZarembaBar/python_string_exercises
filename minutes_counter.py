# 12:30pm-12:00am  == 690 min
# 1:23am-1:08am == 1425 min 

def get_time_indicator(time_string):
    start_hour, end_hour = time_string.split("-")
    start_hour_indicator = start_hour[-2:]
    end_hour_indicator = end_hour[-2:]
    return start_hour_indicator, end_hour_indicator


def get_hours_and_minutes_from_string(time_string):
    hours = time_string.split("-")
    first_hours_and_minutes = str(hours[0]).split(":")
    second_hours_with_minutes = str(hours[1]).split(":")

    hours_list = [int(first_hours_and_minutes[0]), int(second_hours_with_minutes[0])]
    minutes_list = [int(first_hours_and_minutes[1][:2]), int(second_hours_with_minutes[1][:2])]
    return hours_list, minutes_list


def hour_unification(hour, time_indicator):
    if time_indicator == "am" and hour == 12:
        hour += 12
    elif time_indicator == "pm" and hour == range(1, 12):
        hour += 12
    return hour


def count_minutes(hour, minutes):
    return hour * 60 + minutes


def minutes_difference(minutes1, minutes2):
    if minutes1 < minutes2:
        return (1440 - minutes1) + (1440 - minutes2)
    elif minutes1 > minutes2:
        return (1440 - minutes1) + minutes2
    else:
        return 1440


if __name__ == "__main__":
    print("Example for time format: 12:40pm-4:23am")
    time = input("Your minutes counter, between hours: ").strip()
    time_indicators = get_time_indicator(time)
    hours, minutes = get_hours_and_minutes_from_string(time)

    first_uni_hour = hour_unification(hours[0], time_indicators[0])
    second_uni_hour = hour_unification(hours[1], time_indicators[1])

    first_hour_minutes_sum = count_minutes(first_uni_hour, minutes[0])
    second_hour_minutes_sum = count_minutes(second_uni_hour, minutes[1])

    print(minutes_difference(first_hour_minutes_sum, second_hour_minutes_sum))
