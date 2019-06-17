# 读取文件中所有的文件
from pathlib import Path
from itertools import islice
import re

path_list = []

p1 = Path("C:\\Users\\Administrator\\Desktop\\log")

pys = p1.glob('*.log')

for i in pys:
    path_list.append(i)

for j in path_list:
    print(str(j))
    with open(str(j), encoding='UTF-8') as f:
        while True:
            next_n_lines = list(islice(f, 6))
            str_lines = str(next_n_lines)
            # print(next_n_lines)
            if len(next_n_lines) == 6 and next_n_lines != []:

                # print(next_n_lines[5])

                pattern = r'''(?P<date>[\w\s:-]+)\S+\w+\S\s+(?P<time>[\d.]+)'''

                regex = re.compile(pattern)

                matcher = regex.findall(next_n_lines[5])
                print(matcher)

            if not next_n_lines:
                break
