#
# @lc app=leetcode.cn id=5 lang=python
#
# [5] 最长回文子串
#
# 解法1(T5% S99%): 双指针法，左指针依次迭代，每次从最右边一个一个比较，如果相等二者都往中间走一步，如果某一次不想等，左指针归位，右指针从最开始的前一个重新来过
#   要注意的是某次匹配上了，之后有可能会错，所以要加flag
#   改进1(T20% S97%): 右指针每次匹配错了要回到右边时如果比当前最好结果还短就不用看了
#
# 解法2**(T87% S70%): 中心扩散，每个位置往左右两边扩散，找到最长的那个
#    要注意 a aa aaa这种都是对称的，因此初始化right时应用一个while一直把相等的都算做初始的中心串
#
# 解法3(T40% S28%): 动态规划
#     设dp[i][j]代表从i到j的子串是否为回文串
# 
#     转移方程：如果里面的子串是回文，并且把头的两个还想等，则可以往左右各扩展一位
#     dp[i][j] = True if dp[i+1][j-1] and s[i]==s[j]; else False
# 
#     边界条件：一个字符肯定是回文，两个相邻字符如果相同则为回文
#     dp[i][i] = True, (dp[i][i+1] and s[i]==s[i+1]) = True
# 
#     需要注意，因为dp是不断往i+1和j-1方向扩展的，因此要首先从右下角开始扩展，同时由于对称结构j从i的下一位开始就好了
# 不需要把整个dp数组先建立完再两重循环找，做完dp[i][j]就可以直接进行判断了


# @lc code=start
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 解法2
        ans = s[0]
        for i in range(len(s)):
            center = i
            left = i 
            right = i
            while right+1<len(s) and s[right+1]==s[right]:
                right += 1

            while left>-1 and right<len(s) and s[left]==s[right]:
                left -= 1
                right += 1

            if len(s[left+1:right]) > len(ans):
                ans = s[left+1:right]

        return ans

    
    def otherSolution(self, s):
        # 解法3
        ans = s[0]

        dp = [[False]*len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            if i+1<len(s) and s[i]==s[i+1]:
                dp[i][i+1] = True 
        
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if i+1<len(s) and j>-1 and dp[i+1][j-1] and s[i]==s[j]:
                    dp[i][j] = True

                if dp[i][j] and j-i+1>len(ans):
                    ans = s[i:j+1]
        
        return ans


        # 解法1
        if len(s) == 1:
            return s

        ans = s[0]
        for i in range(len(s)):
            left, right = i, len(s)-1
            start = left
            has = False
            if right-left+1 < len(ans):
                break

            while left < right:
                if s[left] == s[right]:
                    if not has:     # 第一次匹配上记录又端点
                        has = True
                        end = right
                    left += 1
                    right -= 1
                else:
                    if has:         # 如果之前匹配上了但中间有不匹配的
                        has = False
                        left = start
                        right = end-1
                        # 改进1
                        if right-left+1 < len(ans):
                            break
                    else:
                        right -= 1

            if has and len(ans) < end-start+1:
                ans = s[start:end+1]
        
        return ans
        


Solution().longestPalindrome("xaabacxcabaaxcabaax")
# @lc code=end

