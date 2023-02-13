#
# @lc app=leetcode.cn id=1234 lang=python3
#
# [1234] 替换子串得到平衡字符串
#
# 解法1(解答错误 应该也会超时)：先找出四个字符中超过1/4长度的字母和超过的个数组成pattern字符串，该问题就转换为了找到一个子串，使得子串中超量字符的数量与pattern中的数量相同，可以通过两重循环实现
#
# 解法2(超时 37/40)：解法1的问题转换的很不错，但转换完之后的问题还是只能暴力解。找子串的问题往往要用滑窗思想解，对于本问题，如果我们考虑一个滑窗，当滑窗外面的每个字母个数都少于1/4时，那替换掉该滑窗内的子串一定能使得s平衡，所以问题转换为了求解满足如上条件的滑窗的最小长度。我们设定滑窗的左右端点left right初始均为0，右窗口不断向右，每向右一次哈希表计数器都将该字符数量减一，直到满足如上条件，此时更新最小长度。而左窗口在右窗口找到一个可行解之后向后移动一位并重新进行上述右窗口的循环。
#     超时的原因在于每次左端点移动都相当于重新来过了，本质还是暴力的两重循环，滑窗的核心思想就是将状态都保存在滑窗中，不要一移动循环就重新来过
#     改进1(T18% S61%)：左窗口每次移动的时候只需要再把当前这个字母的技术再加一即可，相当于不选这位作为结果子串的一部份，那肯定要把它之前减去的次数再加回来。另有一点需要注意，如果右指针往右移动，一直移动到字符串结尾也没有可行解，那就证明现在left太靠右了，已经不可能有可行解了，这时候要终止算法提前结束了

# @lc code=start
class Solution:
    # 解法2 改进1
    def balancedString(self, s: str) -> int:
        cnt = Counter(s)

        def check():
            if cnt['Q']<=len(s)//4 and cnt['W']<=len(s)//4 and \
                cnt['E']<=len(s)//4 and cnt['R']<=len(s)//4:
                return True
            else:
                return False
        
        minlen = len(s)
        right = 0
        for left in range(len(s)):
            while right<len(s) and not check():
                cnt[s[right]] -= 1 
                right += 1
            if not check():
                break
            minlen = min(minlen, right-left)
            cnt[s[left]] += 1

        return minlen
        
        

    # 解法2 超时
    def balancedString(self, s: str) -> int:
        cnt = Counter(s)
        if cnt['Q']==len(s)//4 and cnt['W']==len(s)//4 and \
            cnt['E']==len(s)//4 and cnt['R']==len(s)//4:
            return 0
        
        minlen = len(s)
        left, right = 0, 0
        while left<len(s):
            cnt_ = Counter(s)
            while right<len(s):
                cnt_[s[right]] -= 1
                if cnt_['Q']<=len(s)//4 and cnt_['W']<=len(s)//4 and \
                    cnt_['E']<=len(s)//4 and cnt_['R']<=len(s)//4:
                    minlen = min(minlen, right-left+1)
                    break
                right += 1
            left += 1
            right = left

        return minlen
    

    # 解法1 解答错误 应该也会超时
    def balancedString(self, s: str) -> int:
        cnt = Counter(s)
        exceed = list(filter(lambda x: cnt[x]>len(s)//4, cnt.keys()))
        if exceed == []:
            return 0

        pattern = ""
        for it in exceed:
            pattern += it * (cnt[it]-len(s)//4)
        pattern_cnt = Counter(pattern)
        
        minlen = float('inf')
        for i in range(0, len(s)-len(pattern)+1):
            if s[i] in pattern_cnt:
                for j in range(i+len(pattern), len(s)+1):
                    target_cnt = Counter(s[i:j])
                    flag = True
                    for key in pattern_cnt:
                        if pattern_cnt[key] != target_cnt[key]:
                            flag = False
                            break

                    if flag:
                        minlen = min(minlen, j-i)
                        if minlen == len(pattern):
                            return minlen
                        break
        return minlen
# @lc code=end

