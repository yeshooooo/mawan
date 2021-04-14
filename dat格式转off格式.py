def transDotToObj(dict,file_max_num,path_out_filename):
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
        index = [x + numcount for x in index_list] ##针对off文件数组从0开始
        numofface = len(index_list)

        #### 写数据
        ##
        with open(path_out_filename,'a') as fo:
            # group_message = "g num{}\n".format(i)
            # fo.writelines(group_message)
            # fo.writelines("s off\n")
            ###写文件头
            fo.writelines("OFF\n")
            fo.writelines(str(numofpoint))
            fo.writelines(" ")
            fo.writelines(str(numofface))
            fo.writelines(" ")
            fo.writelines("0\n")
            fo.writelines("\n")
            ####写顶点
            for num_p in range(0,len(list_point) - 2,3):
                # fo.writelines("v ")
                fo.writelines(str(list_point[num_p]))
                fo.writelines(" ")
                fo.writelines(str(list_point[num_p+1]))
                fo.writelines(" ")
                fo.writelines(str(list_point[num_p+2]))
                fo.writelines("\n")
            # group_message = "g num{}\n".format(i)
            # fo.writelines(group_message)
            # fo.writelines("s off\n")
            for num_i in range(0,len(index) - 2,3):
                fo.writelines("3 ")
                fo.writelines(str(index[num_i]))
                fo.writelines(" ")
                fo.writelines(str(index[num_i+1]))
                fo.writelines(" ")
                fo.writelines(str(index[num_i+2]))
                fo.writelines("\n")
            # fo.writelines("# end of num {}".format(i))
            fo.writelines("\n")

        numcount += numofpoint
        print("第{}层完成".format(i))
        print("-------------------------------------------------")





if __name__ == '__main__':

    dic_in = r"E:\work\2021.4\mawanmodel\MDT14\MDT14\\"
    out_path = r"E:\work\2021.4\mawanmodel\MDT14\0.off"
    transDotToObj(dic_in,1,out_path)