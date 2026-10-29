def filter_square_sort_loop(nums):  # 使用循环实现过滤、平方和排序
    result = []
    for n in nums:
        if n > 10:
            result.append(n * n)
    result.sort()  # 对结果进行排序
    return result


def filter_square_sort_comp(nums):  # 使用列表推导式实现过滤、平方和排序
    return sorted([n * n for n in nums if n > 10])


if __name__ == "__main__":
    nums = [5, 12, 7, 20, 3, 15]
    print(filter_square_sort_loop(nums))
    print(filter_square_sort_comp(nums))
    # 两个都应该是 [144, 225, 400]
