print('#1')
print('creat dog')
dog = {}
print('#2')
dog['color'] = 'black'
dog['name'] = 'Mike'
dog['legs'] = 'normal'
dog['age'] = '3 month'
print(dog)
print('#3')
student = {'first_name':'Mike',
           'last_name':'Chien',
           'gender':'Male',
           'age':'20',
           'marital status': False,
           'skills':['C','C++','Python'],
           'country':'China',
           'address':'unknown'}
print(student)
print('#4')
print('length of student: ', len(student))
print('#5')
print('show skills: ', student['skills'])
print('skills data type: ', type(student['skills']))
print('#6')
student['skills'].append('eating')
student['skills'].append('sleeping')
print(student['skills'])
print('#7')
keys = student.keys()
print(keys)
print('#8')
values = student.values()
print(values)
print('#9')
print(student.items())
print('#10')
del student['skills']
print(student)
print('#11')
del student