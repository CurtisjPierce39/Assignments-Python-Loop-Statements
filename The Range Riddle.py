#Question 1 Task 1

import random

mood = ["Happy", "Sad", "Energetic", "Calm", "Happy", "Sad", "Energetic"]
day_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

for i in range(len(mood)):
    weekday = random.choice(day_of_the_week)
    moods = random.choice(mood)
    print(f"On {weekday} , you were feeling {moods}.")