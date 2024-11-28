import requests
import re

# C语言中的 main()函数 入口
if __name__ == '__main__':
    url = 'https://www.weather.com.cn/weather.html'
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    print(resp.text)








