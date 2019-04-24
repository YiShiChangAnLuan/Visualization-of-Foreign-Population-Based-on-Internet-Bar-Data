import json

fp = open("test.json", 'r', encoding='gbk')
data = json.load(fp)
pie = {}
send = [{}, {}, {}, {}, {}]

for i in range(len(data)):
    if 0 < int(data[i]['age']) < 17:
        ageTmp = 0
    elif 18 < int(data[i]['age']) < 25:
        ageTmp = 1
    elif 26 < int(data[i]['age']) < 35:
        ageTmp = 2
    elif 36 < int(data[i]['age']) < 60:
        ageTmp = 3
    elif int(data[i]['age']) > 60:
        ageTmp = 4
    send[ageTmp][data[i]['province']] = send[ageTmp].get(data[i]['province'], 0) + 1
    pie[data[i]['province']] = pie.get(data[i]['province'], 0) + 1
for key, value in pie.items():
    pie[key] = value / len(data)
# for key, value in pie.items():
#     print("value:", value)
#     print("name:" + '"' + key + '"')
print(send)
