import matplotlib.pyplot as plt

class SIR:
    def __init__(self,max_time=None, dt=None,s=None,i=None,r=None,beta=None,gamma=None):
        if max_time == None:
            max_time=int(input("Time: "))
            dt = int(input("Timestep: "))
            s=float(input("Susceptible: "))
            i=float(input("Infected: "))
            r=float(input("Recovered: "))
            beta=float(input("Beta: "))
            gamma=float(input("Gamma: "))
        self.max_time = max_time
        self.dt = dt
        self.s=s
        self.i=i
        self.r=r
        self.beta=beta
        self.gamma=gamma
        self.t = 0
        self.s_record = []
        self.i_record = []
        self.r_record = []
        self.t_record = []
        while self.t < self.max_time:
            self.t += self.dt
            self.timestep(self.dt)
            print(str(round(self.s + self.i + self.r,4)) + " : " + str(self.s) + " / " + str(self.i) + " / " + str(self.r))
            self.s_record.append(self.s)
            self.i_record.append(self.i)
            self.r_record.append(self.r)
            self.t_record.append(self.t)
        plt.plot(self.t_record, self.s_record, 'g')
        plt.plot(self.t_record, self.i_record, 'r')
        plt.plot(self.t_record, self.r_record, 'b')
        plt.show()

    def timestep(self,dt):
        ds = -(self.beta * self.i * self.s)
        di = (self.beta * self.i * self.s) - self.gamma * self.i
        dr = self.gamma * self.i
        self.s += ds*dt
        self.i += di*dt
        self.r += dr*dt
