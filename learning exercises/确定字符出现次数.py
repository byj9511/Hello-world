def findstr(find,target):
    j=0
    for i in range(len(target)-1):
        if find==target[i:i+2]:
            #目标字符串中任意相邻两个字符与所给字符相等
            j+=1
    print("字符串在目标字符串中共出现%d次"%j)

findstr(find="im",target="imimim im i m  im")
