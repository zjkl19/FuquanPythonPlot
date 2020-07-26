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
        (np.datetime64('2020-07-17'), np.datetime64('2020-07-24 00:00'))]
ylims = [(-1.0, 1.0),
        (-1.0, 1.0),
        (-1.0, 1.0)]
yList = [[] for i in range(nPoints)]  # 创建的是多行三列的二维列表

fig, ax = plt.subplots(constrained_layout=True, figsize=(xFigsize, yFigsize))

for i in range(0,nPoints):
    startRow=2
    temp=[]    
    for j in range(0,dataCounts):        
        temp.append(sh.cell_value(startRow+j,i+1))
    yList[i] = np.array(temp)

ax.plot(dates, yList[0])
ax.grid()
ax.set_xlim(lims[0])
ax.set_ylim(ylims[0])

plt.savefig(measurePointsList[0]+'.jpg')
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
