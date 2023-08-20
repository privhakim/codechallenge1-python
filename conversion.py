def convert_to_24_hour(hour, minute, period):
    if period == "pm":
        hour = (hour + 12) % 24
    hour_str = str(hour).zfill(2)
    minute_str = str(minute).zfill(2)
    return hour_str + minute_str

print(convert_to_24_hour(8, 30, "am"))
print(convert_to_24_hour(8, 30, "pm"))        