Write a function to make an hour-to-minute converter

Solve:

def hour_to_minute(hour):
    return hour * 60

hour = float(input("Enter hours: "))
minutes = hour_to_minute(hour)
print(f"{hour} hours = {minutes} minutes")
