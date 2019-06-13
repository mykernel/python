"""
 功能：
  
展示面板：
1.添加学生的信息
2.删除学生的信息
3.修改学生的信息
4.查询学生的信息
5.遍历所有学生的信息
6.保存并退出系统
          
需求:
1.可以保存用户数据，下次运行程序时能读取上次保存的数据
2.具有添加、查询、删除用户的功能
                  
优化：
1.规范用户行为，用户输入错误不能直接报错，而是返回相关提示。
2.可以增加项目，比如班主任，成绩等。
3.可以实现排序功能
4.删除一个用户后，索引值自动-1，保证id的连续
5.实现批量增加或者删除？

"""


import csv
from pathlib import Path
import pickle
from prettytable import PrettyTable

p_save = Path('/jupyter/tmp/student/StudentDetails.save')  # 可以提取成配置文件
p_csv = Path('/jupyter/tmp/student/StudentDetails.csv')  # 可以提取成配置文件
# StudenDetails = [['StudentID', 'name', 'age']]
StudenDetails_Tmp = [['StudentID', 'name', 'age']]


def showinfo():
    """doc"""
    print('*' * 40)
    '''展示功能面板'''
    print(" 1.添加学生的信息")
    print(" 2.删除学生的信息")
    print(" 3.修改学生的信息")
    print(" 4.查询学生的信息")
    print(" 5.遍历所有学生的信息")
    print(" 6.保存并退出系统")


def save_csv(x):  # 保存为csv文件

    if not p_csv.parent.exists():
        p_csv.parent.mkdir(parents=True)  # 相对危险的操作
        p_csv.touch()
    with open(str(p_csv), 'a+') as f:
        writer_student = csv.writer(f)
        writer_student.writerows(x)


def save(x):
    if not p_save.parent.exists():
        p_save.parent.mkdir(parents=True)  # 相对危险的操作
        p_save.touch()
    with open(str(p_save), 'wb+') as f:
        pickle.dump(x, f)

        
def pick_load():
    with open(str(p_save), 'rb') as f:
        StudenDetails_Tmp = pickle.load(f)
        return StudenDetails_Tmp

        

def generate_counter(lst=[0]):  ##闭包实现自增功能==> 学生学号
    CNT = lst

    def add_one():
        CNT[0] += 1
        return CNT[0]

    return add_one


def show_student_details(lst: list, show_id: int):  # 根据输入的id，打印学生的详情
    for ii in lst:
        for xx in ii:
            if xx == show_id:  #
                details_list = ii

            else:
                continue
    return details_list


def StudentManagement():  # 主体函数

    while True:  # TODO 完成所有操作最后持久化
        print('*' * 40)
        option_tmp = input("请选择您的操作：")
        while True:
            if option_tmp.isdigit():
                break
            else:
                option_tmp = input("请输入正确的操作（1-6）：")
        option = int(option_tmp)

        if option == 1:
            StudentID = counter()  # TODO 自增问题

            name = input("请输入学生的姓名：")
            while True:
                if (u'\u4e00' <= name <= u'\u9fff'):
                    break
                if name.isalpha():
                    break
                else:
                    name = input("请输入正确的年龄（中文或者字母）：")

            age = input("请输入学生的年龄：")
            while True:
                if age.isdigit():
                    break
                else:
                    age = input("请输入正确的年龄（1-99）：")

            StudenDetails_Tmp.extend([[StudentID, name, age]])


        elif option == 2:  # 输入学生的id就可以删除
            DelID = int(input("请输入需要删除的学生id："))
            del_list = show_student_details(StudenDetails_Tmp, DelID)
            StudenDetails_Tmp.remove(del_list)
            print("删除用户成功：", del_list)
         

        elif option == 3:  # 输入学生的id，然后弹出需要修改的选选项，输入值进行修改
            ChgDetil = int(input("请输入需要修改的学生id："))
            show_list = show_student_details(StudenDetails_Tmp, ChgDetil)
            print("该学生目前的信息：", show_list)
            chg_name = input("请输入学生的姓名：")
            chg_age = input("请输入学生的年龄：")
            new_student_details = [ChgDetil, chg_name, chg_age]
            st_index = StudenDetails_Tmp.index(show_list)
            StudenDetails_Tmp[st_index] = new_student_details

        elif option == 4:  # 根据学生id查找学生信息  TODO 可改进为根据任意一个字段查找
            ChgDetil = int(input("请输入需要查询的学生id："))
            show_list = show_student_details(StudenDetails_Tmp, ChgDetil)
            tb4 = PrettyTable()
            tb4.field_names = ['StudentID', 'name', 'age']
            tb4.add_row(show_list)
        
            print(tb4)

        elif option == 5:  # 查询所有的学生信息
            tb5 = PrettyTable()
            for idx,v in enumerate(StudenDetails_Tmp):
                if idx == 0:
                    tb5.field_names = v
                if idx > 0:
                    tb5.add_row(v)
     
            print(tb5)
        
        elif option == 6:
            
            save_csv(StudenDetails_Tmp)  #保存为csv格式便于下载
            save(StudenDetails_Tmp)   #数据序列化保存
            print('保存成功：',StudenDetails_Tmp)
            break

        else:
            print('请输入正确的选项(1-6)')
            continue


if __name__ == "__main__":
    if p_save.exists():
        StudenDetails_Tmp = pick_load()
        index_student = [StudenDetails_Tmp[-1][0]]
    else:
        index_student = [0]
    showinfo()
    counter = generate_counter(index_student)
    StudentManagement()
    pick_load()
    # print(StudenDetails_Tmp)

