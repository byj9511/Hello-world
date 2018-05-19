import re

# ()用于分组，虽然不知道为什么，但是使用完|有必要加()
r = re.search(r'((25[0-5]|2[0-4]\d|[01]?\d?\d)\.){3}'
              r'(25[0-5]|2[0-4]\d|[01]?\d?\d)', '1.128.1.1')


print(re.search(r'(([01]\d\d|2[0-4]\d|25[0-5]|\d\d|\d)\.){3}([01]\d\d|2[0-4]\d|25[0-5]|\d\d|\d)', '192.168.41.8'))

def find_span(r):
    if r == None:
        print("没有匹配到结果")
        return
    #查找到的字符串在整个字符串中起始位置
    a = r.start()
    #查找到的字符串在整个字符串中终止位置
    b = r.end()
    #r.string是被match的内容，而人r[0]是所要match的内容
    print(r,a,b，r[0],r.string)
    if r.string[a-1].isdigit() or r.string[b].isdigit() :#判断匹配的结果两端字符是否为数字
        print(r.string[a:b],"可能不是你想要的")
    else:
        print(r.string[a:b],"匹配成功")


NUM0_255 = r'([01]\d\d|2[0-4]\d|25[0-5]|\d\d|\d)'

mystr = '1e[color=Red]r33192.168.41.833[/color]oo3o5548'
mystr1 = '日日日日'
mystr2 = '1e[color=Red]r192.168.41.83[/color]oo3o5548'
