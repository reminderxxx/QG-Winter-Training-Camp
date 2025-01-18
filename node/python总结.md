# Python 学习总结

## 1. 基础语法与缩进
- **缩进规则**：Python 使用缩进来定义代码块，通常使用 **4个空格** 作为缩进。缩进不一致会导致语法错误。
- **注释**：
  - 单行注释：使用 `#`，例如：`# 这是一个注释`。
  - 多行注释：使用三个单引号 `'''` 或三个双引号 `"""`，例如：
    ```python
    '''
    这是一个多行注释
    可以写多行内容
    '''
    ```

---

## 2. 数字类型
Python 支持多种数字类型：
- **int（整数）**：如 `10`, `-5`, `0`。
- **float（浮点数）**：如 `3.14`, `-0.001`, `2.0`。
- **bool（布尔值）**：`True` 或 `False`（注意首字母大写）。
- **complex（复数）**：如 `1+2j`，其中 `1` 是实部，`2` 是虚部。

---

## 3. 数据结构
Python 提供了多种内置数据结构：

### 3.1 字符串（str）
- 不可变序列，用单引号 `'` 或双引号 `"` 定义。
- 示例：
  ```python
  s = "hello"
  print(s[0])  # 输出 'h'
  print(s + " world")  # 字符串拼接
  ```



### 3.2 列表（list）

- 可变序列，用方括号 `[]` 定义。

- 示例：

  python

  复制

  ```
  lst = [1, 2, 3, 4]
  lst.append(5)  # 添加元素
  print(lst[1:3])  # 切片，输出 [2, 3]
  ```

### 3.3 字典（dict）

- 键值对集合，用花括号 `{}` 定义。

- 示例：

  python

  复制

  ```
  d = {'name': 'Alice', 'age': 25}
  print(d['name'])  # 输出 'Alice'
  d['age'] = 26  # 修改值
  ```

### 3.4 元组（tuple）

- 不可变序列，用圆括号 `()` 定义。

- 示例：

  python

  复制

  ```
  t = (1, 2, 3)
  print(t[0])  # 输出 1
  ```

### 3.5 集合（set）

- 无序且不重复的元素集合，用花括号 `{}` 或 `set()` 定义。

- 示例：

  python

  复制

  ```
  s = {1, 2, 3}
  s.add(4)  # 添加元素
  print(s)  # 输出 {1, 2, 3, 4}
  ```

### 3.6 切片

- 用于从序列中提取子集，语法为 `[start:stop:step]`。

- 示例：

  python

  复制

  ```
  lst = [1, 2, 3, 4, 5]
  print(lst[1:4])  # 输出 [2, 3, 4]
  print(lst[::2])  # 步长为2，输出 [1, 3, 5]
  ```

------

## 4. 条件控制与循环控制

### 4.1 条件控制

- 使用 `if`, `elif`, `else` 进行条件判断。

- 示例：

  python

  复制

  ```
  x = 10
  if x > 0:
      print("正数")
  elif x == 0:
      print("零")
  else:
      print("负数")
  ```

### 4.2 循环控制

- **for 循环**：遍历序列。

  python

  复制

  ```
  for i in range(5):
      print(i)  # 输出 0 到 4
  ```

- **while 循环**：条件为真时重复执行。

  python

  复制

  ```
  i = 0
  while i < 5:
      print(i)
      i += 1
  ```

- **break 和 continue**：

  - `break`：退出循环。
  - `continue`：跳过当前迭代，进入下一次循环。

------

## 5. 推导式

推导式是一种简洁的创建数据结构的方式。

### 5.1 列表推导式

- 示例：

  python

  复制

  ```
  squares = [x**2 for x in range(10)]
  print(squares)  # 输出 [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
  ```

### 5.2 字典推导式

- 示例：

  python

  复制

  ```
  d = {x: x**2 for x in range(5)}
  print(d)  # 输出 {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
  ```

### 5.3 集合推导式

- 示例：

  python

  复制

  ```
  s = {x**2 for x in range(5)}
  print(s)  # 输出 {0, 1, 4, 9, 16}
  ```

------

## 6. 错误和异常捕获

- 使用 `try`, `except`, `finally` 来捕获和处理异常。

- 示例：

  python

  复制

  ```
  try:
      result = 10 / 0
  except ZeroDivisionError:
      print("除数不能为零")
  finally:
      print("执行完毕")
  ```

------

## 7. 高阶函数

- **map**：对序列中的每个元素应用函数。

  python

  复制

  ```
  lst = [1, 2, 3]
  result = map(lambda x: x**2, lst)
  print(list(result))  # 输出 [1, 4, 9]
  ```

- **lambda**：匿名函数。

  python

  复制

  ```
  f = lambda x: x + 1
  print(f(2))  # 输出 3
  ```

- **filter**：过滤序列中的元素。

  python

  复制

  ```
  lst = [1, 2, 3, 4]
  result = filter(lambda x: x > 2, lst)
  print(list(result))  # 输出 [3, 4]
  ```

------

## 8. 面向对象编程

### 8.1 类与实例化

- 使用 `class` 定义类，通过类创建实例。

- 示例：

  python

  复制

  ```
  class Person:
      def __init__(self, name, age):
          self.name = name
          self.age = age
  
  p = Person("Alice", 25)
  print(p.name)  # 输出 'Alice'
  ```

### 8.2 类变量与方法

- 类变量是所有实例共享的变量。

- 方法是类中定义的函数。

- 示例：

  python

  复制

  ```
  class Person:
      species = "Human"  # 类变量
  
      def __init__(self, name):
          self.name = name
  
      def greet(self):
          print(f"Hello, my name is {self.name}")
  
  p = Person("Alice")
  p.greet()  # 输出 'Hello, my name is Alice'
  print(Person.species)  # 输出 'Human'
  ```

### 8.3 私有变量与方法

- 使用双下划线 `__` 定义私有成员。

- 示例：

  python

  复制

  ```
  class Person:
      def __init__(self, name):
          self.__name = name  # 私有变量
  
      def __greet(self):  # 私有方法
          print(f"Hello, {self.__name}")
  
  p = Person("Alice")
  # p.__greet()  # 报错，无法直接访问私有方法
  ```

### 8.4 封装

- 隐藏对象的内部状态，通过方法访问和修改。

- 示例：

  python

  复制

  ```
  class Person:
      def __init__(self, name):
          self.__name = name
  
      def get_name(self):
          return self.__name
  
      def set_name(self, name):
          self.__name = name
  
  p = Person("Alice")
  print(p.get_name())  # 输出 'Alice'
  p.set_name("Bob")
  print(p.get_name())  # 输出 'Bob'
  ```

### 8.5 继承

- 子类继承父类的属性和方法。

- 示例：

  python

  复制

  ```
  class Animal:
      def speak(self):
          print("Animal speaks")
  
  class Dog(Animal):
      def bark(self):
          print("Dog barks")
  
  d = Dog()
  d.speak()  # 输出 'Animal speaks'
  d.bark()   # 输出 'Dog barks'
  ```

### 8.6 多态

- 不同类的对象对同一消息做出不同的响应。

- 示例：

  python

  复制

  ```
  class Cat:
      def speak(self):
          print("Meow")
  
  class Dog:
      def speak(self):
          print("Woof")
  
  def animal_sound(animal):
      animal.speak()
  
  animal_sound(Cat())  # 输出 'Meow'
  animal_sound(Dog())  # 输出 'Woof'
  ```

