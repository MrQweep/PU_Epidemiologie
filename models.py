import matplotlib.pyplot as plt


class SIR:
    def __init__(self):
        self.max_time = int(input("Time: "))
        self.n=int(input("Population: "))
        self.s=float(input("Percentage of Susceptible: "))
        self.i=float(input("Percentage of Infected: "))
        self.r=float(input("Percentage of Recovered: "))
        self.beta=float(input("Beta: "))
        self.gamma=float(input("Gamma: "))
        self.t = 0
        self.s_record = []
        self.i_record = []
        self.r_record = []
        while self.t < self.max_time:
            self.t += 1
            self.timestep()
            print(str(round(self.s + self.i + self.r,4)) + " : " + str(self.s) + " / " + str(self.i) + " / " + str(self.r))
            self.s_record.append(self.s * self.n)
            self.i_record.append(self.i * self.n)
            self.r_record.append(self.r * self.n)
        plt.plot(self.s_record, 'g')
        plt.plot(self.i_record, 'r')
        plt.plot(self.r_record, 'b')
        plt.show()

    def timestep(self):
        ds = -(self.beta * self.i * self.s)
        di = (self.beta * self.i * self.s) - self.gamma * self.i
        dr = self.gamma * self.i
        self.s += ds
        self.i += di
        self.r += dr
