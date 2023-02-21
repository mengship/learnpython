# 下载安装包
# python -m pip install requests
# python -m pip install ftfy

import requests
from ftfy import fix_text
data = requests.get('http://www.baidu.com')
print(data.text)
print(fix_text(data.text))





