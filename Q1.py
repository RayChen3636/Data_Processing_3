# Q1：(opendata_request.csv) 讓使用者輸入進行查詢 (單位名稱)，把資料輸出成一個新的 csv 的檔案 (包含標頭檔案)。

import csv

# file = open("opendata_requests.csv",encoding="utf-8")
# reader = csv.reader(file, delimiter=",")

def search_org_name(org_name):
    file = open("opendata_requests.csv", encoding="utf-8")
    reader = csv.reader(file, delimiter=",")
    result_list = []
    for i, data in enumerate(reader):
        if i > 0:
            if data[0] == org_name:
                result_list.append(data)
    file.close()
    return result_list

# 操作迴圈
while True:
    user_input = input("請輸入查詢的機構名稱：")
    result = search_org_name(user_input)

    # 輸出csv檔案
    file = open(user_input+".csv", "w", encoding="utf-8")
    writer = csv.writer(file)

    for data in result:
        writer.writerow(data)

