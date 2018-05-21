import os

#列举目录中的文件名，返回生成一个列表，并赋值
#'.'与os.curdir效果是一样的
all_files = os.listdir('.')
print(all_files, type(all_files))
type_dict = dict()
for each_file in all_files:
    #判断一个文件是否是文件夹
    if os.path.isdir(each_file):
        #字典中没有这个key则会进行赋值，有的话会return对应的value
        type_dict.setdefault('文件夹', 0)
        type_dict['文件夹'] += 1
    else:
        #将文件名与拓展名分开
        ext = os.path.splitext(each_file)[1]
        type_dict.setdefault(ext, 0)
        type_dict[ext] += 1

for each_type in type_dict.keys():
    print('该文件夹下共有类型为【%s】的文件%d个' % (each_type, type_dict[each_type]))
