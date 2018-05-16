syms = r'''`!@#$%^&*()_+-=/*{}[]\|'";:/?,.<>'''
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums = '0123456789'

pd = input('请输入需要检查的密码组合：')
length = len(pd)

while pd.isspace() or length == 0:
    pd = input("您输入的密码为空（或空格），请重新输入：")

if length <= 8:
    con1 = 1
#condition1对密码长度进行分类
elif 8 < length <= 16:
    con1 = 2
else:
    con1 = 3

con2 = 0
#条件2对密码中字母和数字组合判断
for i in pd:
    if i in syms:
        con0 = 1
        #条件0判断密码中是否含有字符
        break
for i in pd:
    if i in chars:
        con2 += 1
        break
for i in pd:
    if i in nums:
        con2 += 1
        break

con3 = 0
#条件3判断密码开头是否为字母

if pd[0] in chars:
    con3 += 1

if con1 == 1 and con2 == 1:
    print("低强度密码")
elif con1 == 2 and (con0 + con2 >= 2):
    # 先进行了运算，在进行了判断
    print("中强度密码")
elif con1 == 3 and (con0 + con2 == 3):
    print("高强度密码")
