'''
关键在于理解“中位数”这个概念---小于前面的，大于后面的

根据其本身的位置特性设计算法，使用两个游标来分割两个数组

两个标记需要满足“中位”这一数量关系，标记处的值也要满足“中位边界”值的关系
'''
def O_log_mn(A, B):
    m = len(A)
    n = len(B)

    if m < n:
        A, B, m, n = B, A, n, m

    imin, imax = 0, m
    halfLen = int((m+n+1)/2)

    while imin <= imax:
        i = int((imin + imax)/2)
        j = halfLen - i
        if i < m and B[j-1] > A[i]:
            imin += 1
        elif i > 0 and A[i-1] > B[j]:
            imax -= 1
        else:
            if i == 0:
                max_of_left = B[j - 1]
            elif j == 0:
                max_of_left = A[i - 1]
            else:
                max_of_left = max(A[i - 1], B[j - 1])

            if (m + n) % 2 == 1:
                return max_of_left

            if i == m:
                min_of_right = B[j]
            elif j == n:
                min_of_right = A[i]
            else:
                min_of_right = min(A[i], B[j])

            return (max_of_left + min_of_right) / 2.0

def notStandardWay(nums1, nums2):
    new_list = nums1 + nums2
    new_list.sort()

    l = len(new_list)

    if l % 2 == 0:
        return float((new_list[int(l / 2 - 1)] + new_list[int(l / 2)]) / 2)
    else:
        return float(new_list[int(l / 2)])



if __name__ == '__main__':
    # nums1 = [1, 2, 6]
    # nums2 = [2, 4, 8]
    nums1 = [1,3]
    nums2 = [5]
    print(O_log_mn(nums1,nums2))

