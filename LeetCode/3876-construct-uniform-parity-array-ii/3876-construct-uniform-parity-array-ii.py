class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        odd, even = 0, 0
        min_odd, min_even = 1e9, 1e9
        for n in nums1:
            if n%2 != 0:
                odd += 1
                min_odd = min(min_odd, n)
            else:
                even += 1
                min_even = min(min_even, n)
        
        # 다 같으면 성공
        if odd == 0 or even == 0:
            return True
        
        for n in nums1:
            if n%2 == 0 and n < min_odd:
                return False
        
        return True