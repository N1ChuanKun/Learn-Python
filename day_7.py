it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print('Level 1')
print('#1')
print(len(it_companies))
print('#2')
it_companies.add('Twitter')
print(it_companies)
print('#3')
companies = {'Tencent', 'Starbucks'}
it_companies = it_companies.union(companies)
print(it_companies)
print('#4')
it_companies.remove('Tencent')
print(it_companies)
print('#5')
print('Different between of remove() and discard(): \n')
print('If the item is not found remove() will return errors, but discard() doesnt raise error')

print('\nLevel 2')
print('#1')
print('Join A and B')
print('#2')
print(A.intersection(B))
print('#3')
print('Is A subset of B: ', A.issubset(B))
print('#4')
print('Is A and B disjoint sets: ', A.isdisjoint(B))
print('#5')
print(A.union(B))
print(B.union(A))
print('#6')
print('The symmetrice difference between A and B: ', A.symmetric_difference(B))
print('#7')
del A
del B
print('delete A and B')

print('Level 3')
print('#1')
age = set(age)
print(age)
print('#2')
print('Diffence between string, list, tuple and set: ')
print('Type\tSplit\tAdd_Remove\tChangeType\t')
print('list\tYes\tYes\t\tYes')
print('tuple\tYes\tNo\t\tYes')
print('set\tYes\tYes\t\tYes\n')


print('#3')
sentcent = 'I am a teacher and I love to inspire and teach people.'
space_index = 0
start_index = 0
lt = list()

#string to list
while space_index != -1:
    space_index = sentcent.find(' ', start_index)
    lt_sent = sentcent[start_index:space_index]
    lt.append(lt_sent)
    start_index = space_index + 1
print(lt)

#find same word in sentence
test = True
len = len(lt)
word = list()
list_mod = list()
for i in range(0, len-1):
    word = lt[i]
    test = word in lt
    if test == True:
        list_mod.append(word)
print(list_mod)

st = set()
st_mod = set()
st.update(lt)
st_mod.update(list_mod)
print('Unique words in this sencent >> ')
print(st.symmetric_difference(st_mod))