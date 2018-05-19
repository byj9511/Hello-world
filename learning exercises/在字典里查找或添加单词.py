dict1 = {'computer': 'so fast'}
print('a=add,l=look up,q=quit')
while 1:
    answer = input('add or look up a word(a/l/q)?')
    if answer == 'a':
        key1 = input('type the word:')
        value1 = input('type the definiton:')
        dict1[key1] = value1
        print('word and its definition has been added')
    elif answer == 'l':
        key1 = input('type the word:')
        if key1 in dict1.keys():
            print(dict1[key1])
        else:
            print('the word isn\'t in the dictionary')
    elif answer == 'q':
        break
    else:
        print('please enter the right letter:')
