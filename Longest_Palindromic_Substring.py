def main(s):
    s1 = '#'+'#'.join(s)+'#'
    p = [0]*len(s1)
    max_center = [0,0] # center, r
    left_bound = 0
    right_bound = 0
    center = 0
    for i in range(len(p)):
        # i is current center
        r = 1  # current redis
        if i < right_bound:
            r = min(p[2 * center - i], right_bound-i)
        else:
            r=1
        while i+r < len(p) and 0 <= i-r and s1[i+r] == s1[i-r]:
            r += 1

        if r > (right_bound-left_bound-1)/2:
            center = i
            left_bound = i - r
            right_bound = i + r
        if i >= right_bound:
            center = i
            left_bound = i-r
            right_bound = i+r
        if r > max_center[1]:
            max_center[0] = i
            max_center[1] = r
        p[i]=r
    # print(max_center)
    # print(s1)
    # print(p)
    a, b = max_center
    return s1[a-b+2:a+b:2]


c = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# c = 'a'*10
c = "aaaaaaabcaaaaaaa"
print(main(c))
c="cbcdcbedcbc"
# print(len(c),len(main(c)))
# print(c==main(c))
print(main(c))
print(main('babad'))
print(main('cbbd'))
