class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        # Always perform binary search on the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        left = 0
        right = m

        while left <= right:

            # Partition nums1
            partition1 = (left + right) // 2

            # Partition nums2
            partition2 = (m + n + 1) // 2 - partition1

            # Values around the partitions
            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == m else nums1[partition1]

            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == n else nums2[partition2]

            # Correct partition found
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:

                # Odd total number of elements
                if (m + n) % 2 == 1:
                    return float(max(maxLeft1, maxLeft2))

                # Even total number of elements
                else:
                    left_max = max(maxLeft1, maxLeft2)
                    right_min = min(minRight1, minRight2)

                    return (left_max + right_min) / 2.0

            # Move binary search to the left
            elif maxLeft1 > minRight2:
                right = partition1 - 1

            # Move binary search to the right
            else:
                left = partition1 + 1