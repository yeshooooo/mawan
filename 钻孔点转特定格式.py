###为程序可读性，不考虑效率，不使用map函数，也不使用线程池
#utf-8
import pandas as pd
import json

def transFormOfDrills(path_drills_data,out_put_path):
    origindata = pd.read_excel(path_drills_data)
    output = []
    origindata["时代成因合并"] = origindata["时代成因合并"].fillna(' ')
    origindata["稳定水位深度"] = origindata["稳定水位深度"].fillna(' ')
    origindata["开工日期"] = origindata["开工日期"].fillna(' ')
    origindata["竣工日期"] = origindata["竣工日期"].fillna(' ')

    for index,row in origindata.iterrows():
        temp_dict = {}
        temp_dict["FID"] = str(index)
        temp_dict["gcmc"] = row["工程名称"]
        temp_dict["zkbh"] = row["钻孔编号"]
        temp_dict["gcbh"] = row["工程编号"]
        temp_dict["s"] = " "
        temp_dict["x"] = str(row["x"])
        temp_dict["y"] = str(row["y"])
        x = float(row["x"])
        y = float(row["y"])
        jd =  x*-1.62587*0.0000001+y*9.72822*0.000001+112.9402592
        wd =  x*9.02593*0.000001+y*1.46935*0.0000001+22.35169056
        temp_dict["jd"] = str(jd)
        temp_dict["wd"] = str(wd)
        temp_dict["start"] = row["开工日期"]
        temp_dict["finish"] = row["竣工日期"]
        temp_dict["zktype"] = " "
        # if row["稳定水位深度"] == None :
        #     temp_dict["wdswsd"] = " "
        # else:
        #     temp_dict["wdswsd"] = row["稳定水位深度"]
        temp_dict["wdswsd"] = str(row["稳定水位深度"])
        temp_dict["sdcy"] = str(row["时代成因合并"])
        temp_dict["dcbh"] = str(row["地层编号合并"]).replace(' ','-')
        temp_dict["type"] = row["type"]
        temp_dict["H0"] = str(row["孔口高程"])
        temp_dict["S1"] = str(row["层底深度"])
        temp_dict["H"] = str(row["层底高程"])
        temp_dict["G"] = str(row["层厚"])
        temp_dict["yx"] = row["岩层名称"]
        temp_miaoshu = row["岩层描述"]
        temp_miaoshu.replace(' ','')
        if ('wsc图' in temp_miaoshu):
            ii = temp_miaoshu.index("wsc图")
            good_miaoshu = temp_miaoshu[0:ii]
        else:
            good_miaoshu = temp_miaoshu
        temp_dict["D"] = good_miaoshu
        temp_dict["cjsw"] = " "
        temp_dict["lc"] = " "

        output.append(temp_dict)
    print(output)
    with open(out_put_path,mode='w') as f:
        f.write("[")
        for i in range(len(output)):
            if (i < len(output) - 1):
                f.write(str(output[i]).replace('\'','\"') + "," "\n")
            else:
                f.write(str(output[i]).replace('\'','\"'))
        f.write("]")


    # print(output)








if __name__ == '__main__':
    path = r'E:\work\2021.3\数据\妈湾钻孔加虚拟钻孔.xlsx'
    path_out = r"E:\work\2021.3\数据\带虚拟钻孔.json"
    transFormOfDrills(path,path_out)