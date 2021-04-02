#utf-8
import pandas as pd
import matplotlib.pyplot as plt
def conversBoundToTxt(path_xls):
    data= pd.read_excel(path_xls)

    x = data['x'].unique()
    y = data['y']
    plt.plot(x,y)
    plt.title('隧道轴线')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


if __name__ == '__main__':
    path = r'E:\work\2021.3\数据\cad导出轴线.xlsx'

    conversBoundToTxt(path)