def sum2(list1):
    number = len(list1)
    list2 = [list1[i] for i in range(number)if type(list1[i])== float or type(list1[i])== int]
    #列表中的数为小数或者整数式，进行累加
    return sum(list2)


a = [1, 2, 3, 4, 2.41, "a", "b"]
print(sum2(a))
