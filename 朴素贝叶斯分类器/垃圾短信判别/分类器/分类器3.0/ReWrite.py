#coding=utf-8
'''
Author = Eric_Chan
Create_Time = 2015/12/4
'''
'''
将修正后的2818条短信结果,覆盖原来的判定结果
'''
def loadData(filename): #输入读取的文件
    print "开始读取数据集..."

    file1 = open(filename,'r')
    line = file1.readline()
    messageID = [] #记录短信的ID
    classVec = [] #记录短信对应的属性, 1 代表垃圾短信 0 代表普通短信 (result)
    while line:
        temp = line.split(',')
        messageID.append(temp[0])
        classVec.append(temp[1])
        line = file1.readline()
    file1.close()
    return messageID,classVec

def rewrite(rewriteFileName,rewriteResultFileName):
    rewrite_ID,rewrite_vec = loadData("result/%s"%rewriteFileName)
    result_ID,result_vec = loadData("result/result.txt")
    f = open("newResult/%s"%rewriteResultFileName,'w')
    re_num = len(rewrite_ID)
    result_num = len(result_vec)
    j = 0
    for i in range(result_num):
        if (j<re_num-1) & (result_ID[i] == rewrite_ID[j]):

            f.write(result_ID[i]+','+rewrite_vec[j]+'\n')
            j += 1
        else:
            f.write(result_ID[i]+','+result_vec[i])
    f.close()

rewrite("result0_0000000000001.txt","newResult0_0000000000001.csv")
