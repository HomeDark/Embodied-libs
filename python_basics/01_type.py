# 01_types.py
# 运行：python 01_types.py


def ex1_types():
    """题1：造 8 种类型的变量并打印 type"""
    a = 1  # int
    b = 1.5  # float
    c = "hello"  # str
    d = True  # bool
    e = [1, 2, 3]  # list
    f = {"x": 1}  # dict
    g = (1, 2)  # tuple
    h = {1, 2, 3}  # set
    for v in (a, b, c, d, e, f, g, h):
        print(type(v).__name__, v)


def ex2_convert():
    # 题目2：字符类型转换
    s = "123"
    n = int(s)  # 字符串转整数
    back = str(n)  # 整数转字符串

    x = 3.9
    y = int(x)  # 浮点型转整数型，会截断
    print(n, back, y)


def ex3_string():
    # 字符串常用方法
    text = "  Hello World!  "
    text = text.strip()  # 去掉text首尾空白
    print(len(text))  # 长度
    print(text.upper)  # 全大写
    print(text.startswith("Hello"))  # 是否以Hello开头
    print(text.split(" "))  # 按空格切分


def ex4_describe(x):
    """题4：写一个函数，返回类型名"""
    return type(x).__name__


if __name__ == "__main__":
    ex1_types()
    print("-" * 30)
    ex2_convert()
    print("-" * 30)
    ex3_string()
    print("-" * 30)
    print(ex4_describe(1), ex4_describe("a"), ex4_describe([1]))
