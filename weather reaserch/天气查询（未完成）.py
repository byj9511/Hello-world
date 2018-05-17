import urllib.request
from code import city_code
import json

cityname=input('你想要哪个城市：')
citycode=city_code[cityname]
if citycode:
    url='http://www.weather.com.cn/data/cityinfo/%s.html' % citycode
    content = urllib.request.urlopen(url).read().decode()
    #decode完了是json格式的数据，需要进行转换
    converted_content=json.loads(content)
    weatherinfo=converted_content['weatherinfo']
    city=weatherinfo[city]

    print(weatherinfo)
