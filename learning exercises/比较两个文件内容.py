differ = []

#输入两个文件名（txt），然后判别每行是否相同
def file_compare(file_name1, file_name2):
    file_date1 = open(file_name1)
    file_date2 = open(file_name2)
    file_list1 = file_date1.readlines()
    file_list2 = file_date2.readlines()
    total_line1 = len(file_list1)
    total_line2 = len(file_list2)
    max_line = max(total_line1, total_line2)
    count = 1
    if total_line1 == max_line:
        for i in range(max_line):
            try:
                if file_list1[i].strip() != file_list2[i].strip():
                    differ.append(count)
                else:
                    pass
            except:
                differ.append(count)
            count += 1
    else:
        for i in range(max_line):
            try:
                if file_list2[i].strip() != file_list1[i].strip():
                    differ.append(count)
                else:
                    pass
            except:
                differ.append(count)
            count += 1
    file_date1.close()
    file_date2.close()


file1 = input('请输入第一个文件名：')
file2 = input('请输入第二个文件名：')
file_compare(file1, file2)
if len(differ) == 0:
    print('文件完全相同')
else:
    print('全文共有%d行不同' % len(differ))
    for i in differ:
        print('第{0}行不同'.format(i))

