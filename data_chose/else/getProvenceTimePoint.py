def get_provence_time_point():
    fp = open("provenceTimePoint.csv", "r", encoding="UTF-8")
    send_data = []
    pro1 = []
    pro2 = []
    pro3 = []
    other = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    lines = fp.readlines()
    for i in range(len(lines)):
        if i == 0:
            continue
        line = lines[i].strip()
        line = line.split(",")
        if line[1] == "511623":
            pro1.append(int(line[2]))
        if line[1] == "511622":
            pro2.append(int(line[2]))
        if line[1] == "511602":
            pro3.append(int(line[2]))
        for j in range(24):
            if int(line[0]) == j and line[1] is not "511623" and line[1] is not "511622" and line[1] is not "511602":
                other[j] += 1
    send_data.append(pro1)
    send_data.append(pro2)
    send_data.append(pro3)
    send_data.append(other)
    return send_data




