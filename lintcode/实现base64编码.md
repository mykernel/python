要求：
自己实现base64编码

重难点
base64的概念理解

```python
alphabet = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='
teststr = "abc"

def base64(src):
    ret = bytearray()
    length = len(src)
    r = 0
#1. 每三位切割，不够三位凑够三位

    for offset in range(0,length,3):
        if offset + 3 <= length:
            triple = src[offset:offset + 3]
        else:
            triple = src[offset:]
            r = 3 - len(triple)
            triple = triple + '\x00'*r #补0
            ##print(triple)

#2. 移位算法
        b  = int.from_bytes(triple.encode(),'big')
        for i in range(18,-1,-6):
            if i == 18:
                index = b>> i 
            else:
                index = b >> i & 0x3F

#3. 对应编码
            ret.append(alphabet[index])
        
        for i in range(1,r+1):
            ret[-i] = 0x3D
    return ret 

print(base64(teststr))


```

    bytearray(b'YWJj')

