# coding=utf-8
__author__ = 'Eric Chan'
x=[]
y=[]
f = open(r'trainingset.txt')             # 返回一个文件对象 r表示只读
line = f.readline()             # 调用文件的 readline()方法
while line:
    line=line.strip().split(',')  #strip() 取消前后空格
    x.append([1,int(line[0]),int(line[1])])
    y.append(int(line[2]))
   #  print line,                 # 后面跟 ',' 将忽略换行符
   #  print(line, end = '')　　　# 在 Python 3中使用
    line = f.readline()
print x
print y
f.close()

# 将y数组进行缩小 至特征值0~5
yi = []
for i in range(len(y)):
    y[i] = float(y[i])
for i in y :
    yi.append(i/100000)
print yi


epsilon = 0.00000000000001  #收敛程度
alpha = 0.0000003          #学习速率
m = len(x)
j = 0
h = [None] * m
J = [None] * m
dJ = 0
dJ2 = 0
theta0 = 0
theta1 = 0
theta2 = 0
temp0 = 0
temp1 = 0
temp2 = 0
a = 0

while True:
    for i in range(m):
        h[i] = theta0 * x[i][0] + theta1 * x[i][1] + theta2 * (x[i][2])  # 定义预测值公式
        J[i] = h[i] - yi[i]   #代价函数
        temp0 -= (alpha * J[i] * x[i][0]) / m #同步更新theta
        temp1 -= (alpha * J[i] * x[i][1]) / m
        temp2 -= (alpha * J[i] * x[i][2]) / m
    theta0 = temp0
    theta1 = temp1
    theta2 = temp2
    for i in range(m):
        dJ += ((J[i] * J[i]) / (2 * m))

    print theta0,theta1,theta2,dJ  #输出收敛过程中 theta 变化 可有可无

    #判断是否收敛 根据epsilon的大小 可控制精确程度 也会影响运行速率
    if ((dJ-dJ2)**2) < epsilon:
        break
    else:
        dJ2 = dJ
        dJ = 0



# 输出预测值 x1 x2 真实值
for i in range(m):
    h[i] = h[i] * 100000
    print h[i], x[i][1], x[i][2], y[i]











