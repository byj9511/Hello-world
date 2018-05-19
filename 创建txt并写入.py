#创建一个不存在的文本，并写入一些数据
def filewrite():
    file_name = input('请输入文件名：')
    try:
        file_date = open(file_name, 'x')
        print('请输入内容【单独输入\'w\'保存退出】：')
        while 1:
            each_line = input('>>')
            if each_line == 'w':
                break
            else:
                # write()中只接受str类型，不能用list
                file_date.write(each_line + '\n')
        file_date.close()
    except:
        print('文件已存在')


filewrite()
