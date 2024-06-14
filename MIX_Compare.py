import numpy as np
from VLC_RF_MIX import MIX_VLC_RF
from VLC_RF_MIX import ValueIteration

def Sample(action_state, mode, IFH, env):

    PAI_TOTAL = 0
    avr_delay_TOTAL = 0
    n_HHO_TOTAL = 0
    n_VHO_TOTAL = 0
    prob_TOTAL = 0

    for epsoides in range(1):
        #初始化参数 action决定了是OVHO还是IVHO mode决定加不加dwell时间
        s_now = int(np.random.rand() + 0.5)
        s_next = int(np.random.rand() + 0.5)
        x = 2#int(2 * np.random.rand() + 1)
        b = 0#int(10 * np.random.rand())
        w = int(np.random.rand() + 0.5)

        Time_total = 0
        n_VHO = 0
        n_HHO = 0
        Dwell_time = np.array([0, 0.3, 0.6])
        Time_reach = np.zeros((1,1))
        Time_leave = np.zeros((1,1))
        Loc_packet = np.zeros((1,1))

        #mode选择dwelltime
        d_time = Dwell_time[mode]
        #dwell状态下返回一个静态状态列表
        PAI = np.zeros((1, (88 + 88)))
        count1 = 0
        count2 = 0
        count = 0
        #开始采样
        while 1:
            #count += 1
            Sep = 0
            #print(s_now,s_next,x,b,w)
            env.state_read(s_now, s_next, x, b, w)
            x_index = x - 1
            PAI[0, x_index * 88 + w * 44 + b * 4 + s_now * 2 + s_next] += 1

            # 判断dwell:做一个动作1 如果超过dwell时间没结果 那就撤销这个动作 把时间加上dwell时间
            if (s_now == 0) & (w == 1):
                if s_next * IFH == 0: #如果是IHO策略的延伸 那就只在 （0，0）才做1动作dwell

                    action = 1
                    r, P = env.step(action)
                    if P[4] != 0:
                        print("error!")
                        break
                    Time, next_state_vector, Judge, choose = env.display(action, P)

                    if Time < d_time:

                        Time_total += Time

                        # 统计丢包和到包
                        if choose == 0:
                            count2 += 1
                            if b == 10:
                                count1 += 1

                        # 有新的包到来 记录时间和位置
                        if next_state_vector[1] - b == 1:
                            Time_reach = np.append(Time_reach, Time_total)
                            Time_leave = np.append(Time_leave, Time_total)
                            Loc_packet = np.append(Loc_packet, next_state_vector[1])

                        w, b, x, s_now, s_next = next_state_vector

                        if Time_total >= 40000:
                            break
                        continue

            action = action_state[w, b, x_index, s_now, s_next]
            action = int(action)
            r, P = env.step(action)
            Time, next_state_vector, Judge, choose = env.display(action, P)

            if w == 1:
                if (action == -1) & (Judge == 1):
                    action_Hand = 1
                    _, P_Hand = env.step(action_Hand)
                    Time_Hand, next_state_vector_Hand, Judge_Hand, choose_Hand = env.display(action_Hand, P_Hand)
                    if Time_Hand < env.tao_HHO:
                        Time, next_state_vector, Judge, choose = Time_Hand, next_state_vector_Hand, Judge_Hand, choose_Hand
                        action = action_Hand
                    else:
                        Time += env.tao_HHO

                if (action == 0) & (Judge == 1):
                    action_Hand = 1
                    _, P_Hand = env.step(action_Hand)
                    Time_Hand, next_state_vector_Hand, Judge_Hand, choose_Hand = env.display(action_Hand, P_Hand)
                    if Time_Hand < env.tao_VHO:
                        Time, next_state_vector, Judge, choose = Time_Hand, next_state_vector_Hand, Judge_Hand, choose_Hand
                        action = action_Hand
                    else:
                        Time += env.tao_VHO
            else:
                if (action == -1) & (Judge == 1):
                    action_Hand = 1
                    _, P_Hand = env.step(action_Hand)
                    Time_Hand, next_state_vector_Hand, Judge_Hand, choose_Hand = env.display(action_Hand, P_Hand)
                    if Time_Hand < env.tao_VHO:
                        Time, next_state_vector, Judge, choose = Time_Hand, next_state_vector_Hand, Judge_Hand, choose_Hand
                        action = action_Hand
                    else:
                        Time += env.tao_VHO

                if (action == 1) & (Judge == 1):
                    action_Hand = 1
                    _, P_Hand = env.step(action_Hand)
                    Time_Hand, next_state_vector_Hand, Judge_Hand, choose_Hand = env.display(action_Hand, P_Hand)
                    if Time_Hand < env.tao_VHO:
                        Time, next_state_vector, Judge, choose = Time_Hand, next_state_vector_Hand, Judge_Hand, choose_Hand
                        action = action_Hand
                    else:
                        Time += env.tao_VHO

            '''
            if w == 1:
                if (action == -1) & (Judge == 1):
                    if Time < env.tao_HHO:
                        n_HHO -= 1
                        next_state_vector[0] = 1
                        #next_state_vector = [w, b, x, s_now, s_next]
                        #Time = env.tao_HHO
                        if choose == 4:
                            next_state_vector[1] = b
                            #Time_total += Time
                        if choose == 0:
                            count1 += 1
                            count2 += 1
                            #Time = env.tao_HHO
                            next_state_vector[1] = b
                        #Time_total += d_time * (1 - s_now) * (1 - IFH * s_next)
                        #w, b, x, s_now, s_next = next_state_vector
                        #continue

                if (action == 0) & (Judge == 1):
                    if Time < env.tao_VHO:
                        n_VHO -= 1
                        next_state_vector[0] = 1
                        #next_state_vector = [w, b, x, s_now, s_next]
                        #Time = env.tao_VHO
                        if choose == 4:
                            #Time_total += Time
                            next_state_vector[1] = b
                        if choose == 0:
                            #Time = env.tao_VHO
                            count1 += 1
                            count2 += 1
                            next_state_vector[1] = b
                        #Time_total += d_time * (1 - s_now) * (1 - IFH * s_next)
                        #w, b, x, s_now, s_next = next_state_vector
                        #continue
            else:
                if (action == -1) & (Judge == 1):
                    if Time < env.tao_VHO:
                        n_VHO -= 1
                        next_state_vector[0] = 0
                        #next_state_vector = [w, b, x, s_now, s_next]
                        #Time = env.tao_VHO
                        if choose == 4:
                            #Time = env.tao_VHO
                            next_state_vector[1] = b
                            #Time_total += Time
                        if choose == 0:
                            #Time = env.tao_VHO
                            count1 += 1
                            count2 += 1
                            next_state_vector[1] = b
                        #Time_total += d_time * (1 - s_now) * (1 - IFH * s_next)
                        #w, b, x, s_now, s_next = next_state_vector
                        #continue
                if (action == 1) & (Judge == 1):
                    if Time < env.tao_VHO:
                        n_VHO -= 1
                        next_state_vector[0] = 0
                        #next_state_vector = [w, b, x, s_now, s_next]
                        #Time = env.tao_VHO
                        if choose == 4:
                            #Time = env.tao_VHO
                            next_state_vector[1] = b
                            #Time_total += Time
                        if choose == 0:
                            #Time = env.tao_VHO
                            count1 += 1
                            count2 += 1
                            next_state_vector[1] = b
                        #Time_total += d_time * (1 - s_now) * (1 - IFH * s_next)
                        #w, b, x, s_now, s_next = next_state_vector
                        #continue
            '''
            '''
            #粗略仿真传输延时
            if w == 1:
                if (action == -1) & (Judge == 1):
                    if Time < env.tao_HHO:
                        count += 1
                        #Time = env.tao_HHO
                        #next_state_vector = [1 ,b, x, s_now, s_next]
                        next_state_vector[0] = 1
                        if choose == 4:
                            #Time = env.tao_VHO
                            next_state_vector[1] = b
                        if choose == 0:
                            #count1 += 1
                            #count2 += 1
                            next_state_vector[1] = b

                if (action == 0) & (Judge == 1):
                    if Time < env.tao_VHO:
                        count += 1
                        Time = env.tao_VHO
                        #next_state_vector = [0, b, x, s_now, s_next]
                        next_state_vector[0] = 1
                        if choose == 4:
                            #Time = env.tao_VHO
                            next_state_vector[1] = b
                        if choose == 0:
                            #count1 += 1
                            #count2 += 1
                            next_state_vector[1] = b
            else:
                if (action == -1) & (Judge == 1):
                    if Time < env.tao_VHO:
                        count += 1
                        Time = env.tao_VHO
                        #next_state_vector = [1, b, x, s_now, s_next]
                        next_state_vector[0] = 0
                        if choose == 4:
                            #Time = env.tao_VHO
                            next_state_vector[1] = b
                        if choose == 0:
                            #count1 += 1
                            #count2 += 1
                            next_state_vector[1] = b

                if (action == 1) & (Judge == 1):
                    if Time < env.tao_VHO:
                        count += 1
                        Time = env.tao_VHO
                        #next_state_vector = [1, b, x, s_now, s_next]
                        next_state_vector[0] = 0
                        if choose == 4:
                            #Time = env.tao_VHO
                            next_state_vector[1] = b
                        if choose == 0:
                            #count1 += 1
                            #count2 += 1
                            next_state_vector[1] = b
            '''

            #统计丢包和到包
            if choose == 0:
                count2 += 1
                if b == 10:
                    count1 += 1
                if Judge == 0:
                    count1 += 1


            #统计切换次数
            if w == 1:
                if (action == -1) & (Judge == 1):
                    n_HHO += 1
                if (action == 0) & (Judge == 1):
                    n_VHO += 1
            if w == 0:
                if (action == -1) & (Judge == 1):
                    n_VHO += 1
                if (action == 1) & (Judge == 1):
                    n_VHO += 1


            #计算平均延迟时间
            Time_total += Time + d_time * (1 - s_now) * (1 - IFH * s_next)

            #有新的包到来 记录时间和位置
            if (next_state_vector[1] - b) == 1:
                Time_reach = np.append(Time_reach, Time_total)
                Time_leave = np.append(Time_leave, Time_total)
                if Sep == 0:
                    Loc_packet = np.append(Loc_packet, next_state_vector[1])
                else:
                    Loc_packet = np.append(Loc_packet, 1)

            #有包被处理 所有包的位置前移
            if (next_state_vector[1] - b) == -1:
                Loc_packet = Loc_packet - np.ones(len(Loc_packet))
                #判断有没有包完全离开队列 记录离开时间
                Time_leave[np.where(Loc_packet == 0)] = Time_total

            #更新参数
            w, b, x, s_now, s_next = next_state_vector

            if Time_total >= 40000:
                break


        #返回参数
        PAI = PAI / np.sum(PAI)
        Time_delay = Time_leave[np.where(Loc_packet <= 0)] - Time_reach[np.where(Loc_packet <= 0)]
        print(Time_delay)
        avr_delay = np.mean(Time_delay)
        prob = count1 / count2
        #print(countwhy2 / countwhy)

        PAI_TOTAL += PAI
        avr_delay_TOTAL += avr_delay
        prob_TOTAL += prob
        n_HHO_TOTAL += n_HHO
        n_VHO_TOTAL += n_VHO
        print(count)

    return PAI_TOTAL, avr_delay_TOTAL, n_HHO_TOTAL, n_VHO_TOTAL, prob_TOTAL

