import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#######################总体分布为圆弧1--线段1--圆弧2--线段2
##############1 求中线的总长度
################################各段往左偏移7.5米
##圆弧1段，圆心圆心 点， X=97315.3599  Y=16885.2264  Z=   0.0000
#                半径 1998.5250
#                起点 角度    181
#                端点 角度    188
##往左偏移7.5米，所以偏移后的坐标为圆心 X=97315.3599  Y=16885.2264  Z=   0.0000
#### 半径 2006.0250
##起点 角度181，端点角度188
##其中，端点处的坐标为线段1的起点
###弧长公式为L = n * pi *r/180，此处n为7
###圆的公式为
##x = a + rcos(0)
##y = b + rsin(0)
##圆弧最底部坐标为
arc1Bottom_x = 97315.3599 + 2006.0250 * math.cos(188*math.pi/180)
arc1Bottom_y = 16885.2264 + 2006.0250 * math.sin(188*math.pi/180)

arc1top_x = 97315.3599 + 2006.0250 * math.cos(181*math.pi/180)#
arc1top_y = 16885.2264 + 2006.0250 * math.sin(181*math.pi/180)#此处的xy为线段1的起点
arc1_length = 7 * math.pi *2006.0250/180

###圆弧2
##圆心 点， X=93311.2628  Y=17170.7258  Z=   0.0000
#                半径 2008.9750
#                起点 角度      1
#                端点 角度     15
arc2Bottom_x = 93311.2628 + 2008.9750 * math.cos(1*math.pi/180)
arc2Bottom_y = 17170.7258 + 2008.9750 * math.sin(1*math.pi/180) ##线段1的终点
#########线段1的长度为

line1_length = math.sqrt((arc1top_x - arc2Bottom_x)**2 + (arc1top_y - arc2Bottom_y)**2)

####
arc2top_x = 93311.2628 + 2008.9750 * math.cos(15*math.pi/180)#
arc2top_y = 17170.7258 + 2008.9750 * math.sin(15*math.pi/180)#此处的xy为线段2的起点
arc2_length = 14 * math.pi *2008.9750/180

########################线段2 终点的偏移为 X=94989.7391  Y=18638.6617  Z=   0.0000 往左偏移7.5米
line2_begin = np.array([95244.4013,17689.2601,0])
line2_end = np.array([94989.7391,18638.6617,0])
vecLine2 = line2_end - line2_begin
tem_vec = np.cross(vecLine2,np.array([0,0,1]))
uint_vec = tem_vec/np.linalg.norm(tem_vec)
vec_mig = uint_vec*7.5
mig_end = line2_end - vec_mig ##这个点就是x2的终点的三维形式
line2_end_x = mig_end[0]
line2_end_y = mig_end[1]

###############################line2长度为
line2_length = math.sqrt((line2_end_x-arc2top_x)**2 + (line2_end_y-arc2top_y)**2)

###总长度为
length_all = arc1_length + line1_length + arc2_length +line2_length
# print(length_all)
# step = length_all/1030 ###为了平均掉误差，步长选总长度除以环数
step = 2.01  ###因为后续误差的原因，经过试验，当步长取2.01时，正好能分成1030环

###每段环数

num_arc1 = int(arc1_length/ step) ###121
print(num_arc1)
num_line1 = int(line1_length/step) ###176
print(num_line1)
num_arc2 = int(arc2_length/step) ### 244
print(num_arc2)
num_line2 = int(line2_length/step) ###489
print(num_line2)
print(num_arc1+num_line1+num_arc2+num_line2)


X = []
Y = []
##起点坐标为圆弧段起点坐标
X.append(arc1Bottom_x)
Y.append(arc1Bottom_y)
###############################################################
####圆弧段 121环，每一环的度数为 188 - i* 7 / 121.0
##最后一环的坐标不取，将误差平均进最后一环，坐标取圆弧段实际的的顶部,在线段部分添加

for i in range(1,121):
    tem_degree = 188 - i* 7 / 121.0
    tem_x = 97315.3599 + 2006.0250 * math.cos(tem_degree*math.pi/180)
    tem_y = 16885.2264 + 2006.0250 * math.sin(tem_degree*math.pi/180)
    X.append(tem_x)
    Y.append(tem_y)
print("圆弧段不包括终点的点个数应为121个，实际为： ",len(X))
######################################################
###直线1 段，共计176环，但是起点为圆弧段终点，所以最终添加点个数也为176个，为了逻辑上的统一，最后一环的终点，放在下一段圆弧处添加
line1_x_np = np.linspace(arc1top_x,arc2Bottom_x,177)
line1_y_np = np.linspace(arc1top_y,arc2Bottom_y,177)
# print("aaaaa",len(line1_y_np))
for i in range(len(line1_x_np) - 1):
    X.append(float(line1_x_np[i]))
    Y.append(float(line1_y_np[i]))
print("添加完圆弧后应为176 + 121 = 297个，实际为： ",len(X))
############################################################
###圆弧段2  244环 ，同圆弧段1 ，每一环的度数为1 + i*14 / 244.0 ,同样也不包括终点，放在下一段直线中
##添加圆弧段2起点
X.append(arc2Bottom_x)
Y.append(arc2Bottom_y)

####
for i in range(1,244):
    tem_degree = 1 + i*14 / 244.0
    tem_x = 93311.2628 + 2008.9750 * math.cos(tem_degree * math.pi / 180)
    tem_y = 17170.7258 + 2008.9750 * math.sin(tem_degree * math.pi / 180)
    X.append(tem_x)
    Y.append(tem_y)
######最后一段直线  489环,所以一共490个点，包括起点和终点
line2_x_np = np.linspace(arc2top_x,line2_end_x,490)
line2_y_np = np.linspace(arc2top_y,line2_end_y,490)
for i in range(len(line2_x_np)):
    X.append(float(line2_x_np[i]))
    Y.append(float(line2_y_np[i]))

########测试
# print("X的个数",len(X))
# print("Y的个数",len(Y))
# print(X)
# print(Y)
# plt.plot(X,Y,'o')
# plt.show()



##############################高度部分
path = r'E:\work\2021.3\数据\cad导出轴线.xlsx'
data = pd.read_excel(path)
x = data['x']
y = data['y']
###x之间的差
dis = max(x) - min(x)
print(dis)
print(1030*5)

#####不算这段数据的首尾，一共需要1129个点
##
x_face = []
y_face = []
###加头
x_face.append(16811.2935)
y_face.append(-1129.744)

###函数，已知x，定位x的位置后返回y
def get_y(x_x):
    for t in range(len(x) - 1):
        if (x_x >= x[t]) and (x_x < x[t + 1]):
            k = (y[t+1] - y[t])/(x[t+1] - x[t])
            y_rrr = k*(x_x - x[t]) + y[t]
            return y_rrr


for  i in  range(1,1030):
    x_to_add = 16811.2935 + i*5
    x_face.append(x_to_add)
    y_to_add = get_y(x_to_add)
    y_face.append(y_to_add)


####添加最后一个点
x_face.append(21961.2935)
y_face.append(-1103.459)
print(x_face)
print(y_face)
print(len(x_face))
print(len(y_face))
z_final = [lalala*64.95/163+433.639816 - 7.5 for lalala in y_face]
print(z_final)
data = {'x': X,'y':Y,'z':z_final}
df = pd.DataFrame(data)
df.to_excel(r"E:\work\2021.3\数据\计算得出中轴线每环坐标.xlsx")

####罗德里格旋转公式
def get_xyz(x1,y1,z1,x2,y2,z2,n):
    ###求单位向量
    vecx1x2 = np.array([x2 - x1,y2 - y1,z2 - z1])
    uint_vecx1x2 = vecx1x2/np.linalg.norm(vecx1x2)##x2-x1方向的单位向量就是转动向量
    ####初始向量，所有的环都设置为[0,0,7.5]
    vec_k = np.array([0,0,7.5])
    avg = math.pi /(n)
    first_point = np.array([x1,y1,z1])
    f_container = []

    for i_a in range(0,n):
        vecrot = math.cos(i_a*avg)*uint_vecx1x2 + (1 - math.cos(i_a*avg))*(np.dot(uint_vecx1x2,vec_k)) + math.sin(i_a*avg)*(np.cross(vec_k,uint_vecx1x2))
        tem_fpo = first_point+vecrot
        f_container.append(tem_fpo)
    second_point = np.array([x2,y2,z2])
    s_container = []
    for i_b in range(0,n):
        vecrot2 = math.cos(i_a*avg)*uint_vecx1x2 + (1 - math.cos(i_a*avg))*(np.dot(uint_vecx1x2,vec_k)) + math.sin(i_a*avg)*(np.cross(vec_k,uint_vecx1x2))
        tem_fpo2 = second_point+vecrot
        s_container.append(tem_fpo2)
    print(len(f_container))
    return f_container,s_container
t = get_xyz(95328.8573974027,16606.0416801466,-24.025047803681,95328.576518747,16608.0475829847,-24.0987650702807,12)
print(t)







