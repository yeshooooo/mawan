import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



def get_drills_xy(path_drill):
    or_data = pd.read_excel(path_drill)
    data = or_data.drop_duplicates(subset=['id', 'zkfc', 'zkcdbg'], keep='first')
    dcbh_list = []  ###
    for data_n, data_i in data.groupby('id'):
        dcbh_list.append(data_i['zkfc'].values.tolist())
    x = []  ####
    y = []
    for data_n, data_i in data.groupby('id'):
        x.append(float("".join(list(map(str, list(set(data_i['x'].values.tolist())))))))
        y.append(float("".join(list(map(str, list(set(data_i['y'].values.tolist())))))))

    return x,y
def get_line_L_and_R(path_l,path_r):
    or_data = pd.read_excel(path_l)
    cor = or_data['坐标测量1']
    cor = np.array(cor)



    X = []
    Y = []
    for i in range(len(cor)):

        cor[i] = cor[i].replace('(','')
        cor[i] = cor[i].replace(')','')
        x,y = cor[i].split(",")
        x = float(x)
        y = float(y)
        X.append(x)
        Y.append(y)
    print('x-size',len(X))
    print('y-size',len(Y))
    or_data2 = pd.read_excel(path_r)
    cor2 = or_data2['坐标测量1']
    cor2 = np.array(cor2)
    for i in range(len(cor2)):

        cor2[i] = cor2[i].replace('(','')
        cor2[i] = cor2[i].replace(')','')
        x2,y2 = cor2[i].split(",")
        x2 = float(x2)
        y2 = float(y2)
        X.append(x2)
        Y.append(y2)
    print('x-size',len(X))
    print('y-size',len(Y))
    return X,Y

def plot_drills_and_line(drills,line):
    drill_x = drills[0]
    print(len(drill_x))
    drill_y = drills[1]
    print(len(drill_y))

    line_x = line[1]
    line_y = line[0]
    plt.scatter(drill_x,drill_y,marker='o')
    plt.scatter(line_x,line_y,marker='*')
    plt.show()
def plot_drills_and_bound(drills):
    drill_x = drills[0]
    path_xls = r'E:\work\2021.3\数据\zuobiao.xlsx'
    drill_y = drills[1]

    data= pd.read_excel(path_xls)
    X = data['POINT_X']
    Y = data['POINT_Y']
    plt.plot(data['POINT_X'],data['POINT_Y'])
    plt.title('妈湾边界线框')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.scatter(drill_x,drill_y,marker='*',c = 'red')

    plt.show()

if __name__ == '__main__':
    path1 = r'E:\work\2021.3\数据\all.xlsx'
    path2 = r"E:\work\2021.3\数据\LK.xlsx"
    path3 = r"E:\work\2021.3\数据\RK.xlsx"
    drillxy = get_drills_xy(path1)
    print(drillxy)
    print(len(drillxy[0]))
    print(len(drillxy[1]))
    linexy = get_line_L_and_R(path2,path3)
    # plot_drills_and_line(drillxy,linexy)
    plot_drills_and_bound(drillxy)