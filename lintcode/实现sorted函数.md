

```python
def sorted(iterable):
    ret = []
    for x in iterable:
        for i,y in enumerate(ret):
            if x > y:
                ret.insert(i,x)
                break
        else:
            ret.append(x)
    return ret

print(sorted([1,11,2,3,1,-1]))
```

    [11, 3, 2, 1, 1, -1]



```python
def sorted(iterable,fn = lambda a,b : a<b):
    ret = []
    for x in iterable:
        for i,y in enumerate(ret):
            if fn(x,y):
                ret.insert(i,x)
                break
        else:
            ret.append(x)
    return ret

print(sorted([1,11,2,3,1,-1]))
```

    [-1, 1, 1, 2, 3, 11]



```python

```


```python

```
