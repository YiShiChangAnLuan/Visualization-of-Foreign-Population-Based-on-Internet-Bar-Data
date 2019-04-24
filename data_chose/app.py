# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#import pymysql
from flask import Flask, jsonify
import pandas as pd
import json
app = Flask(__name__)

@app.route('/getManAgeAndNetBarHours/',methods=['GET'])
def get_man_age_and_net_bar_hours():
    fp1 = open("manAgeHours.csv", "r", encoding="UTF-8")
    fp2 = open("manNetBarHours.csv", "r", encoding="UTF-8")
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
    #print(send_data)
    return jsonify(send_data)

@app.route('/get_provence_time_point/',methods=['GET'])
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
    return jsonify(send_data)

@app.route('/get_woman_age_and_net_bar_hours/',methods=['GET'])
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
    return jsonify(send_data)


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0',port=80,debug=True)
