"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        h = {}
        max_so_far = curr_max = start = 0
        for index, c in enumerate(s):
            if c in h and h[c] >= start:
                max_so_far = max(max_so_far, curr_max)
                curr_max = index - h[c]
                start = h[c] + 1
            else:
                curr_max += 1
            h[c] = index
        return max(max_so_far, curr_max)


s = Solution()
str = "abcabcbb"
print(s.lengthOfLongestSubstring(str))
