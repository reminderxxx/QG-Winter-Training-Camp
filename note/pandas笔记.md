# pandas笔记

## 1. 将csv数据导入到Pandas DataFrame 中

```python
import pandas as pd

df = pd.read_csv('data.csv')

print(df.to_string()) 
```

## 2. what is pandas

​	pandas 就是一个处理数据集的python库，包含了数据预处理的能力（去除异常值 去除空值 分析、处理数据）

## 3. pandas 最基础的语法

```python
import pandas

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)
```

```python
    cars  passings
0    BMW         3
1  Volvo         7
2   Ford         2
```

### 同时可以将pandas以别名pd导入

```python
import pandas as pd
```

实际使用如下

```python
import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)
```

### 检查Pandas版本

``` python
import pandas as pd

print(pd.__version__)
```

### 数列的简单语法（Series）

```python
import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)
```

#### output

```python
0     1
1     7
2     2
3     8
4     9
5    10
dtype: int64
```

### 提取数列某个数（labels）

```python
print(myvar[0])
```

### 创建标签

```python
import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)
```

#### output

```python
x    1
y    7
z    2
dtype: int64
```

#### Tips 必须严格对照labels与数据的数量，否则error

### 提取某个label对照的值

```python
print(myvar["y"])
```

### 同样的方法创建series

```python
import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)
```

#### output

```python
day1    420
day2    380
day3    390
dtype: int64
```

### 提取某两个数据

``` python
import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)
```

### Dataframe运用

```python
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)
```

#### output

```python
   calories  duration
0       420        50
1       380        40
2       390        45
```

### 输出第0行的数据

```python
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df.loc[0])
```

#### output

```python
calories    420
duration     50
Name: 0, dtype: int64
```

### 输出0、1行的数据

```python
print(df.loc[[0, 1]])
```

#### output

```python
    calories  duration
  0       420        50
  1       380        40
```

### Dataframe的index

```python
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df) 
```

#### output

``` python
        calories  duration
  day1       420        50
  day2       380        40
  day3       390        45
```

### locate index 的数据

```python
print(df.loc["day2"])
```

#### output

```python
calories    380
duration     40
Name: day2, dtype: int64
```



### 将CSV加载到DataFrame中

```python
import pandas as pd

df = pd.read_csv('data.csv')

print(df.to_string()) 
```

#### Tips : to_string() 用于打印整张DataFrame，如果没有则只展示前五行与后五行

### 查看展示最大行数

```python
import pandas as pd

print(pd.options.display.max_rows) 
```

### 改变最大行数

```python
import pandas as pd

pd.options.display.max_rows = 9999

df = pd.read_csv('data.csv')

print(df) 
```



### 将json加载到DataFrame中

```python
import pandas as pd

df = pd.read_json('data.json')

print(df.to_string()) 
```

### 加载json数据

```pyhton
import pandas as pd

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  }
}

df = pd.DataFrame(data)

print(df) 
```

### 查看前十行数据

```python
import pandas as pd

df = pd.read_csv('data.csv')

print(df.head(10))
```

#### Tips : 若不标明前几行则只默认输出前5行

### 后五行就将head改为tail

### info（）查看更多信息

```python
print(df.info()) 
```



## 4.清理数据值

### 坏数据

1. 空格值
2. 错误的格式
3. 错误的数据
4. 重复值

### （1）处理空值

### 去除空值

```python
import pandas as pd

df = pd.read_csv('data.csv')

new_df = df.dropna()

print(new_df.to_string())
```

#### Tips : 默认情况下，dropna（）会返回一个新表，不会更改原表，若要更改原表可以用以下语法

```python
import pandas as pd

df = pd.read_csv('data.csv')

df.dropna(inplace = True)

print(df.to_string())
```

#### 以上语法就是直接修改原表

### 填补空值

```python
import pandas as pd

df = pd.read_csv('data.csv')

df.fillna(130, inplace = True)
```

#### 但这个方法将所有列空值都替换了

#### 若要替换特定列空值可以用以下语法

```python
import pandas as pd

df = pd.read_csv('data.csv')

df["Calories"].fillna(130, inplace = True)
```

### 用均值、中位数，众数填充空值(其实就是先计算再填补)

```python
import pandas as pd

df = pd.read_csv('data.csv')

x = df["Calories"].mean()

df["Calories"].fillna(x, inplace = True)
```



### （2）更改错误格式（日期）

```python
import pandas as pd

df = pd.read_csv('data.csv')

df['Date'] = pd.to_datetime(df['Date'])

print(df.to_string())
```

#### Tips ： 其上就运用了to_datetime()调整日期格式



### (3) 更改错误数据

```python
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)
```



### (4)去除重复数据

```python
df.drop_duplicates(inplace = True)
```



## 5. 数据相关性展示

```python
df.corr()
```

#### Tips : 数值绝对值越靠近1，相关性越好



## 6. 绘图

```python
#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot()

plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
```

完整绘图程序

### 拆解

#### 可视化

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot()

plt.show()
```

可视化关键代码

### 散点图代码

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')

plt.show()
```

#### Tips : 记得设定x轴，y轴，否则ERROR

### 直方图代码

```python
df["Duration"].plot(kind = 'hist')
```



### 到此Pandas库已经基本介绍完毕，以下附上语法表

![1739256973829](C:\Users\48659\AppData\Roaming\Typora\typora-user-images\1739256973829.png)

![1739256997341](C:\Users\48659\AppData\Roaming\Typora\typora-user-images\1739256997341.png)

![1739257015694](C:\Users\48659\AppData\Roaming\Typora\typora-user-images\1739257015694.png)

![1739257035489](C:\Users\48659\AppData\Roaming\Typora\typora-user-images\1739257035489.png)

![1739257047489](C:\Users\48659\AppData\Roaming\Typora\typora-user-images\1739257047489.png)

![1739257064189](C:\Users\48659\AppData\Roaming\Typora\typora-user-images\1739257064189.png)

![1739257076048](C:\Users\48659\AppData\Roaming\Typora\typora-user-images\1739257076048.png)

![1739257086086](C:\Users\48659\AppData\Roaming\Typora\typora-user-images\1739257086086.png)

