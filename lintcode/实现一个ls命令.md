需求：
ls  -l  -a  --all  -h（人性化显示大小）

实现显示路径下的文件列表
-a和--all是一样的参数，能显示包含. 开头的文件
-l 详细列表显示

-h 人性化显示只能和-l配合使用


### 核心代码


```python
from pathlib import Path

def show_dir(path:Path):
    path.
```


```python
p = Path('/jupyter/tmp/')
```


```python
for i in p.iterdir():
    print(i.name)
```

    test.py
    my.cnf
    sample.txt
    test11.csv
    test_f.py
    test2
    readme.txt
    a
    .ipynb_checkpoints
    123
    test4
    test111.py
    new_path.txt
    test_f1.py
    ini
    testxx.py
    sample.txt.bak
    bin
    test1
    test
    mycsv
    test.csv

 参数分类：
 位置参数，对应一个位置
 选项参数，对应一项功能
 
 

```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```
