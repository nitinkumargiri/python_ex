import datetime
now = datetime.datetime.now()
hour = now.hour
if 5 <= hour < 12:
    print("good morning")
elif 12 <= hour < 17:
    print("good afternoon")
else:
    print("good evening")
