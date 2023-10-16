import matplotlib.pyplot as plt
print (plt.style.available)
#赋值
input_value=range(1,1001)
squares =[x**2 for x in input_value]

fig,ax=plt.subplots()
#渐变
# 散点图折线
ax.scatter(input_value,squares,c=squares,cmap=plt.cm.Blues,s=10)
ax.plot(input_value,squares)
#命名
ax.set_title("square number",fontsize=24)
#x轴命名
ax.set_xlabel("value",fontsize=14)
#y轴命名
ax.set_ylabel("sdhjgf",fontsize=14)
#X,Y轴数值范围
ax.axis([0,1100,1,1100000])
#x轴不用科学计数法
ax.ticklabel_format(style='plain')
#存图像
 #plt.savefig('squares_plot.png',bbox_inches="tight")
#显示图像
plt.show()




