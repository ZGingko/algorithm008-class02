class Solution:
    """
    190.颠倒二进制位 https://leetcode-cn.com/problems/reverse-bits/
    """
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        return result