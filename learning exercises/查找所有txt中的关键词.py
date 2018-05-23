import os

def print_pos(key_dict):
    keys = key_dict.keys()
    keys = sorted(keys)#由于字典是无序的，所以进行排序
    for each_key in keys:
        print('关键字出现在第%s行，第%s个位置。'%(each_key,str(key_dict[each_key])))

#查找一行中对象所在位置
def pos_in_line(line,key):
    pos=[]
    begin = line.find(key)
    while begin != -1:
        pos.append(begin+1)#用户的角度从1开始数
        begin =line.find(key,begin+1)#从下一个位置开始数，找到了返回一个位置，找不到返回-1
    return pos

#打开txt文本并且查找目标对象
def search_in_file(file_name,key):
    f = open(file_name)
    count = 0 #记录行数
    key_dict = dict() #字典，用户存放key所在具体行数

    for each_line in f:
        count+=1
        if key in each_line:
            pos = pos_in_line(each_line,key)
            key_dict[count] = pos

    f.close()
    return key_dict

#查找目录以及子目录下的所有txt文件
def search_files(key,detail):
    all_files = os.walk(os.getcwd())
    txt_files = []

    for i in all_files:
        for each_file in i[2]:
            #将txt文件的路径储存在txt_files中
            if os.path.splitext(each_file)[1] == '.txt':
                each_file = os.path.join(i[0],each_file)
                txt_files.append(each_file)
    for each_txt_file in txt_files:
        key_dict = search_in_file(each_txt_file,key)
        if key_dict:
            print('============================')
            print('在文件【%s】中找到关键字【%s】'%(each_txt_file,key))
            if detail in ['YES','Yes','yes']:
                print_pos(key_dict)

key = input('请将脚本防御到查找的文件夹内，请输入关键字：')
detail = input('请问是否需要打印关键字【%s】在文件中的具体位置（YES/NO）：'%key)
search_files(key,detail)

#自己编写：
# import os
# 
# 
# def find_txt(key, detail):
#     txt_path = []
#     # 用os.getcwd()而不用os.curdir是因为能显示绝对路径，比较直观
#     all_files = os.walk(os.getcwd())
#     for dir_date in all_files:
#         for each_file in dir_date[2]:
#             if os.path.splitext(each_file)[1] == '.txt':
#                 txt_path.append(os.path.join(dir_date[0], each_file))
#     for each_file_path in txt_path:
#         each_file_dict = search_in_file(each_file_path, key)
#         if each_file_dict:
#             print('位置：%s' % each_file_path)
#             if detail in ['YES', 'Yes', 'yes']:
#                 print_pos(each_file_dict)
# 
# 
# def search_in_file(path, key):
#     each_file_dict = {}
#     count = 0
#     file = open(path)
#     for each_line in file:
#         count += 1
#         # 如果一行中包含了key，才执行查找位置命令
#         if key in each_line:
#             each_file_dict[count] = search_in_line(each_line, key)
#     return each_file_dict
# 
# 
# def print_pos(each_file_dict):
#     if each_file_dict:
#         for i in each_file_dict:
#             print('第%d行，位置：' % i, (each_file_dict[i]))
# 
# 
# def search_in_line(each_line, key):
#     start = each_line.find(key)
#     start_list = []
#     while start != -1:
#         start_list.append(start)
#         start = each_line.find(key, start + 1)
# 
#     return start_list
# 
# 
# # path=['e:/python/working directory/1.txt']
# key = 'more'
# detail = 'yes'
# find_txt(key, detail)
