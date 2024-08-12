# -*- coding: gbk -*-
import requests
import datetime
import os
from urllib.parse import quote  # 用于将中文吧名转换为URL编码

# 输入需要爬取的贴吧名称和页数
bbs_name = input('请输入你想爬取的吧名\t')
bbs_page = input('请输入你想爬取的页数\t')

# 获取当前日期
time = datetime.date.today()

# 设置请求头，伪装为浏览器访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76'
}

# rfind在含字符串时输出0，不含时输出-1
# 检查目录是否存在，不存在则创建
if bbs_name.rfind('吧') == -1:
    bbs_name = bbs_name + "吧"

folder_path = f'./贴吧爬取/{bbs_name}_爬取_{time}'
folder = os.path.exists(folder_path)
if not folder:
    os.mkdir(folder_path)

# 发起请求，爬取每一页数据，并保存为HTML文件
for bbs_page in range(int(bbs_page)):
    url = f'https://tieba.baidu.com/f?kw={quote(bbs_name)}&fr={bbs_page * 50}'
    response = requests.get(url, headers=headers).content.decode()
    with open(f'{folder_path}/{bbs_name}_{bbs_page + 1}.html', 'w', encoding='utf-8') as f:
        f.write(response)
    print(f'--------{bbs_name}，第{bbs_page + 1}页，爬取成功--------')

input('\n爬取完成，按任意键退出')
