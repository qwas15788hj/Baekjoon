class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left, mid, right = [], 0, []
        for num in nums:
            if pivot > num:
                left.append(num)
            elif pivot < num:
                right.append(num)
            else:
                mid += 1
        
        return left + [pivot]*mid + right