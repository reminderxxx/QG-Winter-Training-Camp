import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为 SimHei（黑体）
plt.rcParams['axes.unicode_minus'] = False  # 解决负号'-'显示为方块的问题

train = pd.read_csv('train.csv') #读入数据
# print (train.head()) #展示数据成功导入
# print (train.describe()) #获取数据类型列的描述统计信息
# print (train.info()) # 查看每一列的数据类型，和数据总数

n = train['Survived'].value_counts() #查看生还人数 #.valve_counts() 用于查看不同数据出现的次数
#print (n)

'''
plt.figure(figsize=(6,6)) #创建图形窗口
plt.pie(n,autopct='%.2f%%',labels=['死亡','存活'],pctdistance=0.4,labeldistance=0.6,
       shadow=True,explode=[0,0.1],textprops=dict(size=15)) #饼图设置
plt.title('总体生还率') #设置标题
plt.show() #展示绘图
'''
age_range = train['Age']
#print(age_range.min(), age_range.max()) #展示年龄范围

age_num = np.histogram(age_range,range=[0,80],bins=16 )
#print(age_num) #展示各级年龄人数

age_survived = [] #创建空列表
for age in range(5,81,5):
    survived_num = train.loc[(age_range>=age-5) & (age_range<=age)]['Survived'].sum()
    age_survived.append(survived_num) #将当前年龄段的生还人数添加到 age_survived 列表中
# print(age_survived) #展示生还人数
'''
plt.figure(figsize=(12,6)) #创建窗口
plt.bar(np.arange(2,78,5)+0.5,age_num[0],width=5,label='总人数',alpha=0.8) #柱形图设置
plt.bar(np.arange(2,78,5)+0.5,age_survived,width=5,label='生还人数')
plt.xticks(range(0,81,5)) #设定坐标
plt.yticks(range(0,121,10))
plt.xlabel('年龄',position=(0.95,0),fontsize=15)
plt.ylabel('人数',position=(0,0.95),fontsize=15)
plt.title('各年龄阶段人数和生还人数条形图')
plt.grid(True,linestyle=':',alpha=0.6) #增添网格线
plt.legend() #增加图例
plt.show()
'''

embarked_count = train.groupby(['Embarked'])['Survived'].value_counts()
'''
print(embarked_count)

plt.figure(figsize=(3*5,5))
axes1=plt.subplot(1,3,1)
axes1.pie(embarked_count.loc['C'][::-1],autopct='%.2f%%',labels=['死亡','存活'],pctdistance=0.4,labeldistance=0.6,
       shadow=True,explode=[0,0.1],textprops=dict(size=15),colors=['#9400D3','#FFB6C1'],startangle=45)
axes1.set_title('法国瑟堡市乘客生还率')

axes2=plt.subplot(1,3,2)
axes2.pie(embarked_count.loc['Q'],autopct='%.2f%%',labels=['死亡','存活'],pctdistance=0.4,labeldistance=0.6,
       shadow=True,explode=[0,0.1],textprops=dict(size=15),colors=['#4169E1','#AFEEEE'])
axes2.set_title('爱尔兰昆士敦乘客生还率')

axes3=plt.subplot(1,3,3)
axes3.pie(embarked_count.loc['S'],autopct='%.2f%%',labels=['死亡','存活'],pctdistance=0.4,labeldistance=0.6,
       shadow=True,explode=[0,0.1],textprops=dict(size=15),colors=['#698B69','#76EE00'])
axes3.set_title('英国南安普顿乘客生还率')
plt.legend()
plt.show()
'''

#不同票价的生存情况
fare_count = train.groupby(by='Fare')['Survived'].value_counts()
fare_count = pd.DataFrame(fare_count) #将Series转换为DataFrame

fare_count.rename(columns={'count':'Number'},inplace=True) #对列重命名
fare_count.reset_index(inplace=True) #多级索引改为列
# print(fare_count)

# 统计出的各票价乘客总人数
fare_num = fare_count.groupby(by='Fare')['Number'].sum()
fare_num = pd.DataFrame(fare_num)
fare_num.rename(columns={'Number':'Total'},inplace=True)
#生存人数
fare_survived = fare_count.loc[fare_count['Survived']==1]
fare_survived = fare_survived.merge(fare_num,left_on='Fare',right_index=True,how='inner')
#生存率
survived_rate = fare_survived['Number'].div(fare_survived['Total'])
survived_rate.index = fare_survived['Fare']
fare_death = fare_count.loc[fare_count['Survived']==0]
fare_death = fare_death.merge(fare_num,left_on='Fare',right_index=True,how='inner')
# print(fare_death)

# 各票价乘客的死亡率
death_rate = fare_death['Number'].div(fare_death['Total'])
death_rate.index = fare_death['Fare']

plt.figure(figsize=(2*10,5)) # 两张散点图画在同一张图纸上
# 乘客的生还率和票价关系散点图
axes1=plt.subplot(1,2,1)
axes1.scatter(survived_rate.index,survived_rate,marker='o',color='r')
axes1.set_title('乘客生还率和票价关系散点图')

# 乘客的死亡率和票价关系散点图
axes2=plt.subplot(1,2,2)
axes2.scatter(death_rate.index,death_rate,marker='^',color='b')
axes2.set_title('乘客死亡率和票价关系散点图')

plt.show()
