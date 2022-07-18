# 动态规划，给定一个整数n，其中的范围是1<=n<=1000000，再给定一个n个整数的数组nums，
# 请找出一个具有最大和的连续子数组，并返回最大值。


# 假定f为一个n个整数的数据，其中f[i]表示从i前面某个元素到i这个元素的最大子数组和，
# 即f[0]为nums第一个元素，即nums[0]；而f[1]为"f[0]+num[1]，与num[1]"的较大者
def child_str_max_sum(nums: list):
    f = [0] * len(nums)
    i = 0
    while i < len(nums):
        if i == 0:
            f[0] = nums[0]
        else:
            f[i] = max(f[i-1] + nums[i], nums[i])
        i += 1
    return max(f)


# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4, 6, 5, 5, 4, 4, -100, 435, 4]
print(child_str_max_sum(nums))


# 第二题：现在有四个物品，背包总容量为8，背包最多能装入价值为多少的物品


# 假定f为一个二重数组，其中f[y][x]即为在体积为x的情况下，装编号为y之前的商品，能装下的最大的价值数
volume_price_dict = {
    2:3,
    3:4,
    4:5,
    5:6,
                     }


# volume_price_dict = {
    # 1: {'v': 2, 'p': 3},
    # 2: {'v': 3, 'p': 4},
    # 3: {'v': 4, 'p': 5},
    # 4: {'v': 5, 'p': 6},
    #                  }


def max_price_inbag(v_p_dict: dict, f):
    # f = [[0] * 9] * 5
    for y in range(len(f)):
        for x in range(len(f[0])):
            if x == 0:
                f[y][0] = 0
            elif y == 0:
                f[0][x] = 0
            else:
                max_volume = max([i for i in v_p_dict if i <= x and i <= [x for x in v_p_dict][y-1]] or [0])
                # print(y, x, max_volume)
                print(f'max_volume is {max_volume}')
                if max_volume == 0:
                    f[y][x] = 0
                else:
                    print(f'f[y][x - max_volume] is {f[y][x - max_volume]}')
                    max_price = sum([v_p_dict[x] for x in v_p_dict][:y])
                    print(f'max_price is {max_price}')
                    f[y][x] = max(f[y - 1][x], v_p_dict[max_volume] + f[y][x - max_volume] < max_price and v_p_dict[max_volume] + f[y][x - max_volume] or max_price)
            print(f'x:{x}, y:{y}, {f[y][x]}')
    print(f'f is {f}')
    return f


f = [[0] * 9] * 5
a = max_price_inbag(volume_price_dict, f)
print(a)
# print(max_price_inbag(volume_price_dict)[4][8])
