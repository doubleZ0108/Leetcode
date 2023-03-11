#
# @lc app=leetcode.cn id=M705 lang=python
#
# [面试题 17.05] 字母与数字
#
# 解法1(超时 23/45?)：动态规划，看到最长子数组本能的想到了dp，设定`dp[i][j]`代表i～j的子数组中字母和数组分别有多少个，如果建立完dp数组，我们只需要找`dp[i][j][0]==dp[i][j][1]`的第一个最大长度即可，但问题在于动态规划的转移是什么呢？`dp[i][j]`只跟`dp[i][j-1]`有关，如果`array[j]`是数字，则让`dp[i][j-1]`数字部份+1并赋值给`dp[i][j]`，否则则换成字母，而且i≤j，但这样的代码写完发现其实本质上还是个二重暴力循环，因为`dp[i][j]`没有跟上一行建立起联系（其实也能建立起联系，根据`array[i-1]`将`dp[i][j]`整一行都减1），但本质上还是两重循环，对于$10^5$的数据规模太大了
#
# 解法2(T57% S9%)：首先将字母都变为1，数字都变为-1，统计前缀和，如果`prefix[i]==0`则意味着从下标0～i正好满足字母总数和数字总数相同，也就是找到了一个满足的条件；但如果`prefix[i]=A≠0`，也不一定以它结尾就不能满足条件，如果在i之前也存在一个j有`prefix[j]=A`，那j～i的子数组也能满足条件，因此我们只需要通过一个哈希表把所有第一次出现的前缀和下标都记录下来，再遇到相同的前缀和时，二者中间夹的这段就是一个可行解，再找全局最长的就可以了，注意这个j是不包含在内的，是`(j,i]`满足条件


# @lc code=start
class Solution(object):
    # 解法2
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        prefix = [-1 if ch.isdigit() else 1 for ch in array]
        prefix = list(accumulate(prefix))
        table = {}
        start, end = -1, -1
        for idx, item in enumerate(prefix):
            if item == 0:
                if idx > end-start:
                    start, end = 0, idx
            else:
                if item not in table:
                    table[item] = idx
                else:
                    if idx - table[item]-1 > end-start:
                        start, end = table[item]+1, idx
        return array[start:end+1]

    # 解法1 超时
    def findLongestSubarray(self, array):
        """
        :type array: List[str]
        :rtype: List[str]
        """
        n = len(array)
        dp = [[[0, 0]]*n for _ in range(n)]
        maxpair = 0
        res = [-1, -1]   

        for i in range(n):
            for j in range(i, n):
                if i == j:
                    dp[i][i] = [0, 1] if array[i].isdigit() else [1, 0]
                else:
                    if array[j].isdigit():
                        dp[i][j] = [dp[i][j-1][0], dp[i][j-1][1]+1]
                    else:
                        dp[i][j] = [dp[i][j-1][0]+1, dp[i][j-1][1]]

                if dp[i][j][0] == dp[i][j][1] and dp[i][j][0] > maxpair:
                    maxpair = dp[i][j][0]
                    res = [i, j]
        
        return array[res[0]:res[1]+1]

# @lc code=end