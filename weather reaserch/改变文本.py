f = open('city_code.txt')
g = open('3.txt', 'w')
final_result = ''
lines = f.readlines()


def modify_txt(line):
    responding_code = line.split("=")[0]
    city_name = line.split('=')[-1].strip(' \n')
    result = "'{0:s}':'{1:s}'".format(city_name, responding_code)
    return result


for line in lines:
    if '=' in line and line != lines[-1]:
        result = modify_txt(line) + ',' + '\n'
    elif line == lines[-1]:
        result = modify_txt(line)
    else:
        result = ''
    final_result += result
final_result = "city_code={%s}" % final_result
g.write(final_result)
f.close()
g.close()
