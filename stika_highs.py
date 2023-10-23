from pathlib import Path
import matplotlib.pyplot as plt
from datetime import datetime
#引入path模块
#引入scv模块
#通过逗号分割的excel来绘图
import csv
path =Path('weather_data/sitka_weather_07-2014.csv')
lines=path.read_text().splitlines()
#splitlines以换行符进行拆分
print (lines)
reader=csv.reader(lines)
header_row=next(reader)
dates,highs,lows=[],[],[]

#next只返回一行
 #for index,column_header in enumerate(header_row):
  #  print(index,column_header)
    #给每行数值以数字命名
# highs=[]
for row in reader:
    #由于前面已经读过了next所以从第二行开始读取
    #处理数据缺失
    try:
        high=int (row[4])
        low=int (row[5])
    except ValueError:
        print((f"missing data for {current_date}"))
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)



print(highs)
#提取第列的元素
plt.style.use('classic')
fig,ax=plt.subplots()
ax.plot(dates,highs,color='red',alpha=0.1)
ax.plot(dates,lows,color='Blue',alpha=0.1)
ax.fill_between(dates,highs,lows,facecolor='Green',alpha=0.1)
ax.set_title("daliy high tem and low",fontsize=16)
ax.set_xlabel('',fontsize=16)
fig.autofmt_xdate()#绘制倾斜的日期标签
ax.set_ylabel("temperature(F)",fontsize=16)
ax.tick_params(labelsize=16)
plt.show()