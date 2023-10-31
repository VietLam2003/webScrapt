import requests
import pandas as pd
import json
from tqdm import tqdm # Hiển thị tiến độ vòng lặp

#! Tạo list số báo danh
list_SBD = []
for i in range(15000001,15015875):
    list_SBD.append(i)
# print(len(list_SBD))

#! Tạo dataFrame
DiemThi = pd.DataFrame()

# #! Crawl full
for i in tqdm(range(len(list_SBD))):
    url = 'https://dantri.com.vn/thpt/1/0/99/{}/2023/0.2/search-gradle.htm'.format(list_SBD[i])
    link = requests.get(url).text
    res = json.loads(link)['student']
    data_part = pd.DataFrame(res, index=[0])
    DiemThi = pd.concat([DiemThi,data_part])

DiemThi.to_csv('DiemThiPT.csv')

