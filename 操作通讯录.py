from sys import exit
import time

address_list = {}
print('欢迎进入通讯录程序')
print("1：查询联系人资料")
print("2：插入新的联系人")
print("3：删除已有联系人")
print("4: 推出通讯录程序")


def user_action_1():
    name = input("请输入联系人姓名：")
    if name in address_list:
        print(name + ':' + address_list[name])
    else:
        print("您所查找的联系人不存在")


def user_action_2():
    name = input("请输入联系人姓名：")
    if name in address_list:
        print("你输入的用户已存在")
    else:
        adress_list[name] = input("请输入用户联系电话：")


def user_action_3():
    name = input("请输入联系人姓名：")
    if name in address_list:
        del address_list[name]
    else:
        print("您所查找的联系人不存在")


def user_action_4():
    print("感谢使用通讯录程序")
    exit(0)


# user_action 不能用引号括起来，否则就变成了字符串，无法调用函数。
action = {'1': user_action_1, '2': user_action_2,
          '3': user_action_3, '4': user_action_4}

while True:
    number = input('请输入相关指令代码：')
    action[number]()
