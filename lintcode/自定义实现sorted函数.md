要求：
1，返回一个新的列表
2，可以进行正序或者逆序排序
分析：
1，新建一个列表
2，遍历原列表，跟新列表的比较大小然后选择插入到对应的位置，如果无结果则append的到最后


```python
old_lst = [2,3,4,1,-9]
```


```python
def sorted(iterable):
    new_lst=[]
    
    for x in iterable:
        for i,y in enumerate(new_lst): #i = 0 ,x = 2 
            if x > y: 
                new_lst.insert(i,x)
                break
        else:
            new_lst.append(x)
              
    
    print(new_lst)     

                
             
```


```python
sorted(old_lst)
```

    [4, 3, 2, 1, -9]



```python

```


```python

```
