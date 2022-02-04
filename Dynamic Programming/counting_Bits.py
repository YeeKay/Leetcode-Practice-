class Solution:
    def countBits(self, n: int) -> List[int]:
        counter = [0]

        for i in range(1, n + 1):
            counter.append(counter[i >> 2] + i % 2)
            # i >> 1 == i // 2 (faster to perform bit-shifting)
            # i % 2 - determine its parity 
        
        return counter 