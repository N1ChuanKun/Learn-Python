age = 20
height = 110.23
complex_num = 1 + 2j

base = int(input('Enter base: '))
height = int(input('Enter height: '))
print('The area of the triangle is ', 0.5 * base * height)

a = int(input('Enter side a: '))
b = int(input('Enter side b: '))
c = int(input('Enter side c: '))
print('The perimeter of the triangle is ', a+b+c)

length = int(input('length: '))
width = int(input('width: '))
print('perimeter = ', 2 * (length + width))

radius = int(input('radius: '))
print('Area: ',3.14 * (radius ** 2))
print('Circumference', 2 * 3.14 * radius)

x = int(input('x in y=2x-2 :  '))
print('y: ', 2 * x - 2)

print('Find the slope between p(2,2) and p(6,10)')
m = (10-2)/(6-2)
print('Slope: ',m)

print(8 > 9)

x = int(input('x in y=x^2 + 6x+9 :  ' ))
print('y = ', x ^ 2 + 6 * x + 9)
print('when x = ', x)
print(' ')

print('x ^ 2 + 6 * x + 9 = 0, x')
#important for!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
for i in range(0,100):
    if (i ^ 2 + 6 * i + 9) == 0:
        x = i
        break
print('if y=0, x is ', x)

print('python len: ', len('python'))
print('dragon len: ', len('dragon'))
print('python == dragon: ', 'python' == 'dragon')
print('on' in 'python' and 'on' in 'dragon')

sent = 'I hope this course is not full of jargon.'
print('jargon' in sent)

print('on not in python and dragon', 'on' not in 'python' and 'on' not in 'dragon')

len = len('python')
print('len of python', len, type(len))
len = float(len)
print('len of python', len, type(len))
len = str(len)
print('len of python', len, type(len))

num = int(input('Input number: '))
if num % 2 == 0:
    print('num is even')
else:
    print('num is odd')

print('7/3 == int(2.7)? ', 7 / 3 is int(2.7))
print('type "10" is type 10? ', type('10') is type(10))
print('int(9.8) is 10? ', int(9.8) is 10)

hour = int(input('Enter hours: '))
rate = int(input('rate per hour: '))
print('pay = ', hour*rate)

print("You have lived for %d seconds." %(year * 360 * 24 * 60))

for j in range(1,6):
    print(str(j).ljust(2), str(1).ljust(2), str(j).ljust(2), str(j*j).ljust(3), str(j*j*j).ljust(4))
#str.ljust() --> output str at left
#str.rjust() --> output str at right
