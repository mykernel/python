设计一个算法，计算出n阶乘中尾部零的个数n = 1 
nj = 1

n = 2
nj = 1 x 2

n = 3 
nj = 1 x 2 x 3

n = 4 
nj = 1 x 2 x 3 x 4 

```python
def factorial(n):
    num = 1 
    for i in range(1,n+1):
        num *= i
    
    
    
    print('其运行结果的末尾一个出现了{}个O。'.format(len(str(num)) - len(str(num).strip('0'))))
```


```python
factorial(11)
```

    其运行结果的末尾一个出现了2个O。



```python
n = int(input("请输入一个数："))
num = 1 
for i in range(1,n+1):
    num *= i
    
print('其运行结果的末尾一个出现了{}个O。'.format(len(str(num)) - len(str(num).strip('0'))))

```

    请输入一个数：21
    其运行结果的末尾一个出现了4个O。



```python

```
