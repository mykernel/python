# 分解日志

import datetime
import re

logline = '''110.184.45.122 - - [28/Apr/2019:00:04:01 +0800] "GET /v1/images/points/sign_bg.png HTTP/1.1" 304 - "http://wx.kuaijiankang.com/v1/deals" "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.3(0x17000321) NetType/WIFI Language/zh_CN"
'''

ops1 = {
    'datetime': lambda timestr: datetime.datetime.strptime(timestr, '%d/%b/%Y:%H:%M:%S %z'),
    'status': int,
    'size': int
}
ops2 = {
    'datetime': lambda timestr: datetime.datetime.strptime(timestr, '%d/%b/%Y:%H:%M:%S %z'),
    'status': int
}

pattern = '''(?P<remote>[\\d.]{7,}) - - \\[(?P<datetime>.+)\\] "(?P<method>\\w+) (?P<get_url>[\\S/]+) \
(?P<protocol>[\\S/]+)" (?P<status>\\d+) (?P<size>[\\d-]+) "(?P<url>.*)" "(?P<useragent>.+)
'''
regex = re.compile(pattern)


def extract(line) -> dict:
    """正常的返回应为字典，如果返回None说明匹配失败"""
    matcher = regex.match(line)
    print(line)

    info = None
    if matcher:
        if '" 304' in line:
            info = {k: ops2.get(k, lambda x: x)(v) for k, v in matcher.groupdict().items()}
        else:
            info = {k: ops1.get(k, lambda x: x)(v) for k, v in matcher.groupdict().items()}
    return info


print(extract(logline))

# 知识点
# 1. 正则表达式
# 2. 字典的v的格式化