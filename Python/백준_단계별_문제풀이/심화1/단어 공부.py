word = list(str(input()).upper())
unique_words = list(set(word))

count_list = []
for x in unique_words:
    count = word.count(x)
    count_list.append(count)

if count_list.count(max(count_list)) > 1:
    print('?')
else:
    max_index = count_list.index(max(count_list))
    print(unique_words[max_index])