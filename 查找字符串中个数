count = [0, 0, 0, 0]
list2 = []


def count_number(*list1):
    #通过*list1，可以得到一个list1的元组
    list3 = list(list1)
    length = len(list3)
    for i in range(length):
        list3[i] = list(list3[i])
        list2.extend(list3[i])
    #将元组转化成列表
    for i in list2:
        if i.isalpha():
            count[0] += 1
            # 判断字符串中的字母
        elif i.isdigit():
            count[1] += 1
            # 判断字符串中的数字
        elif i == ' ':
            count[2] += 1
            # 判断字符串中的空格
        else:
            count[3] += 1
    print('一句话中有%d个字母，%d个数字，%d个空格，以及其他符号%d个' % (count[0], count[1], count[2], count[3]))


count_number('fdsfs', '3123')
