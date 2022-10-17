class Solution:
    def reverseBits(self, n: int) -> int:
        bit_str = bin(n)[2:]

        bit_str_reverse = bit_str[::-1]

        length_gap = 32 - len(bit_str_reverse)

        bit_str_reverse += '0' * length_gap

        reversed_n = int(bit_str_reverse, 2)

        return reversed_n

    
if __name__ == '__main__':
    s = Solution() 

    r = s.reverseBits(4294967293)
    print(r)