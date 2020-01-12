# Q1：(opendata_request.csv) 讓使用者輸入進行查詢 (單位名稱)，把資料輸出成一個新的 csv 的檔案 (包含標頭檔案)。
import csv
file = open("opendata_requests.csv",encoding="utf-8")
reader = csv.reader(file,delimiter=",")
# print(reader)

agency_name = input("請輸入提供機關名稱:")
search_list = []
for i,data in enumerate(reader):
    if i == 0:
        # data_1 =[]
        #         # for r in data:
        #         #     r = r.replace("\n","")
        #         #     data_1.append(r)
        print("標頭檔案:",data)
        search_list.append(data)
    if i > 1:
        if data[0] == agency_name:
            # data_1 = []
            # for r in data:
            #     r = r.replace("\n", "")
            #     data_1.append(r)
            print(f'第{i}筆: {data}')
            search_list.append(data)

print(search_list)

for r in search_list:
    r = r.replace("\n")


file = open("new_opendata_requests.csv","w",encoding="utf-8")
write = csv.writer(file)
for d in search_list:
    write.writerow(d)
file.close()

# 尚有檔案換行字元問題

