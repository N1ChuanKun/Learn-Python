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
