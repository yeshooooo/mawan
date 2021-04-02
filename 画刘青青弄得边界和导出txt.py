#utf-8
import pandas as pd
import matplotlib.pyplot as plt
def conversBoundToTxt(path_xls,filenametxt):
    data= pd.read_excel(path_xls)
    X = data['POINT_X']
    Y = data['POINT_Y']
    flie = open(filenametxt,'w')
    for i in range(len(X)):
        s1 = str(X[i])
        s2 = str(Y[i])
        flie.write(s1)
        flie.write(',')
        flie.write(s2)
        if i != (len(X)-1):
            flie.write(',')

    flie.close()
    # plt.plot(data['POINT_X'],data['POINT_Y'])
    # plt.title('妈湾边界线框')
    # plt.xlabel('x')
    # plt.ylabel('y')
    # plt.show()


if __name__ == '__main__':
    path = r'E:\work\2021.3\数据\zuobiao.xlsx'
    file = r'E:\work\2021.3\数据\zuobiao_bound.txt'
    conversBoundToTxt(path,file)