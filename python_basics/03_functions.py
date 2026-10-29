def add(a, b=1):  # 默认参数
    return a + b


def average(*nums):  # 可变参数，nums是一个tuple元组
    return sum(nums) / len(nums)


def make_profile(**info):  # 关键字参数，info是一个dict字典
    return info


count = 0


def change_count():
    # global count  # 声明全局变量
    count = 10  # 局部变量
    return count


print(count)
print(change_count())
