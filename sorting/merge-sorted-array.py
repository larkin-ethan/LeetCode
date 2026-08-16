class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Sets value to the value of m because it will move the pointer to the  placeholders
        y = m
        # Covers example 3
        if m == 0:
            # Takes each value from nums2
            for x in nums2:
                # Switches the placeholders with the values of nums2
                nums1[y] = x
                # Moves the pointer one forward
                y += 1
        else:
            for x in nums2:
                nums1[y] = x
                y += 1
            nums1.sort()
