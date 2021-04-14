def transDotToObj(dict,file_max_num):
    ###对每一层得点数进行记录，每一层索引需偏移前面层点个数得总和
    numcount = 0
    # for i in range(0,file_max_num):
    for i in range(0, file_max_num):
        path_i = dict + '{}.dat'.format(i)
        with open(path_i,'r') as f:
            data1 = f.readline()
            data2 = f.readline()
            data3 = f.readline()
            data4 = f.readline()
        # 解析顶点数组,并将字符串转换为浮点数
        data3 = data3.replace('[', '')
        data3 = data3.replace(']', ',')
        data3 = data3.split(',')
        data3.pop(-1)
        # numOfPoint = len(data3)
        list_point = list(map(float,data3))
        numofpoint = len(list_point)


        # 解析索引数组，并转换为整数，注意，原始数组得索引是从1开始得,然后数组中得每个数都要加上numcount
        data4 = data4.replace('[', '')
        data4 = data4.replace(']', ',')
        data4 = data4.split(',')
        data4.pop(-1)
        index_list = list(map(int,data4))
        # index = [x+numcount for x in index_list]
        index = [x  for x in index_list] ##针对off文件数组从0开始
        numofface = len(index_list)
        # print(index)
        line = []
        for num1 in range(0,numofface-2,3):
            line.append({index[num1],index[num1+1]})
            line.append({index[num1+1],index[num1+2]})
            line.append({index[num1+2],index[num1]})
        # print(line)
        count = []
        for l in line:
            tem_1 = line.count(l)
            count.append(tem_1)

        print(count)
        print(max(count))
        ##去重

        norep = list(set(count))
        print(norep)
        print("_________________________{}________________________________".format(i))







if __name__ == '__main__':

    dic_in = r"E:\work\2021.4\mawanmodel\MDT23\MDT23\\"

    transDotToObj(dic_in,141)