class Solution:
    def findComplement(self, num: int) -> int:
        # Количество значащих битов в num
        bits = num.bit_length()
        
        # Маска из bits единиц: 2^bits - 1
        # Например bits=5 → 11111 (31)
        mask = (1 << bits) - 1
        
        # XOR с маской инвертирует все биты
        return num ^ mask
