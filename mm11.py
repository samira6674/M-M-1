import numpy as np
import matplotlib.pyplot as plt
mu = 15
lambda_vec=np.arange(10,15,0.2)

sim_delays = []
an_delays = []

for lamda in lambda_vec:
    AR = []
    DE = []
    q=0
    arrival_time = 0 + np.random.exponential(1 / lamda )
    #departure_time = arrival_time + np.random.exponential(1 / mu)
    departure_time = 0
    t=arrival_time
    AR.append(arrival_time)
    #DE.append(departure_time)
    while t<=1000 :
        if t==arrival_time:
            q=q+1
            arrival_time = t + np.random.exponential(1 / lamda)
            AR.append(arrival_time)
            #print(AR)
            if q==1:
                departure_time = t + np.random.exponential(1 / mu)
                DE.append(departure_time)
                #print(DE)

        if t == departure_time:
            q=q-1
            #departure_time = t + np.random.exponential(1 / mu)
            #DE.append(departure_time)
            if q>0:
                departure_time = t + np.random.exponential(1 / mu)
                DE.append(departure_time)
            else:
                departure_time = np.inf
        if arrival_time <= departure_time:
            t = arrival_time
        else:
            t = departure_time
    Delays=[]
    for j in range(len(DE)):
        Delays.append(DE[j] - AR[j])
    sim_delay_l = np.mean(Delays)
    sim_delays.append(sim_delay_l)
    an_delay_l = 1 / (mu -lamda)
    an_delays.append(an_delay_l)


plt.plot(lambda_vec,sim_delays)
plt.ylabel("sim")

plt.plot(lambda_vec,an_delays)
plt.ylabel("analiz")
plt.show()



