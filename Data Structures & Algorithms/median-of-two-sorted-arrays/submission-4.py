class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Solution consists of binary search and partitioning the arrays
        # Calculate total and half
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        # Make sure A is the smaller array
        if len(A) > len(B):
            A, B = B, A
        
        # Keep making the left partition until it is correct, in which
        # case return the median depending on if total is odd or even
        l, r = 0, len(A) - 1
        while True:
            # Determine how many elements from A and B will join left partition
            i = (l + r) // 2
            j = half - i - 2 # minus 2 to offset index numbers

            # Find the numbers at the boundaries between the left and right partition
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # Determine if left partition is correct, if so return median, otherwise
            # adjust the boundaries
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1