#python初学

##1.注释

在注释中‘#’后可为代码进行注释，提高代码可读性

##2.格式化输出print 的使用格式(format的使用)

```python
age	 =	20
name	=	'Swaroop'
print('{0}	was	{1}	years	old	when	he	wrote	this	book'
      .format(name,	age))
print('Why	is	{0}	playing	with	that	python?'.format(name))
```

输出：

```python
$	python	str_format.py
Swaroop	was	20	years	old	when	he	wrote	this	book
Why	is	Swaroop	playing	with	that	python？
```

亦可以忽略符号内数字

```python
age	 =	20
name	=	'Swaroop'
 print('{}	was	{}	years	old	when	he	wrote	this	book'
       .format(name,	age))
 print('Why	is	{}	playing	with	that	python?'.format(name))
```

关于print拓展

```python
#	对于浮点数	'0.333'	保留小数点(.)后三位
print('{0:.3f}'.format(1.0/3))
#	使用下划线填充文本，并保持文字处于中间位置
#	使用	(^)	定义	'___hello___'字符串长度为	11
print('{0:_^11}'.format('hello'))
#	基于关键词输出	'Swaroop	wrote	A	Byte	of	Python'		
print('{name}	wrote	{book}'
      .format(name='Swaroop',	book='A	Byte	of	Python'))
```

输出

```python
0.333
___hello___
Swaroop	wrote	A	Byte	of	Python
```

###因为python中两个print的使用会默认开启新一行，因此有如下解决方案

```python 
print('a',	end='')
print('b',	end='')
```

###原始字符串的使用方式

```python
r"Newlines	are	indicated	by	\n"
```

在“前加r或者R

意义：避免转义字符如/n /t 无法正常输出