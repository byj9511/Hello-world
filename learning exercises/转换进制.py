while 1:
    a = int(input("输入一个十进制数："))
    print("转化为二进制，%d变为" % a, bin(a))
    print("转化为八进制，%d变为0o%o" % (a, a))
    print("转化为十六进制，%d变为0x%x" % (a, a))
    b = input("如果想继续转化，请输入Q：")
    if b != "Q":
        break
print("停止转化")
