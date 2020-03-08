import numpy as np
import random
from scipy.optimize import minimize
import matplotlib.pyplot as plt



class circle:#封装
    def __init__(self, radius = 0, x = 0, y = 0):#初始化
        self.radius = radius    
        self.x = x   
        self.y = y

    def print_information(self):#输出圆数值      
        print('半径为{}, 圆心坐标为({},{})'.format(self.radius, self.x, self.y))

    def distance(self, c2):    #计算距离
        dis = ((self.x-c2.x)**2+(self.y-c2.y)**2)**0.5
        return dis

    def whether_cross(self, c_list):#判断是否重叠
        for i in range (len(c_list)):
            c2 = c_list[i]
            r1 = self.radius
            r2 = c2.radius
            rr = r1+r2
            dis = self.distance(c2)
            if dis < rr:
                return 0
        return 1
      
def MaxR(c1, c_list):#找出当前最大半径
    x = c1.x
    y = c1.y
    R_list = [1-x,1+x,1-y,1+y]
    for i in range (len(c_list)):
        c2 = c_list[i]
        dis = c1.distance(c2)
        R_list.append(dis-c2.radius)
    return min(R_list)

def func(c_list):#优化
    return lambda x : 1 - MaxR(circle(x[0], x[1], x[2]), c_list)

def Find_center(c, c_list):#找出当前最优圆心
    r = c.radius
    x = c.x
    y = c.y
    rxy = [r,x,y]
    bd_r = (0, 1)
    bd_x = (-1, 1)
    bd_y = (-1, 1)
    bds = (bd_r, bd_x, bd_y)       
    res = minimize(func(c_list), rxy, method='SLSQP', bounds=bds)
    c.x = res.x[1]
    c.y = res.x[2]
    c.radius = MaxR(c, c_list)
    return c


def Find_m_Circuit(m):#m个圆一起
    c_list = []
    for i in range (m):
        r = 0
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        c = circle(r, x, y)
        while not c.whether_cross(c_list):           
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)
            c = circle(r, x, y)
        c = Find_center(c, c_list)
        c_list.append(c)
    return c_list

def plot(c_list):#画图
    plt.figure()
    plt.axes().set_aspect('equal')
    plt.xlim([-1,1])
    plt.ylim([-1,1])  
    theta = np.linspace(0,2*np.pi,50)
    for c in c_list:
        plt.plot(c.x+c.radius*np.cos(theta),c.y+c.radius*np.sin(theta),'b')       
    plt.show()


if __name__ == "__main__":
    m = int(input('请输入圆个数m：'))
    c_list = Find_m_Circuit(m)   
    RR = 0   
    i = 1

    for c in c_list:
        RR += c.radius**2       
        print('第{}个圆的数值：'.format(i))       
        i += 1
        c.print_information()

    print('共{}个圆填充正方形，r^2之和最大为{}'.format(m, RR))
    print('所有圆面积之和占正方形面积的{:.2%}'.format(RR*np.pi/4))
    plot(c_list)
