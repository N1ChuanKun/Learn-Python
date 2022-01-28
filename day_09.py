print('Level 1')
print('#1')
age = input('Enter your age: ')
age = int(age)
if age >= 18:
    print('You are old enough to learn to drive.')
elif age < 0:
    print('Error.')
else:
    print('You need {} more years to learn to drive.'.format(18 - age))

print('#2')
age = input('Enter your age: ')
age = int(age)
if age == 20:
    print('Your age is same as me.')
elif age > 20:
    print('You are {} years older than me.'.format(age - 20))
elif 0 < age < 20:
    print('You are {} years younger than me.'.format(20 - age))
else:
    print('Error')

print('#3')
num_one = input('Enter number one: ')
num_two = input('Enter number two: ')
int(num_one)
int(num_two)
if num_one > num_two:
    max = num_one
    min = num_two
elif num_one < num_two:
    min = num_one
    max = num_two
else:
    print('Is same.')
print('{} is greater than {}.'.format(max,min))

print('\nLevel 2')
print('#1')
scores = input('Enter your scores: ')
scores = int(scores)
if 90 < scores <= 100:
    print('A')
elif 70 < scores < 89:
    print('B')
elif 60 < scores < 69:
    print('C')
elif 50< scores < 59:
    print('D')
elif 0 < scores < 49:
    print('F')
else:
    print('Error')

print('#2')
Fall = ['September', 'October', 'November']
Winter = ['December', 'January', 'Ferbruary']
Spring = ['March', 'April', 'May']
Summer = ['June', 'July', 'August']
season = input('Enter Month(capitalize a word indicates): ')
if season in Fall:
    print('is Fall')
elif season in Winter:
    print('is Winter')
elif season in Spring:
    print('is Spring')
elif scores in Summer:
    print('is Summer')
else:
    print('Error')

print('#3')
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input('Enter a fruit: ')
if fruit in fruits:
    print('That fruit already exist in the list.')
else:
    fruits.append(fruit)
    print(fruits)

print('\nLevel 3')
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
print('Check skills keys: ')
if 'skills' in person:
    lenth = len(person['skills'])
    index = int(lenth/2)
    print(person['skills'][index])

print('Check skills keys, and Python: ')
if 'skills' in person:
    if 'Python' in person['skills']:
        print('skills: ', person['skills'])

front_skills = {'JavaScript', 'Rect'}
backend = {'Node', 'Python', 'MongoDB'}
fullstack = {'React', 'Node', 'MongoDB'}
st_skills = set()
st_skills = set(person['skills'])

if front_skills == st_skills:
    print('He is a front end developer')
elif backend.issubset(st_skills) == True:
    if {'React'}.issubset(st_skills):
        print('He is a backend and fullstack developer.')
    else:
        print('He is a backend developer.')
elif fullstack.issubset(st_skills) == True:
    if {'Python'}.issubset(st_skills):
        print('He is a backend and fullstack developer.')
    else:
        print('He is a fullstack developer')
else:
    print('unknown title')