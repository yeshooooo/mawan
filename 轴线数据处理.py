import pandas as pd
import numpy as np
import re
import locale
import matplotlib.pyplot as plt
from sympy import *
import math

def get_bounds(path,lf_or_rh = 'L',exp_meter=50):
    or_data = pd.read_excel(path)
    cor = or_data['坐标测量1']
    cor = np.array(cor)
    tem_result = []



    for i in range(len(cor)):
        tem_list = []
        cor[i] = cor[i].replace('(','')
        cor[i] = cor[i].replace(')','')
        x,y = cor[i].split(",")
        x = float(x)
        y = float(y)
        tem_list.append(x)
        tem_list.append(y)
        tem_list.append(0.0)
        cor_vec = np.array(tem_list)
        tem_result.append(cor_vec)


    result = np.array(tem_result)
    # print(result)
    if lf_or_rh == 'L':
        left_bound_list = []
        for i in range(len(result) - 1):
            vecAB = result[i] -   result[i+1]
            ####################向量方法###
            tem_left_vec = np.cross(vecAB,np.array([0,0,1]))
            unit_vec = tem_left_vec/np.linalg.norm(tem_left_vec)
            vecAC = unit_vec * exp_meter
            coradd = result[i] - vecAC


        #     ##numpy格式输出
        #     left_bound_list.append(coradd)
            ##最后一个点
            # if i == (len(result) - 2 ) :
            #     corLast = result[i+1]-vecAC
            #     left_bound_list.append(corLast)
        # #print(np.linalg.norm(left_bound_list[0] - result[0]))
        #
        #
            ##去除括号的普通列表格式输出
            left_bound_list.append(coradd[0])
            left_bound_list.append(coradd[1])
        #     #left_bound_list.append(coradd[2])
            ##最后一个点
            if i == (len(result) - 2 ):
                corLast = result[i+1] - vecAC
                left_bound_list.append(corLast[0])
                left_bound_list.append(corLast[1])
                #left_bound_list.append(corLast[2])
        print(left_bound_list)
        return left_bound_list
    if lf_or_rh == 'R':
        right_bound_list = []
        for i in range(len(result) - 1):
            vecAB = result[i+1] - result[i]
            tem_left_vec = np.array([result[i][1]-result[i+1][1],result[i+1][0]-result[i][0],0])
            unit_vec = tem_left_vec/np.linalg.norm(tem_left_vec)
            vecAC = unit_vec * exp_meter
            ####在这改+-号改左右侧
            coradd = result[i] + vecAC
            ##numpy 形式
        #     right_bound_list.append(coradd)
        #     ##最后一个点
        #     if i == (len(result) - 2 ) :
        #         ##在这改+-号改左右侧
        #         corLast = result[i+1]+vecAC
        #
        #         ##
        #         right_bound_list.append(corLast)
        # #print(np.linalg.norm(right_bound_list[0] - result[0]))

            ######去除括号的格式
            right_bound_list.append(coradd[0])
            right_bound_list.append(coradd[1])
            #right_bound_list.append(coradd[2])
            #最后一个点
            if i ==(len(result) - 2):
                ##
                corLast = result[i+1]+vecAC
                right_bound_list.append(corLast[0])
                right_bound_list.append(corLast[1])
        return right_bound_list
def data_save_txt(filename,data):
    file = open(filename,'w')
    for i in range(len(data)):
        s = str(data[i])
        file.write(s)
        file.write(',')
    file.close()
def plot_exp_and_orig(path_left,path_right,bound):

    x_ori = []
    y_ori = []

    ####左线
    or_data_left = pd.read_excel(path_left)
    cor_left_1 = or_data_left['坐标测量1']
    cor_left = np.array(cor_left_1)

    for i in range(len(cor_left)):
        cor_left[i] = cor_left[i].replace('(', '')
        cor_left[i] = cor_left[i].replace(')', '')
        x, y = cor_left[i].split(",")
        x = float(x)
        y = float(y)
        x_ori.append(x)
        y_ori.append(y)
    # plt.scatter(x_ori,y_ori,marker='*')

    ####右线
    x_ori_r = []
    y_ori_r =[]
    or_data_right = pd.read_excel(path_right)
    cor_right_1 = or_data_right['坐标测量1']
    cor_right = np.array(cor_right_1)

    for j in range(len(cor_right)):
        cor_right[j] = cor_right[j].replace('(', '')
        cor_right[j] = cor_right[j].replace(')', '')
        x, y = cor_right[j].split(",")
        x = float(x)
        y = float(y)
        x_ori_r.append(x)
        y_ori_r.append(y)

    ###边界
    x_bound = []
    y_bound = []
    for i in range(len(bound)):
        if i % 2 == 0:
            x_bound.append(bound[i])
        if i % 2 == 1:
            y_bound.append(bound[i])
    plt.scatter(x_ori_r,y_ori_r,marker='o')
    plt.scatter(x_bound,y_bound,marker='^')
    plt.show()




if __name__ == '__main__':
    path1 = r"E:\work\2021.3\数据\LK.xlsx"
    left = get_bounds(path1)
    # print(left)
    # print(type(left))
    path2 = r"E:\work\2021.3\数据\RK.xlsx"
    right = get_bounds(path2,"R")
    print(right)
    print(type(right))
    print(len(right))
    rever_right =[]
    ##合并边界
    for ii in range(len(right) - 1 , 0 ,-2):
        rever_right.append(right[ii -1])
        rever_right.append(right[ii])


    left.extend(rever_right)
    # print(left)
    # print(type(left))
    # print(len(left))
    ##注意：两条轴线不一样长，合并出来形状可能会奇特
    ###xy 互换
    bound = []
    for i in range(0,len(left) - 1,2):
        bound.append(left[i+1])
        bound.append(left[i])
    print(bound)
    path_save_bound = r"E:\work\2021.3\数据\处理结果\Bound.txt"
    data_save_txt(path_save_bound,bound)
    ####看长得啥模样
    # x_1 = []
    # for i in range(0,len(bound),2):
    #     x_1.append(bound[i])
    # y_1 = []
    # for j in range(1,len(bound),2):
    #     y_1.append(bound[j])
    # plt.scatter(x_1,y_1,marker='o')
    # plt.show()


    #####写入excel
    x_1 = []
    for i in range(0,len(bound),2):
        x_1.append(bound[i])
    y_1 = []
    for j in range(1,len(bound),2):
        y_1.append(bound[j])
    df = {'x':x_1,'y':y_1}
    df_data = pd.DataFrame(df)
    data_name = r"E:\work\2021.3\数据\所有边界.xls"
    print(df_data)
    df_data.to_excel(data_name,index=False)