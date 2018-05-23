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
