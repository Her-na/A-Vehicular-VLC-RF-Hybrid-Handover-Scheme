#VLC-RF-MIX 混合信道切换:水平垂直混合模型
import numpy as np
import copy
import random

class MIX_VLC_RF:
    def __init__(self, lamda, gamma_1, gamma_N1, mu_0, mu_1,
                 beta_1, beta_N1, alpha, eta, E_V, E_R, zeta, E_VHO,
                 E_HHO, theta, tao_VHO, tao_HHO, lr_alpha):
        self.E_V = E_V
        self.E_R = E_R
        self.zeta = zeta
        self.E_VHO = E_VHO
        self.E_HHO = E_HHO
        self.theta_1 = theta
        self.theta_2 = theta
        self.tao_VHO = tao_VHO
        self.tao_HHO = tao_HHO
        self.lr_alpha = lr_alpha
        self.lamda = lamda
        self.gamma_1 = gamma_1
        self.gamma_N1 = gamma_N1
        self.beta_1 = beta_1
        self.beta_N1 = beta_N1
        self.alpha12 = alpha
        self.alpha21 = 2 * alpha
        self.eta = eta
        self.mu_0 = mu_0
        self.mu_1 = mu_1
        self.mu_ON_OFF_1 = 0
        self.mu_OFF_OFF_1 = 0
        self.mu_ON_ON_2 = 0
        self.mu_ON_OFF_2 = 0
        self.mu_OFF_ON_2 = 0
        self.mu_OFF_OFF_2 = 0
        self.V_1 = []
        self.V_2 = []
        self.P_ON_OFF_1 = []
        self.P_OFF_OFF_1 = []
        self.P_ON_ON_2 = []
        self.P_ON_OFF_2 = []
        self.P_OFF_ON_2 = []
        self.P_OFF_OFF_2 = []

    def state_read(self, s_now, s_next, x, b, w):
        #当前信道状态、当前信道的下一个信道的状态、当前位置、队列长度、信道接入模式
        self.s_now = s_now
        self.s_next = s_next
        self.x = x
        self.b = b
        self.w = w

    def cal_P(self,action):
        #计算转移概率和速率 返回离散马尔科夫链的转移概率

        #计算转移概率
        self.mu_ON_OFF_1 = (1 - abs(action)) * self.mu_0 + abs(action) * self.mu_1
        self.mu_OFF_OFF_1 = (1 - abs(action)) * self.mu_0
        self.mu_ON_ON_2 = (1 - abs(action)) * self.mu_0 + abs(action) * self.mu_1
        self.mu_ON_OFF_2 = (1 - abs(action)) * self.mu_0 + abs(action) * self.mu_1 * (1 + action) * 0.5
        self.mu_OFF_OFF_2 = (1 - abs(action)) * self.mu_0
        self.mu_OFF_ON_2 = (1 - abs(action)) * self.mu_0 + abs(action) * self.mu_1 * (1 - action) * 0.5

        if action == -1:
            self.alpha12 = 0
        else:
            self.alpha12 = alpha

        self.P_ON_OFF_1 = np.array(
            [[self.lamda / (self.lamda + self.gamma_1 + self.alpha12 + self.mu_ON_OFF_1)],
             [self.gamma_1 / (self.lamda + self.gamma_1 + self.alpha12 + self.mu_ON_OFF_1)],
             [0],
             [self.alpha12  / (self.lamda + self.gamma_1 + self.alpha12 + self.mu_ON_OFF_1)],
             [self.mu_ON_OFF_1 / (self.lamda + self.gamma_1 + self.alpha12 + self.mu_ON_OFF_1)]])

        self.P_OFF_OFF_1 = np.array(
            [[self.lamda / (self.lamda + self.beta_1 + self.alpha12 + self.mu_OFF_OFF_1)],
             [self.beta_1 / (self.lamda + self.beta_1 + self.alpha12 + self.mu_OFF_OFF_1)],
             [0],
             [self.alpha12 / (self.lamda + self.beta_1 + self.alpha12 + self.mu_OFF_OFF_1)],
             [self.mu_OFF_OFF_1 / (self.lamda + self.beta_1 + self.alpha12 + self.mu_OFF_OFF_1)]])

        self.P_ON_ON_2 = np.array(
            [[self.lamda / (self.lamda + self.gamma_1 + self.gamma_N1 + self.alpha21 + self.mu_ON_ON_2)],
             [self.gamma_1 / (self.lamda + self.gamma_1 + self.gamma_N1 + self.alpha21 + self.mu_ON_ON_2)],
             [self.gamma_N1 / (self.lamda + self.gamma_1 + self.gamma_N1 + self.alpha21 + self.mu_ON_ON_2)],
             [self.alpha21 / (self.lamda + self.gamma_1 + self.gamma_N1 + self.alpha21 + self.mu_ON_ON_2)],
             [self.mu_ON_ON_2 / (self.lamda + self.gamma_1 + self.gamma_N1 + self.alpha21 + self.mu_ON_ON_2)]])

        self.P_ON_OFF_2 = np.array(
            [[self.lamda / (self.lamda + self.gamma_1 + self.beta_N1 + self.alpha21 + self.mu_ON_OFF_2)],
             [self.gamma_1 / (self.lamda + self.gamma_1 + self.beta_N1 + self.alpha21 + self.mu_ON_OFF_2)],
             [self.beta_N1 / (self.lamda + self.gamma_1 + self.beta_N1 + self.alpha21 + self.mu_ON_OFF_2)],
             [self.alpha21 / (self.lamda + self.gamma_1 + self.beta_N1 + self.alpha21 + self.mu_ON_OFF_2)],
             [self.mu_ON_OFF_2 / (self.lamda + self.gamma_1 + self.beta_N1 + self.alpha21 + self.mu_ON_OFF_2)]])

        self.P_OFF_OFF_2 = np.array(
            [[self.lamda / (self.lamda + self.beta_1 + self.beta_N1 + self.alpha21 + self.mu_OFF_OFF_2)],
             [self.beta_1 / (self.lamda + self.beta_1 + self.beta_N1 + self.alpha21 + self.mu_OFF_OFF_2)],
             [self.beta_N1 / (self.lamda + self.beta_1 + self.beta_N1 + self.alpha21 + self.mu_OFF_OFF_2)],
             [self.alpha21 / (self.lamda + self.beta_1 + self.beta_N1 + self.alpha21 + self.mu_OFF_OFF_2)],
             [self.mu_OFF_OFF_2 / (self.lamda + self.beta_1 + self.beta_N1 + self.alpha21 + self.mu_OFF_OFF_2)]])

        self.P_OFF_ON_2 = np.array(
            [[self.lamda / (self.lamda + self.beta_1 + self.gamma_N1 + self.alpha21 + self.mu_OFF_ON_2)],
             [self.beta_1 / (self.lamda + self.beta_1 + self.gamma_N1 + self.alpha21 + self.mu_OFF_ON_2)],
             [self.gamma_N1 / (self.lamda + self.beta_1 + self.gamma_N1 + self.alpha21 + self.mu_OFF_ON_2)],
             [self.alpha21 / (self.lamda + self.beta_1 + self.gamma_N1 + self.alpha21 + self.mu_OFF_ON_2)],
             [self.mu_OFF_ON_2 / (self.lamda + self.beta_1 + self.gamma_N1 + self.alpha21 + self.mu_OFF_ON_2)]])

        self.P_ON_ON_2 = (action != -1) * self.P_ON_ON_2 + (action == -1) * self.P_ON_OFF_1
        self.P_ON_OFF_2 = (action != -1) * self.P_ON_OFF_2 + (action == -1) * self.P_OFF_OFF_1
        self.P_OFF_OFF_2 = (action != -1) * self.P_OFF_OFF_2 + (action == -1) * self.P_OFF_OFF_1
        self.P_OFF_ON_2 = (action != -1) * self.P_OFF_ON_2 + (action == -1) * self.P_ON_OFF_1

        #统计速率后归一化
        self.V_1 = np.array([[[self.lamda + self.beta_1 + self.alpha12 + self.mu_0],
                              [self.lamda + self.gamma_1 + self.alpha12 + self.mu_0]],

                             [[self.lamda + self.beta_1 + self.alpha12],
                              [self.lamda + self.gamma_1 + self.alpha12 + self.mu_1]]])

        self.V_2 = np.array([[[self.lamda + self.beta_1,
                               self.lamda + self.gamma_1 + self.mu_1],
                              [self.lamda + self.beta_1,
                               self.lamda + self.gamma_1 + self.mu_1]],

                            [[self.lamda + self.beta_1 + self.beta_N1 + self.alpha21 + self.mu_0,
                              self.lamda + self.beta_1 + self.gamma_N1 + self.alpha21 + self.mu_0],
                             [self.lamda + self.gamma_1 + self.beta_N1 + self.alpha21 + self.mu_0,
                              self.lamda + self.gamma_1 + self.gamma_N1 + self.alpha21 + self.mu_0]],

                            [[self.lamda + self.beta_1 + self.beta_N1 + self.alpha21,
                              self.lamda + self.beta_1 + self.gamma_N1 + self.alpha21],
                             [self.lamda + self.gamma_1 + self.beta_N1 + self.alpha21 + self.mu_1,
                              self.lamda + self.gamma_1 + self.gamma_N1 + self.alpha21 + self.mu_1]]])

        self.V_max = np.max([np.max(self.V_1), np.max(self.V_2)])

        if self.x == 1:
            V_a = self.V_1[action, self.s_now]
            #self.V_max = np.max([np.max(self.V_1)])

            P = V_a / self.V_max * (self.P_ON_OFF_1 * self.s_now + self.P_OFF_OFF_1 * (1 - self.s_now))
        else:
            V_a = self.V_2[action + 1, self.s_now, self.s_next]
            #self.V_max = np.max([np.max(self.V_2)])

            P = V_a / self.V_max * (self.P_ON_ON_2 * (self.s_now * self.s_next)
                               + self.P_ON_OFF_2 * (self.s_now * (1 - self.s_next))
                               + self.P_OFF_OFF_2 * ((1 - self.s_now) * (1 - self.s_next))
                               + self.P_OFF_ON_2 * ((1 - self.s_now) * self.s_next))

        P = np.append(P, (1 - V_a / self.V_max))

        return P

    def cal_r(self, action):

        beta = self.V_max / self.lr_alpha - self.V_max
        r1 = abs(action) * self.E_V + (1 - action) * (1 + action) * self.E_R
        r2 = (abs(action - self.w) * (2 - abs(action - self.w)) * (self.E_VHO + self.theta_1 * self.lamda * self.tao_VHO)
              + 0.5 * (abs(action - self.w) * (abs(action - self.w) - 1) * (self.E_HHO + self.theta_2 * self.lamda * self.tao_HHO)))
        r3 = self.zeta * self.b
        r = 1 / (beta + 1 * self.V_max) * (r1 + r3) + 0.75 * r2
        #print(1 / (beta + 1 * self.V_max) * (r1 + r3),r2)

        return  r

    def cal_next_state(self, action):
        # 获得下一状态
        b_change_1 = self.b + 1
        b_change_2 = self.b - 1
        if self.b + 1 > 10:
            b_change_1 = 10
        if self.b - 1 < 0:
            b_change_2 = 0

        if action != -1:
            if self.x == 2:
                # 没提前水平切换
                next_state = np.array([[abs(action), b_change_1, self.x, self.s_now, self.s_next],
                                       [abs(action), self.b, self.x, (1 - self.s_now), self.s_next],
                                       [abs(action), self.b, self.x, self.s_now, (1 - self.s_next)],
                                       [abs(action), self.b, 1, self.s_next, 0],
                                       [abs(action), b_change_2, self.x, self.s_now, self.s_next],
                                       [self.w, self.b, self.x, self.s_now, self.s_next]])
            else:
                next_state = np.array([[abs(action), b_change_1, self.x, self.s_now, self.s_next],
                                       [abs(action), self.b, self.x, (1 - self.s_now), self.s_next],
                                       [abs(action), self.b, self.x, self.s_now, self.s_next],
                                       [abs(action), self.b, 2, self.s_now, (1 - self.s_next)],
                                       [abs(action), b_change_2, self.x, self.s_now, self.s_next],
                                       [self.w, self.b, self.x, self.s_now, self.s_next]])
        else:
            if self.x == 2:
                # 提前水平切换
                next_state = np.array([[abs(action), b_change_1, 1, self.s_next, 0],
                                       [abs(action), self.b, 1, (1 - self.s_next), 0],
                                       [abs(action), self.b, 1, self.s_now, 0],
                                       [abs(action), self.b, 2, 0, 0],
                                       [abs(action), b_change_2, 1, self.s_next, 0],
                                       [self.w, self.b, self.x, self.s_now, self.s_next]])

        return next_state

    def step(self, action):
        P = self.cal_P(action)
        r = self.cal_r(action)

        return r, P

    def display(self, action, P):

        # 选状态
        prob = np.random.rand()
        if prob == 0:
            prob = np.random.rand()

        if prob <= P[0]:
            choose = 0
        elif prob <= (P[1] + P[0]):
            choose = 1
        elif prob <= (P[2] + P[1] + P[0]):
            choose = 2
        elif prob <= (P[3] + P[2] + P[1] + P[0]):
            choose = 3
        elif prob <= (P[4] + P[3] + P[2] + P[1] + P[0]):
            choose = 4
        else:
            choose = 5

        # 获得速率
        V_display = P[choose] * self.V_max
        #print(self.V_max)
        #print(V_display)
        #print(choose)
        #print(V_display)

        # 获得下一状态
        next_state = self.cal_next_state(action)
        next_state_vector = next_state[choose,:]
        #print(next_state_vector)

        # 计算时间
        Time_change = (-1) * np.log(1 - np.random.rand()) / V_display
        #Time_change = 1 / V_display
        #print(Time_change)

        # 返回切换判断
        Judge = 1
        if choose == 5:
            Judge = 0

        return Time_change, next_state_vector, Judge, choose


# 价值迭代策算法
class ValueIteration:
    def __init__(self, env, kese, alpha):
        self.env = env
        self.kese = kese
        self.alpha = alpha

    def Value_Interation(self):
        V = np.zeros((2,11,2,2,2))#dim1索引w dim2索引b dim3索引位置x dim4索引s—now dim5索引s-next
        V_new = np.zeros((2, 11, 2, 2, 2))
        action_state = np.zeros((2, 11, 2, 2, 2))
        diff = float('inf')
        while 1:
            for s_now in range(2):
                for s_next in range(2):
                    for b in range(11):
                        for w in range(2):
                            for x in range(2):
                                if (x == 0) & (s_next == 1):
                                    action_state[w, b, x, s_now, s_next] = 5
                                    continue
                                self.env.state_read(s_now, s_next, x + 1, b, w)
                                if x == 1:
                                    Q = np.zeros(3)
                                    for action in (-1, 0, 1):
                                        r, P = self.env.step(action)
                                        next_state = self.env.cal_next_state(action)
                                        next_state[:,2] = next_state[:,2] - 1
                                        V_vector = np.array([V[next_state[0,0],next_state[0,1],next_state[0,2],next_state[0,3],next_state[0,4]],
                                                             V[next_state[1,0],next_state[1,1],next_state[1,2],next_state[1,3],next_state[1,4]],
                                                             V[next_state[2,0],next_state[2,1],next_state[2,2],next_state[2,3],next_state[2,4]],
                                                             V[next_state[3,0],next_state[3,1],next_state[3,2],next_state[3,3],next_state[3,4]],
                                                             V[next_state[4,0],next_state[4,1],next_state[4,2],next_state[4,3],next_state[4,4]],
                                                             V[next_state[5,0],next_state[5,1],next_state[5,2],next_state[5,3],next_state[5,4]]])
                                        Q[action + 1] = r + self.alpha * np.dot(V_vector, P)
                                    action_state[w, b, x, s_now, s_next] = np.argmin(Q) - 1
                                    V_new[w, b, x, s_now, s_next] = Q[np.argmin(Q)]

                                if x == 0:
                                    Q = np.zeros(2)
                                    for action in (0, 1):
                                        r, P = self.env.step(action)
                                        next_state = self.env.cal_next_state(action)
                                        next_state[:,2] = next_state[:,2] - 1
                                        V_vector = np.array([V[next_state[0,0],next_state[0,1],next_state[0,2],next_state[0,3],next_state[0,4]],
                                                             V[next_state[1,0],next_state[1,1],next_state[1,2],next_state[1,3],next_state[1,4]],
                                                             V[next_state[2,0],next_state[2,1],next_state[2,2],next_state[2,3],next_state[2,4]],
                                                             V[next_state[3,0],next_state[3,1],next_state[3,2],next_state[3,3],next_state[3,4]],
                                                             V[next_state[4,0],next_state[4,1],next_state[4,2],next_state[4,3],next_state[4,4]],
                                                             V[next_state[5,0],next_state[5,1],next_state[5,2],next_state[5,3],next_state[5,4]]])
                                        Q[action] = r + self.alpha * np.dot(V_vector, P)
                                    action_state[w, b, x, s_now, s_next] = np.argmin(Q)
                                    V_new[w, b, x, s_now, s_next] = Q[np.argmin(Q)]

            diff = np.linalg.norm(V_new - V)
            #print(diff)
            if diff < self.kese:
                break
            else:
                #V = V_new #注意 这是数组名赋值 把指针指向同一个地址！
                V = copy.deepcopy(V_new)
        return action_state

alpha = 0.2
'''
#传参数
lamda = 2
mu_1 = 3.8
mu_0 = 2.2
gamma_1 = 0.4
gamma_N1 = 0.4
beta_1_all = np.array([0.3, 0.4, 0.5, 0.6, 0.7 ,0.8, 0.9, 1.0, 1.1])
beta_N1_all = np.array([0.3, 0.4, 0.5, 0.6, 0.7 ,0.8, 0.9, 1.0, 1.1])
tao_all = np.array([0.2, 0.3, 0.4, 0.5])
beta_fit = 1
tao_VHO = 0.3
tao_HHO = 0.15
E_VHO = 418
E_HHO = 0
E_V = 5e-4 * 1000 * 3600
E_R = 5e-4 * 1000 * 3600
zeta = 500
theta = 1800
eta = 1
lr_alpha = 0.99
kese = 1e-4
env = MIX_VLC_RF(lamda, gamma_1, gamma_N1, mu_0, mu_1,
                 0.4 , 0.4 , alpha, eta, E_V, E_R, zeta, E_VHO,
                 E_HHO, theta, 0.3, 0.2, lr_alpha)
env.state_read(0, 1, 2,4,1)
A = env.cal_P(-1)
B = env.cal_P(1)
C = env.cal_P(0)
#A = np.sum(A)
#B = np.sum(B)
#C = np.sum(C)
print(A)
print(B)
print(C)
env.display(-1,A)
'''