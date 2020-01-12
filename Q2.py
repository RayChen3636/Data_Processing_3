import csv
import glob

def get_location_data(csv_path,location):
    m1_file = open(csv_path,encoding="utf-8")
    reader = csv.reader(m1_file, delimiter=",")
    _list = []
    for i, d in enumerate(reader):
        if d[4] == location:
            _list.append(d)
    return _list


result_list = []
# for i in range(1,101):
#     for d in get_location_data("waterdata/自來水水質抽驗結果(106年"+i+"月).csv","平鎮區"):
#         result_list.append(d)

# 取得檔案
file_path_list = glob.glob("waterdata/自來水水質抽驗結果*.csv")
for f_path in file_path_list:
    for d in get_location_data(f_path, "平鎮區"):
        result_list.append(d)

file = open("waterdata/output.csv","w",encoding="utf-8")
write = csv.writer(file)

for d in result_list:
    write.writerow(d)
