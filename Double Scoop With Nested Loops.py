# Question 2 Task 1

import random

mood = ["happy", "sad", "sleepy"]
day_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
time_of_the_day = ["morning", "afternoon", "night"]

for i in range(len(day_of_the_week)):
    for i in (time_of_the_day):
        moods = random.choices(mood)
        time_of_day = random.choices(time_of_the_day)
        weekday = random.choices(day_of_the_week)
        print(f"On {' '.join(weekday)} {' '.join(time_of_day)}, you were {' '.join(moods)}.")