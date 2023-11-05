# age = 20
# price = 19.95
# first_name = 'Nihad'
# is_online = True
# print(age)

# birth_year = input('Enter your birth year: ')
# age = 2023 - int(birth_year)
# print('Your age is ' + str(age))

# first_num = float(input('first number : '))
# second_num = float(input('second number : '))
# sum_of_numbers = first_num + second_num
# print(sum_of_numbers)

# my_age = float(input('input your age :'))
# is_ok = my_age > 18
# print(is_ok)
# price = 25
# print(not price > 10)
# print(10 < price < 30)
# print(price > 10 or price < 30)
# if price > 20:
#     print('more')
# if price > 23:
#     print('25>')
# elif price > 23:
#     print('25>')

# weight = float(input('Weight : '))
# inp = input('(K)g or (L)bs : ')
# if inp.lower() == 'k':
#     converted = weight * 2.20462262
#     print("Weight in Lb:" + str(converted))
# elif inp.lower() == 'l':
#     converted = weight * 0.45
#     print("Weight in Kg: " + str(converted))
#
# i = 1
# while i <= 5:
#     print(i * '*')
#     i += 1

# names = ['john', 'bob', 'sam']
# names[0] = 'jon'
# names.append('doe')
# names.insert(0, 'mike')
# names.remove('mike')
# print(names[0:5])
#
# numbers = [1,2,3,4,5]
# for item in numbers:
#     print(item)

# numbers = range(5)
# numbers = range(5,10)
# for number in range(10):
#     print(number)

# numbers = (1,2,3)
#
# print(type(numbers))
# s
# def say_hi(name):
#     print(f'hi {name}')
#
#
# def cube(num):
#     return pow(num, 3)
#
#
# say_hi('doe')
# print(cube(3))

employee_file = open('employees.txt', 'r')
print(employee_file.readlines())

for emp in employee_file:
    print(emp)