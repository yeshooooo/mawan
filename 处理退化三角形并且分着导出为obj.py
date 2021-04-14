def is_need_reverse(index1,index2,index3,pointlist):
    if pointlist[index1] ==pointlist[index2] or pointlist[index2] == pointlist[index3] or pointlist[index3] == pointlist[index1]:
        return True
    else:
        return False



def transDotToObj(pathin ,path_out_filename):
    ###对每一层得点数进行记录，每一层索引需偏移前面层点个数得总和

    with open(pathin ,'r') as f:
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
    list_point = list(map(float ,data3))
    list_point1 = []
    ##转换为顶点数组，方便索引
    for ttt in range(0,len(list_point)-2,3):
        list_point1.append([list_point[ttt],list_point[ttt+1],list_point[ttt+2]])


    print(list_point1)
    # 解析索引数组，并转换为整数，注意，原始数组得索引是从1开始得,然后数组中得每个数都要加上numcount
    data4 = data4.replace('[', '')
    data4 = data4.replace(']', ',')
    data4 = data4.split(',')
    data4.pop(-1)
    index_list = list(map(int ,data4))

    line_list = []
    ###
    for i in  range(0,len(index_list)-2,3):
        line1 = [index_list[i], index_list[i + 1]]
        if line1 not in line_list:
            line_list.append(line1)
        else:
            list_point1.append(list_point1[line1[0] - 1])
            list_point1.append(list_point1[line1[1] - 1])
            index_list[i] = len(list_point1) - 1
            index_list[i+1] = len(list_point1)

        line2 = [index_list[i + 1], index_list[i + 2]]
        if line2 not in line_list:
            line_list.append(line2)
        else:
            list_point1.append(list_point1[line2[0] - 1])
            list_point1.append(list_point1[line2[1] - 1])
            index_list[i+1] = len(list_point1) - 1
            index_list[i+2] = len(list_point1)

        line3 = [index_list[i + 2], index_list[i]]
        if  line3 not in line_list:
            line_list.append(line3)
        else:
            list_point1.append(list_point1[line3[0] - 1])
            list_point1.append(list_point1[line3[1] - 1])
            index_list[i+2] = len(list_point1)-1
            index_list[i] = len(list_point1)
    print(len(list_point1))
    ##再展开list_point1
    final_point_list = []
    for iii in range(len(list_point1)):
        final_point_list.append(list_point1[iii][0])
        final_point_list.append(list_point1[iii][1])
        final_point_list.append(list_point1[iii][2])
    print(len(final_point_list))
    list_point = final_point_list
    #### 写数据
    with open(path_out_filename ,'w') as fo:
        # group_message = "g num{}\n".format(i)
        # fo.writelines(group_message)
        # fo.writelines("s off\n")
        ####写顶点
        for num_p in range(0 ,len(list_point) - 2 ,3):
            fo.writelines("v ")
            fo.writelines(str(list_point[num_p]))
            fo.writelines(" ")
            fo.writelines(str(list_point[num_p +2]))
            fo.writelines(" ")
            fo.writelines(str(-list_point[num_p +1]))
            fo.writelines("\n")

        for num_i in range(0 ,len(index_list) - 2 ,3):
            fo.writelines("f ")
            fo.writelines(str(index_list[num_i]))
            fo.writelines(" ")
            fo.writelines(str(index_list[num_i +1]))
            fo.writelines(" ")
            fo.writelines(str(index_list[num_i +2]))
            fo.writelines("\n")

        fo.writelines("\n")



    print("-------------------------------------------------")





if __name__ == '__main__':

    dic_in = r"E:\work\2021.4\mawanmodel\MDT22\MDT22\\"
    out_path = r"E:\work\2021.4\mawanmodel\MDT22\no\\"
    ###批处理
    for i in range(0 ,13):
        path1 = dic_in +'{}.dat'.format(i)
        path2 = out_path + "{}.obj".format(i)
        transDotToObj(path1 ,path2)