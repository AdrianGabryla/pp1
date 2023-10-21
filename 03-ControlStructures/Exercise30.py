time = input("Enter time (24-hour format): ")
hour = int(time[:2])
if hour > 12:
    hour = hour - 12
    print(f"Time: {hour}{time[2:]}pm")
else:
    print(f"{time}am")
