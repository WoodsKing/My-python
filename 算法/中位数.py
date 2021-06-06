# noinspection SpellCheckingInspection
def zhongwei(nums1, nums2):
    nums3 = nums1 + nums2
    nums3.sort()
    a = 0
    b = -1
    while True:
        if not nums3[a] is nums3[b]:
            a += 1
        if nums3[a] is nums3[b]:
            value = (nums3[a - 1] + nums3[b]) / 2
            break
        else:
            b -= 1
        if nums3[a] is nums3[b]:
            value = nums3[b]
            break
    print(value)


num1 = [1, 3]
num2 = [2, 4]
zhongwei(num1, num2)
