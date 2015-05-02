# coding=utf-8
__author__ = 'Eric Chan'
import math

# 将训练集导入
x = []
y = []
f = open(r'testSet.txt')  # 返回一个文件对象 r表示只读
line = f.readline()  # 调用文件的 readline()方法
while line:
    line = line.split()
    x.append([1, float(line[0]), float(line[1])])
    y.append(int(line[2]))
    line = f.readline()
print x
print y
f.close()

#定义变量
epsilon = 0.000000005  # 收敛程度
alpha = 0.00001  # 学习速率
rate = 0.6     # 大于该值则判断 y=0  否则 y=1
m = len(x)
temp_h = [None] * m
h = [None] * m
J = [None] * m
TF = [None] * m
dJ = 0
dJ2 = 0
theta0 = 0
theta1 = 0
theta2 = 0
temp0 = 0
temp1 = 0
temp2 = 0
e = 2.71828182846

while True:
    for i in range(m):
        temp_h[i] = theta0 * x[i][0] + theta1 * x[i][1] + theta2 * (x[i][2])  # 定义预测值公式
        h[i] = 1 / (1 + e ** (-temp_h[i]))
        J[i] = y[i] * math.log(e, h[i]) + (1 - y[i]) * math.log(e, (1 - h[i]))  # cost function
        temp0 -= (alpha * J[i] * x[i][0]) / m  # 同步更新theta
        temp1 -= (alpha * J[i] * x[i][1]) / m
        temp2 -= (alpha * J[i] * x[i][2]) / m
    theta0 = temp0
    theta1 = temp1
    theta2 = temp2
    for i in range(m):
        dJ += -(J[i] / m)

    print theta0, theta1, theta2, dJ  # 输出收敛过程中 theta 变化 可有可无

    # 判断是否收敛
    if ((dJ - dJ2) ** 2) < epsilon:
        break
    else:
        dJ2 = dJ
        dJ = 0


# 输出预测值 h 真实值
for i in range(m):
    if (h[i] >= rate):
        TF[i] = 0
    else:
        TF[i] = 1
    print TF[i], h[i], y[i]



# 输出本次拟合的正确率
correct = 0
all = 0
for i in range(m):
    if TF[i] == y[i]:
        correct = correct + 1
    all = all + 1
correct = float(correct)
print "正确率：" , correct/all
