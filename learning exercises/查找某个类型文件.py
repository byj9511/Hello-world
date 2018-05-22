import os

files_list = list()


def show_file(file_path):
    os.chdir(file_path)
    all_files = os.listdir(os.curdir)
    print(all_files)
    for each_file in all_files:
        # os.path.isdir()可以直接对当前路径下的文件进行判断，否则需要输入绝对路径
        # os.getcwd()可以得到当前的的路径
        # 与os.chdir()配合使用
        if os.path.isdir(each_file):
            print('%s/%s' % (file_path, each_file))
            show_file('%s/%s' % (file_path, each_file))
            # 进入下一级文件后记得要返回上一级文件，不然就变成了一条路走到死，而无法历遍所有的文件夹
            os.chdir(os.pardir)
        else:
            # 没有路径的限制
            # os.path.splitext('2.py')
            # 分割后，拓展名带有小数点
            if os.path.splitext(each_file)[-1] in file_type:
                files_list.append('%s/%s' % (file_path, each_file))
            else:
                pass


file_path = input('请输入文件路径：')
# file_path='f:/python'
# 所要查找的文件类型
file_type = ['.txt', '.py', '.pyc']
show_file(file_path)
files_str = '\n\n'.join(files_list)
content = open('f:/python/working directory/video list.txt', 'w')
content.write(files_str)
# 没有close就无法保存，所以是个文件无法读取内容。
# print(content.read())
content.close()
# 与21行相同，但下面这行就可以打印
# print(open('video list.txt').read())
