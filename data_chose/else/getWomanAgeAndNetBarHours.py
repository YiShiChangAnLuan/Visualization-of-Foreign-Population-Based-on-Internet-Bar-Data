def get_woman_age_and_net_bar_hours():
    fp1 = open("womanAgeHours.csv", "r", encoding="UTF-8")
    fp2 = open("womanNetBarHours.csv", "r", encoding="UTF-8")
    lines1 = fp1.readlines()
    lines2 = fp2.readlines()
    ageNo = [[], [], [], [], []]
    net_bar = [[], [], []]
    for i in range(len(lines1)):
        if i == 0:
            continue
        line = lines1[i].strip()
        line = line.split(",")
        for j in range(5):
            if int(line[1]) == j:
                ageNo[j].append(int(line[2]))
    for i in range(len(lines2)):
        if i == 0:
            continue
        line = lines2[i].strip()
        line = line.split(",")
        # 算出这三个网吧总人数最多
        if line[1] == "50010610009083":
            net_bar[0].append(int(line[2]))
        if line[1] == "50011310000099":
            net_bar[1].append(int(line[2]))
        if line[1] == "50010910000192":
            net_bar[2].append(int(line[2]))
    send_data = ageNo[:]
    for i in range(3):
        send_data.append(net_bar[i])
    return send_data


# 计算网吧总人数
# dic = {}
# dicList = []
# for i in range(len(lines2)):
#     if i == 0:
#         continue
#     line = lines2[i].strip()
#     line = line.split(",")
#     dic[line[1]] = dic.get(line[1], 0) + int(line[2])
# for kv in dic.items():
#     dicList.append([kv[0], kv[1]])
# dicList = sorted(dicList, key=(lambda x: x[1]), reverse=True)
# print(dicList)
