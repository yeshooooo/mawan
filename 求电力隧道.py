import numpy as np
import pandas as pd
def get_obj(infilepath,outfilepath= 0):
    df1 = pd.read_excel(infilepath,sheet_name="高程拐点")
    df2 = pd.read_excel(infilepath,sheet_name="Sheet1")
    x_ce = list(df1['X'])
    y_ce = list(df1['Y'])
    z_ce = list(df1['高度'])
    x_ding = list(df2['X'])
    y_ding = list(df2['Y'])
    point_list_ce = [[x_ce[i],y_ce[i],z_ce[i]] for i in range(len(x_ce))]
    point_list_ding = [[x_ding[j],y_ding[j]] for j in range(len(x_ding))]
    # print(x_ce)
    # print(y_ce)
    # print(z_ce)
    # print(x_ding)
    # print(y_ding)
def get_space_xyz(x1,y1,z1,x2,y2,z2,x,y):
    if (x2 == x1) and (y2 != y1) and (z2 != z1):
        z = (z2 - z1) * (y - y1) / (y2 - y1) + z1
    if (x2 != x1) and (y2 == y1) and (z2 != z1):
        z = (z2 - z1) * (x - x1) / (x2 - x1) +z1
    ###其实上面那两种情况不存在,实际上逻辑上只可能存在下面这两种情况
    if (x2 != x1) and (y2 != x1) and (z2 != z1):
        z = (z2 - z1) * (x - x1) / (x2 - x1) +z1
    if (x2 != x1) and (y2 != x1) and (z2 == z1):
        z = z1
    return [x,y,z]
def get_input_for_space(point0,points_list):
    ###
    if point0[0] == points[0] and point0[1] == points[1]:
        return 1
    else:
        for index_of_point in range(len(points)):
            if point0







if __name__ == '__main__':
    path_in = r"E:\work\2021.4\20140413电力隧道-高程数据.xlsx"
    get_obj(path_in)