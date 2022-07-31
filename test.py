"""
number=input("请输入您的考试分数0-100:")
if number:
    number=int(number)
    if 0<=number<=100:
        if number==100:
            print(f"您的成绩为{number}分，评级为S")
        elif number>=90:
            print(f"您的成绩为{number}分，评级为A")
        elif number>=80:
            print(f"您的成绩为{number}分，评级为B")        
        elif number>=70:
            print(f"您的成绩为{number}分，评级为C")
        elif number>=60:
            print(f"您的成绩为{number}分，评级为D")
        elif number>=0:
            print(f"您的成绩为{number}分，评级为E")
    else:
        print("分数有误")
else:
    print("您没有输入内容")
"""
# year=input("请输入年份：")
# year=int(year)
# if (year %400==0) or(year %4==0 and year % 100 != 0) :
#     print ("你输入是润年")
# else:
#     print("你输入的不是润年")

# a=["小明",95]

# def get_max():
#     a = input('请输入a：')
#     b = input('请输入b：')
#     if a > b:
#         print(f'你输入的a是：{a}\n你输入的b是：{b},{a} > {b}')
#     elif a == b:
#         print(f'你输入的a是：{a}\n你输入的b是：{b},{a} = {b}')
#     elif a < b:
#         print(f'你输入的a是：{a}\n你输入的b是：{b},{a} < {b}')
#     else:
#         print('请输入正确的数字')

# get_max()

# number = [31,28,31,30,31,30,31,31,30,31,30,31]
# number.pop(0)
# print(number)
# number[1] = 28
# print(number)
# number.insert(7,31)
# print(number)
# number.extend([30,31])
# print(number)

# sum = 0
# for i in range(100):
#     if i % 2 ==0:
#         sum += i
# print(sum)
# a = []
# for b in range(5):
#     c = input("请输入五个整数")
#     c = int(c)
#     a.append(c)
# print(f"输入的5个数是: {a}")

# for i in range(len(a)):
#     a[i] *= 2
# print(f"各个元素*2的新列表:{a}")

# d = 0
# for i in a:
#     d = d+i
# print(d)
# a = []
# for i in range(100):
#     if i % 7==0 or  (i % 10 ==7 or i // 10 ==7 ):
#         a.append(i)
# print(a)

# i = 0
# while i < 10:
#     print("浩宇狗")
#     i +=1


# a = ["Food","Moon","Loop"]
# b = "".join([i[0] for i in a ])
# print(type(b))

# a = [2,4,6,8,10,12]
# b = [3,6,9,12]
# c = [i for i in a if i in b ]
# print(c)


# a = [[0,1,2],[3,4,5],[6,7,8]]
# for i in a:
#     for j in i:
#         print(j)
# for i in range(3):
#     for j in range(3):
#         print(f"i={i},j={j}")

# 2.找出100以内所有的质数（质数：大于1 只能被1和本身整除）

# b = []
# for i in range(2,100):
#     a = True
#     for j in range(2,i):
#         if i % j == 0:
#             a = False
#             break
#     if a:
#         b.append(i)
# print(b)

# 3.打印九九乘法表

# for i in range(1, 10):
#     for j in range(1, 10):
#         if j >= i:
#             print(f"{i} * {j} = {i*j:2d}", end=("    "))
#     print("")
# stu1 = {"name": "小王", "chinese": 86, "math": 92}
# stu2 = {"name": "小红", "chinese": 96, "math": 99}
# stu3 = {"name": "小明", "chinese": 72, "math": 84}
# a = {"小王": stu1, "小红": stu2, "小明": stu2}
# b = a["小王"]
# print(b)



from tkinter import W


all_users = [{
    "username": "976410029",
    "password": "123456"},

    {
    "username": "18348393337",
    "password": "123"},
    {
    "username": "15988866622",
    "password": "456"
}
]

"""
def login():
    usr = input("请输入用户名:")
    pwd = input("请输入密码:")
    user_name = []
    pass_word = []
    for user_items in all_users:
        user_name.append(user_items.get('username'))
        pass_word.append(user_items.get('password'))
    if usr in user_name:
        index = user_name.index(usr)
        if pwd == pass_word[index]:
            print("登陆成功!")
        else:
            print("密码错误，登陆失败!")
    else:
        print("用户名不存在!")


login()
"""
# def get_week_with_date(y, m, d):
#     y = y - 1 if m == 1 or m == 2 else y
#     m = 13 if m == 1 else (14 if m == 2 else m)
#     w = (d + 2 * m + 3 * (m + 1) // 5 + y + y // 4 - y // 100 + y // 400) % 7 + 1
#     return w
# a = get_week_with_date(2022,7,29)
# print(a)
def f(a=0,b=0,c=0):
    print(a,b,c)
f(b=8)