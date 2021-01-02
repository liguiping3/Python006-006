import requests
from pathlib import *
import sys
from lxml import etree


ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
header = {'user-agent':ua}
myurl = 'https://www.solidot.org/'
con_list = []
try:
    response = requests.get(myurl, headers=header)
    selector = etree.HTML(response.text)

    #print(response.text)
    title = selector.xpath('//div[@class="block_m"]/div[@class="ct_tittle"]/div[@class="bg_htit"]/h2/a/text()')
    news_info = selector.xpath('//div[@class="block_m"]/div[@class="p_content"]/div[@class="p_mainnew"]/text()')

    # 遍历对应关系字典
    about_info = dict(zip(title, news_info))

except requests.exceptions.ConnectTimeout as e :
    print(f"requests库超时")
    sys.exit(1)

# 获得python脚本的绝对路径
p = Path(__file__)
pyfile_path = p.resolve().parent
# 建立新的目录html
html_path= pyfile_path.joinpath('download')

if not html_path.is_dir():
    Path.mkdir(html_path)
page = html_path.joinpath('zhihu.json')

# 上下文管理器
try:
    with open(page, 'a',  encoding='utf-8') as f:
        f.write(str(about_info))
except FileNotFoundError as e:
    print(f'文件无法打开,{e}')
except IOError as e:
    print(f'读写文件出错,{e}')
except Exception as e:
    print(e)
