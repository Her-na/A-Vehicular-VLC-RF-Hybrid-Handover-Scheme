import numpy as np
from MIX_Compare import Sample
from VLC_RF_MIX import MIX_VLC_RF,ValueIteration

#传参数
lamda = 2
mu_1 = 3.8
mu_0 = 2.2
gamma_1 = 0.4
gamma_N1 = 0.4
beta_1_all = np.array([0.3, 0.4, 0.5, 0.6, 0.7 ,0.8, 0.9, 1.0, 1.1])
beta_N1_all = np.array([0.3, 0.4, 0.5, 0.6, 0.7 ,0.8, 0.9, 1.0, 1.1])
tao_all = np.array([0.1, 0.2, 0.3, 0.4, 0.5])
beta_fit = 1
alpha = 0.2
tao_VHO = 0.3
tao_HHO = 0.15
E_VHO = 418
E_HHO = 0
E_V = 5e-4 * 1000 * 3600
E_R = 5e-4 * 1000 * 3600
zeta = 500
theta = 1000
eta = 1
lr_alpha = 0.99
kese = 1e-4

arv_B_OVHO_total=np.zeros(9)
prob_lost_OVHO_vector=np.zeros(9)
avr_delay_OVHO_total = np.zeros(9)
n_HHO_OVHO_total = np.zeros(9)
n_VHO_OVHO_total = np.zeros(9)

arv_B_IVHO_total=np.zeros(9)
prob_lost_IVHO_vector=np.zeros(9)
avr_delay_IVHO_total = np.zeros(9)
n_HHO_IVHO_total = np.zeros(9)
n_VHO_IVHO_total = np.zeros(9)

arv_B_DVHO1_total=np.zeros(9)
prob_lost_DVHO1_vector=np.zeros(9)
avr_delay_DVHO1_total = np.zeros(9)
n_HHO_DVHO1_total = np.zeros(9)
n_VHO_DVHO1_total = np.zeros(9)

arv_B_DVHO2_total=np.zeros(9)
prob_lost_DVHO2_vector=np.zeros(9)
avr_delay_DVHO2_total = np.zeros(9)
n_HHO_DVHO2_total = np.zeros(9)
n_VHO_DVHO2_total = np.zeros(9)

#变化变量出画图所用的数据 其中O-VHO I-VHO的丢包率队列长度用直接计算得到 而D-VHO的参量则需要返回PAI参数计算
i=0
for tao in tao_all:
#for tao in tao_all:
    #初始化环境和agent
    env = MIX_VLC_RF(lamda, gamma_1, gamma_N1, mu_0, mu_1,
                 1 , 1, alpha, eta, E_V, E_R, zeta, E_VHO,
                 E_HHO, theta, tao, 0.1, lr_alpha)
    #print("-------------------此处分割------------------------------------")

    agent = ValueIteration(env, kese, lr_alpha)

    #读取action_state列表
    action_state_OVHO = agent.Value_Interation()

    #action_state_OVHO = np.zeros((2,11,2,2,2))
    #print(action_state_OVHO)

    action_state_IVHO = np.zeros((2,11,2,2,2))

    action_state_IVHO[:, :, 0, 1, 0] = 1
    action_state_IVHO[:, :, 0, 0, 0] = 0

    action_state_IVHO[:, :, 1, 0, 1] = 0
    action_state_IVHO[:, :, 1, 1, 1] = 1
    action_state_IVHO[:, :, 1, 1, 0] = 1
    action_state_IVHO[:, :, 1, 0, 0] = 0

    action_state_IHO = np.zeros((2, 11, 2, 2, 2))

    action_state_IHO[:, :, 0, 1, 0] = 1
    action_state_IHO[:, :, 0, 0, 0] = 0

    action_state_IHO[:, :, 1, 0, 1] = -1
    action_state_IHO[:, :, 1, 1, 1] = 1
    action_state_IHO[:, :, 1, 1, 0] = 1
    action_state_IHO[:, :, 1, 0, 0] = 0

    '''Q_YR_OVHO = np.zeros((92, 92))
    Q_YR_IVHO = np.zeros((92, 92))

    #计算静态概率
    for w in range(2):
        for b in range(11):
            for s_now in range(2):
                for s_next in range(2):

                    env.state_read(s_now, s_next, b, w)
                    action_OVHO = action_state_OVHO[w, b, s_now, s_next]
                    action_IVHO = action_state_IHO[w, b, s_now, s_next]
                    action_OVHO = int(action_OVHO)
                    action_IVHO = int(action_IVHO)

                    _, P_OVHO = env.step(action_OVHO)
                    _, P_IVHO = env.step(action_IVHO)

                    Q_YR_OVHO[w * 44 + b * 4 + s_now * 2 + s_next, abs(action_OVHO) * 44 + (b + 1) * 4 + s_now * 2 + s_next] = P_OVHO[0]
                    Q_YR_OVHO[w * 44 + b * 4 + s_now * 2 + s_next, abs(action_OVHO) * 44 + b * 4 + (1 - s_now) * 2 + s_next] = P_OVHO[1]
                    Q_YR_OVHO[w * 44 + b * 4 + s_now * 2 + s_next, abs(action_OVHO) * 44 + b * 4 + s_now * 2 + (1 - s_next)] = P_OVHO[2]
                    Q_YR_OVHO[w * 44 + b * 4 + s_now * 2 + s_next, abs(action_OVHO) * 44 + (b - 1) * 4 + s_now * 2 + s_next] = P_OVHO[3]
                    Q_YR_OVHO[w * 44 + b * 4 + s_now * 2 + s_next, abs(action_OVHO) * 44 + b * 4 + s_now * 2 + s_next] = P_OVHO[4]
                    Q_YR_OVHO[w * 44 + b * 4 + s_now * 2 + s_next, abs(action_OVHO) * 44 + b * 4 + (1-s_now) * 2 + (1-s_next)] = P_OVHO[5]

                    Q_YR_IVHO[w * 44 + b * 4 + s_now * 2 + s_next, abs(action_IVHO) * 44 + (b + 1) * 4 + s_now * 2 + s_next] = P_IVHO[0]
                    Q_YR_IVHO[w * 44 + b * 4 + s_now * 2 + s_next, abs(action_IVHO) * 44 + b * 4 + (1 - s_now) * 2 + s_next] = P_IVHO[1]
                    Q_YR_IVHO[w * 44 + b * 4 + s_now * 2 + s_next, abs(action_IVHO) * 44 + b * 4 + s_now * 2 + (1 - s_next)] = P_IVHO[2]
                    Q_YR_IVHO[w * 44 + b * 4 + s_now * 2 + s_next, abs(action_IVHO) * 44 + (b - 1) * 4 + s_now * 2 + s_next] = P_IVHO[3]
                    Q_YR_IVHO[w * 44 + b * 4 + s_now * 2 + s_next, abs(action_IVHO) * 44 + b * 4 + s_now * 2 + s_next] = P_IVHO[4]
                    Q_YR_IVHO[w * 44 + b * 4 + s_now * 2 + s_next, abs(action_IVHO) * 44 + b * 4 + (1 - s_now) * 2 + (1 - s_next)] = P_IVHO[5]

    #对状态转移概率列表完成后 计算静态状态概率
    y=np.ones((1,88))
    Q_YR_OVHO = Q_YR_OVHO[0:88, 0:88]
    Q_YR_IVHO = Q_YR_IVHO[0:88, 0:88]
    A_1_OVHO = (Q_YR_OVHO + np.ones((88, 88)) - np.eye(88))
    A_1_IVHO = (Q_YR_IVHO + np.ones((88, 88)) - np.eye(88))
    A_1_OVHO_inv = np.linalg.inv(A_1_OVHO)
    A_1_IVHO_inv = np.linalg.inv(A_1_IVHO)
    PAI_OVHO = np.dot(y,A_1_OVHO_inv)
    PAI_IVHO = np.dot(y,A_1_IVHO_inv)'''

    #进行循环跑参数
    PAI_OVHO, avr_delay_OVHO, n_HHO_OVHO, n_VHO_OVHO, prob1 = Sample(action_state_OVHO, 0, 0,env)
    print("-----------------------------------------------------------")
    PAI_IVHO, avr_delay_IVHO, n_HHO_IVHO, n_VHO_IVHO, prob2 = Sample(action_state_IHO, 0,0,env)
    PAI_DVHO1, avr_delay_DVHO1, n_HHO_DVHO1, n_VHO_DVHO1, prob3 = Sample(action_state_IHO, 2,1,env)
    PAI_DVHO2, avr_delay_DVHO2, n_HHO_DVHO2, n_VHO_DVHO2, prob4 = Sample(action_state_IVHO, 2,0,env)

    #这里计算平均队列长度和丢包率
    avr_B_OVHO = 0
    avr_B_IVHO = 0
    avr_B_DVHO1 = 0
    avr_B_DVHO2 = 0
    prob_lost_OVHO = 0
    prob_lost_IVHO = 0
    prob_lost_DVHO1 = 0
    prob_lost_DVHO2 = 0
    for w in range(2):
        for b in range(11):
            for s_now in range(2):
                for s_next in range(2):
                    for x in range(2):
                        if (x == 0) & (s_next == 1):
                            continue
                        avr_B_OVHO += b * PAI_OVHO[0,x * 88 + w * 44 + b * 4 + s_now * 2 + s_next]
                        avr_B_IVHO += b * PAI_IVHO[0,x * 88 + w * 44 + b * 4 + s_now * 2 + s_next]
                        avr_B_DVHO1 += b * PAI_DVHO1[0,x * 88 + w * 44 + b * 4 + s_now * 2 + s_next]
                        avr_B_DVHO2 += b * PAI_DVHO2[0,x * 88 + w * 44 + b * 4 + s_now * 2 + s_next]
                    '''if b == 10:
                        prob_lost_OVHO += PAI_OVHO[0, w * 44 + b * 4 + s_now * 2 + s_next]
                        prob_lost_IVHO += PAI_IVHO[0, w * 44 + b * 4 + s_now * 2 + s_next]
                        prob_lost_DVHO1 += PAI_DVHO1[0, w * 44 + b * 4 + s_now * 2 + s_next]
                        prob_lost_DVHO2 += PAI_DVHO2[0, w * 44 + b * 4 + s_now * 2 + s_next]'''

    arv_B_OVHO_total[i] = avr_B_OVHO
    prob_lost_OVHO_vector[i] = prob1 #prob_lost_OVHO
    avr_delay_OVHO_total[i] = avr_delay_OVHO
    n_HHO_OVHO_total[i] = n_HHO_OVHO
    n_VHO_OVHO_total[i] = n_VHO_OVHO

    arv_B_IVHO_total[i] = avr_B_IVHO
    prob_lost_IVHO_vector[i] = prob2#prob_lost_IVHO
    avr_delay_IVHO_total[i] = avr_delay_IVHO
    n_HHO_IVHO_total[i] = n_HHO_IVHO
    n_VHO_IVHO_total[i] = n_VHO_IVHO

    arv_B_DVHO1_total[i] = avr_B_DVHO1
    prob_lost_DVHO1_vector[i] = prob3#prob_lost_DVHO1
    avr_delay_DVHO1_total[i] = avr_delay_DVHO1
    n_HHO_DVHO1_total[i] = n_HHO_DVHO1
    n_VHO_DVHO1_total[i] = n_VHO_DVHO1

    arv_B_DVHO2_total[i] = avr_B_DVHO2
    prob_lost_DVHO2_vector[i] = prob4#prob_lost_DVHO2
    avr_delay_DVHO2_total[i] = avr_delay_DVHO2
    n_HHO_DVHO2_total[i] = n_HHO_DVHO2
    n_VHO_DVHO2_total[i] = n_VHO_DVHO2

    i += 1
    #此处为循环结尾！

print("----------------------------------------------------------------------------------------")
print(arv_B_OVHO_total)
print(arv_B_IVHO_total)
print(arv_B_DVHO1_total)
print(arv_B_DVHO2_total)
print("----------------------------------------------------------------------------------------")
print(prob_lost_OVHO_vector)
print(prob_lost_IVHO_vector)
print(prob_lost_DVHO1_vector)
print(prob_lost_DVHO2_vector)
print("----------------------------------------------------------------------------------------")
print(avr_delay_OVHO_total)
print(avr_delay_IVHO_total)
print(avr_delay_DVHO1_total)
print(avr_delay_DVHO2_total)
print("----------------------------------------------------------------------------------------")
print(n_HHO_OVHO_total)
print(n_HHO_IVHO_total)
print(n_HHO_DVHO1_total)
print(n_HHO_DVHO2_total)
print("----------------------------------------------------------------------------------------")
print(n_VHO_OVHO_total)
print(n_VHO_IVHO_total)
print(n_VHO_DVHO1_total)
print(n_VHO_DVHO2_total)
print("----------------------------------------------------------------------------------------")
print(n_VHO_OVHO_total + n_HHO_OVHO_total)
print(n_VHO_IVHO_total + n_HHO_IVHO_total)
print(n_VHO_DVHO1_total + n_HHO_DVHO1_total)
print(n_VHO_DVHO2_total + n_HHO_DVHO2_total)
print("----------------------------------------------------------------------------------------")