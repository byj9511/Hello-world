var1 = 'HI'


def fun1():
    var1 = 'baby'
    return fun2(var1)


def fun2(var1):
    var1 += "i love you"

    def fun3():
        #nonlocal\global前不能定义参数，不然会冲突。参见https://stackoverflow.com/questions/18807749/name-x-is-parameter-and-global-python
        nonlocal var1
        var1 = "小甲鱼"
        print(var1)

    fun3()
    return var1


print(fun1())
