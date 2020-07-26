# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 10:51:33 2020

@author: 林迪南
"""
import matplotlib.pyplot as plt  # 使用import导入模块matplotlib.pyplot，并简写成plt  
import matplotlib.dates as mdates
import numpy as np  # 使用import导入模块numpy，并简写成np

import datetime

import xlrd #导入x1rd库

dataExcel='Data.xlsx';dataSheet='传感器监测数据报表'
data=xlrd.open_workbook(dataExcel)
sh=data.sheet_by_name(dataSheet)

nPoints=15    #15个测点

dataCounts=7*24    #7天数据，7*24=168个，每小时采集一次数据
scaleFactor=1.0    #控制x轴长度

startRow=2    #从excel表格第3行开始读取
measurePointsList=[]    #测点名称
yList=[]    #监测数据

print(sh.cell_value(startRow-1,15))

for i in range(0,nPoints):
    measurePointsList.append(sh.cell_value(startRow-1,i+1))

for i in range(0,dataCounts):
    yList.append(sh.cell_value(startRow+i,1))

yList = np.array(yList)    #列表转换为nparray

xFigsize=10;yFigsize=3
rotAngle=40    #旋转角度
base = datetime.datetime(2020, 7, 17)

#dates即x轴数据
dates = [base + datetime.timedelta(hours=(1 * i)) for i in range(dataCounts)]    #1小时1个数据
lims = [(np.datetime64('2020-07-17'), np.datetime64('2020-07-24 00:00')),
        (np.datetime64('2020-07-17'), np.datetime64('2020-07-24 00:00')),
        (np.datetime64('2020-07-17'), np.datetime64('2020-07-24 00:00')),
        (np.datetime64('2020-07-17'), np.datetime64('2020-07-24 00:00')),
        (np.datetime64('2020-07-17'), np.datetime64('2020-07-24 00:00')),
        (np.datetime64('2020-07-17'), np.datetime64('2020-07-24 00:00')),
        (np.datetime64('2020-07-17'), np.datetime64('2020-07-24 00:00')),
        (np.datetime64('2020-07-17'), np.datetime64('2020-07-24 00:00')),
        (np.datetime64('2020-07-17'), np.datetime64('2020-07-24 00:00')),
        (np.datetime64('2020-07-17'), np.datetime64('2020-07-24 00:00')),
        (np.datetime64('2020-07-17'), np.datetime64('2020-07-24 00:00')),
        (np.datetime64('2020-07-17'), np.datetime64('2020-07-24 00:00')),
        (np.datetime64('2020-07-17'), np.datetime64('2020-07-24 00:00')),
        (np.datetime64('2020-07-17'), np.datetime64('2020-07-24 00:00')),
        (np.datetime64('2020-07-17'), np.datetime64('2020-07-24 00:00'))]


#F17-D-位移(mm)	G11-D-位移(mm)	F17-L-倾角(°)	G11-L-倾角(°)	D2-2倾角-倾角(°)	ZW24-1倾角-倾角(°)	ZW24-2倾角-倾角(°)	ZE24-1倾角-倾角(°)	ZE24-2倾角-倾角(°)	D2-2-1位移-位移(mm)	D2-2-2位移-位移(mm)	ZW24-1位移-位移(mm)	ZW24-2位移-位移(mm)	ZE24-1位移-位移(mm)	ZE24-2位移-位移(mm)


defaultLeanLims=(-0.1,0.1)

ylabelList=['位移(mm)','位移(mm)','倾角(°)','倾角(°)','倾角(°)','倾角(°)','倾角(°)','倾角(°)','倾角(°)','位移(mm)','位移(mm)','位移(mm)','位移(mm)','位移(mm)','位移(mm)']

ylims = [(-1.0, 1.0),(-1.0, 1.0),defaultLeanLims,defaultLeanLims,defaultLeanLims
        ,defaultLeanLims,defaultLeanLims,defaultLeanLims,defaultLeanLims,(-1.0, 1.0)
        ,(-1.0, 1.0),(-1.0, 1.0),(-2.0, 2.0),(-1.0, 1.0),(-1.0, 1.0)
        ,(-1.0, 1.0),(-1.0, 1.0),(-1.0, 1.0),(-1.0, 1.0),(-1.0, 1.0)
        ,(-1.0, 1.0),(-1.0, 1.0),(-1.0, 1.0),(-1.0, 1.0),(-1.0, 1.0)]

alerLine = [(-1.0, 1.0),(-1.0, 1.0),(-1.0, 1.0),(-1.0, 1.0),(-1.0, 1.0)
        ,(-1.0, 1.0),(-1.0, 1.0),(-1.0, 1.0),(-1.0, 1.0),(-1.0, 1.0)
        ,(-1.0, 1.0),(-1.0, 1.0),(-2.0, 2.0),(-1.0, 1.0),(-1.0, 1.0)
        ,(-1.0, 1.0),(-1.0, 1.0),(-1.0, 1.0),(-1.0, 1.0),(-1.0, 1.0)
        ,(-1.0, 1.0),(-1.0, 1.0),(-1.0, 1.0),(-1.0, 1.0),(-1.0, 1.0)]

yList = [[] for i in range(nPoints)]  # 创建的是多行n列的二维列表
for i in range(0,nPoints):
    startRow=2
    temp=[]    
    for j in range(0,dataCounts):        
        temp.append(sh.cell_value(startRow+j,i+1))
    yList[i] = np.array(temp)

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
   
for i in range(0,nPoints):
    fig, ax = plt.subplots(constrained_layout=True, figsize=(xFigsize, yFigsize))
    
    ax.plot(dates, yList[i])
    ax.set(xlabel='时间', ylabel=ylabelList[i])
    
    ax.grid()
    ax.set_xlim(lims[i])
    ax.set_ylim(ylims[i])
    
    #plt.axhline(y=0.25,c="yellow")#添加水平直线
    plt.savefig(measurePointsList[i]+'.jpg')
#k=0
#for nn, ax in enumerate(axs):
#          
#    ax.plot(dates, yList[k])
#    ax.set_xlim(lims[nn])
#    # rotate_labels...
#    for label in ax.get_xticklabels():
#        label.set_rotation(rotAngle)
#        label.set_horizontalalignment('right')
#    k=k+1
    
#for i in range(0,1):
#    axs[0].plot(dates, yList[i])
#    axs[0].set_xlim(lims[i])
#    # rotate_labels...
#    for label in axs[0].get_xticklabels():
#        label.set_rotation(rotAngle)
#        label.set_horizontalalignment('right')
#
#axs[0].set_title('Default Date Formatter')
#plt.show()

#fig, ax = plt.subplots()
#ax.plot(xList, yList)

#ax.xaxis.set_minor_locator(AutoMinorLocator())

#ax.tick_params(which='both', width=2)
#ax.tick_params(which='major', length=7)
#ax.tick_params(which='minor', length=4, color='r')