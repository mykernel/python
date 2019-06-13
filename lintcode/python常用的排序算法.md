python经典排序算法
1. 冒泡
2. 选择（二元选择排序）
3. 插入排序
4. 堆排序
冒泡

选择


```python
m_list = [
    [1,9,8,5,6,7,4,3,2,2312,3123,434,222222,0,-1111],
    [1,2,3,4,5,6,7,8,9]
    
]

nums = m_list[0]
length = len(nums)

count_swap = 0
count_iter = 0 

for i in range(length):
    maxindex = i 
    for j in range(i+1,length):
        count_iter += 1 
        if nums[maxindex] < nums[j]:
            maxindex = j
    if i != maxindex:
        tmp = nums[i]
        nums[i] = nums[maxindex]
        nums[maxindex] = tmp
        count_swap += 1
print(nums,count_swap,count_iter)
```

    [222222, 3123, 2312, 434, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1111] 9 105


二元选择排序


```python
nums = [1,19,28,5,6,7,4,3,2]
length = len(lst)
count_swap = 0 

for i in range(length//2):  # i = 0,length = 9
    maxindex = i   # maxindex = 0 ,最左边
    minindex = -i-1  #minindex = -1，最右边
    minorigin = minindex
    
    for j in range(i+1,length - i):  #j [1,8)
        if nums[maxindex] < nums[j]:   #最大值 
            maxindex = j  # maxindex = 1
        if nums[minindex] > nums[-j-1]:    #最小值
            minindex = -j - 1 # minindex  = -9
    print(maxindex,minindex)  
        #如果i ！= maxindex 进行交换
    if i != maxindex:
        tmp = nums[i]
        nums[i] = nums[maxindex]
        nums[maxindex] = tmp   # 
        count_swap +=1 
            
        if i ==  minindex or i ==length + minindex:
            minindex = maxindex
        
    if minorigin != minindex:
        tmp = nums[minorigin]
        nums[minorigin] = nums[minindex]
        nums[minindex] = tmp
        count_swap+=1
            
print(nums,count_swap)
        
```

    2 -9
    1 -7
    5 -7
    4 -4
    [28, 19, 7, 6, 5, 4, 3, 2, 1] 6



```python
nums = [1,9,8,5,6,7,4,3,2]
nums[-9]
```




    1



堆排序

插入排序
