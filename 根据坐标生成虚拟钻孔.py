import pandas as pd
import json
import os
class ReadData:
    def __init__(self,path):

        self.__path = path
        self.drills_data = self.__GetDrillData()
        # self.__origin_order = self.GetOriginOrder()##only use for maxnum

    def __GetDrillData(self):
        or_data = pd.read_excel(self.__path)
        data = or_data.drop_duplicates(subset=['id','zkfc','zkcdbg'],keep='first')
        dcbh_list = []###
        for data_n, data_i in data.groupby('id'):
            dcbh_list.append(data_i['zkfc'].values.tolist())
        new_drill = []####
        for data_n,data_i in data.groupby('id'):
            new_drill.append([str("".join(list(map(str, list(set(data_i['id'].values.tolist())))))), \
                              float("".join(list(map(str, list(set(data_i['x'].values.tolist())))))), \
                              float("".join(list(map(str, list(set(data_i['y'].values.tolist())))))), \
                              float("".join(list(map(str, list(set(data_i['kgbg'].values.tolist())))))), \
                              data_i['zkcdbg'].values.tolist(), \
                              data_i['zkfc'].values.tolist()])

        result = []
        for i in range(len(new_drill)):
            temdict = {}
            temdict['id'] = new_drill[i][0]
            temdict['x'] = new_drill[i][1]
            temdict['y'] = new_drill[i][2]
            temdict['kgbg'] = new_drill[i][3]
            temdict['zkfc'] = new_drill[i][5]
            temdict['zkcdbg'] = new_drill[i][4]
            result.append(temdict)
        delete_index = []
        for i in range(len(result)):
            for j in range(i+1,len(result)):
                if (result[i]['x'] == result[j]['x']) and (result[i]['y'] == result[j]['y']):
                    delete_index.append(j)
        no_repeat = [result[i] for i in range(len(result))  if i not in delete_index]
        return no_repeat
    def Getbound(self):
        or_data = pd.read_excel(self.__path)
        data = or_data.drop_duplicates(subset=['id','zkfc','zkcdbg'],keep='first')
        dcbh_list = []###
        for data_n, data_i in data.groupby('id'):
            dcbh_list.append(data_i['zkfc'].values.tolist())
        new_drill = []####
        for data_n,data_i in data.groupby('id'):
            new_drill.append([str("".join(list(map(str, list(set(data_i['id'].values.tolist())))))), \
                              float("".join(list(map(str, list(set(data_i['x'].values.tolist())))))), \
                              float("".join(list(map(str, list(set(data_i['y'].values.tolist())))))), \
                              float("".join(list(map(str, list(set(data_i['kgbg'].values.tolist())))))), \
                              data_i['zkcdbg'].values.tolist(), \
                              data_i['zkfc'].values.tolist()])
        rangexy = []
        x = []
        for i in range(len(new_drill)):
            x.append(new_drill[i][1])
        y = []
        for j in range(len(new_drill)):
            y.append(new_drill[j][2])
        ##边界外扩5mi
        xmin = min(x) - 5
        xmax = max(x) + 5
        ymin = min(y) - 5
        ymax = max(y) + 5
        rangexy.append(xmin)
        rangexy.append(ymin)
        rangexy.append(xmax)
        rangexy.append(ymin)
        rangexy.append(xmax)
        rangexy.append(ymax)
        rangexy.append(xmin)
        rangexy.append(ymax)
        return rangexy




if __name__ == '__main__':
    path = r'E:\work\2021.3\数据\妈湾钻孔修改.xlsx'
    drills = ReadData(path)
    drilldata = drills.drills_data

    # print(type(drills[0][5][1]))
    print(drilldata)
    print('------------------------------------------------------')
    print(len(drilldata))
    bound = drills.Getbound()
    print(bound)
    ##写入json
    path1 = r"E:\work\2021.3\数据\妈湾海路陡峭分割.txt"
    with open(path1,mode='w') as f:
        json.dump(drilldata,f)
