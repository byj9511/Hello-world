from sys import exit

print('新建用户：N/n')
print('登录账号：E/e')
print('退出程序：Q/q')
name_and_password = {}


def register():
    user_name = input('请输入用户名：')
    while 1:
        # 此处in只能判断key中是否有目标，注意数据类型应该一致
        '''a={12:21}
            12 in a
            21 in a
            '12' in a'''
        if user_name not in name_and_password:
            break
        else:
            user_name = input('你输入的用户名已被使用，请重新输入：')
    user_password = input('请输入密码:')
    name_and_password[user_name] = user_password


def roll_in():
    i = 2
    user_name = input('请输入用户名：')
    while 1:
        if user_name in name_and_password:
            break
        else:
            user_name = input('你输入的用户名不存在，请重新输入：')
    user_password = input('请输入密码:')
    while 1:
        if user_password == name_and_password[user_name]:
            print('欢迎进入XXOO系统')
            break
        else:
            if i:
                user_password = input('你输入密码不正确，请重新输入，您还有%d次机会：' % (i - 1))
                i -= 1
            else:
                print('你的机会用完了')
                break

def quit():
    exit(0)

while 1:
    command=input('请输入指令：')
    if command in ['n','N']:
        register()
    elif command in ['e','E']:
        roll_in()
    elif command in ['q','Q']:
        quit()
    else:
        print('指令不存在')
