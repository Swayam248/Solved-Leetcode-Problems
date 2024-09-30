class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def count_steps(curr, n):
            steps = 0
            first, last = curr, curr + 1
            while first <= n:
                steps += min(last, n + 1) - first
                first *= 10
                last *= 10
            return steps
        curr = 1
        k -= 1  # Since we are starting from the first number, we decrement k
    
        while k > 0:
            steps = count_steps(curr, n)
            if steps <= k:
                k -= steps
                curr += 1  # Move to the next sibling in the same level
            else:
                curr *= 10  # Move to the next level (children of the current number)
                k -= 1
        return curr
        