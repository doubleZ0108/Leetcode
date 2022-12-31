#
# @lc app=leetcode.cn id=3 lang=python
#
# [3] 无重复字符的最长子串
#
# 解法1(T15% S5%): 动态规划+循环，设定`dp[i]`代表以第i个位置结尾的最长无重复字符的长度，对于i+1位置，只需要向前寻找dp[i-1]次，如果有相同的字符则长度就为向前试探的步长，如果无重复则`dp[i] = dp[i-1] + 1`，最终返回dp数组的最大值
#   改进1：用一个变量maxLength保存每次的最大值，不用最后再调用`max()`
#
# 解法2(T12% S74%): 同样是双重循环，不过该用set存储元素，遍历直到遇到字符在set中出现过了，那以这个字符开头的最长无重复子串长度就是set的长度（不要用下标来算，容易出现最后一个位置长度差1的问题，set反正也维护了，不如直接获取长度）
#   改进1(T55% S62%)：如何能把$O(N^2)$降到$O(N)$呢？我们可以很自然的相当如果某次往后试探走了很远，那证明中间那些都是不重复的字符，所以下次迭代时没必要重走一遍，直接把上一轮的字符从set中移除即可，所以只需要维护一个通用的set，同时通过右指针标定探索过的右端位置就好

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 解法2 改进1
        if len(s) < 2: return len(s)

        maxLength = 1
        myset = set(s[0])
        j = 1
        for i in range(len(s)-1):
            while j<len(s) and s[j] not in myset:
                myset.add(s[j])
                j += 1
            maxLength = max(maxLength, len(myset))
            myset.remove(s[i])

        return maxLength


    def otherSolution(self, s):
        # 解法2
        if len(s) < 2: return len(s)

        maxLength = 1
        for i in range(len(s)-1):
            myset = set(s[i])
            for j in range(i+1, len(s)):
                if s[j] not in myset: myset.add(s[j])
                else: break
            maxLength = max(maxLength, j-i)
        return maxLength

        # 解法1
        if len(s) < 2: return len(s)

        maxLength = 1
        dp = [0 for _ in range(len(s))]
        dp[0] = 1
        for i in range(1, len(s)):
            for j in range(i-1, i-dp[i-1]-1, -1):
                if s[j] == s[i]:
                    dp[i] = i - j
                    break
            if dp[i] == 0: dp[i] = dp[i-1] + 1
            maxLength = max(maxLength, dp[i])
        
        return maxLength

Solution().lengthOfLongestSubstring("au")
# @lc code=end

