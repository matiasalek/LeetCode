class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_in_list = []
        binary_representation = bin(n)[2:]

        for digit in str(binary_representation):
            binary_in_list.append(int(digit))
        
        not_zero = 0
        for i in binary_in_list:
            if i != 0:
                not_zero = not_zero + 1
        
        return not_zero
