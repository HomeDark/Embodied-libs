def ex5_odd_even(x):
    """题5：写一个函数，判断一个数是奇数还是偶数"""
    if x % 2 == 0:
        return "偶数"
    else:
        return "奇数"


def ex6_grade(score):
    """题6：写一个函数，判断成绩等级"""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def ex7_even_sum():
    """题7：写一个函数，计算 1~100 的偶数和"""
    total = 0
    for i in range(1, 101):
        if i % 2 == 0:
            total += i
    return total


def ex8_guess():
    """题8：写一个猜数字游戏"""
    answer = 42
    for i in range(4):
        guess = int(input(f"第{i + 1}次,猜一个数:"))
        if guess == answer:
            print("恭喜你，猜对了！")
            return
        elif guess < answer:
            print("小了")
        else:
            print("大了")
    print("很遗憾，4次机会用完了，正确答案是:", answer)


if __name__ == "__main__":
    print(ex5_odd_even(3), ex5_odd_even(4))
    print(ex6_grade(85))
    print(ex7_even_sum())
    ex8_guess()
