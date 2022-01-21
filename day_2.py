print('Day 2:30 Days of python programming')

first_name = 'Ke'
last_name = 'N'
full_name = 'N Ke'
country = 'No Where'
city = 'No'
age = '30'
year = '2022'
is_married, is_true, is_light_on = False, True, True

print('Ke type: ',type('Ke'))
print('last name type: ', type(last_name))
print('is_married type: ', type(is_married))
print('is_true type: ', type(is_true))

print(len(first_name))
if len(first_name) > len(last_name):
    print('1')
else:
    print('0')

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
prod = num_one * num_two
div = num_one / num_two
rema = num_two % num_one
exp = num_one ** num_two
divi = num_one // num_two
print(total)
print(diff)
print(prod)
print(div)
print(rema)
print(exp)
print(divi)

radius = 30
area_of_circle = 3.14 * (radius ** 2)
circum_of_circle = 2 * 3.14 * radius
print('Area: ', area_of_circle)
print('Circum: ', circum_of_circle)

radius_input = int(input('Circle radius: '))    # use 'int(input())'  str --> int 
area = 3.14 * (radius_input * radius_input)
print('Area: ', area)

first_name = input('What is your name: ')
print(first_name)
age = input('What is your age: ')
print(age)
