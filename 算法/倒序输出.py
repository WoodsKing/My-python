"""
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def reverse(x):
    """
    :type x: int
    :rtype: int
    """

    if x < 0:
        k = '-' + str(abs(x))[::-1]
        print(k)
        if int(k) <= -2 ** 32:
            k = 0
    else:
        k = str(x)[::-1]
        print(k)
        if int(k) >= 2 ** 31 - 1:
            k = 0
    return int(k)


print(reverse(12331))
print(reverse(-123))
print(reverse(-1563847412))
