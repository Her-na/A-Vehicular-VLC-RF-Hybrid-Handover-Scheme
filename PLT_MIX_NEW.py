import numpy as np
import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate,Image
from reportlab.lib.styles import getSampleStyleSheet
from matplotlib import rcParams

config = {
    "font.family":'Times New Roman'
}
rcParams.update(config)
rcParams['font.size'] = 13
#Handover delay作为自变量  这里固定水平delay为0.1 变化垂直delay

#自变量
tao_all = np.array([0.1, 0.2, 0.3, 0.4, 0.5])

#队列长度
l_OVHO = [1.64079983, 1.67451898, 1.79314761, 1.9869306,  2.30650115]
l_IVHO = [1.49580091, 1.57902374, 1.56342546, 1.70361494, 1.7644226]
l_DVHO1 = [1.77155406, 2.0137756,  2.16888805, 2.18636349, 2.4928682]
l_DVHO2 = [2.1351898,  2.52318286, 2.6470404,  2.79597452, 2.94882495]
l_IHO = [1.3977363,  1.56391858, 1.47518558, 1.58018632, 1.72005902]
l_DIHO1 = [1.68658203, 1.81052168, 2.06850253, 2.16491807, 2.3756205]
l_DIHO2 = [2.15271742, 2.3494197,  2.57146401, 2.73457243, 2.87146036]

#队列长度画图
plt.figure(1)
plt.title("The Average Queue Length")
plt.plot(tao_all, l_OVHO, color='red', marker='o', label='O-HO')
plt.plot(tao_all, l_IVHO, color='blue', marker='s', label='I-VHO')
plt.plot(tao_all, l_DVHO1, color='green', marker='p', label='D-VHO1 Time=0.3s')
plt.plot(tao_all, l_DVHO2, color='yellow', marker='h', label='D-VHO2 Time=0.6s')
plt.plot(tao_all, l_IHO, color='black', marker='*', label='I-HO')
plt.plot(tao_all, l_DIHO1, color='pink', marker='+', label='D-HO1 Time=0.3s')
plt.plot(tao_all, l_DIHO2, color='aqua', marker='.', label='D-HO2 Time=0.6s')
plt.xlabel("Handover Delay \u03C4$_{VHO}$ (s) ")
plt.ylabel("the average queue length l (number)")
plt.legend()

#丢包率
DB_OVHO = [0.417393, 0.436025, 0.628044, 0.731765, 1.166936]
DB_IVHO = [0.283156, 0.411281, 0.308116, 0.536424, 0.561321]
DB_DVHO1 = [0.563897, 0.986462, 1.430429, 1.514847, 2.188386]
DB_DVHO2 = [1.163365, 2.383584, 2.448056, 3.467591, 3.80206]
DB_IHO = [0.249377, 0.3108,   0.350219, 0.40178,  0.470118]
DB_DHO1 = [0.4899,   0.618321, 1.238701, 1.223301, 1.816875]
DB_DHO2 = [1.409196, 2.081572, 2.61763,  3.600706, 3.60446]

#丢包率作图
plt.figure(2)
plt.title("The Packet Loss Rate")
plt.plot(tao_all,DB_OVHO, color='red', marker='o', label='O-HO')
plt.plot(tao_all, DB_IVHO, color='blue', marker='s', label='I-VHO')
plt.plot(tao_all, DB_DVHO1, color='green', marker='p', label='D-VHO1 Time=0.3s')
plt.plot(tao_all, DB_DVHO2, color='yellow', marker='h', label='D-VHO2 Time=0.6s')
plt.plot(tao_all, DB_IHO, color='black', marker='*', label='I-HO')
plt.plot(tao_all, DB_DHO1, color='pink', marker='+', label='D-HO1 Time=0.3s')
plt.plot(tao_all, DB_DHO2, color='aqua', marker='.', label='D-HO2 Time=0.6s')
plt.xlabel("Handover Delay \u03C4$_{VHO}$ (s) ")
plt.ylabel("the packet loss rate \u03C1 (%)")
plt.legend()

#延迟时间
delay_OVHO = [4.11856827, 4.22037172, 4.57079799, 4.71204334, 5.64411848]
delay_IVHO = [3.95297258, 4.09031268, 4.03894236, 4.52657459, 4.52311807]
delay_DVHO1 = [5.117841,   5.58380497, 6.01978672, 5.8921706,  6.70701554]
delay_DVHO2 = [6.21246206, 7.1248253, 7.54033941, 7.6361246,  7.71475276]
delay_IHO = [3.65522436, 4.08092063, 3.83658085, 4.0342487,  4.39245428]
delay_DHO1 = [4.60074119, 4.91700649, 5.50733046, 5.59806124, 6.19954967]
delay_DHO2 = [5.71073395, 6.23001986, 6.72386886, 6.95292486, 7.34202393]

#延迟时间做图
plt.figure(3)
plt.title("Average Delay")
plt.plot(tao_all, delay_OVHO, color='red', marker='o', label='O-HO')
plt.plot(tao_all, delay_IVHO, color='blue', marker='s', label='I-VHO')
plt.plot(tao_all, delay_DVHO1, color='green', marker='p', label='D-VHO1 Time=0.3s')
plt.plot(tao_all, delay_DVHO2, color='yellow', marker='h', label='D-VHO2 Time=0.6s')
plt.plot(tao_all, delay_IHO, color='black', marker='*', label='I-HO')
plt.plot(tao_all, delay_DHO1, color='pink', marker='+', label='D-HO1 Time=0.3s')
plt.plot(tao_all, delay_DHO2, color='aqua', marker='.', label='D-HO2 Time=0.6s')
plt.xlabel("Handover Delay \u03C4$_{VHO}$ (s) ")
plt.ylabel("average delay d (s)")
plt.legend(loc='upper left')

#切换次数（垂直）
n0 = [2602., 2330., 1696., 1388., 739.]
n1 = [4548., 4406., 4298., 3945., 3867.]
n2 = [3722., 3550., 3095., 2953., 2731.]
n3 = [2743., 2509., 2232., 2001., 1729.]
n4 = [4081., 3932., 3797., 3585., 3467.]
n5 = [3336., 3050., 2837., 2587., 2327.]
n6 = [2456., 2158., 1915., 1609., 1439.]

#切换次数做图
plt.figure(4)
plt.title("The Number Of VHO")
plt.plot(tao_all, n0, color='red', marker='o', label='O-HO')
plt.plot(tao_all, n1, color='blue', marker='s', label='I-VHO')
plt.plot(tao_all, n2, color='green', marker='p', label='D-VHO1 Time=0.3s')
plt.plot(tao_all, n3, color='yellow', marker='h', label='D-VHO2 Time=0.6s')
plt.plot(tao_all, n4, color='black', marker='*', label='I-HO')
plt.plot(tao_all, n5, color='pink', marker='+', label='D-HO1 Time=0.3s')
plt.plot(tao_all, n6, color='aqua', marker='.', label='D-HO2 Time=0.6s')
plt.xlabel("Handover Delay \u03C4$_{VHO}$ (s) ")
plt.ylabel("the number of VHO c (times)")
plt.legend(loc='lower right')

#Changing Rate作为自变量 tao_VHO=0.3s tao_HHO=0.1s
#这里 0.75

#自变量
beta_1_all = np.array([0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1])

#平均队列长度
l_OVHO_beta = [2.13460389, 2.12690718, 2.0337518,  1.94500658, 1.8429139,  1.88249194,
 1.78255094, 1.85371239, 1.80895309]
l_IVHO_beta = [2.33136851, 2.10107713, 2.03479147, 1.84517891, 1.832989,   1.78947726,
 1.64498084, 1.64056433, 1.57180931]
l_DVHO1_beta = [3.38457402, 2.83631899, 2.64419925, 2.56121171, 2.41864861, 2.2742143,
 2.12039643, 2.07479986, 1.93438459]
l_DVHO2_beta = [4.40988735, 4.31356934, 3.90432158, 3.69638894, 3.374677,   3.14055798,
 2.99219933, 2.71512593, 2.48423929]
l_IHO_beta = [2.09406882, 1.89961179, 1.73800103, 1.66293633, 1.59589678, 1.61400203,
 1.55572197, 1.57313168, 1.55200785]
l_DIHO1_beta = [2.84752443, 2.84994746, 2.33242223, 2.44002999, 2.2631121,  2.25651371,
 2.02490031, 1.94524505, 1.96368546]
l_DIHO2_beta = [4.37419425, 4.01996917, 3.89771093, 3.35540963, 3.01477874, 2.86919157,
 2.68597196, 2.50480046, 2.36961245]

plt.figure(5)
plt.title("The Average Queue Length")
plt.plot(beta_1_all, l_OVHO_beta, color='red', marker='o', label='O-HO')
plt.plot(beta_1_all, l_IVHO_beta, color='blue', marker='s', label='I-VHO')
plt.plot(beta_1_all, l_DVHO1_beta, color='green', marker='p', label='D-VHO1 Time=0.3s')
plt.plot(beta_1_all, l_DVHO2_beta, color='yellow', marker='h', label='D-VHO2 Time=0.6s')
plt.plot(beta_1_all, l_IHO_beta, color='black', marker='*', label='I-HO')
plt.plot(beta_1_all, l_DIHO1_beta, color='pink', marker='+', label='D-HO1 Time=0.3s')
plt.plot(beta_1_all, l_DIHO2_beta, color='aqua', marker='.', label='D-HO2 Time=0.6s')
plt.xlabel("Rate of optical channel changing \u03B2$_1$ \u03B2$_{-1}$ (s$^{-1}$) ")
plt.ylabel("the average queue length l (number)")
plt.legend()

#丢包率

DB0_beta = [0.866157, 0.773994, 0.583534, 0.540854, 0.41608,  0.69031,
 0.45787,  0.388266, 0.454861]
DB1_beta = [1.321847, 0.856825, 0.982576, 0.551984, 0.508587, 0.454313,
 0.310415, 0.411926, 0.452519]
DB2_beta = [3.585628, 2.796445, 2.153076, 2.065826, 1.833903, 1.418877,
 1.326665, 1.027141, 0.907014]
DB3_beta = [9.904471, 10.455494, 7.32704,  6.774057, 5.895849, 3.976842,
 3.389034, 2.722839, 2.222964]
DB4_beta = [1.011322, 0.504264, 0.709673, 0.469573, 0.310198, 0.655949,
 0.430315, 0.420848, 0.259444]
DB5_beta = [3.118317, 2.777778, 1.693543, 1.790865, 1.144285, 1.243813,
 1.298093, 0.79713,  0.910723]
DB6_beta = [11.257648, 9.765394, 8.406027, 5.772169, 4.229052, 3.260229,
 2.996866, 2.40145,  2.025448]

plt.figure(6)
plt.title("The Packet Loss Rate")
plt.plot(beta_1_all, DB0_beta, color='red', marker='o', label='O-HO')
plt.plot(beta_1_all, DB1_beta, color='blue', marker='s', label='I-VHO')
plt.plot(beta_1_all, DB2_beta, color='green', marker='p', label='D-VHO1 Time=0.3s')
plt.plot(beta_1_all, DB3_beta, color='yellow', marker='h', label='D-VHO2 Time=0.6s')
plt.plot(beta_1_all, DB4_beta, color='black', marker='*', label='I-HO')
plt.plot(beta_1_all, DB5_beta, color='pink', marker='+', label='D-HO1 Time=0.3s')
plt.plot(beta_1_all, DB6_beta, color='aqua', marker='.', label='D-HO2 Time=0.6s')
plt.xlabel("Rate of optical channel changing \u03B2$_1$ \u03B2$_{-1}$ (s$^{-1}$) ")
plt.ylabel("the packet loss rate \u03C1 (%)")
plt.legend()

#平均延时时间

delay1_beta =[5.32898613, 5.1919151,  5.06191665, 4.90918175, 4.61487336, 4.77595364,
 4.41471891, 4.54564838, 4.51934107]
delay2_beta =[6.22222106, 5.49471994, 5.38989767, 4.80997781, 4.98091567, 4.52424914,
 4.33734917, 4.2816576,  4.16301001]
delay3_beta =[10.51446664,  8.51050346,  7.89769511,  7.32459522,  6.93420255,  6.37470519,
  5.99424407,  5.70236459,  5.24928749]
delay4_beta = [14.98503852, 13.9428597,  11.99467981, 11.24979507,  9.98195388,  8.89260179,
  8.32435092,  7.4844999,   6.72455912]
delay5_beta = [5.44846584, 4.71913251, 4.39896435, 4.13780395, 4.10383669, 4.16718101,
 3.95198118, 4.08083444, 3.8630711]
delay6_beta =[8.07018013, 7.78214839, 6.40469577, 6.68366611, 5.98586422, 5.93837831,
 5.43697496, 5.1504106,  5.0686061]
delay7_beta = [13.02439935, 11.53005642, 11.09985616,  9.27450218,  8.24114754,  7.65146038,
  7.05939532,  6.48176827,  6.11570334]

plt.figure(7)
plt.title("Average Delay")
plt.plot(beta_1_all, delay1_beta, color='red', marker='o', label='O-HO')
plt.plot(beta_1_all, delay2_beta, color='blue', marker='s', label='I-VHO')
plt.plot(beta_1_all, delay3_beta, color='green', marker='p', label='D-VHO1 Time=0.3s')
plt.plot(beta_1_all, delay4_beta, color='yellow', marker='h', label='D-VHO2 Time=0.6s')
plt.plot(beta_1_all, delay5_beta, color='black', marker='*', label='I-HO')
plt.plot(beta_1_all, delay6_beta, color='pink', marker='+', label='D-HO1 Time=0.3s')
plt.plot(beta_1_all, delay7_beta, color='aqua', marker='.', label='D-HO2 Time=0.6s')
plt.xlabel("Rate of optical channel changing \u03B2$_1$ \u03B2$_{-1}$ (s$^{-1}$) ")
plt.ylabel("average delay d (s)")
plt.legend()

#VHO切换次数

n0_beta = [2303., 2391., 2497., 2322., 2218., 2230., 2171., 1751., 1681.]
n1_beta = [3027., 3447., 3592., 3743., 3966., 4123., 4126., 4140., 4173.]
n2_beta = [2381., 2837., 2790., 3045., 3042., 3186., 3185., 3085., 3148.]
n3_beta = [1870., 2150., 2303., 2287., 2320., 2376., 2245., 2292., 2178.]
n4_beta = [3184., 3486., 3473., 3606., 3596., 3824., 3841., 3944., 3940.]
n5_beta = [2523., 2719., 2822., 2883., 2893., 2920., 2915., 2872., 2842.]
n6_beta = [2000., 2047., 2080., 2150., 2103., 2090., 1958., 1883., 1783.]

plt.figure(8)
plt.title("The Number Of VHO")
plt.plot(beta_1_all, n0_beta, color='red', marker='o', label='O-HO')
plt.plot(beta_1_all, n1_beta, color='blue', marker='s', label='I-VHO')
plt.plot(beta_1_all, n2_beta, color='green', marker='p', label='D-VHO1 Time=0.3s')
plt.plot(beta_1_all, n3_beta, color='yellow', marker='h', label='D-VHO2 Time=0.6s')
plt.plot(beta_1_all, n4_beta, color='black', marker='*', label='I-HO')
plt.plot(beta_1_all, n5_beta, color='pink', marker='+', label='D-HO1 Time=0.3s')
plt.plot(beta_1_all, n6_beta, color='aqua', marker='.', label='D-HO2 Time=0.6s')
plt.xlabel("Rate of optical channel changing \u03B2$_1$ \u03B2$_{-1}$ (s$^{-1}$) ")
plt.ylabel("the number of VHO c (times)")
plt.legend()

doc1 = SimpleDocTemplate(r"C:\Users\Herna\Desktop\MDPSH_MIX_1.pdf",pagesize=(800,800))
doc2 = SimpleDocTemplate(r"C:\Users\Herna\Desktop\MDPSH_MIX_2.pdf",pagesize=(800,800))
doc3 = SimpleDocTemplate(r"C:\Users\Herna\Desktop\MDPSH_MIX_3.pdf",pagesize=(800,800))
doc4 = SimpleDocTemplate(r"C:\Users\Herna\Desktop\MDPSH_MIX_4.pdf",pagesize=(800,800))
doc5 = SimpleDocTemplate(r"C:\Users\Herna\Desktop\MDPSH_MIX_5.pdf",pagesize=(800,800))
doc6 = SimpleDocTemplate(r"C:\Users\Herna\Desktop\MDPSH_MIX_6.pdf",pagesize=(800,800))
doc7 = SimpleDocTemplate(r"C:\Users\Herna\Desktop\MDPSH_MIX_7.pdf",pagesize=(800,800))
doc8 = SimpleDocTemplate(r"C:\Users\Herna\Desktop\MDPSH_MIX_8.pdf",pagesize=(800,800))
styles = getSampleStyleSheet()
style = styles['Normal']
story1 =[]
story2 =[]
story3 =[]
story4 =[]
story5 =[]
story6 =[]
story7 =[]
story8 =[]
#Image里面写图片的路径
#图片的大小及长宽最好不要超过500*500px,太大了会显示不出来
#写路径时前面最好加r"c:\XXXX"
t1 = Image(r"C:\Users\Herna\Desktop\Figure_MIX_1.png")
t2 = Image(r"C:\Users\Herna\Desktop\Figure_MIX_2.png")
t3 = Image(r"C:\Users\Herna\Desktop\Figure_MIX_3.png")
t4 = Image(r"C:\Users\Herna\Desktop\Figure_MIX_4.png")
t5 = Image(r"C:\Users\Herna\Desktop\Figure_MIX_5.png")
t6 = Image(r"C:\Users\Herna\Desktop\Figure_MIX_6.png")
t7 = Image(r"C:\Users\Herna\Desktop\Figure_MIX_7.png")
t8 = Image(r"C:\Users\Herna\Desktop\Figure_MIX_8.png")
story1.append(t1)
story2.append(t2)
story3.append(t3)
story4.append(t4)
story5.append(t5)
story6.append(t6)
story7.append(t7)
story8.append(t8)
doc1.build(story1)
doc2.build(story2)
doc3.build(story3)
doc4.build(story4)
doc5.build(story5)
doc6.build(story6)
doc7.build(story7)
doc8.build(story8)

plt.show()