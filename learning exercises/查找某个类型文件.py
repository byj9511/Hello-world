import os

files_list = list()


def show_file(file_path):
    os.chdir(file_path)
    all_files = os.listdir(os.curdir)
    print(all_files)
    for each_file in all_files:
        if os.path.isdir(each_file):
            print('%s/%s' % (file_path, each_file))
            show_file('%s/%s' % (file_path, each_file))
            os.chdir(os.pardir)
        else:
            if os.path.splitext(each_file)[-1] in file_type:
                files_list.append('%s/%s' % (file_path, each_file))
            else:
                pass

#file_path = input('请输入文件路径：')
file_path='e:/python'


file_type = ['.txt','.py','.pyc']
show_file(file_path)
files_str = '\n\n'.join(files_list)
content = open('video list.txt', 'w')
content.write(files_str)
# 没有close就无法保存，所以是个文件无法读取内容。
# print(content.read())
content.close()
#与21行相同，但下面这行就可以打印
#print(open('video list.txt').read())
