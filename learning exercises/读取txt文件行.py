try:
    file_name=input(r'请输入要打开的文件(或者输入路径，如f:\python\working directory\1.txt):')
    total_line=input('请输入需要显示该文件前几行【格式如13：21或：21或21：】')
    line_list=total_line.split(':')
    file_date=open(file_name).readlines()
    #对输入后的内容进行一定的修改，方便输出行
    if line_list[0] == '':
        line_list[0]=1
    elif line_list[1] == '':
        line_list[1]=len(file_date)
    else:
        pass
    start_line=int(line_list[0])
    end_line=int(line_list[1])
    print('文件%s从第%d到第%d的内容如下:\n'%(file_name,start_line,end_line))
    for i in range(start_line-1,end_line):
        print(file_date[i],end='')
except:
    print('您输入的文件不存在')
