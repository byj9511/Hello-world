import re


def word_replace(file_name, re_word, new_word):
    file = open(file_name, 'r+')
    pattern = re.compile(re_word)
    date = file.read()
    re_number = len(pattern.findall(date))
    print('文件%s共有%d个【%s】' % (file_name, re_number, re_word))
    print('您确定要把所有的【%s】替换为【%s】吗？' % (re_word, new_word))
    answer = input('yes/no')
    if answer == 'yes':
        #先将文件指针便宜到文件开头
        #文件参见：https://www.cnblogs.com/lotusto/p/5805543.html
        file.seek(0)
        #从当前文件指针处开始清空一定的字节
        file.truncate()
        # replace并没有对date文件本身进行修改，所以需要赋值来保存
        file.write(date.replace(re_word, new_word))
    else:
        #输入yes外的选项时可以进行的操作
        pass
    file.close()

file_name = input('请输入文件名：')
re_word = input('请输入需要替换的单词或字符：')
new_word = input('请输入新的单词或字符：')
word_replace(file_name, re_word, new_word)
