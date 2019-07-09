class Solution:
    def addBinary(self, a: str, b: str) -> str:

        a = list(map(int, reversed(list(a))))

        b = list(map(int, reversed(list(b))))
        c = 0
        res = []
        i = 0
        min = len(a) if len(a) < len(b) else len(b)
        while i < min:
            d = a[i] + b[i] + c
            if d > 1:
                c = 1
                d -= 2
            else:
                c = 0
            res.append(d)
            i += 1
        if i == len(a):
            while i < len(b):
                d = b[i] + c
                if d > 1:
                    c = 1
                    d -= 2
                else:
                    c = 0
                    res.append(d)
                    i += 1
                    while i < len(b):
                        res.append(b[i])
                        i += 1
                    break
                res.append(d)
                i += 1
        elif i == len(b):
            while i < len(a):
                d = a[i] + c
                if d > 1:
                    c = 1
                    d -= 2
                else:
                    c = 0
                    res.append(d)
                    i += 1
                    while i < len(a):
                        res.append(a[i])
                        i += 1
                    break
                res.append(d)
        if c == 1:
            res.append(1)

        return ''.join(map(str, reversed(res)))


if __name__ == '__main__':
    s = Solution()
    print(s.addBinary('110','100'))