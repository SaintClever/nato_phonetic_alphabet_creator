# new_list = [new_item for item in list]
numbers = [1, 2, 3]
new_list = [i + 1 for i in numbers]
print(new_list)


name = 'Saint. Clever'
list_name = [letter for letter in name]
print(list_name)


new_range = [i * 2 for i in range(1, 5)]
print(new_range)


# conditional list comprehension
names = ['Andrew', 'Kirk', 'Cee', 'Donald', 'Brandon', 'Saint. Clever']
short_names = [new_names for new_names in names if len(new_names) < 5]
print(short_names)


long_names = [cap_name.upper() for cap_name in names if len(cap_name) > 5]
print(long_names)


numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆
#Write your 1 line code 👇 below:

squared_numbers = [i**2 for i in numbers] # or [i * i for i in numbers]

#Write your code 👆 above:
print(squared_numbers)


numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above
#Write your 1 line code 👇 below:

result = [i for i in numbers if i % 2 == 0]

#Write your code 👆 above:
print(result)
print('')



with open('file1.txt') as file:
    file1 = file.readlines()

with open('file2.txt') as file:
    file2 = file.readlines()
    
new_result = [int(i) for i in file1 if i in file2]
print(new_result)
print('')



files = ['file1.txt', 'file2.txt']
file_list = [open(i).readlines() for i in files]
new_result = [int(i) for i in file_list[0] if i in file_list[1]]



# Write your code above 👆
print(new_result)