
def JudgeIfPointRepeat(path_read,path_write):
    with open(path_read,'r') as f:
        data1 = f.readline()
        data2 = f.readline()
        data3 = f.readline()
        data4 = f.readline()
    #解析顶点数组
    data3 = data3.replace('[','')
    data3 = data3.replace(']',',')
    data3 = data3.split(',')
    data3.pop(-1)

    point_list = []
    for i in range(0,len(data3)-2,3):
        point = [float(data3[i]),float(data3[i+1]),float(data3[i+2])]
        point_list.append(point)

    ###解析索引数组
    data4 = data4.replace('[','')
    data4 = data4.replace(']',',')
    data4 = data4.split(',')
    data4.pop(-1)
#####################注意，原始数组的索引是从1开始的，而python中下标是从0开始，这里将原始数字减去1，在最后输出时再加1
    index_list = []
    inner_max = []  ##中间变量，用于求实际索引的最大值
    for i in range(0,len(data4)-2,3):
        ############后记############因为会存在引用压根不存在的点情况，所以需要删除引用这些点的索引,在此处判读，如果存在这样的点，则重点此次循环
        if ( (int(data4[i]) - 1) >= len(point_list) ) or ( (int(data4[i + 1]) - 1) >= len(point_list) ) or ( (int(data4[i + 2]) - 1) >= len(point_list) ):
            continue
        else:
            index = [int(data4[i]) - 1,int(data4[i+1]) - 1,int(data4[i+2]) - 1]


            index_list.append(index)
            inner_max.append(max(index))

    # print(index_list)
    ###下面这个打印用于判断是否引用压根不存在的点
    print('原始数组中的点个数为（这个个数就是就是引用所允许的最大计数） + 1 = ',len(point_list))
    print('索引实际用到的从0计数最大值为',max(inner_max))




#########第一步：将索引数组改为使用重复点第一次出现的那个点的旧索引
    #遍历顶点数组
    ##增：建一个空字典，用来装旧索引之间的映射；一个数组，装后面的重复的数字
    ####后记：经试验，原始数据中，会存在 1 == 2 ，然后2 == 3 的情况，这时候3 仍然映射在2 上，2 确已经没了，所以需要设置一种，能搜索所有点，都映射到第一个出现这个点的算法
    ##通过搜索字典的键数组，查看要建立的映射点是否已经退化成键，如果是，要取这个键的值
    old_map = {}
    old_index_to_del = []####这个数组是贯穿两个步骤的中间变量，用于删除
    for i in range(len(point_list) - 1):
        for j in range(i+1,len(point_list)):
            if (point_list[i][0] == point_list[j][0]) and (point_list[i][1] == point_list[j][1]) and (point_list[i][2] == point_list[j][2]):

                print(point_list[i],i,'等于',point_list[j],j)
                if i in old_map.keys():
                    old_map[j] = old_map[i]
                else:
                    old_map[j] = i
                old_index_to_del.append(j)
    ###遍历原始数组，为字典添加不重复点的映射

    for i in range(len(point_list)):
        if i not in old_map.keys():
            old_map[i] = i
    print("映射字典建立完毕")
    # print("old_map",old_map)
    # print("待删除顶点索引",old_index_to_del)
    print(old_map)
    print(old_map.keys())
    print(len(old_map.keys()))
    # return
    ##遍历索引数组
    ##改：将索引数组中的每个元素，改为上一步映射中的键值
    #键为j，则值为old_map[j]
    ##建一个新数组用来装修改后的值（此处不考虑效率，不在原对象上进行修改）
    new_index_list = [] #这个就是第一步的结果，得到了新的索引方法
    for i in range(len(index_list)):
        index = []
        for j in index_list[i]:
            # print(j)
            # print("old_map[j]",old_map[j])
            index.append(old_map[j])
        new_index_list.append(index)
##################################################备注：上面这块忘了给没重复的做映射，所以会出现没有key的错误，明天修改这个地方#############################################################################################
#######第二步：删除旧的顶点数组中重复的点，并且标记旧索引与新索引的映射
    ##遍历顶点数组
    #增：一个空字典，用来装删除后的索引在新数组中的映射关系 即 键为老索引，值为新索引
    #建立映射的方法，①在原始数组顶点数组中加一个数字，这个数字就是，老的索引序号
    #② 删除xyz，相同的（就是第一步中标记出来的那个old_index_to_del中的索引）

    for i in range(len(point_list)):
        point_list[i].append(i)
    ##删除具有相同的xyz的顶点
    final_point_with_old_index = [point_list[pi] for pi in range(len(point_list)) if pi not in old_index_to_del]
    ###建立新旧顶点之间的映射关系,并且得到最终的顶点数组
    final_point = []
    new_map = {}
    for i in range(len(final_point_with_old_index)):
        new_map[final_point_with_old_index[i][3]] = i
        final_point_with_old_index[i].pop(-1)
        final_point.append(final_point_with_old_index[i])
    print("新数组final_point创建完成")

    ##此处得到了最终的顶点数组final_point
  ###############################################################################
    ###利用新建立的映射关系，去替换第一步得出的顶点数组，并且替换后去重
    final_index_with_repete = []
    for i in range(len(new_index_list)):
        temindex = []
        for j in new_index_list[i]:
            temindex.append(new_map[j])
        final_index_with_repete.append(temindex)
    ##索引数组去重
    final_index_0 = []
    for i in final_index_with_repete:
        if i not in final_index_0:
            final_index_0.append(i)
    ###将数组索引依次加1，改为从1开始
    final_index_1 = []
    print('0开始的索引为:',final_index_0)

    for i in range(len(final_index_0)):
        final_index_1.append([final_index_0[i][0] + 1,final_index_0[i][1] + 1,final_index_0[i][2] + 1])
    print('1开始的索引为:', final_index_1)
#######################验证最终结果#################
    print("开始验证最终结果")
    for i in range(len(final_point) - 1):
        for j in range(i+1,len(final_point)):
            if (final_point[i][0] == final_point[j][0]) and (final_point[i][1] == final_point[j][1]) and (final_point[i][2] == final_point[j][2]):

                print(final_point[i],i,'等于',final_point[j],j)

    print("最终结果验证完成")

#########写入最终结果到文件
    cata = data1 ##因为读进来的时候没有删掉换行，所以这里不用换行
    numofpoint = str(len(final_point))
    numofindex = str(len(final_index_1))
    line2 = numofpoint +',' + numofindex
    line3 = (str(final_point))[1:-1] + '\n'
    line4 = (str(final_index_1))[1:-1] + '\n' ###这里也加一行换行符是因为原始文件中也带着换行符
    ###去除中括号之间的逗号
    line3 = line3.replace('],',']')
    line4 = line4.replace('],',']')
    ####去除空格
    line3 = line3.replace(' ','')
    line4 = line4.replace(' ','')



    with open(path_write,'w') as w:
        w.writelines(str(cata))
        w.writelines(str(line2)+'\n')
        w.write(line3)
        w.write(line4)



if __name__ == '__main__':
    dic1 = r"E:\work\2021.3\数据\MDT11\MDT11\\"
    dic2 = r"E:\work\2021.3\数据\MDT11\NRMDT11\\"
    ######批处理
    for i in range(0,23):
        path1 = dic1 + '{}.dat'.format(i)
        path2 = dic2 + '{}.dat'.format(i)
        JudgeIfPointRepeat(path1,path2)