要求：
实现一个cache装饰器，实现可过期的功能，可以不换出

cache数据类型的选择：字典  k --> v

输入一致，结果一致

key的要求：
key必须可hash
key能接受位置参数和关键字参数
关键字参数需要是有序字典，也可以使用元组保存

相同的key：
(4,5)
(4,y=5)
(x=4,y=5)
(y=5,x=4)
key 算法设计视频解答：
第18天 04-自定义cache装饰器

```python
from  functools import  wraps
import  time
import  inspect
import datetime

def logger(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        start = datetime.datetime.now()
        ret = fn(*args,**kwargs)
        d = datetime.datetime.now() - start
        delta =  d.total_seconds()

        print(delta)
        return  ret
    return wrapper


def m_cache(fn):
    local_cache = {}
    @wraps(fn)
    def wrapper(*args,**kwargs):
        #print(args,kwargs)
        key_dict = {}  # sorted排序
        sig = inspect.signature(fn)
        param = sig.parameters  #有序字典

        param_list = list(param.keys())


        #位置参数处理
        for i,v in enumerate(args):

            k = param_list[i]
            key_dict[k] = v


        #关键字参数处理
        key_dict.update(kwargs)
        #for k,v in kwargs.items():
        #    key_dict[k] = y

        # 缺省值
        for k in param.keys():
            if k not  in  key_dict.keys():
                key_dict[k] = param[k].default

        #make_key
        key = tuple(sorted(key_dict.items()))

        if key not in local_cache.keys():
            ret = fn(*args, **kwargs)
            local_cache[key] = ret

        return  local_cache[key]
    return wrapper

@logger
@m_cache
#装饰器顺序不一样，打印结果不一样？
def add(x=1,y=5):
    time.sleep(3)
    ret = x + y

    return ret

print(add(1,5))
print(add(1))
print(add())
print(add(x= 1,y=5))
print(add(y=5,x=1))

```

    3.003217
    6
    0.000102
    6
    5.3e-05
    6
    5e-05
    6
    4.7e-05
    6

缓存的数据结构，字典
k - v 对
便于查询，输入一致，输出一致

重难点：
造key（make_key）

key 由位置参数、关键字参数（字典默认无序）、默认参数三种组成
==> 有序（排序）==> “有序”字典

怎么样才算相同的key？
print(add(1,5))
print(add(1)) #缺省值
print(add()) #缺省值
print(add(x= 1,y=5))
print(add(y=5,x=1))

使用inspect获取参数



```python

```


```python

```


```python

```


```python

```
