import numpy as np
import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate,Image
from reportlab.lib.styles import getSampleStyleSheet
from matplotlib import rcParams
#Handover delay作为自变量  这里固定水平delay为0.1 变化垂直delay

config = {
    "font.family":'Times New Roman'
}
rcParams.update(config)
rcParams['font.size'] = 13
#自变量
tao_all = np.array([0.1, 0.2, 0.3, 0.4, 0.5])

#队列长度
l_OVHO = [1.5320398,  1.59808531, 1.81543515, 2.02389856, 2.20360504]
l_IVHO = [1.46491164, 1.49395531, 1.62149251, 1.70556475, 1.76243529]
l_DVHO1 = [1.77662426, 1.95783921, 2.16723886, 2.25056576, 2.30294479]
l_DVHO2 = [2.13814766, 2.51626137, 2.6871044,  2.87861231, 3.16675077]
l_IHO = [1.46236935, 1.45090772, 1.50277829, 1.52884745, 1.65250684]
l_DIHO1 = [1.73657712, 1.77270766, 1.87440132, 2.18793982, 2.31489833]
l_DIHO2 = [2.05898434, 2.25974393, 2.43678619, 2.61143393, 2.56455775]

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
DB_OVHO = [0.439295, 0.237256, 0.577404, 0.504233, 1.11538]
DB_IVHO = [0.334517, 0.242326, 0.328815, 0.379368, 0.450966]
DB_DVHO1 = [0.523673, 0.643465, 1.081873, 1.192219, 1.753075]
DB_DVHO2 = [1.097463, 1.934358, 2.744473, 3.012007, 4.323109]
DB_IHO = [0.22837,  0.248269, 0.307279, 0.329564, 0.443515]
DB_DHO1 = [0.630559, 0.64772,  0.854813, 1.332278, 2.044304]
DB_DHO2 = [1.005747, 1.505117, 2.103741, 2.879733, 2.714159]

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
delay_OVHO = [3.89249496, 4.03869182, 4.58540593 ,4.91814962, 5.36913066]
delay_IVHO = [4.04148386, 4.07505194, 4.3992161,  4.51544018, 4.8713269]
delay_DVHO1 = [5.3482254,  5.52537108, 6.14869032, 6.43226383, 6.39774205]
delay_DVHO2 = [6.34747371, 7.28851582, 7.55474495, 7.89413771, 8.69333434]
delay_IHO = [3.9142037,  3.82359015, 3.82396311, 3.95122501, 4.23518186]
delay_DHO1 = [4.69850466, 4.80976315, 5.02756888, 5.84299468, 5.89738602]
delay_DHO2 = [5.72150717, 5.98969609, 6.44311985, 6.79254816, 6.36960807]

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
plt.legend()

#切换次数（垂直）
n0 = [2884., 2283., 1611., 1282.,  702]
n1 = [4365., 4250., 4054., 3919., 3691]
n2 = [3589., 3422., 3193., 2849., 2703]
n3 = [2831., 2495., 2292., 2058., 1853]
n4 = [3898., 3758., 3728., 3318., 3201]
n5 = [3205., 3058., 2821., 2523., 2218]
n6 = [2383., 2042., 1867., 1614., 1393]

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
plt.legend()

#Changing Rate作为自变量

#自变量
beta_1_all = np.array([0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1])

#平均队列长度
l_OVHO_beta = [2.14082229, 1.95223762, 1.98370413, 1.83485854, 1.89333074, 1.7580736,
 1.80322863, 1.71762876, 1.78006479]
l_IVHO_beta = [2.29666148, 2.13035528, 2.01836739, 1.84796566, 1.77768379, 1.70688901,
 1.64826442, 1.64467192, 1.54301104]
l_DVHO1_beta = [2.81309564, 2.75637194, 2.55208624, 2.49154235, 2.32818585, 2.20052987,
 2.21364953, 2.05449547, 2.04809225]
l_DVHO2_beta = [4.09926503, 4.07149478, 3.7727245,  3.36276411, 3.20706797, 2.97640197,
 2.88753504, 2.64889706, 2.47979234]
l_IHO_beta = [2.04711162, 1.87660326, 1.84382706, 1.74932104, 1.75806225, 1.67911045,
 1.53091016, 1.46722201, 1.4902936 ]
l_DIHO1_beta = [2.91434047, 2.76767488, 2.48494989, 2.31180129, 2.26390339, 2.17036016,
 2.09959371, 1.96236405, 1.87369229]
l_DIHO2_beta = [4.1018522,  3.78293391, 3.6122875,  3.37223998, 2.95890363, 2.73193174,
 2.57947003, 2.53295344, 2.25667124]

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

DB0_beta = [0.01116751, 0.00556285, 0.00821551, 0.0064023 , 0.00525742, 0.00389004,
 0.00668517, 0.00477008, 0.00563669]
DB1_beta = [0.01429053, 0.01037182, 0.01032019, 0.00545271, 0.00664207, 0.00398541,
 0.00444086, 0.00415102, 0.00356849]
DB2_beta = [0.0264367,  0.02177226, 0.0204067,  0.01899505, 0.01454649, 0.01111574,
 0.01079435, 0.01217094, 0.00914932]
DB3_beta = [0.07793125, 0.07914152, 0.07273254, 0.0519415,  0.04324172, 0.03410864,
 0.0332588,  0.0243953,  0.01555032]
DB4_beta = [0.01038912, 0.00595955, 0.00557033, 0.00754243, 0.00645821, 0.0051837,
 0.00301165, 0.00064537, 0.00309119]
DB5_beta = [0.02975207, 0.02870111, 0.01564178, 0.01591179, 0.01353773, 0.01554946,
 0.0101098,  0.00701685, 0.00738581]
DB6_beta = [0.099068,   0.08151671, 0.06993239, 0.05787189, 0.04112639, 0.02588204,
 0.0259351,  0.02435457, 0.01533034]

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

delay1_beta =[5.4828495,  4.76082399, 4.88869507, 4.78228608, 4.81113924, 4.40630024,
 4.51358382, 4.34991756, 4.57340435]
delay2_beta =[8.89525468, 8.43064997, 7.65797727, 7.3402172,  6.90083201, 6.18195307,
 6.14598428, 5.73525552, 5.76564804]
delay3_beta =[10.37715478,  8.60644126,  8.19487174,  7.94505998,  7.40520346,  6.78107087,
  6.34752086,  6.40803052,  6.35789527]
delay4_beta = [13.97978892, 13.23762335, 11.69784131, 10.37257594,  9.51391997,  8.79429295,
  8.40154339,  7.57498502,  6.73777196]
delay5_beta = [5.22349734, 4.76932715, 4.6515333,  4.39412874, 4.48208984, 4.32251146,
 3.95849577, 3.82322692, 3.84938858]
delay6_beta =[8.33899215, 7.69874485, 6.89337895, 6.12097826, 6.09460563, 5.81256011,
 5.5892053,  5.12066493, 4.84249815]
delay7_beta = [12.24835747, 10.76981186,  9.9260789,   9.19355629,  7.89563005,  7.32062121,
 6.70847064,  6.46891546,  5.80466275]

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

n0_beta = [2190., 2386., 2310., 2316., 2264., 2138., 2139., 1617., 1611.]
n1_beta = [2852., 3223., 3450., 3763., 3756., 3870., 3993., 4075., 4024.]
n2_beta = [2229., 2663., 2885., 2935., 3010., 3121., 3082., 3105., 3169.]
n3_beta = [1836., 2056., 2257., 2302., 2323., 2274., 2324., 2193., 2157.]
n4_beta = [3173., 3169., 3452., 3467., 3598., 3638., 3627., 3512., 3587.]
n5_beta = [2468., 2737., 2667., 2868., 2821., 2814., 2715., 2759., 2746.]
n6_beta = [2040., 2136., 2032., 2135., 2035., 2008., 1972., 1889., 1703.]

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

#Alpha 2->1 作为自变量

#自变量
Alpha21_Alpha12 = np.array([0.25, 0.5, 1, 2, 4])

#队列长度
l_OVHO_alpha = [1.81296662,  1.71923638, 1.80683387, 1.8318788, 1.96544813]
l_IVHO_alpha = [1.61856024, 1.58354156, 1.60912788, 1.5870082, 1.63421727]
l_DVHO1_alpha = [1.96670954, 2.13792515, 2.09870674, 2.17620133, 2.10721617]
l_DVHO2_alpha = [1.93914946, 2.01087561, 2.18597789,  2.59153969, 2.8310217]
l_IHO_alpha = [1.50585675, 1.52485352, 1.55821653, 1.58358898, 1.60265155]
l_DIHO1_alpha = [1.91035148, 1.88431987, 1.96706775, 1.97132198, 2.1213539]
l_DIHO2_alpha = [2.39804724, 2.31473164, 2.53342621, 2.48767346, 2.70834277]

#队列长度画图
plt.figure(9)
plt.title("Average Queue Length")
plt.plot(Alpha21_Alpha12, l_OVHO_alpha, color='red', marker='o', label='O-VHO')
plt.plot(Alpha21_Alpha12, l_IVHO_alpha, color='blue', marker='s', label='I-VHO')
plt.plot(Alpha21_Alpha12, l_DVHO1_alpha, color='green', marker='p', label='D-VHO1 Time=0.3s')
plt.plot(Alpha21_Alpha12, l_DVHO2_alpha, color='yellow', marker='h', label='D-VHO2 Time=0.6s')
plt.plot(Alpha21_Alpha12, l_IHO_alpha, color='black', marker='*', label='I-HO')
plt.plot(Alpha21_Alpha12, l_DIHO1_alpha, color='pink', marker='+', label='D-HO1 Time=0.3s')
plt.plot(Alpha21_Alpha12, l_DIHO2_alpha, color='aqua', marker='.', label='D-HO2 Time=0.6s')
plt.xlabel("\u03B1$_{21}$/\u03B1$_{12}$")
plt.ylabel("Average queue length L (number)")
plt.legend()

#丢包率
DB_OVHO_alpha = [0.00454022, 0.00578481, 0.0061185, 0.00668981, 0.00994496]
DB_IVHO_alpha = [0.00403711, 0.00322359, 0.00373341, 0.00581395, 0.00618543]
DB_DVHO1_alpha = [0.00792178, 0.00935046, 0.01263713, 0.01368193, 0.01350534]
DB_DVHO2_alpha = [0.01037723, 0.01074002, 0.01475712, 0.01801741, 0.02364583]
DB_IHO_alpha = [0.00306748,  0.00216337, 0.00307279, 0.00438318, 0.00224806]
DB_DHO1_alpha = [0.00938778, 0.00779612,  0.00969284, 0.0078648, 0.01211538]
DB_DHO2_alpha = [0.02204524, 0.01684882, 0.02263468, 0.02199673, 0.02654924]

#丢包率作图
plt.figure(10)
plt.title("Packet Loss Rate")
plt.plot(Alpha21_Alpha12, DB_OVHO_alpha, color='red', marker='o', label='O-VHO')
plt.plot(Alpha21_Alpha12, DB_IVHO_alpha, color='blue', marker='s', label='I-VHO')
plt.plot(Alpha21_Alpha12, DB_DVHO1_alpha, color='green', marker='p', label='D-VHO1 Time=0.3s')
plt.plot(Alpha21_Alpha12, DB_DVHO2_alpha, color='yellow', marker='h', label='D-VHO2 Time=0.6s')
plt.plot(Alpha21_Alpha12, DB_IHO_alpha, color='black', marker='*', label='I-HO')
plt.plot(Alpha21_Alpha12, DB_DHO1_alpha, color='pink', marker='+', label='D-HO1 Time=0.3s')
plt.plot(Alpha21_Alpha12, DB_DHO2_alpha, color='aqua', marker='.', label='D-HO2 Time=0.6s')
plt.xlabel("\u03B1$_{21}$/\u03B1$_{12}$")
plt.ylabel("Packet loss rate (%)")
plt.legend()

#平均延时时间

#延迟时间
delay_OVHO_alpha = [4.59782708, 4.5150985, 4.49921104 ,4.59369495, 4.57391581]
delay_IVHO_alpha = [4.58789927, 4.43299757, 4.41951095,  4.16299835, 4.00973178]
delay_DVHO1_alpha = [5.65056164,  6.17769836, 5.91471601, 5.99049074, 5.79218172]
delay_DVHO2_alpha = [5.40481295, 5.56097808, 6.00477307, 6.63401126, 6.85280915]
delay_IHO_alpha = [3.94991764,  3.99181549, 4.09893789, 4.00078431, 4.07530195]
delay_DHO1_alpha = [5.08686809, 4.86952713, 5.13420212, 5.14154099, 5.46721561]
delay_DHO2_alpha = [6.19519013, 6.13107125, 6.5350054, 6.56681377, 6.99670311]

plt.figure(11)
plt.title("Average Delay Time")
plt.plot(Alpha21_Alpha12, delay_OVHO_alpha, color='red', marker='o', label='O-VHO')
plt.plot(Alpha21_Alpha12, delay_IVHO_alpha, color='blue', marker='s', label='I-VHO')
plt.plot(Alpha21_Alpha12, delay_DVHO1_alpha, color='green', marker='p', label='D-VHO1 Time=0.3s')
plt.plot(Alpha21_Alpha12, delay_DVHO2_alpha, color='yellow', marker='h', label='D-VHO2 Time=0.6s')
plt.plot(Alpha21_Alpha12, delay_IHO_alpha, color='black', marker='*', label='I-HO')
plt.plot(Alpha21_Alpha12, delay_DHO1_alpha, color='pink', marker='+', label='D-HO1 Time=0.3s')
plt.plot(Alpha21_Alpha12, delay_DHO2_alpha, color='aqua', marker='.', label='D-HO2 Time=0.6s')
plt.xlabel("\u03B1$_{21}$/\u03B1$_{12}$")
plt.ylabel("Average delay time d(s)")
plt.legend()

#切换次数（垂直）
n0_alpha = [1462., 1414., 1679., 1765., 1862]
n1_alpha = [3718., 3886., 4058., 4122., 4241]
n2_alpha = [3020., 3042., 3104., 3219., 3012]
n3_alpha = [3124., 3006., 2800., 2594., 2081]
n4_alpha = [3275., 3457., 3624., 3819., 4090]
n5_alpha = [2577., 2741., 2758., 2816., 2819]
n6_alpha = [1793., 1856., 1859., 1858., 1754]

#切换次数做图
plt.figure(12)
plt.title("Numbers Of VHO")
plt.plot(tao_all, n0_alpha, color='red', marker='o', label='O-VHO')
plt.plot(tao_all, n1_alpha, color='blue', marker='s', label='I-VHO')
plt.plot(tao_all, n2_alpha, color='green', marker='p', label='D-VHO1 Time=0.3s')
plt.plot(tao_all, n3_alpha, color='yellow', marker='h', label='D-VHO2 Time=0.6s')
plt.plot(tao_all, n4_alpha, color='black', marker='*', label='I-HO')
plt.plot(tao_all, n5_alpha, color='pink', marker='+', label='D-HO1 Time=0.3s')
plt.plot(tao_all, n6_alpha, color='aqua', marker='.', label='D-HO2 Time=0.6s')
plt.xlabel("\u03B1$_{21}$/\u03B1$_{12}$")
plt.ylabel("numbers of VHO (times)")
plt.legend()

plt.show()