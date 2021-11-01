def seconds_to_time(time):
    """
       converts time into hh:mm:ss format

       Args:
           time (int): time in seconds

       Returns:
           str:The time in hh:mm:ss
       """
    if time > 359999 or time<0:
        return None
    seconds_in_hour = 3600
    seconds_in_minutes = 60
    # 3600 seconds in hour
    hours, remainder_from_hours = time // seconds_in_hour, time % seconds_in_hour
    minutes, seconds = remainder_from_hours // seconds_in_minutes, remainder_from_hours % seconds_in_minutes
    if hours == 0:
        return str(minutes).zfill(2) + ':' + str(seconds).zfill(2)
    else:
        return str(hours).zfill(2) + ':' + str(minutes).zfill(2) + ':' + str(seconds).zfill(2)


print(seconds_to_time(59))
