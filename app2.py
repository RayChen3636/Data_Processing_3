# Q2：自動檢查資料夾內(waterdata)水質偵測結果的檔案數量，進行檔案的輸出。
# "waterdata/自來水水質抽驗結果(106年1月).csv"
# "waterdata/自來水水質抽驗結果(106年2月).csv"
# "waterdata/自來水水質抽驗結果(106年3月).csv"
import os
import csv

water_data = os.listdir("C:/Users/yoyo3/PycharmProjects/1125/waterdata")
print(water_data)

result_list = []
for i,file in enumerate(water_data):
    m1_file = open("waterdata/"+file, encoding="utf-8")
    reader = csv.reader(m1_file, delimiter=",")
    for d in reader:
        result_list.append(d)
    i += 1
    print(f'第{i}筆 : {file}')

print("總共檔案數量:",i)
print(result_list)

file = open("result.csv","w",encoding="utf-8")
write = csv.writer(file)

for d in result_list:
    write.writerow(d)

file.close()
