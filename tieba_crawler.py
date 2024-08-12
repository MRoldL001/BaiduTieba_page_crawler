# -*- coding: gbk -*-
import requests
import datetime
import os
from urllib.parse import quote  # ���ڽ����İ���ת��ΪURL����

# ������Ҫ��ȡ���������ƺ�ҳ��
bbs_name = input('������������ȡ�İ���\t')
bbs_page = input('������������ȡ��ҳ��\t')

# ��ȡ��ǰ����
time = datetime.date.today()

# ��������ͷ��αװΪ���������
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76'
}

# rfind�ں��ַ���ʱ���0������ʱ���-1
# ���Ŀ¼�Ƿ���ڣ��������򴴽�
if bbs_name.rfind('��') == -1:
    bbs_name = bbs_name + "��"

folder_path = f'./������ȡ/{bbs_name}_��ȡ_{time}'
folder = os.path.exists(folder_path)
if not folder:
    os.mkdir(folder_path)

# ����������ȡÿһҳ���ݣ�������ΪHTML�ļ�
for bbs_page in range(int(bbs_page)):
    url = f'https://tieba.baidu.com/f?kw={quote(bbs_name)}&fr={bbs_page * 50}'
    response = requests.get(url, headers=headers).content.decode()
    with open(f'{folder_path}/{bbs_name}_{bbs_page + 1}.html', 'w', encoding='utf-8') as f:
        f.write(response)
    print(f'--------{bbs_name}����{bbs_page + 1}ҳ����ȡ�ɹ�--------')

input('\n��ȡ��ɣ���������˳�')
