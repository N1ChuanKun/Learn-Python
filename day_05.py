print('#1')
a = []
b = list()
print('#2')
lst = ['banana', 'apple', 'peach', 'watermelon', 'pineapple']
print('#3')
print(len(lst))
print('#4')
print(lst[0], lst[len(lst)-1], lst[int(len(lst)/2)])
print('#5')
mix = ['Name', 50, 110, False, 'NULL']
print(mix)
print('#6')
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print('#7')
print(it_companies)
print('#8')
print('Num of companies: ', len(it_companies)+1)
print('#9')
print(it_companies[0])
print(it_companies[len(it_companies)-1])
print(it_companies[int(len(it_companies)/2)])
print('#10')
it_companies[0] = 'Startbucks'
print(it_companies)
print('#11')
it_companies.append('Tencent')
print(it_companies)
print('#12')
it_companies.insert(3,'Vision')
print(it_companies)
print('#13')
it_companies[1].upper()
print(it_companies)
print('#14')
print('#; '.join(it_companies))
print('#15')
print('Tencent' in it_companies)
print('#16')
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.sort()
print(it_companies)
print('#17')
it_companies.sort(reverse = True)
print(it_companies)
print('#18')
del it_companies[0:3]
print(it_companies)
print('#19')
lenth = len(it_companies)
del it_companies[ lenth - 3 : lenth]
print(it_companies)
print('#20')
del it_companies[int(len(it_companies)/2)]
print(it_companies)
print('#21')
print('reset list')
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
del it_companies[0]
print(it_companies)
print('#22')
del it_companies[int(len(it_companies)/2)]
print(it_companies)
print('#23')
del it_companies[len(it_companies)-1]
print(it_companies)
print('#24')
it_companies.clear()
print(it_companies)
print('#25')
del it_companies
print('#26')
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
print('Joined')
print('#27')
full_stack = front_end.copy() + back_end.copy()
print(full_stack)
print('#28')
full_stack.insert(5,'Python')
full_stack.insert(6,'SQL')
print(full_stack)
print('\nLEVEL 2')
age = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(age)

age.sort()
min = age[0]
max = age[-1]
print('Min in age is ', min)
print('Max in age is ', max)
age.append(min)
age.append(max)
print(age)

if int(len(age)/2) % 2 == 0:
    print('Output two number')
    print(age[int(len(age)/2) - 1], age[int(len(age) / 2)])
else:
    print('Output one number')
    print(age[int(len(age)/2)])

sum = 0
for i in range(0, len(age) - 1):
    sum += age[i]
ave = sum / len(age)
print('ave: ', ave)

age.sort()
min = age[0]
max = age[-1]
print('Range of ages: ', max - min )
print('min - ave = ', abs(min - ave))
print('max - ave = ', abs(max - ave))
