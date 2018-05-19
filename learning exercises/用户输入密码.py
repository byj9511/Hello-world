cp = "50823046"
pa = input("请输入密码：")
i = 0

while cp != pa and (not i > 2):
    if "*" in pa:
        pa = input("wrong number24,you have%2d chance(s) please input again:" % (3 - i))
    else:
        i += 1
        pa = input("wrong number23,you have%2d chance(s) please input again:" % (3 - i))
if cp == pa and not i > 2:
    print("pass")
if i > 2:
    print("tries is over")
