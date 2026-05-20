class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        if nums1[0] > nums2[-1] or nums1[-1] < nums2[0]:
            return -1
        
        idx1, idx2 = 0, 0
        while True:
            if idx1 >= len(nums1) or idx2 >= len(nums2):
                return -1
                
            if nums1[idx1] == nums2[idx2]:
                return nums1[idx1]
            
            if nums1[idx1] > nums2[idx2]:
                idx2 += 1
            elif nums1[idx1] < nums2[idx2]:
                idx1 += 1