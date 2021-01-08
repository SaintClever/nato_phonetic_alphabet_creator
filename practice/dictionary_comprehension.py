# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items()}
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}

import random

names = ['Andrew', 'Kirk', 'Cee', 'Donald', 'Brandon', 'Saint. Clever']

student_scores = {student:random.randint(75, 100) for student in names}
print(student_scores)


passed_students = {student:score for (student,score) in student_scores.items() if score >= 85}
print(passed_students)


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆
# Write your code below:
# print(sentence.split())
result = {word:len(word) for word in sentence.split()}
print(result)



weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆
# Write your code 👇 below:


weather_f = {day:(temp_c * 9/5) + 32 for (day,temp_c) in weather_c.items()}
print(weather_f)
