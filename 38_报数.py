def cou(pre_num):
    pre = list(pre_num)
    res = ''
    a = 0
    b = 0
    val = pre[0]
    while b < len(pre):
        if val == pre[b]:
            a += 1
        else:
            res += str(a) + str(val)
            val = pre[b]
            a = 1
        b += 1
    if a != 0:
        res += str(a)+str(val)
    return res


print(cou('1'))
print(cou('1211'))